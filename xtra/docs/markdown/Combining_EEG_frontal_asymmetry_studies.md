# Combining_EEG_frontal_asymmetry_studies

Converted from: Combining_EEG_frontal_asymmetry_studies.pdf
Date: 2025-08-19

---

COMBINING EEG FRONTAL ASYMMETRY STUDIES
WITH AFFECTIVE ALGORITHMIC COMPOSITION AND
EXPRESSIVE PERFORMANCE MODELS
Alexis Kirke
Interdisciplinary Centre for
Computer Music Research,
University of Plymouth, UK

Eduardo Miranda
Interdisciplinary Centre for
Computer Music Research,
University of Plymouth, UK

ABSTRACT

and right hand side of the front of the brain (i.e. between
F4 and F3).

This paper draws together two strands of research in
different disciplines: EEG Frontal Asymmetry studies
and Affective-based Algorithmic Composition and
Performance. There have been numerous studies which
support the hypothesis that Frontal EEG asymmetry is an
indicator of arousal and valence of emotion. There have
also been a number of studies examining which music
features are related to which emotional perception, in the
generative composition of, and performance of, music.
This paper presents a novel system – called the
Combined EEG System - which utilises both types of
studies. It takes as input raw EEG data, and attempts to
output a piano composition and performance which
expresses the estimated emotional content of the EEG
data. Such a system may be the first step in the
development of tools allowing unskilled composers or
subjects with problems in emotional expression, to better
express themselves through music.
1.

INTRODUCTION

Alexithymia is a personality trait which includes
(amongst other things) a deficiency in verbally
expressing emotions [1]. There are also medical
conditions such as autism for which sufferers undergo
therapies (including musical) for expression of emotions
[2]. The possibility of bypassing the requirement for,
verbal expression for such people is obviously attractive.
One way individuals with expressive difficulties could
express emotion would be through music [3]. Music has
often been described as a language of emotions [4].
However such expression usually requires significant
musical training. The system described here is a first
step towards allowing the musically untrained to express
themselves emotionally through music. EEG data is
collected from the user, and an attempt is made to
estimate their relative affective state. This approximate
state is then drives an algorithmic composition and
expressive performance system to produce piano music.
2.

EEG FRONTAL ASYMMETRY

The standard 10-20 Electrode placement for EEG
electrodes [5] is shown in Figure 1. Two of these, “F3”
and “F4”, can be used to give a measure of what is
known as EEG Frontal Asymmetry – the difference in a
certain frequency band of power between the left hand

Figure 1. Standard Electrode Placings

[6] proposed that there was a link between asymmetry of
frontal alpha activation and the valence of a subject’s
emotional state. “Valence” refers to the positivity or
negativity of an emotion – e.g. a high valence emotion is
joy or contentment, a low valence one is sadness or
anger. The idea of valence is used in the 2D emotional
representation [7]. In this model, emotions are plotted on
a graph with the first dimension being how positive or
negative the emotion is (Valence), and the second
dimension being how strong the emotion is (Arousal).
For example: Happy – Positive Arousal, Positive
Valence and Fear – Positive Arousal, Negative Valence.
[8] found that frontal brain EEG distinguishes Valence
and Arousal of music-related emotions. Schmidt and
Trainor give results for happy, sad, angry and fearful.
Their results focused on a frequency band called the
“Alpha” band. Their result indicated for example:



3.

Happy - increased left frontal alpha relative to
right frontal alpha indicates increased valence
Fearful - increased over-all frontal alpha
indicates an increased arousal
AFFECTIVE ALGORITHMIC EXPRESSIVE
PERFORMANCE AND COMPOSITION

How do humans make their performances sound so
different to the so-called “perfect” but robotic
performance a computer would give? Two of the most
common performance actions found in Western
“classical” music are changing the Tempo and the
Loudness of the piece as it is played. These should not be
confused with the tempo or loudness changes marked in
the score, like accelerando or mezzo-forte, but to

Figure 2. Standard Electrode Placings

additional tempo and loudness changes not marked in
the score. For example, a common expressive
performance strategy is for the performer to slow
down as they approach the end of the piece [9].
Another factor influencing expressive performance
actions is Performance Context. Performers may wish
to express a certain mood or emotion (e.g. sadness,
happiness) through a piece of music. Performers have
been shown to change the tempo and dynamics of a
piece when asked to express an emotion as they play it
[10].
Computer Systems for Expressive Music
Performance (CSEMPS) are systems designed to add
such expression to non-expressive computer
performances [10]. One of the most influential
CSEMPs – and the one utilised in this paper – is
Director Musices. As well as applying humanisation,
Director Musices is able to implement emotional
expression [13], drawing on work by Gabrielsson &
Juslin [10]. As a result parameters were estimated for
6 rules which mould the emotional expression of a
piece.
There has been research into affective expression
through algorithmic composition, e.g. [13] as well. It
was found that the addition of the microfeature
humanisation rules improved the accuracy of the
emotional expression (as opposed to solely using
macrofeature “recomposition” rules).
4.

COMBINING EEG ASYMMETRY WITH
AFFECTIVE ALGORITHMIC
COMPOSITION/PERFORMANCE

The recorded EEG data for F3 and F4 is processed
and used to estimate the emotional state of the EEG
data - i.e. the valence and arousal levels - using
equations (1) and (2) below. These equations are
based on simple models used in previous EEG

Asymmetry research. In EEG measurements greater
power implies lower activity:
Valence = ln(frontal alpha power(left) - ln(frontal alpha
power(right))
(1)
Arousal = - (ln(frontal alpha power(right)) + ln(frontal
alpha power(left)))
(2)

To give an example of affective state estimation,
consider the following. EEG data was recorded with a
subject listening to a sequence of excerpts of Ambient
and Hard Rock music, interspersed with silence. The
music was presented for approximately 15 seconds
each time. The result EEG analysis (which has been
edited for recording artifacts) is shown in Figure 2.
5.

ALGORITHMIC COMPOSITION AND
PERFORMANCE

The Composition/Performance process of the system
is illustrated graphically in Figure 3.The initial
function in the composition process is the generation
of the piece structure. The user defines the top level
structure, such as “aba”, “abca”, or “aabb”. This
structure is used to generate two lower levels: theme
and phrase structures in a recursive self-similar way.
The phrases that make up the structure (i.e. the actual
notes) are supplied by the user. Examples of ways of
generating phrases include: phrases supplied by a
composer, phrases generated using a cut-up algorithm
applied to a provided whole melody, and phrases
generated by a separate algorithm. Phrases should be
monophonic and contain some rhythmic as well as
pitch content.
During the next stage of the composition, an
expressive performance element is applied: (a) to
humanise the output and make it sound less computerbased, (b) to express the affective state estimated
from the EEG more effectively. However the Director

Structure
Generation

Generation
of Phrase
Notes

Combine Phrases /
Apply Expressive
Performance

Apply Tempo /
Loudness / Pitch Macro
Gestures

Apply
Accompaniment

Figure 3. Composition/Performance Process

Musices Emotion model is not continuous in valence
and arousal – i.e. there is no simple mapping from
continuous valence and arousal indices on to the
parameters of the DM emotional expression
performance model. The Combined EEG System
generates continuous estimates of valence and arousal.
So for the emotional performance system a similar
methodology to [13] is utilised and four DM emotions
are selected as representing the 4 quadrants of
valence/arousal. Specifically happiness, sadness,
anger, and tenderness are selected.
The system makes larger - “compositional” adjustments to key, pitch and tempo to generate
emotional expression similar to those found in [13].
One way this is done is to change pitches based on
emotion. Livingstone proposes that more positive and
active emotions (happiness) have higher average
pitches than more negative and passive emotions (e.g.
sadness). Based on this a series of linear equation rules
were implemented for pitch. Livingstone suggests the
use of Major keys for Happiness, and Minor keys for
Tenderness and Sadness. However, unlike Livingstone
minor keys are not used for “Anger” in the Combined
EEG System. The reason for this is that as long as the
phrases provided to the system are atonal, a keyless
state appears to be closer to communicating “Anger”
than a Minor key. This approach is not utilized in
Livingstone’s CMERS, since it recomposes pieces
rather than building new pieces. The key changes in
the Combined EEG System are applied in a noncontinuous way using the “Representative Emotion”
quadrant already described. The speed, pitch and
loudness are changed continuously based on valence
and arousal values based on [13] using linear
equations.
Also included in the process is a simple tool for
accompaniment. The accompaniment is based on
piano-heuristics developed by the authors of this
paper.
6.

AN EXAMPLE USAGE

New EEG data was recorded with a subject (the first
author) listening to the same sequence of excerpts of
Ambient and Hard Rock music, interspersed with
silence. Two compositions were generated from these
settings. The initial phrases were up to 6 seconds long
and were generated using a simple alleatoric
composition algorithm [14]. In terms of testing the
system, it is outside of the scope of this paper to reexamine the effectiveness of using EEG asymmetry
measurements to estimate affectivity. Only the simple

common results of previous research were used in the
design, rather than attempting to develop new EEG
hypotheses. The main new factors that have been
incorporated into the process are the algorithmic
composition elements (which are not identical to
[13]), a novel accompaniment algorithm, and
combined process itself. All pieces were given the
same emotional profile. Two of the pieces were
randomly chosen and played to 3 independent
listeners. The listeners were asked to mark up the time
where they perceived changes in valence and changes
in arousal. The results of the listening experiments are
displayed in Table 1, showing how accurately each
subject identified the 5 affective changes inserted into
the 2 tracks.
The first thing to note is that there was only 1 run
where a subject detected five states – this was subject
3 on track 2. All other runs except that one detected
extra states (1 extra state was detected in 3 cases, and
2 extra states in one case). This means that the
subjects tended to perceive more changes in valence
and arousal than there actually are. This is not
particularly surprising, given that the source material
used to generate the material – the phrases - was not
controlled for affective content itself. As source
phrases are pasted together to make the track, the pitch
and timings of the initial phrasing may influence the
affective perception.

Subject 1
Subject 2
Subject 3

Track 1
Valence
4/5
4/5
3/5

Arousal
3/5
3/5
4/5

Track 2
Valence
4/5
4/5
5/5

Arousal
4/5
3/5
4/5

Table 1. Results broken down into Valence and Arousal

Another element to observe is that the subjects’
perceptions of affective state sometimes matched
solely in arousal, sometimes solely in valence, and
sometimes in both. It is useful to evaluate separately
the system’s relative abilities in expressing these two
dimensions. Note that a subject is marked as having
detected one of the 5 affective states if during the time
period the system is trying to express that state, the
subject actually detects that particular valence or
arousal state. They may detect other states as well in
that time, but they will still be marked as having
detected the correct state. As long as there are not a
large number of incorrectly additional states identified
in that time period, this will be considered a sufficient
demonstration of concept. That is because both EEG
and music are very approximate input and output

communication modes, rather than precise symbolic
specifications [15][16]. Hence the best that could be
hoped for was approximate accuracy in time in the
music expression.
Based on Table 1 there is an average 80%
communication rate for Valence and a 70%
communication rate for Arousal, though timings vary
from the programmed change times. This observation
needs to be considered in light of the fact that during
the 6 tests (a total of 30 states) there were 5 extra
states detected which were not intended by the system;
and also 1 state was entirely missed. It also needs to be
observed that the breaking down into Valence and
Arousal dimensions is not an infallible method – they
are a simplified model of emotion. Hence any results
based on that breaking down are subject to the same
limitations. Also these tests do not validate the EEGto-emotion methodology, but purely support the
feasibility of the use of the composition/performance
part to communicate that emotion.
The aim of the Combined EEG System is to indicate
changes in valence and arousal in a user through EEG
and music. So it would to aim to increase the valence
communicated in the music, if the valence increased in
the user’s EEG pattern. It is not an attempt to literally
detect if the user is happy, sad, etc.
7.

CONCLUSIONS

This paper has drawn together two strands of research
in different disciplines: EEG Frontal Asymmetry
studies and Affective-based Algorithmic Composition
and Generative Performance. In this paper a novel
system which utilises both sets of studies has been
presented – it takes as input raw EEG data, and
attempts to output a piano composition and
performance which expresses changes in estimated
emotional content of the EEG data. Initial testing
results were given that suggest that the system is
worth developing and performing extended testing on.
There are a number of possible areas for future work
for the system: the algorithmic composition toolbox
could be improved; the accompaniment algorithm is
very simple, and is not affectively manipulated; and
finally, and most importantly, more work needs to be
done on verifying and improving the EEG-to-emotion
detection model.
8.

REFERENCES

[1] Ahrens, F., Deffner, G., “Empirical study of
alexithymia:
methodology
and
results”,
American Journal of Psychotherapy 40, pp430447, 1986.
[2] Hewitt, L. “Music is Medicine”, Wavelength,
pp39-43, 2007.
[3] Aldridge, D., Music Therapy and Neurological
Rehabilitation, Jessica Kingsley,London, 2005.

[4] Cooke, D., The Language of Music. Oxford
University Press, Oxford, 1959.
[5] Jasper, H., “The ten twenty electrode system of
the
International
Federation”,
Electroencephalography
and
Clinical
Neurophysiology 10, pp371-375, 1958.
[6] Davidson, R. J., “The neuropsychology of
emotion and affective style” In Lewis, M.,
Haviland, J. M. (Eds.), Handbook of emotion
pp143-154, Guilford Press, New York, 1993.
[7] Lang, P., “The emotion probe: Studies of
motivation and attention”, The American
Psychologist 50, pp372-385, 1995.
[8] Schmidt, L. A., Trainor, L. J., “Frontal brain
electrical activity (EEG) distinguishes valence
and intensity of musical emotions”, Cognition
and Emotion 15, pp487-500, 2001.
[9] Friberg, A., Sundberg, J., “Does music
performance allude to locomotion? A model of
final ritardandi derived from measurements of
stopping runners”, Journal of Acoustical Society
of America 105, pp1469-1484, 1999.
[10] Gabrielsson, A., Juslin, P., “Emotional
expression in music performance: between the
performer's intention and the listener's
experience”, Psychology of Music 24, pp68-91,
1996.
[11] Kirke, A., Miranda, E.R., A Survey of Computer
Systems for Expressive Music Performance.
ACM Computer Surveys 42(1), 2010.
[12] Friberg, A., Bresin, R., Sundberg, J., “Overview
of the KTH rule system for musical
performance”,
Advances
in
Cognitive
Psychology 2, pp145-161, 2006.
[13] Livingstone, S. R., Muhlberger, R., Brown, A.
R., Loch, A., “Controlling Musical Emotionality:
An Affective Computational Architecture for
Influencing
Musical
Emotions”,
Digital
Creativity 18, 2007.
[14] Roads, C., The Computer Music Tutorial, MIT
Press, Cambridge, Massachusetts, 1996.
[15] Palaniappan, R., Anandan, S., Raveendran, P.,
“Two Level PCA to reduce Noise and EEG from
Evoked Potential Signals”, Proceedings of the
International
Conference
on
Control,
Automation, Robotics and Vision, IEEE, 2002.
[16] Juslin, P., “From Mimesis to Catharsis:
expression, perception and induction of emotion
in music”, In Miell, D., MacDonald, R.,
Hargreaves, D.J. (Eds.), Music Communication
pp85-116, Oxford University Press, New York,
2005.

