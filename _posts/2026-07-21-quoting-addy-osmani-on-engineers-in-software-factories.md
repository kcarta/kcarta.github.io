---
layout: post
title:  Quoting Addy Osmani on engineers in "software factories"
date:   2026-07-21 00:00:00 +0000
tags: [ai]
---

Addy Osmani's concluding thoughts on Dex Horthy's talk ["Harness Engineering is not Enough: Why Software Factories Fail" (7:33-7:52)](https://www.youtube.com/watch?v=htM02KMNZnk&t=27219s):

*Emphasis mine*

> ## Where the human actually goes
> I think engineers need to increasingly own the outer loop. The agents can investigate a bug, write up the diagnosis, implement a fix, run the tests, and write up a report. That’s the execution of the inner loop, and they can do it as efficiently as anyone. 
>
> **But that was never the job.**
>
> The bits you own are what I’d call the outer loop: decide whether it’s the right way to address the problem, verify that the diagnosis and implementation are sound, approve the change, and carry the consequences of being wrong. The boundary between the two loops is evidence, the diffs, the tests, the logs, and a brief explanation that connects them. Types, seams, and rubrics make it possible to oversee all this without doing a lot of work for every change.
>
> **I think it’s useful to put it this way: you’re not down on the line writing changes any more; you’re up at the end of the production line designing it and guarding the gate.**
>
> There’s a lot you can do to make the model better and the harness more capable, but I’ve observed that identifying problems that are expensive in the long term is not typically something you can automate away. The core thing that’s still the job is to exercise human judgment better than any flow of paper and computing power.

Earlier in the post:
> We’ve always said we care about good architecture. But now that we’re using automated coding agents, that architecture is finally doing a second job as a cheap and hard-to-fake safety net against the mistakes the agent will make.
>
> That safety net has to live outside the model, because the model won’t supply it...

Osmani's analysis is worth reading in full, especially if like me you feel existential dread at the mention of "dark software factories" (I still have Park Chan-wook's must-see [No Other Choice](https://en.wikipedia.org/wiki/No_Other_Choice) running in my head).
