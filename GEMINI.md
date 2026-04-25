# Project Overview: Turbo's AI Blog & Portfolio

Welcome! This repository houses the personal portfolio and technical blog of **Metee Yingyongwatthanakit**, an AI Software Engineer specializing in Agentic AI and data-driven solutions.

The site is built using the [Hugo](https://gohugo.io/) static site generator with a heavily customized version of the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme. It serves as a central hub for sharing research, professional projects, and technical tutorials in both English and Thai.

### Core Features

*   **Multilingual Support:** Seamlessly switch between English and Thai content.
*   **Agentic AI Focus:** Dedicated sections for research on LLM workflows, RAG optimization, and autonomous agents.
*   **Technical Content Automation:** Includes a Python-based pipeline to convert Jupyter Notebooks directly into Hugo blog posts, preserving scientific formatting and interactive elements.
*   **Optimized Reading Experience:**
    *   Expanded layout (1000px) for better visualization of dataframes and code blocks.
    *   Scientific-style tables (Booktabs) with automated index column handling.
    *   A custom sticky Table of Contents (TOC) for easy navigation through long-form technical articles.
    *   Integrated local search powered by Pagefind (Cmd+K).

### Getting Started

To run the development server locally:
```bash
hugo server -D
```

To generate a production build with search indexing:
```bash
hugo --minify -d dist
npx pagefind --site dist
```

### Automation Scripts

You can convert a Jupyter Notebook into a site-ready post using the provided script:
```bash
python3 scripts/convert_notebook.py path/to/notebook.ipynb
```

### Connect with Me

*   **LinkedIn:** [Metee Yingyongwatthanakit](https://www.linkedin.com/in/metee-yingyong/)
*   **GitHub:** [turbokernel-th](https://github.com/turbokernel-th)
*   **Email:** metee.ying@gmail.com
