# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development

```bash
# Local development (includes drafts)
hugo server -D

# Production build
hugo --minify -d dist
npx pagefind --site dist

# Convert Jupyter notebook to Hugo post (leaf bundle)
python3 scripts/convert_notebook.py path/to/notebook.ipynb
```

- Hugo: 0.146.0 (extended), Go: 1.25.5
- Deployment: GitHub Actions (`.github/workflows/hugo.yaml`) builds Hugo + Pagefind on push to `main`, deploys to GitHub Pages at `tbb3kernel.github.io`. Build timezone is Asia/Bangkok.

## Architecture

Hugo static site using the **PaperMod** theme (via Go modules, not forked). All customization happens through layout overrides, CSS extensions, and footer-injected JS — the theme itself is never modified.

### Layout Override Chain

PaperMod provides base layouts. This repo overrides specific templates in `layouts/`:

- **`index.html`** — Custom homepage: profile card + "Selected Work" / "Recent Writing" sections (pulls from `projects` and `posts` sections, 3 entries each)
- **`_default/single.html`** — Post layout with left-sidebar TOC grid (280px sidebar + content on desktop ≥1200px, stacked on mobile)
- **`_default/list.html`** — Standard PaperMod list with profileMode branch for homepage
- **`_default/search.html`** — Dedicated `/search` route with inline Pagefind UI initialization
- **`partials/post_entry.html`** — Card component with `post_type` badge support (renders "Jupyter Notebook", "Blog Post" etc. from front matter)
- **`partials/index_profile.html`** — Profile card (photo resized to 300×300 for HiDPI, title, subtitle, social icons, CTA buttons)
- **`partials/extend_footer.html`** — PaperMod's extension point. Contains all custom JS (299 lines): table wrapper/pandas index detection, Cmd+K search modal (lazy-loads Pagefind), TOC toggle, ScrollSpy, notebook output labeling
- **`shortcodes/plotly.html`** — `{{< plotly json="path" height="400px" >}}` for interactive Plotly charts

### CSS

All custom styles live in `assets/css/extended/custom.css` (1177 lines) — PaperMod auto-includes files from this directory. Key systems:

- **Content width**: `--main-width: 1000px` (wider than PaperMod default for data tables/code)
- **Booktabs tables**: Scientific-style with no vertical borders, thick top/bottom rules. JS auto-wraps tables for horizontal scroll and hides pandas DataFrame index columns (`.has-index` class). DataFrames with 8+ rows get `.tall-table` (max-height 600px, scrollable). Long cells (>300 chars) get `.cell-scroll` (max-height 200px, scrollable).
- **Sidebar TOC**: CSS Grid layout with sticky positioning, collapse animation, active-state border on scroll (ScrollSpy via IntersectionObserver). Nested lists indented.
- **Mobile TOC**: Below 1200px — FAB button fixed bottom-left (44px circle) toggles `.toc-mobile-open`; TOC renders as card below content, not sidebar.
- **Cmd+K search modal**: Fixed overlay with backdrop blur, 600px max-width, 80vh max-height. Pagefind UI style overrides for both themes.
- **Dark mode**: All components use PaperMod CSS variables (`--primary`, `--secondary`, `--border`, `--entry`, `--theme`) with `body.dark` overrides where needed.

### JavaScript (extend_footer.html)

All custom JS is footer-injected. Key behaviors:

- **Table wrapping**: Auto-wraps all tables in `.table-wrapper` for horizontal scroll; detects pandas DataFrames by header pattern.
- **Notebook output detection**: Elements directly after code blocks are labeled `.notebook-output` with an "Output" label.
- **Search modal**: Nav link with `href="#search"` is transformed to show "Search... ⌘K" hint; Pagefind JS/CSS lazy-loaded on first open; Escape closes.
- **TOC toggle**: Desktop toggles `.toc-collapsed` on the grid (sidebar collapses with opacity/visibility animation). Mobile toggles `.toc-mobile-open` and FAB visibility.
- **ScrollSpy**: IntersectionObserver tracks active heading and updates `.active` class on TOC links.

### Search

Pagefind-based static search. Index is generated post-build (`npx pagefind --site dist`). The search modal in `extend_footer.html` lazy-loads Pagefind JS/CSS on first open. Triggered by clicking the nav "Search..." element or pressing Cmd+K / Ctrl+K.

**Important**: Search won't work in `hugo server` dev mode — the Pagefind index only exists after a production build.

## Content

### Front Matter

```yaml
title: ""
date: YYYY-MM-DD
draft: false
post_type: "Jupyter Notebook"  # Optional — renders badge in list views
summary: ""
tags: []
```

### Content Types

- **Posts** (`content/posts/`): Blog articles. Jupyter-converted posts use leaf bundles (`post-name/index.md` + images). Standard posts are single `.md` files.
- **Projects** (`content/projects/`): Portfolio entries. Single `.md` files.
- **About** (`content/about.md`): Uses HTML highlights grid (`<div class="about-highlights">`) and skill tags (`<div class="skill-tags">`). Unsafe HTML rendering is enabled in `hugo.yaml`.
- **Archives** (`content/archives.md`): Standard PaperMod archive list.
- **Search** (`content/search.md`): Triggers the `_default/search.html` template; actual search UI rendered by Pagefind.

### Notebook Conversion

`scripts/convert_notebook.py` converts `.ipynb` → Hugo leaf bundle:
1. Runs `jupyter nbconvert --to markdown`
2. Extracts first H1 as title, injects YAML front matter with `post_type: "Jupyter Notebook"`, date, empty summary
3. Moves output to `content/posts/{name}/index.md` with images in `{name}_files/`

## Multilingual

English (default) and Thai. Language strings in `i18n/{en,th}.yaml` (currently only TOC label translated). Thai content served under `/th/` prefix. Each language has its own profile title/subtitle/buttons configured in `hugo.yaml` under `languages.th.params`.
