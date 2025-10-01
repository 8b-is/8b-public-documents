# Emotional_and_Multi_agent_Systems_in_Com

Converted from: Emotional_and_Multi_agent_Systems_in_Com.pdf
Date: 2025-08-19

---

Emotional and Multi-agent Systems in Computer-aided
Writing and Poetry
Alexis Kirke1, Eduardo Miranda1
Abstract. MASTER (Multi-Agent System for Text Emotion
Representation) is an artificial society in which each member has
a digital emotional state. Member agents attempt to influence
each other’s emotions by reciting “poems” to each other which
express their own emotional state. As agents do this, larger texts
are developed in the society through social learning. The
resulting texts are not meaningful in the normal prosaic sense the sound and word repetition generates meaning. Like normal
English, there is actually a hierarchical structure to the repetition
(i.e. repetitions within repetitions), and the words are often
evocative and sometimes contrasting.

1 INTRODUCTION
Some computer poetry research focuses on demonstrating the
ability of a technique at simulating poetry, whilst others focus on
assisting in the creative acts. This can be viewed as similar to the
distinction in computer music between algorithmic composition
and computer-aided composition [1]. Computer-aided
composition is used as a form of digital collaborator between
human and computer which can move the human composer into
new areas of creativity, perhaps breaking them out of old habits.
In this paper a computer-aided poetry system is introduced,
MASTER (Multi-Agent System for Text Emotion
Representation) [2]. MASTER is designed to investigate if a
Multi-agent System which has no explicit knowledge of how
language is constructed, can still help to generate emergent
poetry. There has been work on MAS analysing poetry [3] and
on MAS being used for story generation and character evolution
in prose [4, 5]. As far as we are aware MASTER is the first
generative poetry system utilizing multi-agent systems and
artificial emotion.
Figure 1: A Heuristic Representation of MASTER

which observes and acts upon an environment (i.e. it is an agent)
and directs its activity towards achieving goals. Examples of
problems which are appropriate to multi-agent systems research
include online trading, disaster response, and modelling social
structures. A key property of MAS is their ability to generate
unexpected or novel responses to problems, sometimes called
“emergence” [7]. They have been used successfully in computeraided composition, because of their emergent properties.

2 COMPUTER POETRY
Common techniques in algorithmic and computer-aided
poetry include words being chosen from a hand-crafted
dictionary and inserted into a framework [8] (e.g. haiku or
sonnet form). It is also possible to make a statistical language
model based on existing poems or other texts – this incorporates
information about which words / phrases follow which, and their
frequency of occurrence [9]. A further approach is to create a set
of rules for generating (or re-generating text) based on a manual
or automatic analysis of other poetic text [10].
An example output of [9] (Kurzweil’s “Cybernetic Poet”) is
shown below. It is called “Wondered” and is written after the
system was trained on the poems of Dave Gitomer:
today i wondered
if i mused
today i saw you
i learned
in awe and you
if i wondered
if i mused
today i had one wish
if i saw you
if i saw you
if i had one wish

Another poet, human this time, who has written in this rhythmic
style is the German surrealist Kurtz Schwitters:
What a b what a b what a beauty
What a b what a b what a a
What a beauty beauty be
What a beauty beauty be
What a beauty beauty beauty be be be
What a be what a b what a beauty
What a b what a b what a a
What a be be be be be
What a be be be be be
What a be be be be be be be a beauty be be be
What a beauty.

Multi-agent systems (MAS) [6] are composed of multiple
interacting intelligent agents. An agent is an autonomous entity

Here is an excerpt from another of Schwitters’ texts:

My corpse is too large, in the night - crumbles, crumbles,
crumbles - too large is my corpse. Waters whip unsoftened
valley - crumbles, crumbles, crumbles - too large is my
corpse, giants arch dome into crumbs - crumbles, crumbles,
crumbles, my corpse is too large, Cagliostro’s shroud crumbles crumbles crumbles - my corpse is too large, for the
orphanage alms-for-the-poor - crumbles crumbles crumbles too large is my corpse…

emotion is (Arousal). For example “Happy” is high valence high
arousal affective state, and “Stressed” is low valence high
arousal state.
Figure 2: The Valence/Arousal Model of Emotion

This form of poetic text is not meaningful in the normal prosaic
sense, but the sound and word repetition generate meaning. Like
normal English, there is actually a hierarchical structure to the
repetition (i.e. repetitions within repetitions), and the words are
often evocative and sometimes contrasting. The structure of
MASTER leads to poetic text of this type, as will now be seen.
This approach to generative poetry is consistent with issues
founds in AI poetry research, where there can be a trade-off
between semantic clarity and rhythmic interested [11]

3 ‘quiet’: A POEM BY MASTER
quiet book comet and fornicate quiet
tourist ignite live quiet quiet book comet and wine ejaculate
and boring welfare fire with fornicate
quiet book comet and rape boring fatigued sadness it quiet
tourist ignite live quiet quiet book comet and wine ejaculate and hysterical rage
collaborations fornicate quiet tourist
ignite live quiet
quiet book comet and wine ejaculate and boring
welfare fire with hysterical explosion sensations
explosion explosion provoked explosion
explosion prizes quiet quiet
quiet book comet and wine ejaculate and quiet quiet book comet and fornicate
quiet tourist ignite live quiet
quiet book comet and wine ejaculate and boring welfare
fire with fornicate quiet book comet
and rape boring fatigued sadness
it quiet tourist
ignite live quiet
quiet book comet and wine ejaculate
and hysterical rage collaborations fornicate
quiet tourist ignite live quiet quiet book comet and wine ejaculate and boring
welfare fire with hysterical explosion sensations explosion explosion provoked
explosion explosion prizes want explosion and huge explosion and

This poem was written as a “collaboration” between the first
author of this paper and MASTER. The author provided the title
and line breaks. MASTER produced the text. This particular
implementation of MASTER involved 8 agents who had a slight
“depressive” tendency, and 3 of whom were initially happy, 3
initially “relaxed” and 1 angry and 1 sad. The poem comes from
agent 8, after 16 interaction cycles. These terms, and the
MASTER system, will now be explained in more detail.

4 MASTER
Before introducing the emotional intelligence of MASTER,
affective representation will be briefly discussed. The
dimensional approach to specifying emotion utilizes an ndimensional space made up of emotion “factors”. Any emotion
can be plotted as some combination of these factors. For
example, in many emotional music systems [12] two dimensions
are used: Valence and Arousal. In that model, emotions are
plotted on a graph (see Figure 2) with the first dimension being
how positive or negative the emotion is (Valence), and the
second dimension being how intense the physical arousal of the

Part of the core “emotional intelligence” in the agents in
MASTER comes from a 1000 word database called ANEW [13]
which each agent has internalized. This contains a list of words
which have had their valence and arousal measured by human
experiments. For example “ace” has an average valence of 6.88
and “accuse” has an average valence of 2.54 – i.e. rated
significantly less emotionally positive. Similarly “alert” has an
average arousal of 6.85 whereas “affection” has a much lower
average arousal of 0.86.
Poems are written in MASTER by allowing the agents
interact in a specific way. This interaction cycle is shown in
Figure 3. In the next two sections, the modules in the diagram
will be examined.

Figure 3. MASTER interaction cycle

5 AGENT A RECITES ITS TEXT
An agent starts with an initial emotional state. This can be
neutral (e.g. valence and arousal set to 0), or some bias (e.g.
“depressed” with valence = -1, “excited” with arousal = 1, etc).
An agent will also have an Initial Text. This can be a single word
chosen by the user, or selected from a database. Agents then take
it in turn to recite their text. They will recite to every other agent.
This is called a single Cycle. Then it is a second agent’s turn to
recite for a Cycle, and so forth. So if there are 4 agents it takes 4
interaction cycles for them all to have recited their text to each
other.
An agent’s recitation is adjusted by its emotional state. Firstly
the reciting agent estimates the valence and arousal of its own
stored internal text/poem. To measure valence the agent locates
the valence values for all words in its poem which are included
in its Emotional Text Database. It calculates the average of
these. Not all words in the agent’s text will be in the Emotion
Database, so it ignores these in the averaging. For example,
suppose an agent has the text “Happy smelly death”. “Smelly” is
not in the ANEW database so will be ignore. But “happy” has
valence 0.82 and “death” has valence -0.64. The valence of the
phrase is thus calculated as 0.09 (the mean of happy and death).
Arousal is calculated slightly differently. As well as
calculating the average arousal from the database, average word
length is used. This is based on the idea of parallels between
music and speech [14]. For example music that has a higher
tempo has a higher arousal [15]. Similarly texts with many
syllable words will tend to read more rapidly and thus with
higher arousal, whereas texts with shorter words will tend to
have more intra-word gaps and be read more slowly, and thus
with slower arousal. So the longer the average word length, the
lower the calculated arousal. The formula is shown in Equation
1. The precise weightings in the formula are designed to
combine with the types of values found in the ANEW database,
and also to lead to total arousal values of the order -1 to 1 where
possible (as commonly used in many valence / arousal models).
arousalEstText = 2*average(wordLength)/3 - 1

(1)

For example: “Happy Smelly Death” will have a higher arousal
(0.87) than “Happy as Death” (0.57), because its average word
length is greater.
When estimating the arousal of its internal text, an agent also
uses its ANEW database. Then it combines the value in the
ANEW database (if the word is in the database) with the value
calculated in equation (1), as shown in equation (2), weighting
the database arousal contribution twice as much as the word
length calculation.
arousalEst = (2/3)*arousalDatabase + (1/3)*arousalEstText
(2)
Part of the logic behind this weighting is that the ANEW
database is a highly tested approach to word emotion, whereas
equation (1) is very much heuristic and has not been tested on
human subjects.
At the end of the process agent A will then have an estimate
of the affective content of its internal stored text. Once an agent
has estimated the emotional content of its stored text, it
compares this to its own emotional state (its own valence and
arousal). If its valence is different to its internal text, the agent

adds an emotional word to the end of its text when reciting it to
another agent. This is to raise or lower the valence of the text to
bring it in line with how it’s feeling. It does this by searching
through the database for a word whose valence will pull the
phrase’s estimated valence up or down towards the agent’s own
current valence, whilst keeping arousal roughly the same.
Similarly if the agent’s current arousal is different to its
estimation of the arousal of its internal text, then while reciting
the agent adds to its text. Firstly, as with valence, it searches the
emotion database for a word which will help to adjust its text
arousal (but not its valence), and it adds the word to the end of
its text. Secondly, it attempts to change the average word length
of its phrase while reciting it. This is done using another
database the agent has. This is a database of “neutral” words –
the Neutral Database.
The neutral database is generated by compiling text from
source material from online (e.g. poems, articles etc.) This text is
then searched and words are in the emotion database are
removed. The remaining list of words is used as the neutral
database. This process allows for the user to adjust the neutral
database to change the nature of the final generated poems. For
example, a neutral database of one of the keynote poets at the
Poetry and Source Conference 2012, Plymouth, UK was used in
the creation of “quiet”.
So the agent searches for a neutral word of an appropriate
length to change its text arousal in the right way. For example if
it wants to increase the text arousal, it searches for a longer
neutral word. If it wants to decrease text arousal it searches for a
shorter neutral word.
5.1 An Example Recital
Suppose agent A has the text “Happy smelly death” and
currently has a low valence of -0.5 and high arousal of 0.5 (e.g.
“angry”). The ANEW database will estimates the valence of this
text as 0.09. So because the agent is “feeling” pretty negative, it
wants to adjust the valence of the text to be more negative. It
could adjust the sentence valence downwards (from 0.09 towards
-0.5) by adding the word “bad” (valence -0.43 from the ANEW
database) to its recited text. (Note – these changes are only
applied to what the agent recites, not to the text that is stored.)
Now it estimates the arousal of its phrase as 1.06, using the
ANEW database and equation (2). It could adjust recital arousal
downwards (from 1.06 towards 0.5) by adding the word “calm”
(arousal 0.42 in the database) to its recited text. To try and
reduce arousal further agent A adds neutral words It adds “of”
which has an estimated arousal of 0.33 using equation (1).
So the final final text becomes: “Happy smelly death bad
calm of”. The first three words are Agent A’s internal text. The
next is to reduce valence, and the last two are to reduce arousal.
Using ANEW and equation (2), the calculated valence and
arousal of this recital are: valence of 0.06 and arousal of 0.67. So
according to that, the agent has decreased valence too little, and
increased arousal too little as a result of trying to match its own
valence and arousal values (-0.5 and 0.5).

6 AGENT B ESTIMATES AFFECT AND ADDS
When Agent B hears agent A’s recitation it estimates the
affective content in the same way that that Agent A estimated it
in Section 5 above. In other words it estimates the valence from
the database, and the arousal using the database and equation (2).

Then Agent B will compare that value to its own arousal and
valence. If they are close enough in value then Agent B adds
Agent A’s text to the end of its own internal text – thus updating
its internal text. So for example if Agent A recites something
“happy” and Agent B feels “happy”, then Agent B would add the
text to its own. But it Agent B was feeling “sad” it would not. It
is through this addition process amongst multiple agents that
poems are built up.
Whether or not Agent B adds Agent A’s recital to its own text
Agent B is effected “emotionally” by hearing the recital. B’s
own valence and arousal are moved towards the estimated
valence and arousal of the recited text from A, using equations
(3) and (4). This can be compared to a happy person hearing a
sad poem from another person, and it depressing them slightly.

Cycle 15:
Agent 1 (more happy again): “hostage conquer relaxed bird
marry a erotic explosion anticonsumerist relaxed bloom
extreme one conquer relaxed bird marry a relaxed soothe
extreme at hostage conquer relaxed bird marry a erotic
explosion anticonsumerist relaxed
bloom extreme one
extreme shock this infatuation explosion slide”
Agent 2(more angry again): “conquer relaxed bird marry a
relaxed soothe extreme at hostage conquer relaxed bird
marry a erotic explosion anticonsumerist relaxed bloom
extreme one extreme shock this”
Agent 3(more happy again): “relaxed conquer relaxed bird
marry a relaxed soothe extreme at hostage conquer relaxed
bird marry a erotic explosion anticonsumerist relaxed bloom
extreme one extreme shock this infatuation explosion slide”

(3)
(4)
Thus the interaction of the Agents could be summarized as
follows. Agents recite texts to each other, adjusting the recital
(adding words to it) based on their emotional state. The agents
influence each other’s emotional state by the text they recite.
When an agent hears a text which has an emotion content close
to the way it is “feeling”, it adds that text to the end of its own.
Thus MASTER is a society of emotional agents who generate in
parallel a collection of ever growing poems based on trying to
influence each other’s emotional states (and communicate their
own.)

The system can be examined more deeply by looking in detail at
the emotional internals of a single agent, Agent 1. These changes
are shown in Figure 4. Agent 1 starts “Angry”, then gradually
arousal and valence increases because of influence of the recitals
from the happy and relaxed agents. So the agent gets “happier”.
The agent’s internal text estimate approximately tracks this
change in emotion, perhaps because of the affective threshold.
Agent 2 and 3’s emotion evolution is shown in Figure 5.
Figure 4: Emotional evolution of Agent 1: Internal state (Top
graph); Internal Text Affective Estimate (Bottom Graph)
Agent 1
1

7 ANALYZED EXAMPLE
Consider a MASTER example made up of 3 Agents, with initial
valence / arousal states of -0.5/0.5, 0.5/0.5 and 0.5/-0.5.
Anthropomorphically these could be thought of as angry, happy
and relaxed. The Affective Similarity Threshold is how close an
agents affective state must be to the recited text it hears before
adding it to its own. This is calculated as the Euclidean distance
in the valence / arousal space, and is set to 0.55 for this example.
Agents are initialized each with a single word - the word in
ANEW whose emotional state is closest to their own emotional
state. For example for Agent 2 it is a Happy word (since its
initial valence is 0.5, arousal 0.5). So its initial word is
“Conquer”. A value of 0.1 for the gamma sensitivities in (3) and
(4) used. The 3 agents are then left to interact for 20 cycles, with
the results shown below:
Cycle 1:
Agent 1’s (“angry” agent) initial Text: “hostage”
Agent 2’s (“happy” agent) initial Text: “conquer”
Agent 3’s (“relaxed” agent) initial Text: “relaxed”
Cycle 10:
Agent 1 (slightly more happy): “hostage conquer relaxed
bird marry a erotic explosion anticonsumerist relaxed bloom
extreme one”
Agent 2 (slightly more angry): “conquer relaxed bird marry
a relaxed soothe extreme at”
Agent 3 (slightly more happy): “relaxed”

V
A
0.5

0

-0.5

0

5

10

15

20

25

Agent 1 Est
2
V
A

1

0

-1

0

5

10

15

20

25

Simply changing the initial words will change the evolution.
For example – requiring that the arousal and valence of the first
three initialising words be more emotionally positive and or
higher arousal (in this case increased them by 0.4) makes the
words selecting from ANEW come up as: “shock”, “orgasm”
and “snuggle”. Then Agent 1’s text at 15 cycles becomes:
“shock orgasm shock chaos rage it anxious extreme and
orgasm shock chaos rage it snuggle pillow power a shock
orgasm shock chaos rage it anxious extreme and hysterical
rage the hysterical extreme this snuggle free explosion on
orgasm shock chaos rage it snuggle pillow power a shock
orgasm shock chaos rage it anxious extreme and hysterical
rage the snuggle home extreme at shock orgasm shock chaos
rage it anxious extreme and orgasm shock chaos rage it
snuggle pillow power a shock orgasm shock chaos rage it

anxious extreme and hysterical rage the hysterical extreme this
snuggle free explosion on explosion shark this explosion
extreme this”
Figure 5: Emotional evolution of Agents 2 and 3
Agent 2 Est

Agent 2
0.8

1.4
V
A

0.7
0.6

1

0.5

0.8

0.4

0.6
0

10

20

V
A

1.2

0.4

30

0

10

Agent 3

20

30

Agent 3 Est

1

1.5
V
A

0.5

V
A

1
0.5

0

-0.5

0

0

10

20

-0.5

30

0

10

20

8 QUIET

30

The poem “quiet” used as the introductory example in Section 3
came from an 8 agent system. The makeup of the initial
population was 3 happy and 3 relaxed agents, 1 angry and 1 sad
agent. The initial word selected was much lower in valence than
arousal than the agent was “feeling” – it was required to be 0.4
below each agent’s arousal and valence. The Affective Similarity
Threshold was set to 0.43. The poem is the internal text of Agent
8 after 16 cycles. Agent 8’s emotional evolution as it wrote the
text for quiet can be seen in Figure 6.

9 CONCLUSIONS AND FUTURE WORK
MASTER is the first multi-agent system approach for
computer-aided creation of poetry and, as far as we are aware,
the first generative poetry system utilizing artificial emotion.
This combination of social interactions and emotional dynamics
allows the system to avoid all random processes, which are often
required by creative systems [16]. The creativity emerges as a
result of the complex interactional dynamics. The resulting texts
are not meaningful in the normal prosaic sense -the sound and
word repetition generates meaning. Like normal English, there is
actually a hierarchical structure to the repetition (i.e. repetitions
within repetitions), and the words are often evocative and
sometimes contrasting.
There are a number of key areas which would benefit from
further work. One is the emotional estimation system. In
particular the arousal detection system utilizes ideas which need
to be more fully tested. Furthermore the emotional estimation
system is only on a word level. Emotion is generated by text
through the cumulative effect of many words, phrases, stanzas
and so forth. MASTER has no embedded sense of this process.
For example a phrase made up of 3 happy words and 3 sad
words is not necessarily emotionally neutral. In fact in many
cases there may be little correlation between the emotive effect
of a stanza and the emotive effect of its individual words.
Even though MASTER is not designed to write sentences, it
would benefit from a clearer “understanding” of language
structure. Emotional impact may be increased if the orderings of
words in a MASTER text are a little more reminiscent of normal
writing. Or at the very least it would be useful tool to have a
parameter that allowed this to be implemented. Such a method
could involve simple statistical models of word orderings, and an
agent only adding text to the end of its own text if there is a
sufficient statistic likelihood of such word orders.
Despite these limitations it is hoped that MASTER indicates
the potential for the use of affective computing in generative
poetry, and additionally indicates the potential of multi-agent
systems in this field.

Figure 6: Emotional evolution of Agent 8 as it wrote “quiet”

REFERENCES
Agent 8

1.

0.5
V
A

2.

0

-0.5

0

2

4

6

8

10

12

14

16

18

3.

Agent 8 Est
1.5
V
A

1
0.5

4.

0
-0.5

0

2

4

6

8

10

12

14

16

18

5.

6.

Miranda, E.R. Special Issue: Aesthetic Decisions in
Computer-Aided Composition, Contemporary Music Review.
Vol. 28, No. 2 (2009)
Kirke, A. and Miranda, E. R. MASTER: Towards the use of
emotional multi-agent systems in algorithmic writing and
poetry. Presentation, Contemporary Poetry and Source 2012,
Plymouth University, Plymouth UK (2012).
Dahl, V., Jiménez-López, M.D. and Perriquet, O. Poetic
RNA: Adapting RNA Design Methods to the Analysis of
Poetry, Trends in Practical Applications of Agents and
Multiagent Systems, Advances in Intelligent and Soft
Computing, Vol. 71, pp. 403-410 (2010)
Riedl, M.O. and Young, R.M. An Intent-Driven Planner for
Multi-Agent Story Generation. Proceedings of 2004
Conference on Autonomous Agents and Multi-agent Systems,
July 19-23, New York, New York, USA, ACM (2004)
Nairat, M., Dahlstedt, P. and Nordahl, M.G. Character
evolution approach to generative storytelling, Proceedings of
2011 IEEE Congress on Evolutionary Computation, pp.12581263 (2011)
Wooldridge, M.. An Introduction to Multi-Agent Systems.
John Wiley and Sons (2004)

7.

8.

9.
10.

11.

12.

13.

14.
15.

16.

Bentley, P.J. Everything Computes, Proceedings of the Third
International Conference on Generative Art, Melbourne,
Australia (2005)
Gervas, P. An expert system for the composition of formal
spanish poetry. Journal of Knowledge-Based Systems 14(3–
4):181–188 (2001)
Kurzweil, R., Ray Kurzweil’s Cybernetic Poet, Kurzweil
CyberArt Technologies (2000)
Toivanen, J.M., Toivonen, H., Valitutti, A. and Gross, O.
Corpus-Based Generation of Content and Form in Poetry,
Proceedings of 2012 International Conference on
Computational Creativity, Dublin, Ireland (2012)
Manurunga, R., Ritchie, G. and Thompson, H., Using genetic
algorithms to create meaningful poetic text, Journal of
Experimental and Theoretical Artificial Intelligence, Vol.24,
No. 1 (2012)
Kirke, A. Application of Intermediate Multi-Agent Systems
to Integrated Algorithmic Composition and Expressive
Performance of Music, PhD Thesis, Plymouth University,
Plymouth, UK (2011)
Bradley, M., Lang, P. Affective norms for English words
(ANEW): Stimuli, instruction manual and affective ratings.
Technical report C-2, Gainesville, F. The Center for Research
in Psychophysiology, University of Florida, USA (2010)
Jackendoff, R. Parallels and Non-Parallels between Language
and Music. Music Perception, Vol. 26, pp.195-204 (2009)
Kirke, A. and Miranda, E. R. Combining EEG Frontal
Asymmetry Studies with Affective Algorithmic Composition
and Expressive Performance Models. Proceedings of 2011
International Computer Music Conference, Huddersfield, UK
(2011)
Montfort, N. and Fedorova, N. Small-Scale Systems and
Computational Creativity. Proceedings of 2012 International
Conference on Computational Creativity, Dublin, Ireland
(2012)

