#!/usr/bin/env python3
"""
Script: Jupyter to Hugo Converter
Description: Converts a Jupyter Notebook (.ipynb) into a Hugo-compatible Markdown content bundle.
Usage: python3 scripts/convert_notebook.py path/to/notebook.ipynb
Dependencies: 
    - jupyter
    - nbconvert
    - python-frontmatter (optional, but we'll do manual parsing to keep it simple)

install: pip install jupyter nbconvert
"""

import os
import sys
import argparse
import subprocess
import shutil
from datetime import datetime

# ==========================================
# Configuration & Constants
# ==========================================
# The directory where Hugo content lives. 
# We target 'content/posts' by default for blog posts.
CONTENT_DIR = "content/posts"

# The Front Matter template.
# We use YAML format (--- ... ---) which Hugo supports natively.
# We inject:
#   - title: Detected from the first H1 (# Header) in the notebook.
#   - date: Current date in YYYY-MM-DD format.
#   - post_type: "Jupyter Notebook" (To trigger our custom badge CSS).
FRONT_MATTER_TEMPLATE = """---
title: "{title}"
date: {date}
draft: false
post_type: "Jupyter Notebook"
summary: "{summary}"
tags: []
---

"""

def parse_arguments():
    """
    Parses command line arguments.
    We only need the input file path.
    """
    parser = argparse.ArgumentParser(description="Convert Jupyter Notebook to Hugo Markdown")
    parser.add_argument("notebook", help="Path to the .ipynb file to convert")
    return parser.parse_args()

def convert_notebook(notebook_path):
    """
    Runs the 'jupyter nbconvert' command to generate the initial Markdown.
    
    Why: 
    - 'nbconvert' is the gold standard for this. It handles code cells, 
      outputs, and extracts images into a side folder automatically.
    
    Returns:
    - properties: A dict containing paths to the generated .md file and the support files directory.
    """
    print(f"🔄 Converting {notebook_path}...")
    
    # Run the shell command: jupyter nbconvert --to markdown <file>
    # We use subprocess.run to execute it safely.
    result = subprocess.run(
        ["jupyter", "nbconvert", "--to", "markdown", notebook_path],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"❌ Error during conversion:\n{result.stderr}")
        sys.exit(1)
        
    # nbconvert creates a file with the same name but .md extension
    base_name = os.path.splitext(os.path.basename(notebook_path))[0]
    original_dir = os.path.dirname(notebook_path)
    
    # The generated markdown file path
    md_file = os.path.join(original_dir, f"{base_name}.md")
    
    # The generated resource directory (contains images/plots)
    # nbconvert convention: <notebook_name>_files
    files_dir = os.path.join(original_dir, f"{base_name}_files")
    
    return {
        "base_name": base_name,
        "md_path": md_file,
        "files_dir": files_dir if os.path.exists(files_dir) else None
    }

def process_content(md_path):
    """
    Reads the raw Markdown and performs Hugo-specific cleanups. 
    
    Tasks:
    1. Extract the Title (First H1 header).
    2. Remove the Title from the body (to avoid duplication with Hugo's title).
    3. Detect a summary (first paragraph).
    """
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    title = "Untitled Notebook"
    summary = "Generated from Jupyter Notebook"
    new_content = []
    
    title_found = False
    
    for line in lines:
        # Check for H1 header (# Title)
        # We only take the FIRST one we find as the main title.
        if line.startswith("# ") and not title_found:
            title = line.strip("# ").strip()
            title_found = True
            # We do NOT add this line to new_content, effectively removing it.
            continue
            
        new_content.append(line)
        
    return {
        "title": title,
        "summary": summary,
        "body": "".join(new_content)
    }

def organize_for_hugo(info, processed_data):
    """
    Moves the generated files into the Hugo content structure.
    
    Structure created:
    content/posts/
      └── {notebook_name}/       (Leaf Bundle Directory)
          ├── index.md           (The content file)
          └── {notebook_name}_files/  (Images)
    """
    base_name = info["base_name"]
    target_dir = os.path.join(CONTENT_DIR, base_name)
    
    # 1. Create the target directory (e.g., content/posts/my-notebook/)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"📁 Created directory: {target_dir}")
        
    # 2. Construct the final Front Matter + Body
    final_content = FRONT_MATTER_TEMPLATE.format(
        title=processed_data["title"],
        date=datetime.now().strftime("%Y-%m-%d"),
        summary=processed_data["summary"]
    ) + processed_data["body"]
    
    # 3. Write 'index.md'
    # Why 'index.md'? Hugo treats a folder with 'index.md' as a Leaf Bundle.
    # This allows us to keep the markdown and its images together in one folder.
    target_md_path = os.path.join(target_dir, "index.md")
    with open(target_md_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"✅ Wrote content to: {target_md_path}")
    
    # 4. Move the support files directory (images) if it exists
    if info["files_dir"]:
        source_files = info["files_dir"]
        target_files = os.path.join(target_dir, os.path.basename(source_files))
        
        # Remove existing target files dir if it exists (overwrite)
        if os.path.exists(target_files):
            shutil.rmtree(target_files)
            
        shutil.move(source_files, target_dir)
        print(f"🖼️  Moved images to: {target_files}")
        
    # 5. Clean up the original intermediate .md file generated by nbconvert
    if os.path.exists(info["md_path"]):
        os.remove(info["md_path"])

def main():
    args = parse_arguments()
    
    if not os.path.exists(args.notebook):
        print(f"❌ File not found: {args.notebook}")
        sys.exit(1)
        
    # Step 1: Convert .ipynb -> .md (raw)
    info = convert_notebook(args.notebook)
    
    # Step 2: Read and Process the Markdown (Extract Title, cleanup)
    processed_data = process_content(info["md_path"])
    
    # Step 3: Move to Hugo structure (Leaf Bundle)
    organize_for_hugo(info, processed_data)
    
    print("\n🎉 Conversion Complete! Run 'hugo server' to preview.")

if __name__ == "__main__":
    main()
