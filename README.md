# kriscarta.com

Source for [kriscarta.com](https://www.kriscarta.com). Hugo, deployed to GitHub Pages via Actions on push to `master`.

## Local dev

```sh
brew install hugo
hugo server -D   # http://localhost:1313, -D includes drafts
```

CI pins the Hugo version in `.github/workflows/deploy.yml`.

## New post

`content/posts/YYYY-MM-DD-slug.md` (URL `/posts/slug/`, date from the filename):

```yaml
---
title:  "The title"
date:   2026-05-21 00:00:00 +0000
tags: [thoughts, ai]
---
```

Link to another post: `[text]({{< relref "2024-11-18-rad-llms.md" >}})` (build fails if it doesn't exist).

Drafts = untracked files in `content/posts/`, or `draft: true`. Push when ready.

## Tags

Any tag in front matter gets a `/tag/<name>/` page.

## Feeds

`/feed.xml` (last 10) and `/feed-emacs.xml` (last 10 tagged `emacs`, read by Planet Emacslife), both from `layouts/_partials/rss.xml`.
Item guid/link/pubDate must not change, or readers re-show old posts. CI runs `.github/scripts/check-feeds.py` against the live feeds before deploying.

## Layout

- `content/posts/` — posts; `content/about.md`, `content/now.md`
- `layouts/` — `baseof`, `home`, `page`, `posts/page`, `term` (tag pages), feeds
- `static/` — served at `/static/`: `css/main.css` (plain CSS), post images in `img/posts/`
- `assets/icons/` — social icon SVGs, inlined by `layouts/_partials/icon.html`
- `.github/workflows/deploy.yml` — build, feed check, deploy

## Credits

Originally forked from [agusmakmun/agusmakmun.github.io](https://github.com/agusmakmun/agusmakmun.github.io).
