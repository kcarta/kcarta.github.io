---
layout: post
title:  "How I Emacs (#1)"
date:   2024-12-28 00:00:00 +0000
tags: [tools]
---

This first post is about how I, as a beginner, have been using Emacs.

This might be interesting for  non-users, could be relevant for fellow Emacs noobs, and will definitely be hair-pulling for anyone with more experience than I have (which, as you'll see, is very little). I have an idea to make this a series, with a new post whenever I feel like I've reached a new stage in my Emacs evolution.

I'll divide this into sections, ordered roughly by the amount I've spent on each.

## Taking notes

The killer app for me has always been [Org mode](https://orgmode.org/features.html). At work, I always have my main notes.org file open, and use capture and refile to sort my to-dos and quick notes as I go through the day. When focusing on a single customer/project, I usually have that org file open as well.

I'll reserve a longer writeup on my Org use for a future post, especially in a few weeks when I'm back at work at in my usual workflow again. In short, Emacs + Org mode is an absurdly powerful note-taking toolset, and I know I've only scratched the surface with my use so far.

## Writing this blog

Very early on, I took to using Emacs to write this blog. It felt like a natural evolution of my Emacs use. This site is written in [Jekyll](https://jekyllrb.com/docs/front-matter/), so 95% of the time I'm just writing posts in Markdown. The rest of the time I'm editing HTML or CSS.

I've configured Emacs to help write the posts in Markdown. I use [Markdown Mode](https://jblevins.org/projects/markdown-mode/), which provides a slew of helpful commands for writing & editing Markdown. Recently I configured Emacs to use the Georgia font when in a Markdown buffer, so that the posts have a similar look when I'm editing them to how they'll look when published.

I also have some custom functions for Jekyll, so I don't have to write boilerplate like the [Front Matter](https://jekyllrb.com/docs/front-matter/) by hand. I have lots of ideas for more, maybe even enough to write a new plugin along the lines of some of [those I see on GitHub](https://github.com/masasam/emacs-easy-jekyll).

## Configuring Emacs 🙃

My original config was [literate](https://en.wikipedia.org/wiki/Literate_programming) and inspired by [(i.e. lifted nearly wholesale from)](https://gitlab.com/dwt1/configuring-emacs) Derek Taylor's [DistroTube series on Configuring Emacs](https://www.youtube.com/watch?v=d1fgypEiQkE&list=PL5--8gKSku15e8lXf7aLICFmAHQVo0KXX). I hooked onto his explanatory way of walking step-by-step through the process of building a sane config, so this is where I started.

My current Emacs config is on [GitHub](https://github.com/kcarta/.emacs.d.git) for anyone interested. 

I started using Emacs about 6 months ago,[^1] and my configuration reflects that I'm still very much a noob in this space. I'm learning, and completely fearless about trying something new or living with something kludgy. I know I'll eventually learn how to do something better, and will slowly remove the duct-taped parts with something better (hopefully simpler).

Since, I've gone away from having a literate config, as I found it easier to just be writing Elisp with comments,  and have scrapped a great deal of the code to narrow down to my core use cases. I feel very uncomfortable with config that I don't understand (which is why Doom Emacs and Spacemacs do not appeal to me).

A few times I've used an LLM to generate handy functions. I'm happy doing this, as a first step to learning how to write Elisp. The generated code probably isn't idiomatic, but when they work, I don't care - it's a first step to me learning how to do this myself.

My current priorities for my Emacs config:
- Primary: Support my blogging (Jekyll/GH Pages) & personal organization.
- Secondary: Support my dev projects, which range from little Ruby scripts to full Flutter apps.
- Look-and-feel on par with a modern editor like Zed or Sublime Text.
- Be *mostly* understandable to me when I go to read & tweak it.

There are things I *don't* need or want from Emacs right now, that perhaps might sound foolish to a more advanced user:
- Right now I don't have the capacity to learn Emacs commands, so I don't really ever use `C-x` or `M-x` directly.
  - I have a leader key bound to `SPC`, and `SPC SPC` binds to `M-x` which opens up Consult to help me fuzzy-find the relevant command.
  - I also have a slew of handcrafted mnemonic bindings registered in General.
- I prefer my own handcrafted mnemonic bindings to Transient menus. There's so much already to learn, I don't want to also have to learn someone else's bindings.
- I don't use the much-vaunted [Magit](https://magit.vc). After over a decade of daily git terminal use, I'm good with what I've got. This means I usually have a terminal open alongside Emacs.

My future goals & wishes for my Emacs config:
- ~~Remove Elpaca and just do native package management.~~ Done!
- Use Emacs-native packages as possible.
  - Emacs 30 will probably help a lot with this ([e.g. with completions](https://eshelyaron.com/posts/2023-11-17-completion-preview-in-emacs.html)) 
- Limit Vim bindings/motions (Evil) to only editing inside text buffers, and slowly replace my mnemonic bindings with Emacs commands.
- Support code suggestions and documentation in my main languages, which these days are JS/TS, Ruby, and Dart.

What I still haven't figured out:

- Finding and ironing out every little UI wrinkle, especially nit-picky things that I know require some complicated config to wrangle.
- Good terminal emulation, and whether I should use Eshell, and if so, getting it to not suck to use compared to any terminal app, or if I should use a full terminal emulator like Vterm. I've read folks suggesting to just use Emacs commands/packages directly instead of going to the terminal, but I'm not so far in my journey just yet.
- Any standard Emacs key commands. Right now I'm fully in Evil and custom keybindings, and I'm fine with this. 
- Full programming support, to par with what I get from VS Code or Zed. I'm lost in LSP's and Eglot and Treesitter. There's just too much complexity and rough edges, and I'm a bit lost with only [pieces of a map](https://www.masteringemacs.org/article/how-to-get-started-tree-sitter) to work from. Hopefully the picture becomes clearer over 2025 and the Emacs 30 releases, or I'll just 'get good' and grok it eventually.

## Coding

As stated in the Config section, I've gone back and forth on trying to get a good LSP setup. I think I might be expecting too much, especially when I'm coding in a dynamic language like JS or Ruby, and hoping for completions that the LSP simply isn't set up to provide (but I can get from an IDE like RubyMine...). 

I did have some success with the [Dart LSP](https://github.com/emacs-lsp/lsp-dart), so I may do my next Flutter app in Emacs, or I might warm up my very rusty C# or Java skills and see if I can get a little project going in them.

## Abandoned packages for consuming the world in text

I'm a text fanatic. My fascination with Emacs comes from this passion; if I could, I would orient my entire life around text buffers, and the reading & processing of them. Text just feels right to me in a way that rich graphical applications don't. It's much easier for me to craft a pleasing text-based workflow than it is to find a graphical UI with adequate usability.[^2] 

It then comes as little surprise that I've dabbled in Emacs packages like EWW for web browsing and [Elfeed](https://github.com/skeeto/elfeed) for consuming RSS feeds. I've quickly abandoned all the ones I've used, but might return again at some point when I'm more comfortable with configuration. 

I used Elfeed for the longest of these, a few weeks, but stopped as I was too frustrated by the UI, which I felt difficult if not impossible to configure to my liking. Again, maybe I'll come back at some point.

## Conclusion: happy minimums, and kludges abound!

To summarize, I'm joyfully and productively using Emacs for some important (to me) core tasks, even though I know I'm just seeing the very tip of the iceberg.

I've been dipping my toes into the community, especially through [Sacha Chua's praiseworthy work in compiling news](https://sachachua.com/blog/). I watched along with [Emacs Conf 2024](https://emacsconf.org/2024/), inspired by the community involvement I saw.

It's exciting to me to know that there's a vast amount of awesome things I can do with this tool, both built-in and also [from the community](https://github.com/emacs-tw/awesome-emacs). I'm giddy to see where I'll be in another 6 months' time!

[^1]: 3 months of which have been subsumed into parenting a newborn and so it's hard to call it a full 6 months 😵‍💫

[^2]: It should come as no surprise I'm also a [TUI](https://terminal-apps.dev) dork. In my early days with Emacs I came very close to using something like [tmux](https://github.com/tmux/tmux/wiki) or [ghostty](https://ghostty.org) with Neovim.
