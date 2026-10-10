---
title: Radixor
description: Learns word-to-stem transformations from dictionaries and compiles reduced patch-command tries, with independent models and reproducible multilingual evaluation.
hide:
  - navigation
---
<div class="project-lead is-amber">
  <div class="project-art" aria-hidden="true"><img src="../../assets/img/art-radixor.webp" alt="" loading="eager" decoding="async"></div>
  <div class="project-lead-breadcrumb"><a href="../">← All projects</a><span>EGOTHOR · LANGUAGE</span></div>
  <div class="lead-columns"><div><p class="overline">COMPUTATIONAL LINGUISTICS</p><h1>Radixor</h1><p class="project-punchline">Compiling morphological knowledge into a deterministic language primitive.</p><p>Learns word-to-stem transformations from dictionaries and compiles reduced patch-command tries, with independent models and reproducible multilingual evaluation.</p><div class="lead-links"><a href="https://leogalambos.github.io/Radixor/">Documentation ↗</a><a href="https://github.com/leogalambos/Radixor">Repository ↗</a></div></div><div class="big-mark" aria-hidden="true">Rᵡ</div></div>
</div>
<div class="project-prose" markdown="1">
## Research & publications

Nine author-released research manuscripts are maintained together with experimental methods, result data and reproducibility references. The publications are project-associated manuscripts; **availability on ResearchGate is not a peer-review claim**.

<div class="paper-list">
<div class="paper-row"><span>01</span><p>Does a Lexicon-Trained Stemmer Generalize? A 20-Language Study of Held-Out Lexical Families</p></div>
<div class="paper-row"><span>02</span><p>Edit Costs as Structural Hyperparameters in Dictionary-Induced Stemming: A Multilingual Sensitivity Study</p></div>
<div class="paper-row"><span>03</span><p>Classifying Multilingual Stemmers by Pareto Strata: Error Regimes in Pairwise Lexical Conflation</p></div>
<div class="paper-row"><span>04</span><p>The Stemming Policy Is Data: Adapting a Lexicon-Trained Stemmer to Alternative Conflation Objectives</p></div>
<div class="paper-row"><span>05</span><p>Runtime Efficiency of Lexicon-Trained Stemming: Compiled Structure and a Speed–Reference-Agreement Envelope in Radixor</p></div>
<div class="paper-row"><span>06</span><p>Lexical Resource Consistency and Learned Transformation Vocabulary in Multilingual Stemming</p></div>
<div class="paper-row"><span>07</span><p>Compiling Learned Lexical Transformations: Semantic Canonicalization and Accepting-Leaf Generalization in Patch-Command Tries</p></div>
<div class="paper-row"><span>08</span><p>Where Retrieval Quality Goes: Rethinking Stemming in Modern Search</p></div>
<div class="paper-row"><span>09</span><p>From Lexical Edits to Verified Stemming Policies: Two-Sided Adaptation in Radixor</p></div>
</div>

[View the complete research series, papers and evidence ↗](https://leogalambos.github.io/Radixor/scientific-results/){ .research-link }

## Engineering model

Lexical examples are transformed into compact executable patch commands and a reduced trie. Language knowledge is learned and validated offline; production lookups execute a compiled read-only model. Deterministic alternative outputs preserve ambiguity for downstream search or analysis.

[Technical architecture and model formats ↗](https://leogalambos.github.io/Radixor/)
</div>
<div class="next-project"><a href="../">← Project overview</a><a href="../zeroecho/">Next: ZeroEcho →</a></div>
