---
layout: post
title:  "My Delivery Sheet"
date:   2025-03-06 00:00:00 +0000
tags: [agile-pm]
---

Since 2019 I have been re-using the same Excel sheet for project budgeting.

Over time I have used many variations of this sheet across many different software deliveries. All sorts of highs and lows have occurred across these deliveries, but none have ever had a surprise budget overrun[^1] - so I'll take that to mean this tool has served its purpose well.

I'd like to take a moment to describe and then reflect on this special little piece of software I made years ago and continue to go back to. 

## The sheet

At its most basic, the sheet is built up of:
- A top set of rows for time periods (start & end), ideally equal in length - usually weeks, months, or sprints.
- An upper set of rows for team members, with a cell for their role and then the remaining cells for the amount of time they work within each time period. 
- A lower set of rows aggregating the spend per time period per role.
- A "Setup" sheet with variables, like a roles-rates mapping and list of holidays. 

It ends up looking something like this:

![Screenshot of an Excel-based budget sheet](/static/img/posts/budget-sheet.png)

### Variations
Over the years I've made variants with abilities like:
- Comparing snapshots of planned vs. actual time & budget.
- Comparing best v. worst case forecasts.
- Planning team allocations based on % instead of raw time.
- A Gantt-style roadmap of activities to provide context for the time & budget allocations.
- Plotting spend against burndown, using a backlog imported from Jira (and some PM black magic 🧙🏻‍♂️). 
- Pivot tables to explore things like the amount spent per feature and the amount spent on changes vs. original requirements.[^4] 
- Updating hours automatically based on data from a time registration platform.
- Margin % based on team member 'blended' internal rate (i.e. cost to us) v. external rate (i.e. cost to customer).

## The mindset behind the sheet

The nature of my work as a consulting PM means that I usually run *project deliveries*, so even when my team is building a product, we deliver it across one or more projects, backed by contracts that are typically based on time & material.

I want to run agile deliveries - that is, I want to agree on a plan, but leave open the ability to adapt the plan as new and better knowledge arrives. Additionally, I like to let my team focus on delivering value & quality, and let me and the project sponsor worry about the budget.

If a project manager has one overriding mandate, it is to hold within an agreed budget. Scope and timeline, even when specified in a contract, tend to be more flexible than budget. Because of this, when filling out this sheet as a forecasting activity, I tend towards over-allocation by assuming full-time allocation without accounting for leave or random sick days. When negotiating with customers for contracts, I typically explain that the numbers in this sheet represent an upper-limit on the budget.

In this way, this sheet helps me figure out a 'frame' for the delivery, with a very conservative overall budget.

How does this help me run agile deliveries? 

For one, it means I don't have to enact strict controls on time, because the conservative forecasting *usually* results in there being a buffer I can draw from. This buffer absorbs overruns from needing to increase or extend team member allocations. I find this balancing to happen naturally over the project lifetime, and so I rarely need strict time controls - and when I do, I see it coming long in advance as I update my sheet. In most cases, I have plenty of time to discuss with the customer about whether to look for a budget extension, or to re-prioritize the backlog.

Secondly, it means I get to make my delivery plan based on a *rough* overall forecast, estimating the team size & duration needed to deliver on the expected project objectives. I much prefer this to the alternatives, like aggregating "precise" time-based estimates and then plotting out allocations from that.[^5] If estimates are useful, I typically do relative-sizing exercises with the team and then perform some calculations from there to get me back to the high-level planning. I'm a fan of "rather roughly right than precisely wrong", and my practices around using this sheet let me hold to that instead of running to the false security of nitty-gritty time-based estimates.

Finally, this sheet is only one tool in my toolchest. At a minimum, I have a backlog & kanban board to run my delivery from - that's where most of my effort actually goes, and where I get the most benefit from working with my skilled team members. Because I typically keep budget planning & tracking at the highest level possible, I find very little benefit in extracting time estimates from my team.[^6] 

## Critical questions

Looking back on all these years & projects, I've started wondering - why does this sheet still work for me? That has led to further questions, like: 

- Why do I keep returning to *this* sheet? Why have I never adopted an alternative?
- Why Excel? Why not some other tool? If the basic format & logic usually stays the same, why haven't I written a piece of software to do this?
- Is this usable for anyone besides myself? Does this help my customers or my colleagues?
- Any number of counters to the lengthy explanation I gave in the previous section on how this sheet supports me in framing agile deliveries...

Like most PM's, I have a love-hate relationship to Excel. I love it for its flexibility - just see the long list of variations I've whipped up over the years - and I hate it for its random gotchas and hard-to-spot errors. 

I think the primary reason I keep going back to this sheet, is that each project comes with its own nuances, and having used this tool for so many years, I find it easy to tailor it to different purposes. I'm experienced enough to trust my own opinions. When I have tried other products, I have found myself irritated by having to conform to someone else's opinionated approach to project management, baked into those tools.

So far, I haven't had a customer complain about having to use this sheet with me. I usually have to explain how it works at first, but it's simple enough to be pretty easy to grok - hours on top, spend on the bottom. I don't know if any senior PM colleagues have ever adopted this sheet (they usually have their own go-to tools), but I have seen junior PM's use it effectively in their own projects.

Does it *really* enable me to run agile deliveries? Without attempting detailed long refutation of my previous points, in my experience, I typically spend most of my efforts negotiating backlog priorities with my customers, and relatively little negotiating week-by-week costs. To me, this is a positive sign.

I'd love to gather thoughts from other consulting PM's - are we all going around with our favorite Excel sheets? Or in 2025 are there better tools for balancing flexibility & control over deliveries? And in product companies, do product managers have more advanced tools for tracking spend? Or are they going around with their own Excel sheets too?

[^1]: Or a severe underrun, which in the consulting business is undesirable as it can cause nasty surprises to revenue forecasts.

[^4]: Fun with fixed-cost deliveries!

[^5]: Or worse, creating detailed gantt-style plans with specific team member hours tied to sequenced work package deliveries.

[^6]: One way of putting this, is that I'm trying to create ideal conditions for development - [Kent Beck's proverbial "Forest"](https://tidyfirst.substack.com/p/forest-and-desert)

