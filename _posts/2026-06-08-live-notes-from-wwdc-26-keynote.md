---
layout: post
title:  "Live thoughts from WWDC 26 Keynote"
date:   2026-06-08 00:00:00 +0000
tags: [thoughts]
---

Like every year since my conversion to Apple fanboy (and to try to justify my personal developer license 💸), I tuned into today's WWDC keynote with great anticipation.

This year, my notes ended up being structured and complete enough that I figure I can publish them here - for posterity's sake if nothing else. Will be fun to look back on this in a year and see what has held, and what has ended up being empty promises (\*ahem\* WWDC 24 \*ahem\*).

## Obligatory five-point AI summary

<🤖>
> - Apple's framing this year is about fixes, iteration, and foundation (with some eye-rolling at the Liquid Glass spin).  
> - Opt-in child accounts for parental protections, preferred over mandatory age verification.  
> - Siri/Apple Intelligence gets multimodal and context-aware. Gemini models under the hood (for now), Apple privacy on top. Not in the EU (for now).  
> - Natural-language generation of Safari extensions, Mail suggestions, Shortcuts/Automations, and on-device image gen/editing — Shortcuts the most exciting part.  
> - Xcode agents add model selection and Figma integration; open question whether the dev side gets the same framing focus on fixes.  

</🤖>

## Focus on fixes

On Liquid Glass: "Natural process where we take a big leap forward and then continue to iterate"

I need to remember this weasel line for future use...

"...further refinements, starting with the foundation..." 

😂


## Child accounts

Parents are obliged to create accounts for their children, to enable protections and set age-appropriate limits and tracking.

I like this. Opt-in protections makes sense - instead of the draconian direction it seems all governments are pushing for, [requiring all adults to verify with biometric identification for potentially age-sensitive online interactions.](https://digital-strategy.ec.europa.eu/en/factpages/blueprint-age-verification-solution-help-protect-minors-online
)

## Search improvements

Better indexing for search, to be (or at least feel) semantic.
Wonder how much has been done under-the-hood, if this will have the same cut corners as other major Apple releases of late...

## Apple Intelligence

Multi-modal - curious how this translates to useful features.

I'm curious where the improvements are because I've basically not knowingly used Apple Intelligence so far since these features were rolled out, despite some prolonged efforts to find use cases for them.

Privacy in AI is non-negotiable. God bless!

Siri AI (what was it before? Not AI? AI is dead, long live AI!)

Multi-modality used in screen awareness - Better search and answers on vague requests is compelling. 
I tend not to use Siri because I don't like gaming it to figure out if it can do what I actually want.

Siri "just finding things for me" is intriguing, pulling on context. Seems related to the aforementioned improved search indexing?

This is what I've long been expecting, and why I've been hedging against frameworks like OpenClaw: *useful* AI assistant features are getting built into the OS - this came in the near-term timeframe I had expected. The advantages to living-past-the-edge never seemed to balance out against the enormous risks.

This is Gemini behind the scenes, but with Apple's privacy architecture that makes it much less frightening to open up to my Mail, Photos, files, etc. Including drafting emails "how you typically write".

These features seem to respond to casual ChatGPT personal use ("will this backpack work as a carry-on for my flight in September?") rather than about productivity.

Seems a bit iffy to show Siri AI answering confident yes/no questions.

## Apps

Vibe coding extensions in Safari - "Simply describe what you want in natural language and Safari can create a native extension" -> Cool! Not a surprise if Google also offers this, if this is all Gemini under-the-hood.

Suggestions in Mail. This has stunk in every iteration I've seen so far in other products, curious if it'll be useful in Apple Mail.
My "Feed | Paper Trail" sorting method might pay dividends!

"Describe" (vibe coding) Shortcuts and Automations! 👯 Yes! This has always been so tedious to set up manually. I'd consider myself a relative power user yet I always run up against the same steep wall whenever I try to set up a non-trivial flow.
Will be interesting to see what the tweaking process is like. Will the generation be a standard Shortcut/Automation that can then be edited as any other?

AI image generation and editing on-device. My wife and I have been using Gemini to generate design and remodeling ideas for our house, being able to do it "natively" on our phones is welcome.

In-scene perspective changing with generative fill-in is going to feel like magic and probably going to become normal. This runs up against the uncomfortable edge of the AI<>Reality border. Is a "reframed" photo still "real"? Is this fingerprinted in a way that lets others know that a photo has been partially AI-generated? As a society have we just accepted AI modification as a given?

Google Photos is my last remaining hook into Google's ecosystem.

Siri AI not available in the EU. Ooph. Oh well. I think I've found a comfortable equilibrium in my needs/wants and the available AI tools. Most of what Apple presented here will just be replacing the tools I use today, not workflows or use cases (except for generating Shortcuts/Automations, that I am genuinely hyped about!).

I hope Apples move towards child accounts undermines the growing momentum towards online age verification, which will add another nail to the coffin of the open web as we know (knew) it, under the guise of protections for minors.

# Development

## Xcode agents

Model selection.
Integration with Figma - interesting.

The keynote started with an emphasis on OS-level fixes and performance enhancements.

Will be interesting to follow the platform talks to see if there's a similar focus on fixes and stablization, to get past the current ["scars from dozens of paper cuts" state of affairs in places like SwiftUI](https://daringfireball.net/2026/06/swiftui_only_makes_it_easy_to_develop_bad_apps
).
