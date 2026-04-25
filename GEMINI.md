# Project Overview

This project is a personal portfolio and blog for **Metee Yingyong**, an AI Software Engineer. Built with [Hugo](https://gohugo.io/) and the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, it features multilingual support (English/Thai) and a focus on technical content like Jupyter Notebooks and Agentic AI research.

## Key Technologies

- **Static Site Generator:** Hugo (Extended)
- **Theme:** PaperMod (Go Modules)
- **Search:** Pagefind (Static search)
- **Notebook Conversion:** Jupyter nbconvert
- **Deployment:** GitHub Actions to `dist` directory.

## Building and Running

### Commands

#### Local Development
```bash
hugo server -D
```

#### Production Build
```bash
hugo --minify -d dist
npx pagefind --site dist
```

## Utility Scripts

The project includes custom scripts for content automation:

### Jupyter Notebook Conversion
Convert a `.ipynb` file to a Hugo Leaf Bundle (Markdown + Images) with scientific styling:
```bash
python3 scripts/convert_notebook.py path/to/notebook.ipynb
```
- **Features:** Extracts titles, injects front matter, handles images, and applies `post_type: "Jupyter Notebook"`.

## Styling & UX Refinements

Custom styles and behaviors are managed in `assets/css/extended/custom.css` and `layouts/partials/extend_footer.html`:

- **Main Content Width:** Expanded to **1000px** for wide dataframes and code.
- **Profile Card:** Increased to **600px** max-width for better visual presence.
- **Header Spacing:** Reduced top margin (`40px`) for a tighter connection between navigation and content.
- **Scientific Tables (Booktabs Style):** 
  - Minimalist design: No vertical borders, thick top/bottom rules, thin header rules.
  - Tabular numbers for alignment.
  - Automatically scrollable via JS wrapper.
  - **Pandas Index Detection:** Automated JS logic hides the redundant index column in DataFrames.
- **Post Badges:** Blog list cards display badges (e.g., "Jupyter Notebook", "Blog Post") based on `post_type` front matter.
- **Dark Mode:** Fully theme-aware components including tables, navigation, search modal, and code blocks.

## Sidebar Navigation (Table of Contents)

The site features a highly customized sidebar for blog posts:
- **Positioning:** Fixed to the **left side** on desktop for optimized reading flow.
- **Toggleable:** A "Table of Contents" (or "เนื้อหา") button in the post header allows users to show/hide the sidebar.
- **ScrollSpy:** Automatically highlights the current section in the sidebar as the user scrolls.
- **Sticky Layout:** Remains visible while scrolling through long technical articles.
- **Responsive:** Hidden by default on mobile to save space, but toggleable via the header button.
- **Multilingual:** Fully localized using Hugo's `i18n` system (English/Thai).

## Search Feature (Cmd+K)

The site uses a customized local search implementation via Pagefind:
- **Trigger:** A "fake" search bar in the navigation with a search icon and `⌘K` badge.
- **Modal:** Responsive modal with backdrop blur, dark-mode aware, and keyboard focus management.
- **Keyboard Shortcut:** `Cmd+K` (Mac) or `Ctrl+K` (Linux/Windows) to toggle the search interface.
- **Indexing:** Static search index is generated post-build and queried locally for high performance.

## Interactive Visualizations

The site supports interactive Plotly graphs via a custom shortcode:
- **Usage:** `{{< plotly json="path/to/graph.json" height="400px" >}}`
- **Mechanism:** Fetches a JSON file containing Plotly data and layout, then renders it using `plotly-latest.min.js`.

## Content Management

- **About Me:** Synced with the latest professional profile, detailing experience at Saifa AI (Agentic AI), Data Wealth, and GBDi.
- **Blog Posts:** Supports standard Markdown and Jupyter-converted notebooks.

## Project Structure

- **`scripts/`**: Automation tools for content processing.
- **`i18n/`**: Localization strings for multilingual support (e.g., TOC labels).
- **`layouts/_default/single.html`**: Overridden to support the left-sidebar grid layout and TOC toggle.
- **`layouts/partials/post_entry.html`**: Overridden to support custom badges in lists.
- **`layouts/partials/extend_footer.html`**: Injects JS for table wrapping, search modal, and **TOC ScrollSpy/Toggle logic**.
- **`layouts/shortcodes/`**: Custom shortcodes (e.g., Plotly).
- **`assets/css/extended/custom.css`**: Central location for all design overrides, including Booktabs tables, Search modal, and **Sidebar TOC layout**.
