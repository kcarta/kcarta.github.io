# kriscarta.com

Source for [kriscarta.com](https://www.kriscarta.com). Jekyll 4, deployed to GitHub Pages via Actions on push to `master`.

## Local dev

```sh
bundle install
bundle exec jekyll serve   # http://127.0.0.1:4000
```

Restart on `_config.yml` changes.

## New post

`_posts/YYYY-MM-DD-slug.md`:

```yaml
---
layout: post
title:  "The title"
date:   2026-05-21 00:00:00 +0000
tags: [thoughts, ai]
---
```

Drafts = untracked files in `_posts/`. Push when ready.

## Tags

Current: `agile-pm`, `ai`, `emacs`, `integrations`, `non-software`, `reading`, `teams`, `testing`, `thoughts`, `tools`.

To add a new one, create `tag/foo.md`, or `/tag/foo` 404s:

```yaml
---
layout: posts_by_tag
tags: foo
title: foo
permalink: /tag/foo
---
```

## Layout

- `_layouts/` — `default`, `page`, `post`, `posts_by_tag`
- `_posts/` — posts (+ untracked drafts)
- `tag/` — one stub per tag
- `static/img/posts/` — post images
- `.github/workflows/jekyll.yml` — build + deploy

## Credits

Forked from [agusmakmun/agusmakmun.github.io](https://github.com/agusmakmun/agusmakmun.github.io).
