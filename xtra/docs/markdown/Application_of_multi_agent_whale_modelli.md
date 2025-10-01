# Application_of_multi_agent_whale_modelli

Converted from: Application_of_multi_agent_whale_modelli.pdf
Date: 2025-08-19

---

APPLICATION OF MULTI-AGENT WHALE MODELLING TO AN
INTERACTIVE SAXOPHONE AND WHALES DUET
Alexis Kirke
Interdisciplinary
Centre for Computer
Music Research,
University of
Plymouth, UK

Samuel Freeman
CeReNeM,
University of
Huddersfield, UK

ABSTRACT
„Fast Travel‟ is named after a Blue Whale call, and is
both a scientific experiment in computer-modelling of
schools of artificial singing whales and a live
performance for saxophone and electronics. The
audience hear a live surround sound interaction
between a saxophonist and artificial schools of
whales. The whales hear the sax as if it is another
whale. The audience are surrounded by at least four
speakers and a sub-woofer with a saxophonist in the
middle. The whale sounds, driven by a computer
model, move from speaker to speaker, as the invisible
but audible artificial whales move within an invisible
sea - the audience are "underwater" with the schools
in this “sound sea”. The artificially intelligent whale
models sing synthesized electronic sounds, evolving
new songs live based on hearing each others'
performances. The composition title is not just
because of the Blue Whale-type song, but because of
the way it speeds up the evolution of the whales‟
song-tuning. Decades are compressed down into the
12 minutes as the audience time travel through the
evolution of the underwater music. But the song
evolution is driven here by the saxophone, rather than
solely by other whales or man-made acoustic
phenomena. The scored saxophone is audible to the
whales, and influences their tunes through imitation.
Although the majority of the saxophone music will be
pre-scored, the behaviour of the whales is not 100%
predictable because of complex interactions, thus the
performance will differ each time.
1.

INTRODUCTION

The term “Fast Travel” refers to the songs blue
whales sing when they are moving fast rather than, for
example, their “milling” songs [1]. The Fast Travel
calls come in repeated A-B pairs. The B songs were
found by recent research to have the extraordinary
property of perfect tuning to the key of C, having
dropped a major 3rd from the key of E in the last half
century[2].
The performance is called “Fast Travel” not just
because of this inspiration but because of the way it
speeds up the evolution of the whales‟ song- tuning.
Decades are compressed down into the 12 minutes as

Eduardo Miranda
Interdisciplinary
Centre for Computer
Music Research,
University of
Plymouth, UK

Simon Ingram
Marine Institute,
University of
Plymouth, UK

the audience time travel through the evolution of the
underwater song. But the tuning evolution is driven
here by the saxophone, rather than solely by other
whales or marine acoustic phenomena. The
saxophone is audible to the whales, and influences
their tunes through imitation. Hence the saxophonist
was able to use a score to move the whales‟ songs
from its initial tuning down to a lower tuning. Within
this time whales communicate and learn pitches from
each other too. The artificial whale schools are not
limited to the deep calls of Blue Whales, but extended
to include Humpbacks, renowned for beautiful social
singing. The reason for this was that Blue Whale song
is not so interesting from a pitch variation point of
view, and from a pitch adaptation point of view, and
its pitch range verges on the subsonic [2].
Whereas Humpback whales songs have a wide
range and variation, and are so beautiful they have
been released on many CDs. Humpback song appears
to be culturally adaptive in interesting ways as well
[3].
2.

WHALE SONG

Blue Whale males sing, with the purpose of this
singing having both been considered as being for
echo-location and perhaps social [4]. Recent research
has shown that certain part of blue whale songs – the
second part their “Fast Travel” calls - are incredibly
closely tuned to the key of C, though it is not clear
why this should be the case [5]. There is evidence that
Blue Whale song used to be in the key of E and has
lowered to the key of C over the last 50 years.
Blue Whale song is in a large part subsonic, and the
most famous form of Whale song is in fact heard from
male Humpback whales. The first in depth
examination of Humpback whale song was done by
Roger Payne [6] and led to the release of best-selling
record. One of the most interesting aspects of Payne‟s
analysis was the proposal of a form of hierarchical
musical structure in the Humpback Whale song. This
is shown in Figure 1. As well as having a musical
structure, Humpback whale song appears to actually
change over time as a result of interaction between the
whale songs [3].

Figure 1. Humpback Whale Song Structure

3.

MULTI-AGENT SYSTEMS

The precise definition of multi-agent systems has been
approached in different ways. For example [7]
focuses on agents that are situated in an environment,
with each agent autonomous, and with explicit goaldirected behaviour – not purely reactive. However
there are a number of multi-agent system where the
agents have a central controller [8][9], and there are a
number of researchers who include reactive-based
systems as multi-agent. This paper will take this
second, more wide-ranging approach. We will focus
on one particular area of MAS, where the agents are
provided with Biologically-inspired constraints –
often called Instance-based Models (IBM) [10].
One of the first was investigate such systems in the
context of modeling musical culture is [11]. The
system generates musical motifs in a way designed to
study the evolution of culture. In this case the agents
use a two-way imitation procedure to bond socially.
Agents can store a repertoire of tunes and have a basic
biological model of an adaptive voice box and
auditory system. Agents pick other agents to interact
with randomly. When two agents A and B interact the
following process occurs: if agent A has tunes in its
repertoire it picks one randomly and sings it, if not
then it sings a random tune. These tunes are three
notes long and do not grow in length. Agent B
compares the tune from A to its own repertoire and if
it finds one similar enough, plays it back to agent B as
an attempted imitation. Then agent B makes a
judgement about how good the imitation is. If it is
satisfied with the imitation it makes a “re-assuring”
noise back to agent A, otherwise it does not. Based on
the success of the imitation Agents A and B update
their repertoires and their voice box settings to try and
improve their chances of socially bonding in later
interactions – e.g. by deleting or re-enforcing tunes,
or making random deviations to their voice box
parameters. The aim of the system is to see how the
repertoire is generated and affected under such social
pressures. As a result of the social bonding
interactions a community repertoire begins to emerge.

There are other approaches utilizing this basic idea,
such as [12].
There has been some research into modeling and
synthesizing of whale song [13] but not into whale
song interaction. So how closely these multi-agent
modelling approaches relate to humpback or blue
whale tune interactions is unknown, but is being
investigated in projects we are developing. The Fast
Travel system differs to those approaches in a number
of ways, including the fact that the agents in Fast
Travel are embedded in an artificial sea. Thus the
impact that whales’ songs have on each other is
dependent on their relative position. Furthermore the
system allows a heterogeneous agent to be inserted
externally – in this case a human saxophonist. For the
purposes of this project, the focus was on the artistic
result rather than accurate whale modeling at this
stage. Hence a relatively simple whale model has
been produced, which will then be augmented in
future research. Furthermore the whale song synthesis
algorithm was not designed to model whale biology
but to produce an artistically convincing sound.
4.

WHALE MODEL

For the first implementation of the "Fast Travel"
multi-agent system (FTMAS), a generic artificial
whale agent (AWA) model was used for all agents of
the whale school. This is similar to the approach taken
by Anwar et al[14] to simulate human-whale
interactions in the St. Lawrence Estuary in Quebec,
Canada. No differentiation was made between the 12
species of marine mammals in the estuary because the
main focus of their research was on the behaviour of
whale-watching tour boat operators. In "Fast Travel" it
is the whale songs which are of most interest. The
sounds of both Blue and Humpback whales are
included in our model, with more of the Humpback
type sounds being used because of the well
documented musicality of these. Also in contrast to the
multi-agent system designed by Anwar et al., the
human aspect of the FTMAS is derived from real-time
audio analysis of the live saxophone performance,
rather than being simulated. The AWAs react to each
other, to their environment, and to the saxophonist

Figure 2. Fast Travel Model Display

with behavioural models for both navigation and aural
interaction (listening and singing).
There are two modes of navigation. The first is
based on social interaction between the whales, and in
which an agent will move either towards or away from
another whale using a number of short term personal
tendencies to decide which other agent (looking first
for the nearest), and which direction. The second
mode represents migrational movements of the whales.
A parameter is used to set the balance between these
two modes of navigation.
In this mode the trajectory of each AWA is
determined by the agent's current location within the
environment in conjunction with an unchanging
personal tendency to move in particular direction.
Each AWA is initialised with its own 'pitch centre'.
Pitch tracking analysis of the audio input from the
saxophone assigns an ever changing pitch centre to the
input. The AWAs are aware of the input pitch as well
as when the input is and is not 'singing'. The AWAs
are also able to 'hear' each other in terms of pitch and
singing-or-not. A set of probability weightings is used
by each AWA to determine not only if they will sing
or not, but also what they will sing. An AWA will
change its own pitch centre in reaction to those of the
last heard pitch of the input, of the whale they are
currently focused on for social navigation, and of the
last AWA to have started singing. A subset of whale
song audio used by the composer to derive the scored
saxophone part is used in a granular sound engine to
give voice to the artificial whale agents. This engine
allows the agents to alter the duration of a whale sound

independently of an evolving pitch envelope of the
same. The AWA model is written as a JavaScript for
Max/MSP/Jitter (awa.js), and a second JavaScript
(fastTravel.js) is used to dynamically create and
control agents.
Saxophone
1 Slower tempo, low loudness.
When score complete, finish
with 60 seconds
improvisation, focusing on call
and response interaction with
whales.
2 Medium tempo, medium
loudness.

3 No saxophone for first 90
seconds. Then 60 seconds
extended saxophone
improvisation, imitating nonpitched whale sounds.
4 Faster tempo, loud. At end of
scored notes, 60 second
improvisation, imitating nonpitched whale sounds.

Whale parameter
evolution
Humpbacks only. Low
density. No whale song
overlap allowed

Low density
Humpbacks and Blue
Whales. Overlap of
songs allowed. Nonpitched songs allowed.
High density
Humpbacks only. Full
overlap allowed.

High Density.
Humpbacks and Blue
Whales. Full overlap
allowed. On last score
page allow density to
fade down.

Table 1. Overview of the composition “Fast Travel”

5.

COMPOSITION STRUCTURE

A database of humpback whale song was collated
from available recorded song; some pitched and some
rhythmic. Out of these, half were incorporated into the
whale song synthesis algorithm, and half were utilized

in the saxophone composition. The sound files were
de-noised and cleaned. A series of “building block”
phrases were written for the tenor saxophone. This
was done with the help of a pitch tracking algorithm
[15] to transcribe the rhythms and pitches found in the
Humpback whale database. These phrases were then
ordered, repeated and transformed based on the
composer‟s preferences. Part of the process involved
taking into account leaving space for the whales to
respond either in serial or in parallel; and taking into
account the fact that the whales start off quietly in the
distance and move closer, attracted by the sound of
saxophone. The general structure of the piece is
shown in Table 1.
6.

CONCLUSION

Humpback whale song is incredibly beautiful,
especially when heard echoing underwater by divers
lucky enough to be near a school. Most of us will
never get to swim amongst singing Humpbacks. Also
most of us will never get to hear the deep throbbing
and subsonic blue whale song. Through the use of
sound diffusion techniques in MAX/MSP and whale
song modelling it becomes possible to immerse the
audience not only in an artificial whale environment,
but also in a musical composition. The scored
saxophone is audible to the whales, and influences
their tunes through imitation. Although the majority
of the saxophone music will be pre-scored, the
behaviour of the artificial whales is not 100%
predictable because of their complex interactions, and
so the performance will different each time. Fast
Travel was commissioned by Peninsula Arts,
University of Plymouth. The technologist is Samuel
Freeman, University of Huddersfield; the Marine
Mammal Consultant is Simon Ingram at the Marine
Institute, University of Plymouth. As a result of the
initiation of Fast Travel as an artistic project, a new
project is being developed in the purely scientific
arena for humpback whale modelling. This is an
unusual example of an artistic project being the
inspiration for a hard science project, rather than the
other way round.
7.

REFERENCES

[1] Oleson, E., Calambokidis, J., Burgess, W.,
McDonald, M., LeDuc, C., Hildebrand, J.,
“Behavioral context of call production by eastern
North Pacific blue whales”, Columbia
University, Marine Ecology Progress Series, Vol
330: 269-284, 2007
[2] McDonald, M., Hildebrand, J., Wiggins, S.,
“Increases in deep ocean ambient noise in the
Northeast Pacific west of San Nicolas Island,
California”, J. Acoust. Soc. Am., Volume 120,
Issue 2, Pp. 711-718, 2006

[3] Mercado III, E., Herman, L., and Pack, A.,
“Song copying by humpback whales: themes and
variations”. Animal Cognition. Vol. 8, No. 2.,
2005
[4] McDonald, M., Hildebrand, J., Mesnick, S.,
“Biogeographic Characterization Of Blue Whale
Song Worldwide: Using Song To Identify
Populations”, Journal of Cetacean Research and
Management, 8 (1):55-65, 2006
[5] Hoffman, M., Garfield, N., Bland, R.,
“Frequency synchronization of blue whale calls
near Pioneer Seamount”, J. Acoust. Soc. Am.,
Volume 128, Issue 1, Pp. 490-494, 2010
[6] Payne, R., McVay, S., “Songs of Humpback
Whales”, Science, vol. 173, no. 3997, 1971
[7] Wooldridge, M., An Introduction to Multi-Agent
Systems, John Wiley and Sons, 2004
[8] Murray-Rust, D., Smaill, A., “Musical Acts and
Musical Agents”, Proceedings of the 5th Open
Workshop of MUSICNETWORK, Vienna,
Austria, 2005
[9] Baxter, J., Horn, G., Leivers, D., “Fly-by-Agent:
Controlling a Pool of UAVs via a Multi-Agent
System.” Proceedings of the Twenty-seventh
SGAI International Conference on Innovative
Techniques and Applications of Artificial
Intelligence (AI-2007), Cambridge, UK, 2007
[10] Grimm, V., Railsback, S.F. “Agent-Based
Models in Ecology: Patterns and Alternative
Theories of Adaptive Behaviour”, In AgentBased Computational Modelling, Physica-Verlag
HD,139-152, 1995
[11] Miranda, E., “Emergent Sound Repertoires in
Virtual Societies”, Computer Music Journal 26,
77-90, 2002
[12] Gong, T., Zhang, Q., Wu, H., “Music evolution
in a complex system of interacting agents.”
Proceedings of IEEE Congress on Evolutionary
Computation, Edinburgh, UK, 2005
[13] Dhar, P., Mohammad I., Deb, K., Kim, J., “A
Modified
Spectral
Modeling
Synthesis
Algorithm for Whale Sound”, International
Journal of Computer Science and Network
Security, vol. 10, no. 9, Sept. 6, 2010
[14] Anwar, S., Jeanneret, C., Parrott, L., Marceau,
D., “Conceptualization and implementation of a
multi-agent model to simulate whale-watching
tours in the St. Lawrence Estuary in Quebec,
Canada”, Environmental Modelling & Software,
Volume 22 Issue 12, 2007
[15] Apple Corporation, Logic Studio (Logic Pro 9),
2009

