---
layout: post
title:  "Defining Estimates"
date:   2024-12-11 00:00:00 +0000
tags: [agile-pm, thoughts, teams]
---

I think about estimates **a lot**. My six years of technical/engineering management have been spent in consulting, mostly in product development with my teams and working alongside our customers. In my line of work, I am always weighing, tracking, and communicating estimates.

I find it useful to consider two types of estimates: **explicit** and **implicit**, with a preference for using the latter.[^1] 

## Explicit Estimates

Explicit estimates are typically given in measurable units, usually of time.

Examples of explicit estimates: 
- 10 hours for a task.
- 6 story points on a user story.
- 600 man-hours for a module.
- €1.2 million budgeted for a project.
- 6 weeks to deliver on a key program dependency.

Explicit estimates can have a resolution between *wild-ass guess* and *exacting*.

## Implicit Estimates

Implicit estimates occur any time a plan is made without units being specified, including:
- Commitment from a Scrum team to a sprint backlog at the end of a Planning session.
- Prioritizing one feature over others.
- Breaking down items on a kanban board until they are 'equal size'.
- Ranking features by relative value or effort.
- Making architectural decisions (weighing complexity/effort etc.).
- Deciding to make a 'hotfix' now and a full fix later.
- Planning what to put into an 'MVP'.

Usually, implicit estimates are given, and committed to, without the recognition that an estimate has even been made. 

Implicit estimates are usually the result of a collaborative effort and (hopefully) a degree of shared understanding.

## Estimates underpin agility

Whenever software is being written, estimation must occur.

Explicit estimates reflect a commitment, usually from one side to another (developer->manager, manager->stakeholder, vendor->customer,  ...). Since these commitments are almost always made when we are at a place of *least knowledge*, the pressures and potential consequences arising from the uncertainty of whether we can actually meet these commitments is why we so often rue having to make them, and having them loom over the work we do.

Is there a better way to work together, that doesn't rely on explicit estimates?

The Agile Manifesto provides clues:

### Individuals and interactions over processes and tools
By placing trust in each other, and our ability to deliver and learn together, we break from trusting in the slavish application of a chosen process, or in what our tools allow us to do.
- Explicit estimate: "Azure DevOps says we have 240 developer hours and 120 tester hours in the next sprint, so we will add user stories with up to 360 hours of sub-tasks on them (more with overtime)." We trust in our process and our tool, and can point to these if we fall short of our commitment.
- Implicit estimate: "Before we commit to this backlog for the next sprint, can we make a rough plan for how we can actually deliver it?" By planning together, the team is able to validate their commitment, and ensure it has a reasonable level of certainty before committing to a plan.[^2] 
- Implicit estimate: "Is a backlog item broken down enough to go into development on our board?"

### Working software over comprehensive documentation
- Explicit estimate: "When is the delivery date, given the days it will take to deliver each constituent part?" A manager (or team lead, or Scrum Master, ...) assumes responsibility for documenting a comprehensive plan.
- Implicit estimate: "What's the next feature *of relatively small size* that *adds value*?" The onus is placed on continuing to deliver working software, and how to do this in a way that is valuable (hopefully in a measurable way - another place for estimation).

### Customer collaboration over contract negotiation
- Explicit estimate: "Requirements 1-55 will be delivered by January 1st at a cost of €900,000 and 750 man-days, as seen in the included weekly allocation chart." Uncertainty is 'secured' in a contract, which usually outlines who assumes what risks.
- Implicit estimate: "What governance setup enables the business to steer the software delivery, working closely with the team, and what information & decision-making ability is needed to support this?" Clear responsibilities can be divided in a way that allows for working together and learning, before, during, and after deliveries of (working) software.

### Responding to change over following a plan
- Explicit estimate: "In the upcoming PI, team A will deliver features 23 and 24 which enables team B to work on feature 25 in the subsequent PI. (We will re-assess at the next PI Planning)" Responsibility is placed in a plan, often one spanning an extended length of time such as a quarter. Managers are needed to assume this responsibility and track progress, often in the form of explicit estimates.
- Implicit estimate: "The PO for team A will work together with the PO for team B to align deliveries from their backlogs from sprint to sprint (as long as there are dependencies between the products)." Responsibility is placed between people with decision-making authority and equipped to handle changes as they occur and based on our best knowledge as it develops.

Implicit estimates are better by nature because they reflect agile values of individuals interacting, to deliver working software, in collaboration within and across groups, and with the ability to re-plan as needed. Explicit estimates often impede agility because they represent a hard, recorded commitment, representing our *past* knowledge and not our current knowledge, and expressing a negative consequence if they turn out to be incorrect. There are always risks to changing an explicit estimate once it has been recorded, and so we are often too weak to confront these risks instead of facing new truths as they arise.

## Conclusion: No Estimates?

I've followed the 'no estimates' movement closely, and sympathize with what it expresses. I once left a company in part because I felt demoralized by being asked to make 'wild ass guesses' ranging upwards of 100+ man-days at a time, without being privy to the decisions that would be committed to on the back of my estimates. Too many developers are subject to the tyranny of being held accountable for explicit estimates, even in this day and age where everyone involved knows that these types of estimates can never be accurate (hence the hand-wringing and apologies that often come with the requests). We only **know** when the software is shipped, and if we are equipped to **learn**.

In my experience, a good leader should be able to track a delivery and manage a contract without requiring explicit estimates from their team. I have never had a delivery that failed because we didn't have enough estimates, or because the estimates weren't "good" enough. Explanations for this could be the basis of a future post, but I don't respect arguments to the contrary, because I've seen (second-hand) enough projects that fell apart because the estimates they were built on turned out to be inaccurate, and the deliveries were constructed wholly around these estimates. This way of working turns out to be remarkably fragile.

I find it useful to ask questions to test my deliveries, and how well we are doing at working with implicit rather than explicit estimation:
- When my team makes a plan, has a valuable interaction occurred? Do I come out knowing more about the technical challenges we face, and does my team know more about the context we're delivering under?
- When I plan with my customer, are they in more control of the delivery or has more control been left with me to steer against our contract? Am I more or less aware of their goals and constraints?
- When my team delivers software, are we able to learn and improve on how we make the next delivery? Are my customer, stakeholders, and sponsor able to see and assess the value delivered?
- How often does my team and/or my customer meet unanticipated change, and how effective are we at responding to it? 

Pondering questions like these, and referring back to the [Agile Manifesto](http://agilemanifesto.org) & [Principles](http://agilemanifesto.org/principles.html), and the [Scrum Guide](https://scrumguides.org/scrum-guide.html), usually helps me decide what path to take next. Hopefully it is in a direction of more trust, which underpins the ability to work off of implicit estimates. Explicit estimates are often borne of distrust, and in a worst-case, dissolution of trust necessitates the drawing up of detailed documents chock-full of explicitly-estimated plans. Unfortunately this rarely leads to re-establishment of trust. 

I see two cases where it is counter-productive to resist explicit estimates:

When communicating with customers & stakeholders, explicit estimates are used because the business needs to allocate resources, usually in the form of money, and to assume things like risk & opportunity cost. Most supplier/customer relationships are formed on the basis of a contract with explicit estimates. I have had the pleasure of delivering on the basis of true 'agile contracts' that didn't specify time/budget/scope aside from working on products, but this is rare and I'm not naive enough to expect the industry to shift to this model as a default.[^3] I don't see a way to avoid the use of explicit estimates here. The key is that both sides need to be open to change, and governance for responding to change needs to be agreed, understood, and practiced at least as much as the mechanisms for tracking progress towards the plan (i.e. estimates on top of estimates).

Secondly, I have had projects where the end result is *known* - e.g. [an integration]({% post_url 2020-08-23-agile-in-esi-projects %}) - and the work to be done is close to *known*. When I have had the pleasure of having colleagues with decades of experience in the specific domain, I find their estimates to be remarkably accurate, and counter-productive for me to insist on ignoring these in favor of agile collaboration - if we know what to do, how to do it, and what effort is required, is there *really* a need to implement a process around learning & open to (radical) change?

[^1]: I do not know where I came up with these categories. Maybe there's a better way to name this dichotomy. Googling brings up [a single result](https://thinklouder.com/task-explicit-implicit/), but not one I reckon I've ever read before. 

[^2]: Scrum provides the team, and the PO especially, flexibility if the plan turns out to be inadequate or becomes invalidated for some reason.

[^3]: Ironically the largest & longest-running agile contract I had was with a customer that had more money than sense, but the deliveries turned out to be successful (as far as I could glean & measure, at least), and we were able to pivot easily without needing to re-align a contract.
