# GIT_GUIDE.md

Conventional Commits — `type(scope): subject`. No emoji. Lowercase, imperative, ≤72 chars, no trailing period. Body explains *why*.

## Types
`feat` `fix` `refactor` `style` `docs` `chore` `perf` `test` `revert`

## Scopes
`css` `shortcode` `layout` `blog` `i18n` `search` `toc` `build` `design`

## Granularity
One logical change per commit. Each commit must build on its own. If the body needs "also" or unrelated files are touched, split.

## Examples
```
refactor(css): extract widget, chip, role-step primitives
feat(blog): add python functional programming post
fix(toc): scrollspy missing first heading on long posts
docs(design): document text, motion, shadow scales
```

## Anti-examples
- `Update CSS` — no type, vague
- `feat: stuff` — no scope, no detail
- `fix(css): fixed bug` — past tense
- `add new post.` — trailing period, no type

## Branching
`main` auto-deploys via GitHub Actions. Non-trivial work goes via PR; trivial fixes (typos, content) can land directly.
