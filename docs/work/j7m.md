---
title: J7M
description: Java 25 distributed-object middleware and an application platform for services, durable work and recoverable workflows.
hide:
  - navigation
---
<div class="project-lead is-slate">
  <div class="project-art" aria-hidden="true"><img src="../../assets/img/art-network.svg" alt="" loading="eager" decoding="async"></div>
  <div class="project-lead-breadcrumb"><a href="../">← All projects</a><span>EGOTHOR · DISTRIBUTED SYSTEMS</span></div>
  <div class="lead-columns"><div><p class="overline">JAVA 25 · DISTRIBUTED OBJECTS · DURABLE WORK</p><h1>J7M</h1><p class="project-punchline">Distributed services and recoverable application workflows.</p><p>Java middleware combining live remote-object references, application packaging and deployment, durable work and explicit host security policies.</p><div class="lead-links"><a href="https://www.egothor.org/J7M/">Documentation ↗</a><a href="https://github.com/Egothor/J7M">Source ↗</a></div></div><div class="big-mark" aria-hidden="true">J7M</div></div>
</div>
<div class="project-prose" markdown="1">
## Objects and services

J7M is a **Java 25 distributed-object middleware and application platform**. Its runtime uses live `ObjectRef` identities, automatic proxies for Java service interfaces and decentralized discovery. References can pass between services as arguments, results and callbacks. Transport-neutral invocation uses gRPC as the default modern channel, with RMI retained as a legacy transport.

## Applications and durable work

The platform supports versioned `.j7m` application packages, verification, repositories and activation. Developers can use annotated components or explicit APIs to build distributed applications.

Reliability modules provide durable logs and queues, coordination, consensus, idempotency, fencing, inbox/outbox integration, jobs and saga workflows. These capabilities depend on their documented durability contracts and on application side-effect discipline. Security, ownership and resource policies remain explicit host responsibilities; remote invocation enforces authorization at the server boundary.

## Engineering documentation and boundaries

The [J7M manual](https://www.egothor.org/J7M/) covers programming patterns, deployment, security, operations and implementation limits. The [source repository](https://github.com/Egothor/J7M) includes runnable examples and repository-local validation. J7M is an active implementation; generic exactly-once distributed execution and transactions across arbitrary external systems are not claimed.

J7M continues the [J5M middleware lineage](heritage.md), bringing that foundation to a new generation of distributed Java applications.

<!-- Content owner: Leo Galambos. Review by: 2027-10-25. Sources: official J7M manual (https://www.egothor.org/J7M/) and Egothor/J7M README, consulted 2026-10-25. -->
</div>
<div class="next-project"><a href="../">← Project overview</a><a href="../radixor/">Next: Radixor →</a></div>
