---
layout: post
title:  "Note Capturing for Fun and Profit"
date:   2024-11-11 00:00:00 +0000
tags: [tools]
---

# The Journey to Note-taking Paradise

In this first section I'll put some context on how I've ended up with the tools I use today for taking and organizing notes. Hopefully there will be plenty to relate to.

## Piles of Post-its

In work and life, I find myself very often needing to jot down notes, for future filing.

Up until 2018, I wrote in notebooks and on post-its, with piles of both on my desk. At some point each day, I would sort through my notes and manually type anything important into different Markdown files, which I stored in a repo-backed folder on my Desktop.

This system had great upsides:
- [Hand-writing is so effective for me retaining information](https://www.scientificamerican.com/article/why-writing-by-hand-is-better-for-memory-and-learning/), to the extent that much of what I wrote down, I didn't actually need to file away later (see `downsides` 😝).
- Taking notes by hand during meetings & workshops is a nice hack to stay focused.
- If I needed to recall something, I just had to do a project search in my .md files - I prided myself then (and now) on being able to reference *anything* important said during *any* meeting, as if it were a magic trick (and not just the result of diligent organization)!

But there were downsides:
- I wrote reams of notes, much of which weren't actually that important. Sorting the signal from the noise became a large part of the organizing work.
- Having my notes scattered around in .md files was bad for discoverability. I had not yet grocked grep-like tooling for searching in my notes 'project' as I'd do today, so the aforementioned project searching was clumsy in practice.
- Structuring and re-structuring my notes was awkward at best, even though I could fly around in my Vim .md buffers.
- I tried, and always gave up on, homegrown tagging and sorting systems for organizing my typed notes.
- In online meetings, I was always looking down at my notes, and I think this looked like I was distracted.
- Manually re-typing notes became untenable as my work days intensified and my time for organizing shrunk to 'forget about it' levels. The daily filing gradually turned into weekly, and then ultimately never.

Value to effort, this was not sustainable.

## Notion: An Affair to Remember

In late 2018, I found and fell in love with [Notion](https://notion.so), which quickly became my daily driver for organizing my work & personal life, all the way up until 2023. [I've documented my organization strategy here]({% post_url 2020-11-24-todo %}). I still use Notion for organizing my personal & family life, but have migrated away from it for work.

Eventually, Notion became untenable for using at work:

- Notion stores everything on its cloud with no functional 'offline mode', and despite promises of GDPR compliance, I couldn't defend storing sensitive notes in Notion, especially as my daily work tends to be highly confidential.
- After more than a decade of steadfast Vim use, I **hate** every time I am forced to move my hands from the keyboard to the mouse. Talk about a [flow breaker!]({% post_url 2024-11-04-finding-flow %})! Notion has never had good support for keyboard motions.
- Notion search was *not good* for a very long time, and still lags behind my desire to jump around in my notes.

## Emacs: True Love Ways

At the end of last year I decided to make the cut, and during the holiday downtime I deleted my Notion workspace for work, and migrated everything over to the old Markdown-based system I had before, this time using VS Code.

I quickly felt the same pains I'd had before, so I desperately went looking for alternatives. This 'crisis period' overlapped with me exploring Clojure and installing [Emacs](https://en.wikipedia.org/wiki/GNU_Emacs) for the first time, and on a whim I started dipping my feet into [Org mode](https://orgmode.org/orgguide.html) in Emacs.

After a few hesitant days of first use, I saw the light and have since fully converted over to the Church of Emacs 😇. Betcha didn't think this would turn into a religious conversion story, huh?

Now, my workflow for organizing notes at work is:

0. (Emacs is always open)
1. [Capture](https://www.gnu.org/software/emacs/manual/html_node/org/Capture.html) notes into my main todo.org file - see below for more on how I typically do this on macOS.
2. [Refile](https://orgmode.org/manual/Refile-and-Copy.html) notes as needed.
   - I have a very small hierarchy of .org docs to file notes into for long-term storage.

I enjoy the benefits of this system, which is made by and for nerds like me. As my knowledge of Emacs ([and my config!](https://github.com/kcarta/.emacs.d)) improves, I get better at taking and organizing my notes! Org (2003) and Emacs (1976) are OLD, which means they are 1) stable and 2) vast in scope and depth. Unlike the other digital tools I'd used previously, Emacs is endlessly customizable, in a Lisp that I find easy to grock and write. So far any need I've had, there has been either an existing package for, or an easy function I can use or script on top of.

Best of all, Org mode comes with rich functionality for tagging and sorting tasks and notes, and Emacs is loaded with tools for sifting and searching though text at lightning-speed. I've never been so fast at organizing notes and then finding them again later!

I'm slowly expanding on my simple workflow, and kept motivated by the [seemingly-endless amount of excellent content I'm finding online](https://sachachua.com/blog/2024/11/excerpts-from-a-conversation-with-john-wiegley-johnw-and-adam-porter-alphapapa-about-personal-information-management/) 😍

# Capturing Notes

Finally, I want to show off the Apple Shortcuts that I leverage to quickly capture notes.

I have two pairs of Shortcuts, one for Org mode / Emacs and one for Notion.

## Notion Shortcuts for Taking & Copying Notes

I'll start with the Notion shortcuts, as even though I'm no longer using Notion for work, I still find these useful in my private life, and love using the 'Take a Notion' shortcut from my iPhone and Apple Watch with Siri (though dictation is spotty at times...).

These Notion Shortcuts [leverage the Notion API](https://developers.notion.com/docs/working-with-databases#adding-pages-to-a-database), and simply create a new item in a Database I have named 'Notions'. It's easy to set up if you are patient enough to navigate like 7 layers deep in the horrendous Shortcuts UI for editing JSON.

### 'Take a Notion'

This Shortcut starts a prompt / dictation and adds the result to my 'Notions' database:

![Take a Notion shortcut](/static/img/posts/take-a-notion.png)

### 'Copy a Notion'

This Shortcut is the one I use the most often privately - it takes whatever I have in my clipboard and adds it to my 'Notions' database. Usually this is a URL I want to circle back to.

![Copy a Notion shortcut](/static/img/posts/copy-notion.png)

## Emacs Shortcuts for Capturing & Copying Notes

These shortcuts are the ones I use constantly at work. Both append into my todo.org file and quickly get refiled as needed (despite what the screenshots here show - these are from my personal computer and go into a different location).

### 'Take a Note'

This Shortcut starts a prompt / dictation and appends it to my todo.org file. I like to bind this to a keypress like ⌥⌘N, so I can quickly type a note and get back to my meeting or task-at-hand.

![Take a Note shortcut](/static/img/posts/take-a-note.png)

![Taking a Note](/static/img/posts/taking-a-note.png)


### 'Copy Clipping'

I use this less at work than I do the 'Copy a Notion' shortcut, but it's still useful if there's clippings of documentation or a chat thread that I need to remember verbatim.

![Copy a Notion shortcut](/static/img/posts/copy-clipping.png)
