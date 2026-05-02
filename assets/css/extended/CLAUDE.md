# assets/css/extended/CLAUDE.md

Scoped notes for editing `custom.css`. The full design system spec is `/DESIGN.md`. Read that first; this file documents the *implementation* conventions.

## File order matters

PaperMod auto-includes every file in this directory in alphabetical order. There is currently one file (`custom.css`), but if it ever splits, name files `00-tokens.css`, `01-base.css`, `10-primitives.css`, `20-widgets/*.css` etc. so the cascade stays predictable.

## Tokens (defined in `:root`, dark overrides in `body.dark`)

| Group | Vars |
|---|---|
| Brand | `--brand`, `--brand-emphasis`, `--brand-tint`, `--brand-on` |
| Roles | `--role-{user,think,act,observe,answer,error}` + `*-tint` variants |
| Tints | `--tint-{04,06,08,10,12,15,18}` — neutral `rgba(127,127,127,N)` |
| Spacing | `--space-{xs,sm,md,lg,xl,xxl}` — 4/8/16/24/40/64px |
| Radius | `--radius-{sm,md,lg,pill}` — 4/8/12/999px |
| Type | `--text-{xs,sm,base,md,lg,xl,2xl}` — 12/13/14/16/18/24/32px |
| Motion | `--transition-{fast,base,slow}` — 0.12/0.2/0.4s |
| Shadow | `--shadow-{sm,md,modal}` |

Surface tokens come from PaperMod and are **not redefined**: `--primary`, `--secondary`, `--border`, `--theme`, `--entry`, `--code-bg`, `--tertiary`.

## Primitives (compose into widgets)

These live near the top of `custom.css` under "Primitives — reusable building blocks". When building a new dynamic-viz widget, **compose these first**; only add widget-specific CSS for what's truly unique.

- `.widget` — card container (border + radius-lg + padding-md + margin-xl + entry bg). Modifiers: `.widget--inset`, `.widget--flat`.
- `.widget-header` — flex row, `space-between`, with `.widget-header__title`, `.widget-header__sub`, `.widget-header__controls` slots.
- `.chip` — pill button. Modifiers: `.chip--active` (also responds to `[aria-pressed="true"]`), `.chip--square`, `.chip--ghost`.
- `.role-step` — role-coded teaching step. Reads `data-role="user|think|act|observe|answer|error"` for the left-border color. Adds `.is-current` for the active step.

Compound class pattern in HTML: `<div class="widget react-loop">` — `.widget` provides chrome, `.react-loop` provides only what's unique.

## Hard rules

1. **No hardcoded colors below the token block.** Anywhere a `#hex`, `rgb(`, or `rgba(` appears outside `:root`/`body.dark`, fix it. Only documented exceptions: `transparent`, `currentColor`, true black/white. Decorative gradients (e.g. `.cmp-fill`) currently use literal HSL — flag if you touch them.
2. **No new gray.** Use a `--tint-*` step. If the alpha you need isn't there, add the token.
3. **No magic radii or paddings.** Use the scale (`--radius-*`, `--space-*`).
4. **Don't override PaperMod surface vars** (`--primary`, `--theme`, etc.). Add new tokens alongside; never replace.
5. **Don't add `box-shadow` ad-hoc.** Use `--shadow-*` or extend the scale. Depth is borders + tonal layers first.

## Validation when adding/editing

```bash
# Hex/rgba audit — should match only :root, body.dark, and known exceptions
rg -n 'rgba?\(|#[0-9a-fA-F]{3,8}\b' assets/css/extended/custom.css

# Build test
hugo -d /tmp/hugo-test
```

Test light + dark at desktop (≥1200px) and mobile (≤700px) before declaring done.

## Common gotchas

- The `cat -s` + brace-aware awk pass collapses blank lines inside rule blocks; if a future linter reflows the file with new whitespace, run that pass again instead of hand-formatting.
- Hugo PaperMod's `--code-bg` and `--tertiary` are surface tokens we depend on but don't define here.
- `.cmp-fill` and a couple of token-pill rules use literal `hsl(...)` for didactic gradients — these are scheduled to migrate to role tokens but are not violations *yet*.
