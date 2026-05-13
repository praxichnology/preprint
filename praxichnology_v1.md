# Praxichnology: Naming the Field That Reads Footprints in Designed Environments — From Serious Games to AI

**Author:** Christian S. Loh, Ph.D.¹

¹ Southern Illinois University, Carbondale, IL, USA

**Correspondence:** [csloh@siu.edu](mailto:csloh@siu.edu)

**Preprint version 1.0** · Filed 2026-05-06 · License: CC-BY 4.0

**Zenodo:** [https://doi.org/10.5281/zenodo.20148907](https://doi.org/10.5281/zenodo.20148907)

**GitHub:** [https://github.com/praxichnology](https://github.com/praxichnology) 

---

> *"The recording of his activity or work… evaluation requires comparison."*
> — Bekhterev (1932, p. 220)
>
> *"An ant, viewed as a behaving system, is quite simple. The apparent complexity of its behavior over time is largely a reflection of the complexity of the environment in which it finds itself."*
> — Simon (1996, p. 52)

---

## Abstract

Multiple fields — serious games analytics, learning analytics, human-computer interaction, expertise research, sport science, and the behavioral analysis of AI agents — produce and read *traces* of situated activity inside instrumented environments, treating the records as evidence of learning, performance, and the development of expertise. The trace-reading is not in dispute. What has been missing is a field-level name for it. Without one, the foundational case for trace-as-evidence has been rebuilt paper after paper, and the cost compounds when the work travels across host disciplines whose readers have not seen the prior literature.

This preprint proposes **praxichnology** — from Greek *praxis* (purposeful action), *ichnos* (track or footprint), and *-logy* (study of) — as that name. The field is defined as the disciplined study of traces produced through situated activity in designed environments, used to infer the development of actors through learning, performance, and expertise. Two intellectual ancestors are named: Vladimir M. Bekhterev (1857–1927), for the empirical-realist commitment that observable action is admissible evidence of integrated psychological life; and Herbert A. Simon (1916–2001), for the operational principle that the trace of an actor's path is jointly determined by actor and environment, and that the means recorded in the trace can be read for the end the actor was acting toward. Either alone is insufficient; together they constitute the inheritance.

The preprint distinguishes praxichnology from cognate fields (ethology, paleontological ichnology), introduces a three-root scope diagnostic, and leaves the field theoretically open along two axes — theoretical commitment, and substrate, instrumentation, or actor — including an *artificial praxichnology* covering AI agents and human-AI collaborative work. Its purpose is to substantiate the term, name its ancestors, and stake priority in the open-science record so that downstream methodological papers and other researchers may cite it as a stable reference.

**Keywords:** praxichnology; trace data; serious games analytics; learning analytics; expertise; Vladimir M. Bekhterev; Herbert A. Simon; situated activity; AI agents

---

## 1. The Naming Problem

Action-traces have no field-level name.

Consider what already exists. Serious games analytics (SGA) has accumulated a catalog of trace-reading methods over the past fifteen years: learning curves, transition matrices, gate-event signatures, *q*-gram analyses of action sequences, the Expert Similarity Index (ESI), the Maximum Similarity Index (MSI), and behavioral fingerprinting, to name a few. Learning analytics reads navigation logs, clickstreams, time-on-task, and discussion-forum patterns to ask comparable questions. Human-computer interaction reads interaction logs and gaze paths. Expertise research reads protocol-analysis transcripts, performance-trial trajectories, and skill-acquisition sequences to characterize the difference between novices and experts. Sport science reads movement-capture data. Military training reads after-action replay logs from instrumented ranges and command simulators. Researchers studying the behavior of AI agents, increasingly, read traces of agent action inside designed environments.

What unites them is that all of them read records of situated activity — variously called *traces*, *action-traces*, or *footprints* — to infer something about the actor — typically competence, learning, adaptation, decision-making, or expertise. The actor may be human or an AI agent; but it is their actions, when traced, that become the admissible evidence in their own right.

The names available to describe this collection of works are inadequate. *Behaviorism* and *behavior analysis* carry the historical baggage of stimulus-response reductionism and the Skinnerian rejection of inferred mental life that most researchers in these fields explicitly do not share. *Reflexology* in modern English refers to a pseudomedical pressure-point massage practice; the term's older scientific usage is now largely obscured. *Ethology* belongs to the Lorenz–Tinbergen tradition of reading instinctive behavior in natural settings, and carries commitments to fixed action patterns and evolutionary fitness that do not apply to most trace-reading work in instrumented learning environments. *Telemetry* describes the collection of data, not its interpretation. *Learning analytics* is a real and useful field, but it is one substrate among several, not a name for the broader work. *Trace data* names the material itself, leaving the discipline that reads it without a name.

The result is that researchers across these fields do trace-reading without an explicit name for what they are doing. A reader new to the literature has no obvious term for a database search. A graduate student looking for a theoretical home assembles one from fragments. And a reviewer encountering a paper that uses interaction traces to characterize expertise development has no shared vocabulary to fall back on.

The consequence is not only lexical. Without a name to cite, every paper in this space pays a hidden tax: the foundational case for trace-as-evidence has to be rebuilt before the methods section can begin. That tax is visible in the present author's own paper trail.

## 2. The Retelling Problem

The naming problem first surfaced for the present author within serious games analytics. The methodological catalog is already substantial: SGA has been gathering trace-reading methods for over a decade under the heading of *performance measurement, assessment, and improvement* (Loh, Sheng, & Ifenthaler, 2015). What was missing was the name — and what kept getting rebuilt, paper after paper, was the foundational argument that action traces from designed environments count as evidence of learning at all. *Information Trails* (Loh, 2012) made the case that direct observation inside virtual environments is unavailable, so traces must serve as the assessment substrate. The String Similarity paper (Loh & Sheng, 2013) re-argued that competency could be demonstrated from a player's course of action in problem solving. The Maximum Similarity Index paper (Loh & Sheng, 2014) repeated the move, framing performance as something measurable from actions taken within the training environment *in situ*, as evidence of learning. A 2016 comparison paper (Loh, Li, & Sheng, 2016) rebuilt the same in-situ-traces-as-evidence claim from scratch. Even after the 2015 *Serious Games Analytics* chapter was available as a partial home, later papers continued to cite it for methods rather than for the foundational case.

Three reinforcing pressures kept producing this pattern. The first is the absence of a field-level citation home: with no name for the field to cite, the trace-reading-as-evidence argument had to be remade each time. The second is the gap between method and reader. ESI, MSI, and other sequence-similarity methods come from computer science and engineering, but SGA's readers are educators, instructional designers, educational technologists, nursing and health-professions researchers, and others without the computer-science or engineering background that makes these methods feel routine. The third is cross-disciplinary fanout. SGA applies across nursing, education, cybersecurity awareness, military training, leadership development, and other subject areas, so the kind of lineage-consolidation that builds up inside a single discipline — where readers stay inside computer science or electrical engineering paper after paper — does not build up here. The next SGA paper is likely to land in a different host discipline, with a different reader base who has not seen the prior work, and the foundational case has to be remade for that audience. Rajasegeran et al. (2024) is a recent illustration. A nursing-research team at Singapore General Hospital, with Loh and Sheng as collaborating co-authors, applied serious-game competency assessment to blood-transfusion training in *International Journal of Digital Health*. Even with the originators of ESI and MSI on the byline, the trace-as-evidence argument had to be rebuilt for a nursing-and-health-IT readership that had no prior exposure to SGA. Each paper therefore carries three burdens at once: re-arguing the foundational logic, onboarding readers to unfamiliar methods, and bridging into a host discipline that has not seen the prior literature.

A name for the field of study addresses the first pressure directly. Once such a name exists and can be cited, methods sections can cite the foundation rather than rebuilding it. The other two pressures do not disappear — readers in non-computer-science host disciplines will still need to be introduced to ESI, MSI, and similar methods, and SGA will continue to land across a wide span of subject areas. What changes is that those onboarding burdens stop having to carry the epistemological case along with them. A paper can teach its specific method to its host-discipline audience without also re-establishing the frame in which the method makes sense.

This preprint proposes the name **praxichnology** (*prax-ichno-logy*) for the field.

## 3. Two Intellectual Ancestors: Bekhterev and Simon

Praxichnology claims two intellectual ancestors in its conception. The two-parent framing is load-bearing: either ancestor alone is insufficient to ground the field; together they constitute its inheritance. Neither did research in praxichnology — the term did not exist in their lifetimes. What the field takes from each is a specific commitment drawn from their writings, not a relabeling of their research programs.

### 3.1 Bekhterev: the empirical-realist commitment

Vladimir Mikhailovich Bekhterev (1857–1927) was a Russian neurologist, psychiatrist, experimental psychologist, and institution-builder. His major program — *Objective Psychology*, published in Russian across 1907–1910 — predated John B. Watson's 1913 manifesto *Psychology as the Behaviorist Views It* by six years. Watson became the canonical reference in English-language behavioral science. Bekhterev did not. His program was buried under translation difficulty, terminological drift across his career (objective psychology → psychoreflexology → reflexology → collective reflexology), Soviet-era political cycles after his death, and the unfortunate conflation of *reflexology* with the foot-massage practice of the same name in modern English usage. The 1932 Murphy and Murphy English translation, *General Principles of Human Reflexology: An Introduction to the Objective Study of Personality*, remains the cleanest English anchor for direct citation.

Bekhterev grounded his program in the study of observable human activity in relation to the conditions that shape it — in his own terms, *the external peculiarities of the activity of man* and *their relation to external influences* (Bekhterev, 1932, p. 35). His methodological imperative was to record what people do and to evaluate it comparatively — the *recording of his activity or work*, with the clarification that *evaluation requires comparison* (Bekhterev, 1932, p. 220). The program is nearly tailor-made for a field that did not yet exist.

What praxichnology adopts from Bekhterev is the empirical-realist commitment that observable action, read with care for context, is ***admissible evidence*** of integrated psychological life. *Admissible*, not *exhaustive*: the commitment does not say that traces are all there is to know about the actor. It says that traces are evidence — that what people do in designed environments is, when read carefully, real information about what they are doing and what they are becoming.

What praxichnology does *not* inherit is more important to state than what it does. The specific neurological claims about reflex arcs and conditioned response stay with Bekhterev. So does the Soviet-era political vocabulary that occasionally entered his later work. The pseudomedical *reflexology* conflation is a problem of English-language usage and never had anything to do with his program in the first place. The bigger exclusion is how Bekhterev's program was absorbed, after his death, into Watson-Skinner behaviorism — a transmission that narrowed it considerably, stripping the *bio-social* and integrative elements in favor of stimulus-response reductionism. The commitment that observable action is admissible evidence of integrated psychological life is a much broader claim than the behaviorist claim that observable action is the only evidence of anything psychologically real.

We cite Bekhterev as ancestor. We do not annex his program.

### 3.2 Simon: the operational principle

Herbert A. Simon (1916–2001) is the second ancestor. *The Sciences of the Artificial* (first edition 1969; third edition 1996) contains a parable that has become canonical in cognitive science but whose methodological consequences for trace-reading have not, to the author's knowledge, been claimed for a coherent field. An ant moves across a beach. Its path is intricate, full of curves and corrections. A naïve reader might infer that the ant has a complex internal model of the beach. Simon's point is the reverse: the complexity of the path reflects the complexity of the beach, not the complexity of the ant. The trace is jointly determined by actor and environment, and the apparent intricacy of behavior often belongs to the environment that shaped it.

What praxichnology adopts from Simon is the operational principle that the trace of an actor's path is jointly determined by actor and environment, that trace-reading can in principle separate the two contributions, and that the ***means*** recorded in the trace can be read to infer the ***end*** the actor was acting toward. This is the methodological warrant for what praxichnology actually does as research practice: read the trace, hold the designed environment fixed (or vary it deliberately), and recover what is attributable to the actor versus to the habitat — including the ***goal*** toward which the path was organized.

The principle is consequential. Without it, every interesting feature of a trace is ambiguous: did the player hesitate because the player is uncertain or misled, or because the interface forced a pause? Did the trajectory improve because the learner is learning, or because the level got easier? Simon's framing licenses the methodological move that sorts these out — design the environment to be characterizable, then attribute residual variance in the trace to the actor.

### 3.3 Joint inheritance

Either ancestor alone would be insufficient. Read Bekhterev by himself and the program looks, to a skeptical reviewer, like warmed-over behaviorism — empirical commitment without a clear methodological account of how environment and actor are separated. Simon's Parable of the Ant, taken on its own, is operationally elegant but doesn't address the prior question of what kind of evidence action-traces are in the first place.

Together they constitute the inheritance praxichnology takes: from Bekhterev, the empirical-realist commitment that action-traces are admissible evidence of integrated psychological life; from Simon, the operational framework that lets us read traces with the actor and the habitat distinguished, and that lets the *means* recorded in the trace be read for the *end* the actor was acting toward. The combination is what permits a disciplined field. Neither ancestor did praxichnology. Praxichnology is what becomes possible when both commitments are taken together.

## 4. Praxichnology Coined

The field is named **praxichnology** (*prax-ichno-logy*), from three Greek roots:

- *praxis* (πρᾶξις) — purposeful action; situated, intentional doing
- *ichnos* (ἴχνος) — track, footprint, trace
- *-logy* (-λογία) — study of, discourse about

**A note on *praxis*.** The *praxis* root here is the Greek philosophical sense of purposeful or intelligent action — Aristotle's *praxis*, contrasted with *poiesis* (production) and *kinesis* (mere motion). It is not the Marxist-Hegelian sense in which Marx (1845/2024) and Gramsci (2020) developed praxis as world-transforming activity unifying theory and practice, nor the critical-pedagogy descendant of that tradition developed by Freire (2020) and Grundy (1987), in which praxis names a dialectical reflection-action loop oriented toward emancipatory social transformation. Praxichnology shares the etymological root with these traditions but not their political-philosophical commitments. Where Marxist praxis and its critical-pedagogy descendants use *praxis* to claim a particular *aim* for action (transformation, emancipation), praxichnology uses *praxis* to claim a particular *kind* of action (situated, intentional, observable) regardless of its aim.

A second clarification, equally important: the coinage is the compound *praxis* + *ichnos*, not a praxis-tradition derivative with a suffix tacked on. What praxichnology names is the study of *footprints* or *traces left by purposeful action*, and the ***ichnos*** element is doing as much work in the coinage as the ***praxis*** element. A reader who mentally splits the word as *praxi-chnology* and infers a Freirean lineage has misread the morphological seam; the seam falls between ***praxis*** and ***ichnos***, and the field name should be read as *prax-ichno-logy* (etymologically *praxis-ichno-logy*) — the study (-logy) of traces (ichnos) of purposeful action (praxis).

**Pronunciation:** prak-SIK-no-LO-jee.

**Grammatical forms:** the adjective is *praxichnological*. A practitioner is a *praxichnologist*.

**Formal definition:**

> Praxichnology is the disciplined study of traces produced through situated activity in designed environments, used to infer the development of actors — through learning, performance, and expertise.

The definition is deliberately compact. It commits to four elements and only four. *Traces*: the field reads recorded residues of activity, not the activity itself in real time and not the actor's introspective account of the activity. *Situated activity*: the activity is purposeful and embedded in context, broader than discrete action; it includes hesitation, timing, abandonment, recovery, and coordination. *Designed environments*: the habitat is structured, instrumented, and characterizable, distinguishing praxichnology from the natural-settings commitments of ethology. *Inference about the development of actors*: the trace-reading is for something — it is inferential, not merely descriptive, and the inference is about how actors develop within the habitat — read through learning, performance, and expertise.

The definition names *what* is being inferred (the development of actors, read through learning, performance, and expertise). It does not enumerate *what the inference is used for*, which runs along a second axis: performance measurement, assessment, and improvement (Loh, Sheng, & Ifenthaler, 2015). Further axes — which may include theoretical commitment, substrate, and the philosophical-anthropological framing within which trace-reading is situated — are open to imagination and development. Serious games analytics has worked along that second axis for over a decade. Praxichnology is the field that hosts both axes.

**What praxichnology is.** Anyone who reads interaction traces, decision sequences, or telemetry from a designed habitat — and reads them to make claims about what the actor is doing, learning, or becoming — is doing praxichnology, whether or not they have called it that. Closely related research communities that already do much of this work, often under their own names, include learning analytics, HCI, expertise research, sport science, military training simulation, and the behavioral analysis of AI agents (whether learned-policy or authored-policy). The term may simplify what is currently called something else; it is not an annexation of those fields.

**What praxichnology is not.** Praxichnology is not the study of player monetization, retention, or A/B-tested feature design; the trace is read to optimize a business outcome, not to infer the development of actors. Praxichnology is not the study of outcomes alone — pre-test/post-test scores, win/loss records, conversion counts — without the trace of how the actor got there. Praxichnology is not the measurement of movement, physiology, or interaction events for their own sake, with no inference attached about the development of actors — through learning, performance, or expertise. And praxichnology is not a relabeling of behaviorism: the inheritance from Bekhterev is the empirical-realist commitment that observable action is admissible evidence of integrated psychological life, not the stimulus-response reductionism that Watson and Skinner made of it. Researchers whose work matches these descriptions are unlikely to find the term useful, and the term is not aimed at them.

That is the field. The next section addresses what it establishes in its current form and what it deliberately leaves open.

## 5. Distinguishing Praxichnology from Ethology and Ichnology

### 5.1 Praxichnology is not ethology

Ethology, in the Lorenz–Tinbergen tradition, reads behavior live, in natural settings, with strong theoretical commitments to instinct, fixed action patterns, and evolutionary fitness. The reading is naturalistic in a specific sense: the environment is the unmodified habitat of the organism under study, not an environment the researcher has designed.

Praxichnology reads preserved or live-captured traces inside designed or instrumented habitats, with no ontological commitment about what the activity fundamentally is. It does not require that the trace correspond to an evolved fixed action pattern, and it does not require that the habitat be natural. The fields are cousins in the sense that both read records of activity carefully and treat the records as evidence. They are not the same.

A study that reads instinctive bird foraging in unmodified terrain is ethology. A study that reads player decision sequences in an instructional simulation is praxichnology. A study that reads movement traces in an instrumented sport-training environment is praxichnology, even though the activity itself is bodily and the lineage of trace-reading in sport science overlaps with ethological methods.

### 5.2 Praxichnology is not paleontological ichnology

Praxichnology and paleontological ichnology share the Greek root *ichnos*. They are etymological cousins. They are also disciplinary independents.

The disciplinary differences are substantive. Paleontological ichnology reads fossilized traces — preserved tracks, burrows, feeding marks — in *natural* environments shaped by geological time, to infer the behavior of *extinct* organisms and to reconstruct *paleo-environments*. The temporal mode is preservation across millions of years, the inferential targets are species and ecosystems, and the instruments are stratigraphy, sedimentology, and comparative anatomy. The reader community is paleontology and Earth science.

Praxichnology reads traces — usually digital, sometimes physical — in *designed* or *instrumented* environments, on timescales running from seconds to years. The actors are alive; the inference is about their situated activity, learning, and developing expertise. The instruments are interaction telemetry, log analysis, and sequence comparison. Readers come from learning analytics, serious games analytics, HCI, expertise research, and adjacent fields.

The relation is like *biography* and *autobiography* sharing *graphein*: etymological cousinship, not disciplinary inheritance. Neither field is senior to the other, and neither inherits the other's methods or commitments. Praxichnology stands on its own.

## 6. The Field Is Open — Future Modulations

Praxichnology names the field. The field is theoretically open: it establishes an object of study (traces of situated activity in designed environments) and a kind of inference (about the development of actors). It does not establish a single stance about how the inference should be drawn.

For now, the praxichnology described in this preprint has just one methodological flavor — the one inherited from Bekhterev: empirical-realist, externally observable, situated in designed habitats, with the trace read as admissible evidence of integrated psychological life. This is what Bekhterev called *objective*. It is not how the field has to be — only where the field stands at first naming. One research program is too thin a foundation to support internal differentiation. As praxichnology develops and attracts researchers from other intellectual traditions, methodological diversification is not only welcome but expected.

When future researchers develop modulations of the field, the naming convention is *X praxichnology* (e.g., *objective praxichnology*), sharing the field's root. Two axes of modulation are imaginable.

The first axis is *theoretical commitment*. A *cognitive praxichnology* would read traces with computational accounts of mind in view. An *ecological praxichnology* would foreground organism-habitat coupling and draw on the Gibson tradition. A *constructi++v++ist praxichnology* would attend to learners' meaning-making as an organizing concern. A *constructi++on++ist praxichnology* would read activity through Papert's commitment that learners build understanding by building external things (Papert & Harel, 1991). These are named here as placeholders, not as developed programs. What each would actually look like — what its analytic moves would be, what claims it would license, where it would draw its theoretical resources — is for researchers in those traditions to develop, not for the present author to specify on their behalf.

The second axis is *substrate, instrumentation, or actor* — what the trace is constituted by. A *somatic praxichnology* (from Greek *soma*, body) would read whole-body traces — sport movement, dance, live-action motion capture. A *tangible praxichnology* would read traces of physical pieces in physical space, digitally instrumented (board games with computer vision, physical-token interfaces, hybrid physical-digital exhibits). An *artefactual praxichnology* would read learner-built artefacts — Scratch projects, maker-space outputs, user-built games — together with the construction-process traces that produce them, such as version histories and prototype iterations. The artefact substrate is theory-neutral: it is read from constructi++on++ism (Papert & Harel, 1991), activity theory, distributed cognition, and other traditions, depending on the theoretical commitment brought to it. An *artificial praxichnology* — in Simon's sense (1996): designed rather than natural — would read traces where artificial agents are part of the actor, covering both pure AI agents acting in designed environments and human-AI collaborative work where both parties contribute to the trail (§7 develops the application cases). A study may combine these within a single design.

A note on terminology is warranted here. Papert coined *constructi++on++ism* explicitly as a reconstruction of Piaget's *constructi++v++ism* (Papert & Harel, 1991), and the two are routinely confused even by specialists. They are kept distinct in praxichnology: *constructi++v++ist praxichnology* (with a *v*) attends to how learners make meaning; *constructi++on++ist praxichnology* (with *on*) attends to how learners build understanding by building external things. The underlines on -++v++- and -++on++- are retained throughout this preprint as a visual reminder of which is which.

A researcher could in principle describe their work along both axes — a *cognitive tangible praxichnology* of physical chess training under cognitive-load instrumentation, for example. The cross-product is open and not specified here.

Methods of analysis — quantitative, qualitative, mixed-methods, Bayesian, network-analytic, and so on — are not a third axis. They apply across both axes: any praxichnology, on any axis combination, can be analyzed through any technique that suits the trace and the inferential question. For this reason, it is not appropriate to coin a *Bayesian praxichnology* or *qualitative praxichnology* — Bayesian inference, qualitative coding, and similar tools are techniques applied within a praxichnology, not ways of being one.

The field also needs two kinds of contributor that cut across the areas above.

**Methodologists.** Praxichnology borrows its analytical tools from other fields — sequence comparison, transition modeling, hidden-state inference, survival analysis, and similar techniques. The field needs methodologists who see trace data as a coherent object of study, not as a series of one-off applications.

**Instrumentation engineers.** The instrumentation — digital probes that log clicks and state changes inside software, telemetric probes that stream sensor data from physical environments, motion-capture rigs, eye-trackers, biomechanical sensors, agent-harness hooks for AI behavior — is the substrate of the field. What the engineers decide to record determines what the praxichnologist can later infer. Engineering is part of praxichnology, not separate from it: every claim the field makes rests on instrumentation decisions made earlier.

These are the field's to develop, not this preprint's to specify.

## 7. Where Praxichnology Applies — and Where It Does Not

### The three-root test

Praxichnology's name carries its scope. The three Greek roots — *ichnos*, *praxis*, and *-logia* — each name a condition that must hold for an activity to count as praxichnology:

1. **Trace must exist (*ichnos*).** A captured record of action.
2. **Purposeful action must exist (*praxis*).** The action traced must be directed toward skill, learning, performance, or expertise — not random, incidental, or merely operational.
3. **Study must exist (*-logia*).** The trace must be read inferentially for insight into actor development.

Lack any one and the activity is not praxichnology. A security camera produces trace but no purposeful actor pursuing development. A YouTuber filming birdhouse construction has trace and purposeful action but no study. A phenomenological interview captures actor(s) and study but no trace. The three-root test is what keeps "praxichnology" from inflating to "any data anyone reads" — empiricism with a Greek name.

**A note on actors.** *Praxis* does not specify whose action. The actor may be human, artificial, or hybrid — and the cases involving artificial agents are where praxichnology is positioned to do new work. Following Simon's sense of "the artificial" (1996) — designed rather than natural — *artificial praxichnology* names this family broadly: AI agents producing traces that human researchers read for capability, drift, or alignment, and human-AI collaborative work where both parties contribute to the trail (per Centaur Chess) [^1]. Future researchers will want finer distinctions inside this family; the foundational document plants the seed and leaves the specific corners for them to claim.

### Applies

- Serious games analytics: instrumented learning environments where decision sequences, hesitation, recovery, and trajectory toward expert performance are read as evidence of learning. Trace modalities extend beyond behavioral logs (clicks, navigation, decision sequences) to include eye-tracking, dialogues, and physiological signals, read alongside behavioral traces for richer inference. This is the originating domain.
- Learning analytics, where the practice fits.
- Human-computer interaction research that reads logged interactions or gaze paths to characterize how people use, learn, or struggle with a designed system.
- Expertise-development research across theoretical traditions: expert-novice trace comparison, deliberate-practice trajectories, protocol analyses of skilled performance, naturalistic decision reconstruction, and skill-acquisition studies more broadly.
- Sport-based training games and live sport training where the inferential interest is on skill acquisition: pitch recognition trainers, golf putting trainers, basketball free-throw trainers, football formation analysis, baseball pitch recognition. The *somatic praxichnology* descriptor fits this domain well.
- Military command-and-control training. Digital strategy and command-decision simulators (StarCraft-as-training research, tabletop digital wargames) are read primarily for their decision traces. Live force-on-force exercises with movement instrumentation — laser-engagement training at large combat-training centers — tilt toward *somatic praxichnology* when the inferential interest is on movement, maneuver, and kinematic decision-making under time pressure.
- Behavioral analysis of artificial agents — AI agents broadly, including learned-policy agents (reinforcement learning, large language model [LLM] agents) and authored-policy agents (persona-driven scripted agents) — when the agents act inside designed environments and the researcher reads their traces to characterize agent capability, drift, or alignment.
- AI-collaborative environments where humans and AI agents jointly produce action traces. Coding assistants like Cursor and Claude Code are the most familiar example — the developer's prompts, the agent's responses, and the resulting code form a shared trail. The same pattern holds wherever a person and an AI work together inside a system that records what each of them does. The traces are read in both directions: to improve the AI's behavior, and to characterize the human practitioner's evolving competence with these tools. The actor in such traces is hybrid; the environment is the harness; the inference runs reflexively on both sides.
- User research that uses logged interaction data to infer how users learn or develop competence with a system.

### Rich signals, thin proxies

The three-root test asks whether an activity is praxichnology at all; this section asks how trace data should be read once it is.

Praxichnology is not separated from related methods by what kind of signal it reads. Behavioral, cognitive, affective, psychophysiological (galvanic skin response, heart rate, EEG/brainwave), haptic, and biomechanical traces are all admissible — clicks, eye-tracks, facial-coding streams, force-plate output, yawns, motion capture, and so on. The line is *how* the signal is read.

Praxichnology treats traces as rich signals — signals that can be recombined with other traces, reinterpreted under different conditions, compared against expert or baseline traces, and read in relation to the designed habitat that produced them. The Matthew Effect Index (MEI), and other indices like ESI and MSI, are measurement instruments built on rich-signal logic: each computes a number from trace data, but the number means something only because the trace it summarizes was read in context. Performance measurement, assessment, and improvement (Loh, Sheng, & Ifenthaler, 2015) all fit comfortably inside this kind of reading.

What falls outside the field is the thin-proxy treatment of trace data: one signal, read in isolation, correlated with an outcome construct without contextual framing, treated as a one-step inference. Counting clicks and inferring engagement is the canonical thin proxy in digital settings. The somatic equivalent is counting yawns and inferring boredom. In biomechanics, reading force-plate output as the endpoint of an ergonomics evaluation does the same kind of thing. The signal types themselves are not the issue — the thinness is.

This distinction matters most for sport science, biomechanics, and operational training, where measurement is standard practice. Praxichnology is fully compatible with measurement when the measurement is built on contextual, recombinable, comparatively-read trace data. It parts company only when measurement is performed as a one-shot proxy, with no interest in how the actor produced the trace under what conditions.

### Lighter fit

Andragogy can be *served* by praxichnology — workplace simulations, professional training environments, adult-learner instructional design — but the fields are not co-extensive. Knowles' framework is centrally about adult-learner self-direction and not centrally about traces. Where adult learning research uses trace data, it overlaps with praxichnology; where it does not, it does not.

### Does not apply

Activities that fail any of the three roots fall outside the field — see the diagnostic at the top of this section. Survey research, phenomenology, retrospective interviews, pre-post outcome-only designs, and purely theoretical work fail the *ichnos* condition; pure biomechanical measurement and pure operational pass-fail evaluation typically fail the *-logia* condition (see "Rich signals, thin proxies" above).

The exclusions are not value judgments. Survey research, phenomenology, and outcome-only designs answer questions that praxichnology cannot answer; praxichnology answers questions that they cannot answer. The fields are complementary, not competitors.

## 8. Finding Yourself in Praxichnology — Audience On-Ramps

This section is for readers asking whether the term applies to what they already do.

**AI agent researchers studying agent behavior.** When you read agent traces inside designed environments to characterize capability, you are doing praxichnology with artificial actors. The field's commitments — admissible evidence, joint actor-environment determination of trace shape — apply directly, whether the policy is learned (reinforcement learning, LLM agents) or authored (persona-driven scripted agents). Authored-policy synthetic agents are particularly useful for instrument validation, because the policy is known by construction. A growing strand of this work reads traces of human-AI interaction inside coding harnesses and agentic systems as training signal for next-generation models — praxichnology applied bidirectionally, where the same traces inform both the AI agent's improvement and the human practitioner's tooling.

**Educators and instructional designers.** If you build learning environments and want to know whether learners are actually learning rather than performing, and you have access to records of what learners do — the footprints they leave — inside the environment over time, you are positioned to do praxichnology. The term gives a name to the half of your practice that is not covered by curriculum design or assessment vocabulary.

Instrumented inquiry classrooms — real-time sensor labs, computational-science modules, simulation-based science — fit this pattern. The sensor stream and the physical phenomenon are the object of student inquiry, not the praxichnological trace. The trace is the student's own action record around the inquiry task: sampling decisions, graph annotations, hypothesis revisions, lab-notebook entries. Reading those records to characterize how scientific reasoning developed is praxichnology, in math education, science education, or wherever instrumented inquiry happens. The teacher monitoring the students is the praxichnologist; the students using the instruments are the actors.

**Learning analysts.** If the term fits your practice, it is yours to use. Learning analytics has been doing praxichnology since before the term existed. The two share the same trace-reading commitment, applied across overlapping but distinct ranges: learning analytics specializes in digital learning environments — clickstreams, course-management logs, online interaction traces — while praxichnology also covers parallel work in physical instrumentation, sport science, training simulators, instrumented inquiry classrooms, AI agent behavior, and other substrates that don't fit comfortably under the "learning analytics" banner.

**Serious games researchers.** Praxichnology is the field-level name for what your accumulated trace-reading methods already do — transition matrices, gate-event analyses, *q*-gram comparisons, log sequential analysis, behavioral fingerprinting, and the methods still being developed. Citing it lets methods sections shorten and theoretical foundations stabilize, so that a paper landing in nursing, cybersecurity, leadership, instructional design, or any other host discipline can teach its specific method to its audience while citing praxichnology for the foundational case, instead of rebuilding that case from scratch each time.

**Game designers building for learning, training, or behavior change.** If you instrument your game to ask whether the design works, the trace-reading you do is praxichnology. The term distinguishes that work from monetization-driven game analytics.

**Computer scientists working on educational technology, intelligent tutoring, or learner modeling.** Where your models are trained on or evaluated against traces of actual learner activity inside a designed system, the reading of those traces is praxichnology. The modeling is a method within the field; the field's commitments predate the modeling.

**Expertise researchers.** Expertise-development work is praxichnology in substance, whatever the theoretical home. Newell and Simon's *Human Problem Solving* (1972) is the operational template praxichnology now names.

**Sport scientists, kinesiologists, and sport psychologists.** Where your work reads movement-capture or interaction traces to infer skill acquisition or perceptual-motor learning, it is praxichnology, often somatic in substrate. Where it measures biomechanics as engineering output, it is not. The inference-versus-measurement line above is the test.

**Military trainers, simulation designers, wargamers, and command-and-control researchers — including the I/ITSEC community.** If the after-action data you collect from instrumented exercises and simulators is read to characterize how decision-making develops, you are doing praxichnology.

## 9. Closing

The purpose of this document is to substantiate the term, to name its two intellectual ancestors, and to stake priority in the open-science record so that downstream methodological papers and other researchers may cite it as a stable reference.

Praxichnology is the disciplined study of traces produced through situated activity in designed environments, used to infer the development of actors — through learning, performance, and expertise.

Bekhterev held that the study of action required a science willing to read action as evidence; Simon held that the trace of an actor's path through an environment is shaped by both. Praxichnology takes both inheritances forward.

The field is open. Its methodological diversification is the work of the researchers who will populate it.

---

## References

Bekhterev, V. M. (1907–1910). *Objective psychology* [Russian original].

Bekhterev, V. M. (1932). *General principles of human reflexology: An introduction to the objective study of personality* (E. Murphy & W. Murphy, Trans.). New York: International Publishers.

Freire, P. (2020). Pedagogy of the oppressed. In *Toward a Sociology of Education* (pp. 374-386). Routledge.

Gramsci, A. (2020). Selections from the prison notebooks. In *The Applied Theatre Reader* (pp. 141-142). Routledge.

Grundy, S. (1987). *Curriculum: Product or praxis?* Falmer Press.

Loh, C. S. (2012). Information trails: In-process assessment of game-based learning. In D. Ifenthaler, D. Eseryel, & X. Ge (Eds.), *Assessment in game-based learning.* (pp. 123–144). Springer. [https://doi.org/10.1007/978-1-4614-3546-4_8](https://doi.org/10.1007/978-1-4614-3546-4_8) 

Loh, C. S., & Sheng, Y. (2013). Measuring the (dis-)similarity between expert and novice behaviors as serious games analytics. *Education and Information Technologies, 20*(1), 5–19. [https://doi.org/10.1007/s10639-013-9263-y](https://doi.org/10.1007/s10639-013-9263-y)

Loh, C. S., & Sheng, Y. (2014). Maximum Similarity Index (MSI): A metric to differentiate the performance of novices vs. multiple-experts in serious games. *Computers in Human Behavior, 39*, 322–330. [https://doi.org/10.1016/j.chb.2014.07.022](https://doi.org/10.1016/j.chb.2014.07.022) 

Loh, C. S., Sheng, Y., & Ifenthaler, D. (Eds.). (2015). *Serious games analytics: Methodologies for performance measurement, assessment, and improvement*. Springer. [https://doi.org/10.1007/978-3-319-05834-4](https://doi.org/10.1007/978-3-319-05834-4)

Loh, C. S., Li, I.-H., & Sheng, Y. (2016). Comparison of similarity measures to differentiate players' actions and decision-making profiles in serious games analytics. *Computers in Human Behavior, 64*, 562–574. [https://doi.org/10.1016/j.chb.2016.07.024](https://doi.org/10.1016/j.chb.2016.07.024) 

Marx, K. (2024). *Theses on Feuerbach* (Vol. 16). Marchen. (Original work written 1845)

Newell, A., & Simon, H. A. (1972). *Human Problem Solving* (Vol. 104, No. 9). Prentice-hall.

Papert, S., & Harel, I. (1991). Situating constructionism. In I. Harel & S. Papert (Eds.), *Constructionism* (pp. 1–11). Ablex Publishing.

Rajasegeran, D. D., Liu, K., Sheng, Y., Loh, C. S., Choh, A. C. L., Teo, K. Y., Fan, P. E. M., Tan, M. Y., Aloweni, F., & Ang, S. Y. (2024). Potential of serious games as a competency assessment tool for acute care nurses on the blood transfusion procedure. *International Journal of Digital Health, 4*, S1–S10. [https://doi.org/10.1097/JH9.0000000000000006](https://doi.org/10.1097/JH9.0000000000000006)

Simon, H. A. (1996). *The Sciences of the Artificial* (3rd ed.). MIT Press. (Original work published 1969)

Watson, J. B. (1913). Psychology as the behaviorist views it. *Psychological Review, 20*(2), 158–177. [https://doi.org/10.1037/h0074428](https://doi.org/10.1037/h0074428)

---

## Notes

[^1]: "Centaur chess" (also *advanced chess*) was organized by Garry Kasparov starting in 1998. Human players paired with chess engines competed in tournaments where the team could outperform either alone. The 2005 Playchess.com freestyle event sharpened the lesson: mid-rated humans using off-the-shelf engines with good process beat both grandmasters and dedicated supercomputers.
