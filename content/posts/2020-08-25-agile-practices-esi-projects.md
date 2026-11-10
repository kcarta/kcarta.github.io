---
title:  "Partial application of Agile practices in enterprise systems integration projects"
date:   2020-08-25 00:00:00 +0000
tags: [agile-pm, integrations, reading]
---

In the previous post, I raised the question of how Agile practice fits into the context of enterprise systems integrations projects, which I assert are non-Agile by design.

I recently came across a series of posts by Samad Adaine, of "Guerilla Project Management", which to my excitement explored a similar theme: [http://www.guerrillaprojectmanagement.com/agile-practices-in-large-system-integration-projects](http://www.guerrillaprojectmanagement.com/agile-practices-in-large-system-integration-projects). 

The posts date back to 2010, but such is the state of this segment of the industry that I have little doubt about the posts' relevancy.

I can reveal already that his series ends abruptly and unsatisfyingly, without having taken on any of the hardest points of my central question. I think there are some interesting points along the way, that warrant discussion.

In this post and a couple to follow, I will attempt to engage with Samad's writings, and gather what insights can be found. I'm mostly curious about real-life experiences, so the "ERP Case Study" interview he has with Jason Fair is particularly intriguing.

On the extent of Agile practice adoption in a large (i.e. enterprise) integration project, Samad Aidane has this to say:

> A theme that kept coming up in all these discussion is the need to customize and tailor Agile practices to fit the special needs of these types of projects. On the other hand, I also heard a number of people advising against customization. The most cited argument against customizing or partially implementing Agile is that doing so prevents an organization from realizing Agile’s full benefits such as speed, efficiency, and cost savings.

> In my experience, some agile practices are not easy to implement, as originally conceived, in packaged applications implementation projects...

> ...Most practitioners I know want flexibility to pick and choose which Agile practices to introduce to their organizations and when. We need to be able to selectively adopt, adapt, and apply whatever Agile practices that help us reach the finish line and deliver projects successfully. Insisting that an Agile method (or any method for that matter) must be implemented exactly as it was originally conceived for all projects becomes an obstacle to its adoption in many organizations and project"

In 2020, partial application appears to be the name of the game, albeit unwittingly. This usually occurs through attempting to put a known framework into practice, like Scrum. I want to eventually discuss purposeful partial application of Agile values/practices, but for now I want to focus on the consequences of attempting to apply Agile via a standard framework/methodology. I'll call this "full application" of Agile practices even if I pessimistically think the end result is some sort of partial applicaiton.

As far as I've seen, enterprise integration projects attempt Scrum but usually fall short of the *Scrum Guide* standard. I've seen "Wild West with Sprints → *kinda Scrum*", "Waterfall delegating to pre-planned Sprints → *kinda Scrum*", "Baseline requirements, with backlog planning to feed Sprints → *kinda Scrum*", and "SAFe for coordination, breaking goals/features down to *kinda Scrum"*. 

I imagine that in a project attempting to follow "proper Scrum", the PO would quickly bend themselves out of shape trying to link their sprint planning with the known integration points & integration flow [^1].

The common framework approaches, from the "kinda Scrum" strategies all the way to scaled SAFe/Prince2/etc., look inspiring on paper, but run into the same central problems: the final state of the project is *known* from the start, and value doesn't appear until the very end, so what is this "Agile" overhead for, when change is not expected or desired?

One assumes that if the point of applying these frameworks isn't about business agility, there must be enough "other derived value" to warrant all the overhead. 

Do these frameworks prescribe standard practices that are so great, that they provide tangible benefits even in a non-Agile context? 

If so, at best this means that organizations are misleading themselves into mistaking "good software delivery practices" for Agility - misunderstanding what Aidane describes as "Agile’s full benefits such as speed, efficiency, and cost savings." At worst, it means they are making a costly investment into practices that provide a placebo effect and the resulting false confidence.

Aidane ends by listing the following as some Agile practices that can be beneficial :

- Use single prioritized backlog of work
- Plan with time-boxing
- Use Rolling Wave schedule
- Plan work in short iterations
- Apply daily 15 minute standup meeting

*Spoiler: Aidane never actually discusses any of these in his following posts, as best as I can tell* 😩 But I will 😇

What I'm led to understand, is that if an Agile framework - i.e. Scrum - is a poor natural fit for this type of project where the end goal is known and the scope is all but set, then it can only be valuable if *full application* results in more benefits than drawbacks. 

In the next post I will examine in turn each of the Agile practices that Aidane mentions, in the context of a standard enterprise system integration project.

[^1]: Also assuming that the PO is even able to parse and prioritize the extremely technical integration requirements