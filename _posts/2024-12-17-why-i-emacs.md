---
layout: post
title:  "Why I Emacs"
date:   2024-12-17 00:00:00 +0000
tags: [tools,emacs]
---
I LOVE text editors. 

I’ve been nerding about text editors from the beginning of my software development career, which started circa 2011.

Over the years I’ve tried *most* popular editors & IDE's.[^1] 

Emacs is currently my editor-of-choice and the one I expect to use by default from now until whenever it or I die (Emacs is eternal, right?).

But I started with [Vim](https://www.vim.org).

I made a fortuitous decision to learn Vim very early on in my career. I can't remember why, but I stubbornly persisted, even though it took months to fully 'grok'. I walked *everywhere* with several printed [cheatsheets](http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html) folded into my pocket, and would study them any time I had the chance.

Vim taught me some important lessons:
- It pays to invest in learning your editor; your editor is the most important tool you'll use as a developer.
- The best editors are available wherever you need them (especially if it's a random server you're SSH'ing into).
- Good editors are open source and Free (as in speech AND as in beer).
- Stability, community, and stewardship are good predictors of quality.
- Good editors teach you good habits, the very best teach you habits that are generalizable.
- Good editors are customizable.

## The Long Journey

Perhaps because I invested so heavily in Vim early on, I stayed away from Emacs, and managed to do so for nearly 15 years. As a self-professed editor nerd, I *thought* I knew everything I need to know about Emacs - [rms, GNU, overly-complicated, "a great OS, but lacks a decent text editor."](https://en.wikipedia.org/wiki/Editor_war)

For over a decade, I used Vim as my primary editor and then whatever IDE I found best for my active project (as you can see in the footnote, that turns out to be a lot). I also kept dabbling in other editors, just to see what's out there. I always loved Vim, but stopped short of using it as a full-on code editor, preferring the power of a good IDE (with Vim mode enabled, of course).

I stopped using Vim as my go-to general editor in favor of VS Code around 2020, when I was fully moved over to management and stopped developing at work, but kept coding as a hobby. I'd been using & following VS Code since its initial release, and at that time I was most fluent in .NET, which was obviously very well supported in VS Code as an editor / lightweight IDE.

My first real foray into Emacs came in March 2023, when I started playing with Clojure during a vacation. I found that Emacs had the best support ([Cider](https://github.com/clojure-emacs/cider)) for writing Clojure, so I took the plunge. Finding base Emacs too...basic..., I tried out [Spacemacs](https://www.spacemacs.org) and [Doom Emacs](https://github.com/doomemacs/doomemacs). After my vacation ended I stopped my tour of Clojure and deleted Emacs. But somewhere along that short journey, something stuck - Spacemacs & Doom showed me that Emacs had surprising depth. Also, after spending so many years with Vimscript, the prospect of configuring my editor with a Lisp was enticing.

## The Conversion

My come-to-god moment happened around April this year, after some frivolous irritation I was having with VS Code. As I wrote in [a previous post]({% post_url 2024-11-11-taking-notes %}), I had deplatformed from Notion at work and was back to writing & organizing my notes in markdown with VS Code. I wanted to do something I thought was simple: associate custom icons with file names/extensions & folder names in my file tree. I tried everything, from community extensions to going 'deep' and writing my own. None of it met my needs. I found that VS Code's API exposed some parts but awkwardly, and kept the core editor parts closed off. Finding that my fairly "simple" goal was impossible due to seemingly random limitations made me feel sick.

Around this time, a co-worker started nudging me about Org-mode. With Doom Emacs, I tried out Org and stopped, and tried again. Eventually it all 'clicked'. But I still didn't like using Doom or Spacemacs. I feel something akin to thalassophobia using them - I don't feel comfortable with a config that isn't my own and feels impossibly deep. 

So with a fresh install, I spent a weekend building up my Emacs config following the [video guides from DistroTube](https://www.youtube.com/watch?v=d1fgypEiQkE&list=PL5--8gKSku15e8lXf7aLICFmAHQVo0KXX). I had so much fun writing Elisp, and a [literate](https://en.wikipedia.org/wiki/Literate_programming#:~:text=Literate%20programming%20is%20a%20programming,source%20code%20can%20be%20generated) config to boot!

For the uninitiated, Emacs is mostly written & configured in its own simple Lisp, and exposes basically the entire editor internals to customization (down to the C layer at the very bottom, but I don't want to touch that anyways!). Everything is easily inspectable and hackable in the editor, and the documentation is insanely helpful and easy to bring up for every function and variable. I've never used a tool that begs me to hack on it like Emacs does.

With my own (mostly stolen) config in place, I was off to the races, and have never looked back. I'm completely in love with Emacs, and feel like I've embarked on a lifelong journey of learning & slowly building up towards mastery. What a joy!

## What Emacs has taught me

In addition to the lessons I learned from Vim, Emacs has taught me that the best editors are fully open to customization, and customization and mastery should be joyful. I *should* feel powerful customizing my editor - this is my main tool for interacting with the world,[^2] why shouldn't it reward me for tailoring it to my specific needs (& whims)!?

Now that I have my religious conversion story out, I'm going to write an ongoing series about *how* I Emacs. I think it might be useful for anyone on or considering a similar path.

[^1]: To wit, probably missing a few: Vim, Neovim, Brackets, Notepad++, Notepad, Zed, nano, ed, gedit, Pico, IDLE, Sublime Text, Atom, DrRacket, Cuis, Arduino IDE, VS Code, Visual Studio, Visual Studio for Mac (i.e. Xamarin Studio), SQL Server Management Studio, Xcode, TextEdit, Eclipse, NetBeans, most JetBrains IDEs (IntelliJ, WebStorm, DataGrip, RubyMine, Rider, PhpStorm), Android Studio, Unity, Scratch, and for writing, Obidian and Notion.

[^2]: I feel so nerdy writing this, but it's true.
