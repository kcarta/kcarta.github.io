---
title:  "The value of writing tests"
date:   2020-08-30 00:00:00 +0000
tags: [testing, thoughts]
---

In this post, I'd like to share some of my thoughts on the value of a good automated test, and why I think that even the teams that write them, don't appreciate their tests enough.

I often come across organizations that write tests, and are quite defensive about doing so, but they don't seem to value the tests they have, or the ones they write. Tests are commonly seen as a necessary pain, a bare minimum effort for quality assurance. In the pipelines or dev environments where tests are run, they are *barely* supported, and never looked at until they fail. I think it is a true shame that there is such a widespread culture of writing tests, but not of valuing them.

**The act itself of writing a test should provide immediate, obvious value. Once written, a test should continue providing clear and measurable value.**

If your tests fail to live up to this standard, take that as a red flag (and read on!).

Before I jump in, note that I am lumping all unit, integration, system, end-to-end, etc. tests together - everything I will write here goes for all manner of automated code tests equally.

# The purpose of a test

I think most developers would agree that the primary purpose of an automated test is to fail. In failing, a test alerts the team to a broken part of the system. Writing tests to achieve this behavior is an easily-understood form of quality control. In most teams and on most projects, more tests is usually taken to equate to higher quality, and "write unit tests" is always a box high up on the checklist to "Done" [^1].

However, I think that's a very unambitious understanding of what a test can do. I think writing a test to fail, requires the bare minimum effort and produces the bare minimum result.

# The value of a good test

> Does the test that never fails still have value? 
> (*If a tree doesn't fall in the woods...*)

## Writing tests **helps a team uncover faults in a specification**

A test should be the first place where you encode a new specification into your system. At the very least, the test should exist at a higher level of abstraction than the code under test, one where the outline and intent of the specification should be clear. 

If the specification doesn't make sense in the context of your test, then there is probably something wrong about how the spec fits into the system, how the spec is described, or how it is understood. The earlier you can write a test that helps you gain this awareness, the better - in my opinion this is why teams that make effective use of TDD and BDD perform so well. They simply reject inadequate requirements, demanding good quality from the very beginning of the development process. 

## Tests are living **documentation**

By encoding a specified behavior into a real, working system, a good test suite shows the actual cases and contexts in which that specification is meant to be used, and how it is expected to behave. When any of these encoded assumptions no longer hold true, a test (or multiple) fails. In this way a good test suite creates living documentation.

If the specified behavior or its design is violated, the result will be failing, flaky, or difficult-to-understand tests. A good development team should be able to see what tests fall into this category and flag them as technical debt. Metrics on test quality can help a team to understand what areas of a product are high-quality and which areas need improvement. 

If even the development team failed to understand or express a behavior clearly enough to write good tests for it, what is the likelihood that the end user will understand or enjoy using it?

## Tests **support good design practices**

One of the main advantages I see to TDD practice is that when you write a test *first,* the code you write has to support reuse from the very beginning. Code written following TDD will always start with two clients: its test, and its collaborator(s) in the system. 

As previously stated, a good test mimics real usage and acts as documentation. Practicing TDD makes it painful to write bad code, since the starting objective is to write a good test [^2]. The code I write following TDD usually follows principles like SOLID by default, and the constraint of a test written in a specific way means that when I write my code, I can focus entirely on the behavior I am trying to achieve. 

On the flip-side of this, tests can expose and punish poor design. A poorly designed system is *brutally difficult and expensive* to write tests in.

# So, why don't teams write good tests?

As a developer, I've seen colleagues laugh at the thought of even trying to write tests, I've been in teams that didn't think they had time to write tests, and I've lived in codebases that make testing so difficult that its easier to just give up and accept the risks of never testing adequately.

I think the following reasons cover most of the cases where a team doesn't write good tests:

- The team doesn't understand their system or their specifications well enough
- The system design & architecture doesn't allow the team to write good tests
- The team has never learned how to write good tests or design testable systems
- Culture doesn't allow the team to prioritize testing or to have a system that supports good tests

In these cases, the path forward would involve a combination of a culture change, and a prolonged effort to pay down technical debt. Both require an enormous undertaking and large amounts of willpower and patience. The sad truth is that some organizations and some teams can get good testing done right from the start, others have to learn and pay the expense of improving along the way, and others are stuck suffering in the hellscape that's been created.

To not end on a pessimistic note, I'll share this fantastic video from the inimitable Sandi Metz, an OOP design guru:

[https://www.youtube.com/watch?v=URSWYvyc42M](https://www.youtube.com/watch?v=URSWYvyc42M)

[^1]: This is also why teams go astray with valuing test coverage as a metric for code quality. 

[^2]: I find that anti-patterns like crazy injection techniques, brute-force mocking, etc, usually result from code-first-then-test practices, when a test must cover "bad" code with dependencies, poor visibility design. In this way bad code design drives bad tests, whereas in TDD you have the opportunity for good tests to drive good code design.