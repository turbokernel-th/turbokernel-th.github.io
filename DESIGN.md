---
version: alpha
name: Turbo Engineer's Notebook
description: >-
  Design system for Metee Y \ Turbo 🚀 — a personal blog blending technical
  precision with warm, conversational prose. Vermilion accent on neutral
  surfaces, scientific tables, generous whitespace, theme-aware everything.

colors:
  brand: "#E14F2A"
  brand-emphasis: "#C0411F"
  brand-tint: "#FCEEE9"
  brand-on: "#FFFFFF"

  brand-dark: "#FF6B45"
  brand-emphasis-dark: "#FF8A6F"
  brand-tint-dark: "rgba(255, 107, 69, 0.14)"
  brand-on-dark: "#1A1B1D"

  role-user: "#3B7BD9"
  role-think: "#7C5CFF"
  role-act: "#E2A038"
  role-observe: "#2DB482"
  role-answer: "#3B7BD9"
  role-error: "#B45050"

  tint-04: "rgba(127, 127, 127, 0.04)"
  tint-06: "rgba(127, 127, 127, 0.06)"
  tint-08: "rgba(127, 127, 127, 0.08)"
  tint-10: "rgba(127, 127, 127, 0.10)"
  tint-12: "rgba(127, 127, 127, 0.12)"
  tint-15: "rgba(127, 127, 127, 0.15)"
  tint-18: "rgba(127, 127, 127, 0.18)"

typography:
  body:
    fontFamily: system-ui
    fontSize: 18px
    lineHeight: 1.7
    fontWeight: 400
  body-mono:
    fontFamily: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace
    fontSize: 14px
    lineHeight: 1.5
  h1:
    fontFamily: system-ui
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
  h2:
    fontFamily: system-ui
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
  h3:
    fontFamily: system-ui
    fontSize: 19px
    fontWeight: 600
    lineHeight: 1.3
  caption:
    fontFamily: system-ui
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5

rounded:
  sm: 4px
  md: 8px
  lg: 12px
  pill: 999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  base: 16px

components:
  link:
    color: "{colors.brand}"
    color-hover: "{colors.brand-emphasis}"
    underline-offset: 3px
  button-primary:
    backgroundColor: "{colors.brand}"
    backgroundColor-hover: "{colors.brand-emphasis}"
    textColor: "{colors.brand-on}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.secondary}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  card:
    backgroundColor: "{colors.entry}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  blockquote:
    backgroundColor: "{colors.brand-tint}"
    borderLeft: "3px solid {colors.brand}"
    padding: "{spacing.md}"
    rounded: "0 {rounded.md} {rounded.md} 0"
  table:
    borderTop: "2px solid {colors.primary}"
    borderBottom: "2px solid {colors.primary}"
    headerBorderBottom: "1px solid {colors.primary}"
    rowBorderBottom: "1px solid {colors.border}"
    rowStripe: "{colors.tint-04}"
    rowHover: "{colors.tint-08}"
---

# Turbo Engineer's Notebook — Design System

## Overview

A personal-blog design system for technical writing that wants to feel like an **engineer's notebook**: information-dense, scientifically precise, but warm and conversational where prose lets it. The reader is here to learn — every choice serves comprehension first, aesthetics second.

Three constants:

- **Vermilion brand, used sparingly.** A single warm accent (echoing the rocket favicon) reserved for links, primary buttons, focus, and active markers. Never on body copy or large surfaces.
- **Theme-aware via PaperMod.** Surfaces, primary text, and borders follow the PaperMod variables (`--primary`, `--secondary`, `--border`, `--theme`, `--entry`) so the site's light/dark toggle keeps working without a rewrite. Brand and role tokens have their own dark-mode variants.
- **Didactic role palette.** Teaching diagrams (the ReAct loop, context stack, chatbot-vs-agent) use a fixed five-role palette. These colors **never** appear in chrome — only inside diagrams. This keeps "what's clickable" visually distinct from "what's instructional."

The implementation lives in `assets/css/extended/custom.css` (token definitions in `:root` at the top of the file). Every component below references those tokens via CSS variables — no hardcoded colors.

## Colors

The palette has three layers, used for different jobs.

**Brand (`brand-*`):**

- **`#E14F2A` / `#FF6B45` (dark):** "Turbo Vermilion." Links, primary buttons, focus rings, the active TOC marker, blockquote bars. Saturated enough to draw the eye, warm enough to feel inviting. *Goal: ≤2% of pixels on any given page.*
- **`#C0411F` / `#FF8A6F`:** Brand-emphasis for hover and pressed states.
- **`#FCEEE9` / `rgba(255,107,69,0.14)`:** Brand-tint for selection, blockquote backgrounds, subtle highlights.

**Didactic roles (`role-*`):**

| Token | Hex | Used for |
|---|---|---|
| `role-user` / `role-answer` | `#3B7BD9` | The human side of a transcript — input and final answer. |
| `role-think` | `#7C5CFF` | The LLM reasoning step in a ReAct trace. |
| `role-act` | `#E2A038` | A tool call. (Amber, deliberately *not* orange — to stay distinct from the brand.) |
| `role-observe` | `#2DB482` | A tool result coming back. |
| `role-error` | `#B45050` | Failure markers in comparisons (e.g. "chatbot can't fetch"). |

Each role color also has a `*-tint` variant at ~12% alpha for fills behind text and diagram backgrounds.

**Neutral surface tints (`tint-*`):**

Range from `tint-04` (subtle striping) to `tint-18` (strong dividers). All are `rgba(127, 127, 127, ...)` so they read consistently in both themes without a theme switch. Use these for:

- Table row striping and hover
- Card backgrounds inside cards
- Dashed dividers between sub-elements
- "Pressed" states for ghost buttons

**Surface tokens come from PaperMod:** `--primary` (text), `--secondary` (muted text), `--theme` (page background), `--entry` (card background), `--border` (rules). DESIGN.md does not redefine these; it inherits them so the theme toggle keeps working.

## Typography

The system stays on PaperMod's font stack — system-ui for prose, SFMono / Consolas for code — chosen for zero FOIT, native rendering at every size, and the "engineer's notebook" voice (no novelty face). Hierarchy is built with size and weight, not typeface variety.

- **Body:** 18px / 1.7 line-height. Generous line-height because most posts have technical asides; readers' eyes need air.
- **Code:** Inherits PaperMod's monospace at ~0.9× body. Inline code is tinted; block code uses `--code-bg`.
- **Headings:** 600–700 weight, tightly tracked. Section headings (`h2`) bear a top margin of `--space-xl` to make sections visibly distinct.
- **Labels and captions:** 12–13px, often in monospace for technical metadata (token IDs, file paths, step counters).

## Layout

The site uses a single content column at **1000px max-width** (`--main-width`) — wider than the PaperMod default to keep wide tables and code samples readable without horizontal scroll on most posts.

On posts ≥1200px viewport, a **left-aligned sidebar TOC** uses CSS Grid (`280px sidebar + 1fr content`). Below 1200px the TOC collapses into a floating action button (FAB) at bottom-left.

**Spacing scale (8px base):**

- `xs` 4px — chip padding, micro-gaps inside dense rows
- `sm` 8px — small gaps, icon-to-label
- `md` 16px — default block padding, gaps between paragraphs, form field padding
- `lg` 24px — gaps between major content blocks, blockquote vertical margin
- `xl` 40px — section breaks (`h2` top margin)
- `xxl` 64px — page-level separators (rare)

Use these via `var(--space-md)` etc. Never invent ad-hoc pixel values for new components.

## Elevation & Depth

Depth is achieved through **borders and tonal layers**, not shadows. The exception is the Cmd+K search modal, which uses a soft shadow + backdrop blur to lift it above scrolled content.

- **Cards** (e.g. `.react-loop`, `.chatbot-vs-agent`, `.tokenizer-widget`): 1px `var(--border)` outline, `var(--entry)` fill, `var(--radius-lg)` corners.
- **Inset surfaces** (mini-steps, transcripts inside cards): `var(--tint-04..tint-08)` fill, no border, `var(--radius-md)` corners.
- **Modals:** `var(--theme)` background, large radius, `box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1)` only.

The flat-with-borders aesthetic keeps the page calm and prints well; shadows are visual debt that don't survive zoom or print.

## Shapes

Corner radii follow a tight scale:

- `sm` 4px — pill chips, small badges, code inline highlights
- `md` 8px — buttons, inputs, mini-steps, table cells
- `lg` 12px — cards, modals, large containers
- `pill` 999px — fully rounded chips, dots, progress bars

Visual shape language is **soft-but-not-bubbly.** Cards and inputs share `md`/`lg` radii; nothing is sharp-cornered (modern but not brutalist) and nothing is fully circular except deliberate UI dots and avatars.

## Components

All components are documented in code at `assets/css/extended/custom.css` and consume tokens via CSS variables. Notable ones:

- **`.react-btn-primary`** — primary action button. Uses `--brand` background, `--brand-on` text, `--radius-md`, hovers to `--brand-emphasis`.
- **`.react-btn-ghost`** — secondary action. Transparent fill, `--secondary` text, `--border` outline, hovers to `--primary` text + `--secondary` border.
- **`.tool-tile`** — info card in a grid (`.tool-grid`). `--entry` background, `--border` outline, `--radius-lg` corners, vertical layout: icon → name → description.
- **`.react-step`** — one step in a ReAct walkthrough. Role-coded left border (`--role-user/think/act/observe/answer`), `--tint-04` fill, `--radius-md` (right side).
- **`.cva-bubble-bot` / `.cva-bubble-agent`** — chat-style bubbles in the chatbot-vs-agent comparison. Role-tint fill, role-color left border.
- **`.tokenizer-widget`, `.bpe-stage`** — interactive teaching widgets in the token post. Same card pattern as above.
- **`.img-placeholder`** — drafting aid: dashed-border frame with description and copyable Imagen prompt.
- **Inline SVG diagrams** (loop diagram, context stack) — `viewBox` for fluid scaling, role colors via `var(--role-*)` so they re-skin automatically with the rest of the system.

## Do's and Don'ts

- **Do** consume all colors via CSS variables. Hardcoded `rgb()`, `rgba()`, or `#hex` in `custom.css`, shortcodes, or inline post SVG is a system violation — except for documented OS-rendering exceptions (`black`, `white`, `transparent`, true `currentColor`).
- **Do** use the brand color sparingly: links, primary buttons, focus rings, active markers. If brand color appears in three new places on one component, one of them is wrong.
- **Do** keep didactic role colors *inside* teaching diagrams. A ReAct-purple text color in body copy is a system violation — that purple has a meaning ("LLM reasoning") and using it elsewhere muddies the meaning.
- **Do** maintain WCAG AA contrast (4.5:1 normal text, 3:1 large text) in both themes. Brand on white passes; brand-tint as background needs `--brand-emphasis` text on top.
- **Don't** introduce a new neutral gray. Use the `tint-*` scale. If you need an alpha not in the scale, add a token to `:root` first.
- **Don't** mix scales — radii are 4 / 8 / 12 / pill, full stop. No 6px, no 10px, no 16px-corner card.
- **Don't** add shadows for hierarchy. Use borders, tonal layers, and the `tint-*` scale.
- **Don't** override PaperMod's `--primary`, `--secondary`, `--theme`, `--entry`, `--border` — they are the surface system. Add tokens alongside them, never replace them.

## Validation

When adding a new component or post:

1. Open `assets/css/extended/custom.css` and confirm new rules use only `var(--*)` for colors, spacing, and radii.
2. Test light + dark mode at desktop (≥1200px) and mobile (≤700px) widths.
3. Run `grep -E "rgba?\(|#[0-9a-fA-F]{3,6}"` against any new file. The only matches should be in token definitions inside `:root` or `body.dark`, or inside post-content SVG that explicitly references `var(--role-*)` (the variable lives in CSS, the SVG just substitutes it at render time).
4. For diagrams, verify role colors actually carry their meanings — `role-think` for reasoning steps, `role-act` for tool calls, `role-observe` for tool results, `role-user`/`role-answer` for the human-facing endpoints.
