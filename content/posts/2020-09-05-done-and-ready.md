---
title:  "Definitions of Done and Ready - A manager's perspective"
date:   2020-09-05 00:00:00 +0000
tags: [agile-pm, teams, thoughts]
---

The effective Scrum teams I've worked with maintain a pair of documents called a **definition of ready** and a **definition of done**, which describe when an item is prepared adequately enough so that the team can commit to implementing it, and when an item is completed to the point that the team can deliver it.

I'm confident there are thousands of articles on what these documents are about, and how a team should go about writing and using them. I'm not concerned about any of that. I expect my teams to be able to understand the basic ins and outs of these contracts, and if they don't for some reason, then coaching becomes a whole other topic.

I'm interested in how a *manager* [^1] can observe how a team negotiates and maintains these documents, as one source for gauging the overall health of the team. 

As a manager, I value teams that make active use of their definitions of ready and done, because doing so fosters a healthy culture around the work the team delivers.

I am particularly interested in gaining insights into the health of my teams, by looking at how the teams use their **definition of ready** and **definition of done**.

# A healthy team avoids waste

 The team should care about these agreements because they ensure quality on the team's input and output streams.

A healthy team cares about the quality of the work they take on, because they know the adage:

## Garbage in, garbage out

A team that takes on work that isn't adequately prepared will very likely face increased levels of waste. This waste most often presents itself in the forms of aborted development attempts and rework, often egregiously late into the development cycle. Healthy teams hate waste and will work together to eliminate its sources. As a manager, you should expect see your team having discussions about rework waste, and pointing back to the definition of ready if they believe they have found instances where criteria weren't being met.

In complex projects it can be very difficult for a team to determine whether certain work items meet the definition of ready, and criteria chosen previously can, over time, come out of alignment with the level of preparation needed for new work items. To root out this issue, it can be useful to look at the level of waste the team encounters. If your team ever has to redo work after it has been delivered, or uncovers costly problems during code review, QA assessment, or PO approval, then gather the team and take another look at the definition of ready. With the benefit of hindsight, the team should make sure the items in the contract are still relevant for the work being done.

## Dissatisfaction downstream

When the team doesn't follow their definition of done, or their chosen criteria are inadequate, then waste will occur downstream from the delivery. This waste often appears in the form of missing documentation, holes in test coverage, missing configuration, and glitchy UI/UX and typos in content, which come back to the team to resolve. Tracking post-delivery waste is where a manager's higher-level vision comes into play, as a manager should be attuned to complaints coming from downstream parties such as operations, implementation consultants, end-users, and so on. A good manager should be able to bring these problems back to the team in a constructive way, and help them to trace issues back to the definition of done.

Teams hate having to re-open closed issues, especially as this usually interferes with their currently planned work. It can also be personally embarrassing for the team members that collaborated on an issue that turns out to have been poorly received [^2]. For these reasons, it is important to watch how the team negotiates post-delivery waste, and if they point back to violations of their definition of done, or improve the document as they find flaws with it.

Waste can also manifest in the form of work that doesn't provide value. Scrum puts a major emphasis on doing work that increases value, and avoiding work that doesn't. A mature team senses when it has delivered a piece of work that won't add value, and flags this case for internal discussion - was the item not prepared properly, did the PO not understand its purpose, or were there missing "done" criteria that means the item is delivered incomplete and therefore without value?

# A healthy team self-enforces

Who on the team is responsible for ensuring that the definitions of ready and done get followed? 

The easy answer is *everyone on the team.* On a mature team, everyone from the junior-most to senior-most members will raise perceived issues freely, especially in the context of a retrospective. A scrum master is another obvious choice, as they should be vigilantly protecting the team from impediments and waste.

I don't think it's realistic in practice to expect all team members to engage equally in policy enforcement, due to the differing levels of visibility that more senior and more junior team members will have. A team lead or senior-level architect will tend to have responsibilities that go beyond the development cycle, so they will be more likely to spot waste deriving from violations of the definitions of ready and done. On the flipside of this, I would be surprised to see junior and mid-level team members raising issues deriving from upstream and downstream, since they tend to focus on the issues at-hand and aren't usually looking outside the boundaries of the development cycle.

As a manager, I want to see that *anyone* on the team is spotting and flagging waste due to violations of ready and done. I tend to look to the more senior team members for this, but I would also be delighted to see a more junior team member raising issues, since that would tell me the team is collaborating at a high level and visibility is high across the team (or that junior member is maturing). The earlier, the better, as well. A healthy team enforces quality as early as possible, so waste can be mitigated if not avoided entirely.

It is also important to take note of how a team self-enforces their definitions of ready and done. Are issues brought up in a constructive manner, that allow the team to learn and improve? Or do team members complain and point fingers? A healthy team takes collective responsibility and grows together. The definitions of ready and done are more than documents that sit somewhere on the team wiki and gather dust - these are contracts made by the team together, and so team members show their respect for their teammates by taking these contracts seriously, and by using them actively to safeguard the team's delivery and learn and grow. 

# A healthy team inspects and adapts

As a manager, one easy way to inspect a team's growth over the course of a project is to check the "last updated" date on the definitions of ready and done. A mature, healthy team will have updated these contracts as they go along and find holes or wasteful constraints. If, however, these were agreed on at the beginning of the project and then never revised since, this is a sign that either:

- The team did a remarkable job of defining exactly the right constraints on their input and output
- The team have not prioritized the maintenance of these documents, and probably hasn't gained much value from them

It's common to see teams focus narrowly on the constant stream of incoming work, and then forget to maintain and improve their practices. A team that faces internal and external chaos, for example, will likely struggle to focus on improvement. Even if team members flag issues related to work being inadequately prepared or completed, if the team does not have the ability to agree on and enact new practices, they will continue to be mired in these same recurring problems. The end result is often slumping morale and a pile of technical debt that can quickly grow out of hand.

As a leader, if you see these symptoms on your team, you can:

A) Help the team get the space, stability, and awareness it needs to self-inspect and improve. Often this requires a multi-pronged effort: coach members of the team to lead this effort, resolve sources of chaos, and lighten up on upstream/downstream pressures. A team that is struggling to get its basic needs met cannot be expected to operate at a high level, and as a manager/servant leader it falls to you to help the team get its needs met so it can move forward.   

B) Do nothing and hope the team/project makes it to the other end safely. I don't mean this to seem so glib - we've all been on projects with crippling problems that persist stubbornly, despite being known and acknowledged. For reasons ranging from technical to political, some problems remain simply intractable (or are *essential*), and as a manager might not be worth burning the necessary capital to try to resolve, or you might simply lack the necessary capital. The team still needs to be made aware that select problems will continue to nag it, and that other problems can still be resolved.  

[^1]: I use the term *manager* loosely here, to describe someone with responsibility for employing a team on a project and assessing the quality of the work the team delivers - servant-leader is another good industry term.
[^2]: We all know how fragile developer ego can be (*see: impostor syndrome*)