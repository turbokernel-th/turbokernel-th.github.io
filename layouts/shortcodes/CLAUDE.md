# layouts/shortcodes/CLAUDE.md

Scoped notes for authoring Hugo shortcodes. Companion to `assets/css/extended/CLAUDE.md` (CSS primitives) and `/DESIGN.md` (tokens).

## Existing shortcodes

| Shortcode | Primitives used | Purpose |
|---|---|---|
| `react-loop` | widget, widget-header, role-step | Animated ReAct walkthrough (think → act → observe → answer with role coloring) |
| `tokenizer` | widget, widget-header, chip | Live tokenizer with encoding selector and presets |
| `tokenizer-compare` | widget, widget-header, chip | Bar-chart comparison of tokenization strategies |
| `bpe-merge` | widget, widget-header, chip | Step-through animation of BPE building tokens from a toy corpus |
| `chatbot-vs-agent` | widget | Side-by-side comparison: chatbot transcript vs agent with tool calls |
| `img-placeholder` | — | Drafting aid: dashed-frame image placeholder with copyable Imagen prompt |
| `plotly` | — | Embed Plotly chart from JSON file |
| `gdrive` | — | Embed Google Drive video |

All five interactive widgets share the same `.widget` chrome and `.widget-header` flex header. When in doubt, copy the structure from `tokenizer-compare.html` (smallest, cleanest reference).

## Authoring conventions

### 1. Compose primitives, don't reinvent chrome

Reach for these CSS primitives (see `assets/css/extended/CLAUDE.md` for the full list):

- `.widget` — card container. Use as `<div class="widget my-widget">` so widget-specific CSS only declares what's unique.
- `.widget-header` — flex row with `__title`, `__sub`, `__controls` slots.
- `.chip` — pill button. Toggle `.chip--active` (not `.active`) for selected state in JS.
- `.role-step` — role-coded step block. Reads `data-role="user|think|act|observe|answer|error"`.

**Reference migration:** `tokenizer-compare.html` was migrated to use `.widget` + `.widget-header` + `.chip`. Look there before authoring a new shortcode.

### 2. Unique IDs

Use the Hugo idiom for collision-free IDs across multiple shortcode instances on one page:

```go-html-template
{{- $id := printf "myviz-%s" (substr (sha1 (string .Ordinal)) 0 8) -}}
<div class="widget my-widget" id="{{ $id }}">…</div>
```

### 3. JS bootstrap pattern

Each shortcode ships its own `<script type="module">`. Use the `data-bound` guard so re-initializations (e.g. live reload) don't double-bind:

```js
const root = document.getElementById('{{ $id }}');
if (!root || root.dataset.bound) return;
root.dataset.bound = '1';
```

### 4. Use design tokens in inline styles and SVG

Inline SVG can reference CSS variables — they resolve at render time:

```html
<svg ...>
  <rect fill="var(--role-think-tint)" stroke="var(--role-think)" />
</svg>
```

Don't hardcode hex/rgba in shortcode HTML or inline `style=""` attributes.

### 5. Animations and transitions

Use `--transition-fast` / `--transition-base` / `--transition-slow` from CSS. JS-driven progressive reveals (e.g. `react-loop` step counter) should respect `prefers-reduced-motion`.

### 6. Accessibility

- Buttons need a `type="button"` attribute (not `type="submit"`).
- Provide `aria-label` on icon-only controls.
- Toggle states should also set `aria-pressed="true"` — `.chip` listens for both `.chip--active` and `[aria-pressed="true"]`.
- Decorative SVGs get `aria-hidden="true"`.

## When NOT to use a shortcode

- One-off images: just use Markdown image syntax.
- Static diagrams that don't need interactivity: write inline SVG in the post (it can reference `var(--role-*)` directly).
- Heavy data viz: prefer the `plotly` shortcode pointing to a JSON file in `static/` over inlining everything.

## Checklist before merging a new shortcode

1. Composes `.widget` + `.widget-header` + `.chip` where applicable, doesn't redeclare card/header/button styles.
2. Unique ID via `.Ordinal + sha1`.
3. JS uses `data-bound` guard.
4. No hardcoded colors.
5. Tested in both light and dark mode.
6. Tested at mobile width (≤700px).
7. CSS additions live near other widget-specific blocks in `custom.css`, not inline.
