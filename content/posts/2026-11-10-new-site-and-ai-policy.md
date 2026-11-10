---
title:  "New site and AI policy"
date:   2026-11-10 00:00:00 +0000
tags: []
---

## Goodbye, Jekyll

I have a backlog of articles that I've been meaning to finish and publish, but time has not been on my side.

Part of the issue is the friction and distraction involved every time I come around to finally write an article. This site is built on Jekyll, on the Ruby toolchain, and as my only long-lasting Ruby project in recent years,[^1] this site incurs a dependency upgrade headache seemingly every time I touch it. The time between posts seems to be just enough for my toolchain to get out of date, and for me to completely forget the specific upgrade sequence.

In previous years, I've considered porting over to a new static site generator, but hesitated due to the tedious labor involved, and, of course, since the site works just fine on Jekyll - the main issue is my own laziness.

## Hello, Hugo!

After yet another round of hitting bundler errors, I decided it's time to point Claude at this issue and make it go away.

In a short evening session, we managed to:
- Port the site from Jekyll to [Hugo](https://gohugo.io)
- Fix a bunch of bugs (more than I thought there could be in a site this simple!)
- Rip out a bunch of unused cruft, mostly leftovers from previous hobby projects (like that time I really got into [Gauge](https://gauge.org/index.html))
- Make a new Emacs package for supporting my writing flow

Once I've checked *one final time* that the migration won't cause any RSS feeds to re-import my entire post history(!), I'll be pushing up the new site.

## AI Policy

It should go without saying, but:

> I do not use any form of AI in any part of the writing process for any content on this blog.

For better and for worse! I write here as a means of exercising my brain (part of the reason so many drafts go unpublished), so using an LLM, even for something as innocent as a grammar check, would defeat the purpose.

[^1]: I've had several short-lived projects, none long enough to require updating dependencies.
