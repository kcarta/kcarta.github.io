---
layout: post
title:  "How I Org (part 0)"
date:   2025-01-21 00:00:00 +0000
tags: [emacs]
---

As I've been writing lately, I'm early on in adopting Emacs into (practically) every aspect of my life.

In my first round of posts on [how I take notes]({% post_url 2024-11-11-taking-notes %}) and [how I've been starting to use Emacs]({% post_url 2024-12-28-how-i-emacs %}), I mentioned that I'd write 'later' about how I've been using Org mode to do my daily note-taking at work - and that time is now!

> Disclaimer: This is **not** a guide to using Org mode effectively. It is titled "part 0" because it is a snapshot of where I'm at in my early stage of adopting this toolset.

## Org primer

Org is both a format for structured plain text (file ext: `.org`), and a collection of tools, built into Emacs, for operating on Org-formatted plain text.

I've been a fan of Markdown for many years, and have been using it to structure my work notes, so after a litle time getting used to a new syntax, I found it natural to write in Org format.

Here's a quick run-through of some of the common syntax:

```org
* Header 1 :tag1:tag2:
** Header 2
   Here is some regular text with *emphasis*, /italic/, and =code=.

*** Header 3
      #+BEGIN_SRC python
      def hello_world():
          print("Hello, world!")
      #+END_SRC

* TODO [2023-10-01] Write blog post about Org mode
  DEADLINE: <2023-11-15 Tue>
  SCHEDULED: <2023-09-25 Mon>
** DONE Prepare initial draft                           :writing:
   CLOSED: [2023-09-20 Sat]
```

## TODO

I use my 

## Refile & archive

## Finally, the files

For now, I have my files structured in the old way, when I was writing Markdown files.

In my notes/ folder I have files in this pattern:

`todo.org`
`todo-archive.org`
`cust.customername.org`
`proj.projectname.org`

I use org-refile to send 
