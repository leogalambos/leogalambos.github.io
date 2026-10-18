---
title: conflux
description: A focused Java library for type-safe shared keys and concurrent state changes, keeping independently developed components decoupled.
hide:
  - navigation
---
<div class="project-lead is-slate">
  <div class="project-art" aria-hidden="true"><img src="../../assets/img/art-conflux.webp" alt="" loading="eager" decoding="async"></div>
  <div class="project-lead-breadcrumb"><a href="../">← All projects</a><span>EGOTHOR · JAVA INFRASTRUCTURE</span></div>
  <div class="lead-columns"><div><p class="overline">SMALL JAVA INFRASTRUCTURE</p><h1>conflux</h1><p class="project-punchline">Shared context and change events, without a large framework.</p><p>A focused Java library for type-safe shared keys and concurrent state changes, keeping independently developed components decoupled.</p><div class="lead-links"><a href="https://www.egothor.org/projects/conflux/">Project overview ↗</a><a href="https://gitea.egothor.org/Egothor/conflux">Source ↗</a></div></div><div class="big-mark" aria-hidden="true">cx</div></div>
</div>
<div class="project-prose" markdown="1">
## Engineering documentation

The source and [project overview](https://www.egothor.org/projects/conflux/) document the intended small API: typed keys, shared current state, change notifications, weak listeners and thread-safe coordination. There is no standalone scientific publication asserted for this component.

## Design principle

Independent modules often need to publish a little state and notify each other. conflux deliberately solves that narrow problem without attempting to become a dependency injection framework, distributed broker or full application platform.

## Shared context and events

The library combines a shared processing context with an event bus. A component can expose state through typed keys and communicate changes without coupling its implementation to every component that consumes them. Shared current state and change notifications provide complementary ways for independently developed modules to coordinate.

This focus places conflux within the Java infrastructure side of the Egothor portfolio: a small coordination component that applications can use alongside their own processing logic.

<!-- Content owner: Leo Galambos. Review by: 2027-10-18. Source: imported selected-work portfolio and existing project overview. -->
</div>
<div class="next-project"><a href="../">← Project overview</a><a href="../jai/">Next: JAI →</a></div>
