# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Working agreement — keep this file lean

When finishing any non-trivial task:

1. **Update this root `CLAUDE.md`** if the change affected architecture, conventions, or the design system in ways future sessions need to know about. Stale facts (e.g. line counts, file paths that moved, removed components) get fixed in the same commit.
2. **Refactor toward locality.** If a piece of guidance only applies to one directory (e.g. CSS-only rules, shortcode-only conventions), move it into a directory-local `CLAUDE.md` and leave a one-line pointer here under "Subdirectory references". The harness loads local `CLAUDE.md` files on demand, so locality = less context spent per session.
3. **One source of truth.** If a fact lives in `/DESIGN.md` or a directory `CLAUDE.md`, don't duplicate it here — link to it. Duplication rots.

Existing directory `CLAUDE.md` files:

- `assets/css/extended/CLAUDE.md` — CSS tokens, primitives, edit rules.
- `layouts/shortcodes/CLAUDE.md` — shortcode authoring conventions.

Add a new one whenever a directory accumulates rules >~150 words that don't apply elsewhere.

Topic guides at the repo root (read on demand):

- `DESIGN.md` — design system spec (Stitch format).
- `GIT_GUIDE.md` — commit message format (Conventional Commits, no emoji), commit granularity rules.

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

## Design system

`/DESIGN.md` is the authoritative design system for this site, written to the [Stitch DESIGN.md spec](https://stitch.withgoogle.com/docs/design-md/specification/). It defines brand color (Turbo Vermilion `#E14F2A`), the didactic role palette (think/act/observe/user/answer), neutral surface tints, the spacing scale, radius scale, and component conventions.

**Implementation lives in `assets/css/extended/custom.css`** — all tokens are defined as CSS variables in `:root` (and dark-mode overrides in `body.dark`). Every component below the token block consumes them via `var(--brand)`, `var(--role-think)`, `var(--space-md)`, `var(--radius-lg)`, etc. Hardcoded `rgb()`, `rgba()`, or `#hex` outside the token block is a system violation — fix it, don't add another.

The token block also defines typography (`--text-{xs..2xl}`), motion (`--transition-{fast,base,slow}`), and shadow (`--shadow-{sm,md,modal}`) scales — use those instead of magic values.

**Primitives** (`assets/css/extended/custom.css` — "Primitives" section): `.widget`, `.widget-header`, `.chip`, `.role-step`. Compose these into widget-specific classes via compound selectors (`<div class="widget react-loop">`) so each widget only carries CSS for what's unique to it. The `tokenizer-compare` shortcode is the reference migration — copy its pattern when authoring new dynamic-viz shortcodes.

When adding a new component, post, or shortcode:
1. Read `/DESIGN.md` for the relevant section (Colors, Layout, Components, Do's & Don'ts).
2. Compose the primitives above before writing custom CSS. Only add widget-specific rules for what's truly unique.
3. Use existing tokens. If a needed value doesn't exist, add a token to `:root` first, document it in DESIGN.md, then use it.
4. Inline SVG inside Markdown can reference CSS variables: `fill="var(--role-think)"`, `stroke="var(--brand)"` — the variable resolves at render time.
5. Verify both light and dark mode at desktop and mobile widths before declaring done.

### Subdirectory references (load on demand for harness efficiency)

- **`assets/css/extended/CLAUDE.md`** — read when editing `custom.css`: token map, primitives reference, hardcode-color audit command, light/dark validation steps.
- **`layouts/shortcodes/CLAUDE.md`** — read when authoring or modifying shortcodes: existing shortcode list, authoring conventions, primitive composition pattern, accessibility checklist.

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

All custom styles live in `assets/css/extended/custom.css` — PaperMod auto-includes files from this directory. See `assets/css/extended/CLAUDE.md` for the token map, primitives, and edit conventions. Key systems:

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

### Cover Images

Thumbnail ratio: **16:9**.

Style reference: `static/images/anime_coder.jpeg` — painterly anime illustration, moody warm desk lighting, detailed lived-in environment, cinematic feel. All cover images should feel like a scene from the same world as that image.

When suggesting an image prompt:
- Ground it in a **narrative scene** (character + environment + mood) tied to the post's topic — not a diagram, chart, or abstract concept
- Feature the same dark-haired coder in hoodie where it makes sense to maintain visual continuity across the series
- Include environmental storytelling details: cluttered desk, coffee cups, Linux penguin plushie, sticky notes, glowing screens
- End with: `painterly anime style, no text`
- Never specify aspect ratio in the prompt — the image tool handles that separately

Example for a post about "how agents think":
```
Anime illustration, same young dark-haired coder in hoodie leaning back in his chair staring at a small friendly robot sitting on his desk; the robot has its chest panel open and a soft warm glow spilling out, casting light on the coder's face and the cluttered desk — coffee cups, sticky notes, a Linux penguin plushie; moody warm ambient lighting, detailed environment, painterly anime style, no text
```

### Notebook Conversion

`scripts/convert_notebook.py` converts `.ipynb` → Hugo leaf bundle:
1. Runs `jupyter nbconvert --to markdown`
2. Extracts first H1 as title, injects YAML front matter with `post_type: "Jupyter Notebook"`, date, empty summary
3. Moves output to `content/posts/{name}/index.md` with images in `{name}_files/`

## Multilingual

English (default) and Thai. Language strings in `i18n/{en,th}.yaml` (currently only TOC label translated). Thai content served under `/th/` prefix. Each language has its own profile title/subtitle/buttons configured in `hugo.yaml` under `languages.th.params`.
