---
title:  "Thoughts on 'Tailoring Agile Practices for Enterprise System Integration Projects'"
date:   2020-08-27 00:00:00 +0000
tags: [agile-pm, integrations, reading]
---


In the previous posts, I question the applicability of Agile methodology in the arguably non-Agile context of an enterprise systems integration project. 

To recap, how do I consider this type of project to be non-Agile? I think these are so by design. To the project stakeholder(s), the advantage of a project like this is confidence in the "known" end result. This is counterbalanced by the expectation that they will not begin to see value on their investment until the project is delivered in full. They know what the finished product should be, and any project plan they sit with will be seen as the roadmap to reaching that finished product. Any deviation from this roadmap would have to be seen a failure. The project team is expected to meet that roadmap, simply laying the tracks between the start point and the end point. The only desirable deviation from the stakeholder's plan would be a decrease in effort/budget/timeline, which *never happens* [^1]*.*

If the project is not Agile by nature, then what is the purpose of using an Agile framework for it, from Scrum to SAFe?

In his ["Tailoring Agile Practices for Enterprise System Integration Projects"](http://www.guerrillaprojectmanagement.com/tailoring-agile-practices-for-enterprise-system-integration-projects-part-1) post series, Samad Aidane suggests that the key can be found in partially application of Agile via a set of practices including:

- Planning with time-boxing
- Rolling Wave scheduling
- Planning work in short iterations
- Daily 15-minute standup meetings
- Retrospectives
- [Have a] Product Owner
- Single prioritized backlog of work
- Continuous Integration

The assumption I take from this list, and from the current industry practice of running popular frameworks, is that *a framework that prescribes these practices, will increase the chances of success for a team delivering a large integration project.*

In this post and those to come, I'll examine each of these topics in turn.

## Use Rolling Wave schedule

Basically: start with as detailed a project plan as possible, then update and improve your project plan at stages as you move along.

Think of the high-level scope of an enterprise integration project - the level at which a high-level sponsor will engage with it:

*Legacy COTS system A integrates with COTS component B via integration suite C*

What sponsor, looking at such a clearly defined project, would commit to a project plan where the goalposts could move backwards endlessly? A sponsor in this instance is justified in their desire to fix a budget and timeline as much as possible. *It doesn't matter that this approach never works*.

### Stakeholders Will Reject Moving Goalposts

How does one sell Agility to a sponsor, especially when the whole purpose of the enterprise integration project is supposed to be its predictability?

*I don't have a good answer to this.*

I don't think making a project plan on the basis of Rolling Wave, and sharing it with a sponsor or stakeholders, can work. I don't think real-life sponsors will accept the level of uncertainty that a rolling wave plan makes explicit. Especially considering how these expensive enterprise integration projects are sold and run in today's market, sponsors will always expect a high level of confidence and predictability. Remember that they typically won't see any value until the project is completed.

### What *Can* a Project Team Do?

For the project team, the unpredictability in the actual effort needed necessitates a careful strategic approach, knowing full well that the project sponsor is likely going to resist creating the conditions in which modern software project usually succeed.

Right now, without a better answer, I think that it is acceptable to acknowledge that any project that starts under these circumstances is irrevocably damaged. Damage control becomes the only possible way forward. 

It falls to the project team to do whatever they can to promote the necessary conditions for Agile project delivery.

- Build buffers for timeline and budget into the project plan - ideally in plain sight and with the cooperation of the sponsor.
- Do rolling wave implicitly - update the project plan regularly based on the data you can gather [^2], make the updates to the plan highly visible, and loop in the project sponsor and key stakeholders frequently so they retain ownership and responsibility.

> The project sponsor should always have the insight and authority required to make difficult decisions, even canceling the project.

- Highlight and escalate risks, early and often.
- Convince the sponsor to retain a considerable reserve budget.

Hopefully all of this damage control lets the project team maintain a reasonable level of flexibility, and ultimately secure project success. Unfortunately it will likely cause members of the project team to grow a few grey hairs along the way, as *change is failure* on these projects.

I believe it is at the earliest project planning activities that enterprise systems integration projects fail, as it is here that Agility gets kicked to the curb, as budget, timeline, and scope get etched in stone. I would *love* to hear ideas for how project participants - from members of the project team to bidders in an RFP process - could assist the project sponsor/stakeholders in retaining the basis for Agile practices in these early planning & contracting activities. *This of course assumes Agile delivery practices are ideal on enterprise integration projects*.

## Plan with time-boxing

Large Agile project management frameworks like Prince2 [^3] encourage the use of staged, time-boxed planning - highly reminiscent of rolling wave.

My problem with time-boxed planning on an integration project, is that you are emphasizing an *output element* - time - instead of the driver for integrations projects, which are the integration milestones. These milestones are largely technically-driven, won't make sense to a businessperson, and are notoriously difficult to estimate after. 

If you make an initial 3-month timebox (a long one in Agile PM terms), which happens to end three-fourths of the way before the next major milestone is met, have you gained anything at all from this? You won't have any deliverable product, won't have met a decision point, and probably have very little to report back to the stakeholders.

Planning after milestones is probably a much better approach to take. It is unlikely that the milestones will come at even time intervals. I imagine in most enterprise projects it would be difficult to attach a trustworthy timeline to any of the integration point milestones, at least which won't need to be pushed back once or twice.

## Plan work in short iterations

*I.e. run sprints*.

Across the software industry, most teams practice iterations in the form of Scrum sprints. 

The Scrum Guide states:

> Each Sprint may be considered a project with no more than a one-month horizon. Like projects, Sprints are used to accomplish something. Each Sprint has a goal of what is to be built, a design and flexible plan that will guide building it, the work, and the resultant product increment.

In a large integration project, is it possible to plan a limited timebox with a clear (single) goal, a flexible plan, and a *deliverable* product increment?

Does doing so allow the project team to steer, to respond to change?

In my experience in these types of projects, *not typically*.

Sometimes, meaningful and deliverable iterations come quickly one after the other, and other times reaching a deliverable iteration takes a colossal amount of work, which cannot fit into a single iteration cycle (or more!) and resists any attempts at deconstruction or splitting. The bottom line is that increments rarely arrive predictably. In the enterprise integration arena I often experience Scrum teams digging their way out of an avalanche of work that splits painfully across sprints. When the iteration cycle tightens, the pain grows even further.

I suspect that one of two approaches could solve this issue, though I haven't tried them myself yet:

### Larger Timeboxes

I am curious to see what benefits could be gained from a one-month iteration cycle (sprint). Is this long enough to allow for consistency in reaching deliverable product increments? If so, is the feedback loop still tight enough to allow the project team to improve, respond to change, mitigate risks, identify and remove impediments, and all the other benefits usually derived from a well-run iteration cycle?

### Kanban

Let's do away with the timeboxes, which as I've stated above are arguably problematic for so many reasons on an integration project, and opt for a continuous, flow-based process - i.e. Kanban. 

If timeboxes/milestones help in project planning, keep them high-level and let the project team pull work as it is ready. Focus on flow, continual practice improvement, and adjusting WiP. The awkward pressure of having to meet a coherent increment within artificial timeboxes is lifted. The team can focus on the work at hand, releasing when meaningful increments are met.

I'm feeling most optimistic about this approach, and would like to investigate it in practice, and come back to it in future posts.

## Apply daily 15 minute standup meeting

This is an unquestionable good, and one followed by most software teams today. 

Do most of these teams derive actual value from their daily standup? 

**Probably not**, as it commonly devolves to a mindless status update, and the team falls into a hazy daily cycle of "what did I do yesterday, uhhh, oh yeah, I had two meetings and worked on X, today I'll finish working on X and then I'll do Y".

But the benefits of a well-run daily standup are many, as this opportunity for daily self-inspection is instrumental in any team's ability to self-organize. A team that uses this short time to coordinate their efforts, resolve impediments, and raise issues, stands a good chance at success.

## Retrospectives

Another unquestionable good.

If your team doesn't have a way to periodically self-inspect and learn, how does it improve? How do team members take responsibility and ownership of their practices?

[^1]: I reckon even a positive deviation could be seen as a problem in an org that tightly maps their project portfolio, contracts, and staffing to a timeline.   

[^2]: Metrics - another future topic! Well-gathered and meaningfully presented data can be your lifeline when reporting to stakeholders. 

[^3]: Fair warning, I know next to nothing about PRINCE2.