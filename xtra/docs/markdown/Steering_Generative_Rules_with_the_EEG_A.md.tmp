STEERING GENERATIVE RULES WITH THE EEG:
AN APPROACH TO BRAIN-COMPUTER MUSIC INTERFACING
Eduardo Reck Miranda and Bram Boskamp
Computer Music Research
School of Computing, Communications and Electronics
University of Plymouth
United Kingdom
http://cmr.soc.plymouth.ac.uk
ABSTRACT
This paper introduces a system that uses brainwaves, or
EEG (electroencephalogram), information to steer
generative rules in order to compose and perform music
on the fly. The paper starts by noting the various
attempts at the design of systems to produce music from
EEG, followed by a short technical introduction to EEG
sensing and analysis. Next, it introduces the generative
component of the system, which employs Artificial
Intelligence techniques (e.g., ATN grammars) for
computer-replication of musical styles. Then, it presents
a demonstration system that constantly monitors the
EEG of the subject and activates generative rules that
are associated with the most prominent frequency band
in the spectrum of the EEG signal. The system also
measures the complexity of the EEG signal in order to
modulate the tempo (beat) and dynamics (loudness) of
the performance. The paper concludes with a brief
discussion on the achievements and limitations of our
research so far, and comments on its contribution for the
development of assistive technology for severe physical
and neurological disability, which is one of the main
goals of this work.
1.

INTRODUCTION

Human brainwaves were first measured in 1924 by Hans
Berger [5]. Today, the EEG has become one of the most
useful tools in the diagnosis of epilepsy and other
neurological disorders. Further, the fact that a machine
can read signals from the brain has sparked the
imaginations of scientists, artists and other enthusiasts,
and the EEG has made its way into a myriad of other
applications.
In the early 1970s, Jacques Vidal did the first
tentative work towards a system to communicate with a
computer with the EEG. The results of this work were
published in 1973 in a paper entitled Toward Direct
Brain-Computer Communication [30]. This field of
research is known as Brain-Computer Interface (BCI)
and there is a growing number of researchers worldwide
working in this field. Many attempts followed with
various degrees of success. To cite but one example, in
1990, Jonathan Wolpaw and colleagues developed a
system to allow primitive control of a computer cursor
by subjects with severe motor deficits. Subjects were
trained to use their EEG to move the cursor in simple
ways [31]. For recent reports on BCI research please

refer to the special issue of IEEE Transactions on
Biomedical Engineering published in June 2004 (Vol.
51).
We are devoted to the development of BCI systems
for musical applications and we pay special attention to
the development of generative music techniques tailored
for such systems. We might call such systems BrainComputer Musical Interfaces (BCMI) and we are
primarily interested in BCMI as assistive technology to
enable people with severe physical and neurological
disabilities to have the opportunity to make music.
The idea of using EEG to produce music is by no
means new. Essentially, what is new in our work is the
use of EEG information to steer generative rules.
As early as 1934, a paper in the journal Brain had
reported a method to listen to the EEG [1]. It is now
generally accepted that it was composer Alvin Lucier,
who composed the first musical piece using EEG in
1965: Music for Solo Performer [16]. Pioneers such as
Richard Teitelbaum [28], David Rosenboom [26, 27]
and a few others followed with a number of interesting
systems and pieces. Back in 1975 David Rosenboom
edited a remarkable book on the topic [25] and more
recently Andrew Brouse published a review on using
brainwaves to produce music [8].
Our research builds on the work developed by these
pioneers in a number of ways. Firstly, we are employing
and developing more sophisticated analysis techniques
to harness the EEG signal. Furthermore, we are
developing new psychophysical experiments in order to
gain a better understanding of the EEG components
associated with musical cognition and methods to train
subjects to generate such EEG components. Finally, we
are developing generative techniques especially
designed for musical composition and performance with
a BCMI. The psychophysical experiments are beyond
the scope of this paper. More details about this aspect of
the research can be found in [18, 19].
2.

TECHNICAL BACKGROUND

The EEG is measured as the voltage difference between
two or more electrodes on the surface of the scalp
(Figure 1), one of which is taken as a reference.
The EEG expresses the overall activity of millions of
neurons in the brain in terms of charge movement, but
the electrodes can detect this only in the most superficial
regions of the cerebral cortex.

There are basically two conventions for positioning
the electrodes on the scalp: the 10-20 Electrode
Placement System (as recommended by the International
Federation of Societies for EEG and Clinical
Neurophysiology), and the Geodesic Sensor Net
(developed by a firm called Electric Geodesics, Inc.).
The former is more popular and is the convention
adopted for the systems described in this paper: it uses
electrodes placed at positions that are measured at 10%
and 20% of the head circumference (Figure 2). In this
case, the terminology for referring to the position of the
electrodes uses a key letter that indicates a region on the
scalp and a number: F = frontal, Fp = frontopolar, C =
central, T = temporal, P = parietal, O = occipital and A
= auricular (the ear lobe; not shown in Figure 2). Odd
numbers are for electrodes on the left side of the head
and even numbers are for those on the right side.
The set of electrodes being recorded at one time is
called a montage. Montages fall into one of two
categories: referential or bipolar. Referential means that
the reference for each electrode is in common with other
electrodes; for example, each electrode may be
referenced to an electrode placed on the earlobe. An
average reference means that each electrode is
compared to the average potential of every electrode.
Bipolar means that each channel is composed of two
neighbouring electrodes; for example, channel 1 could
be composed of Fp1-F3, where Fp1 is the active
electrode and F3 is the reference, then channel 2 could
be composed of Fp2-F4, where Fp2 is the active
electrode and C4 is the reference; and so forth.

Figure 1. Brainwaves can be detected with electrodes
placed on the scalp.
The EEG is a difficult signal to handle because it is
filtered by the meninges (the membranes that separate
the cortex from the skull), the skull and the scalp before
it reaches the electrodes. Furthermore, the signals
arriving at the electrodes are sums of signals arising
from many possible sources, including artifacts like the
heartbeat and eye blinks. Although experts can diagnose
brain malfunctioning from raw EEG plots, this signal
needs to be further scrutinized with signal processing

and analysis techniques in order to be of any use for a
BCI system.

Figure 2. The 10-20 electrode placement system.
2.1. EEG Analysis
There are a number of approaches to EEG analysis,
such as power spectrum, spectral centroid, Hjorth,
event-related potential (ERP), principal component
analysis (PCI), correlation, to cite but a few. Brief
non-mathematical introductions to EEG power
spectrum and Hjorth analyses are given below due to
their relevance to our system. A discussion on other
analysis techniques and how they have been used in
neuroscience of music research can be found in
references such as [6, 13, 14, 21, 29].
Power spectrum analysis is derived from
techniques of Fourier analysis, such as the Discrete
Fourier Transform (DFT). In short, DFT analysis
breaks the EEG signal into different frequency bands
and reveals the distribution of power between them.
This is useful because the distribution of power in the
spectrum of the EEG can reflect certain states of mind.
For example, a spectrum with salient low-frequency
components can be associated with a state of
drowsiness, whereas a spectrum with salient highfrequency components could be associated with a state
of alertness. There are five recognised frequency
bands of EEG activity, also referred to as EEG
rhythms, each of which is associated with specific
mental states: delta, theta, alpha, low beta and high
beta rhythms. They certainly indicate different mental
states, but there is, however, some controversy as to
the exact boundaries of these bands and the mental
states with which they are associated.
Hjorth introduced an interesting method for
clinical EEG analysis [12], which measures three
attributes of the signal: its activity, mobility and
complexity. Essentially, it is a time-based amplitude
analysis. This method is interesting because it
represents each time step (or window) using only these
three attributes and this is done without conventional
frequency domain description. The signal is measured

for successive epochs (or windows) of one to several
seconds. Two of the attributes are obtained from the
first and second time derivatives of the amplitude
fluctuations in the signal. The first derivative is the
rate of change of the signal’s amplitude. At peaks and
troughs the first derivative is zero. At other points it
will be positive or negative depending on whether the
amplitude is increasing or decreasing with time. The
steeper the slope of the wave, the greater will be the
amplitude of the first derivative. The second derivative
is determined by taking the first derivative of the first
derivative of the signal. Peaks and troughs in the first
derivative, which correspond to points of greatest
slope in the original signal, result in zero amplitude in
the second derivative, and so forth.
Activity is the variance of the amplitude
fluctuations in the epoch. Mobility is calculated by
taking the square root of the variance of the first
derivative divided by the variance of the primary
signal. Complexity is the ratio of the mobility of the
first derivative of the signal to the mobility of the
signal itself. A sinewave has a complexity equal to 1.
Figure 3 shows an example of Hjorth analysis. A raw
EEG signal is plotted at the top (C:1) and its
respective Hjorth analysis is plotted below: activity
(C:2), mobility (C:3) and complexity (C:4).

Figure 3. An example of Hjorth analysis.
There is no clear agreement as to what these
measurements mean in terms of mental states. It is
common sense to assume that the longer a subject
remains focused on a specific mental task, the more
stable is the signal, and therefore the lower is the
variance of the amplitude fluctuation. However, this
point questions the possible affects of fatigue,
habituation and boredom, which we have not yet
accounted for in our research.
2.2. Generative Rules
The system uses a rule system that generates music,
based on given examples. The EEG-signals can
influence in a well-defined way the mixture of
different style-elements found in the different musical
examples given to train the system. It can generate
music that contains, for example, more Schumann-like
elements when the spectrum of the subject’s EEG

contains salient low-frequency components and more
modern or jazzy elements when the spectrum of the
EEG contains salient high-frequency components.
(These associations are arbitrary.)
Example-based musical-generation systems are often
based on formalisms such as transition networks or
Markov Chains to re-create the transition-logic of whatfollows-what, either at the level of notes [15] or at the
level of similar “vertical slices” of music [9, 10]. For
example, David Cope uses such example-based musicalgeneration methods but adds phrase-structure rules,
higher-level composition structure rules, and wellplaced signatures, earmarks and unifications [9, 10]. The
act of recombining the building blocks of music material
together with some typical patterns and structural
methods has proved to have great musical potential.
This type of self-learning predictors of musical elements
based on previous musical elements could be used on
any level or for any type of musical element such as:
musical note, chord, bar, phrase, section, and so on.
However, there must be logical relations on all those
levels; if a musical note is very close related to its
predecessor(s) then a list of predecessors can predict
quite well what note will follow. The same holds true
for chords, phrase-level, and section-level elements.
For the moment, we have chosen to stick to a
statistical predictor at the level of short vertical slices of
music such as a bar or half-bar, where the predictive
characteristics are determined by the chord (harmonic
set of pitches, or pitch-class) and by the first melodic
note following the melodic notes in those vertical slices
of music (see example below).
We implemented a simple method for generating
short musical phrases with a beginning and an end that
also allows for real-time steering with EEG information.
The system generates musical sequences by defining
top-level structures of sentences and methods of
generating similarity- or contrast-relationships between
elements. Consider the following example (LISP-like
notation):
S -> (INC BAR BAR BAR BAR BAR
HALF-CADENCE 8BAR-COPY)

From this top-level, we then generate rules for
selecting a valid musical building block for each
symbol, including rules for incorporating the EEG
information in all decisions. For example:
INC ->((EQUAL 'MEASURE 1)
(EQUAL 'COMPOSER
EEG-SET-COMPOSER))
BAR ->((CLOSE 'PITCH 'PREV-PITCH-LEADING)
(CLOSE 'PITCH-CLASS
'PREV-PITCH-CLASS-LEADING)
(EQUAL 'COMPOSER
EEG-SET-COMPOSER))

This defines a network that generates a valid
sentence with a beginning and an end, including real-

time EEG control through the variable EEG-SETCOMPOSER. The generative engine will find a musical
element for each of the constraint-sets that are generated
above from INC and BAR, by applying the list of
constraints in left-to-right order to the set of all musical
elements until there are no constraints left, or there is
only one musical element left. This means that it can
happen that some of the given constraints are not
applied.
The database of all musical elements contains music
from different composers, with elements tagged by their
musical function such as measure 1 for the start of a
phrase, cadence for the end, composer for the composer,
and the special tags pitch and pitch-class that are both
used for correct melodic and harmonic progression or
direction. The selection process is illustrated below.
The example database in the Appendix shows the
main attributes that are used to recombine musical
elements. P-CLASS (for pitch-class) is a list of two
elements. The first is the list of start-notes, transposed to
the range of 0-11. The second is the list of all notes in
this element (also transposed to 0-11). P is the pitch of
the first (and highest) melodic note in this element; by
matching this with the melodic note that the previous
element was leading up to we can generate a melodic
flow that adheres in some way to the logic of “where the
music wants to go”. The PCL (for pitch-class leading)
elements contain the same information about the
original next bar; this is used to find a possible next bar
in the recombination process. Then there are the INC,
BAR, and CAD elements. These are used for establishing
whether those elements can be used for phrase-starts
(incipient), or cadence.
Simply by combining the musical elements with the
constraint-based selection process that follows from the
terminals of the phrase-structure rewrite-rules, we end
up with a generative method that can take into account
the EEG information. This generates musical phrases
with a domino-game like building block connectivity:
((EQUAL 'MEASURE 1)
(EQUAL 'COMPOSER EEG-SET-COMPOSER))

constraint will order the available options according to
their closeness to the stored value. For example, after
choosing:
(SCHU-1-1-MEA-1
P-CLASS ((0 4) (0 3 4 6 7 9))
P 76
PCL ((2 7 11)(2 5 7 9 11))
PL 83
BAR INC
CO SCHU)

as the beginning, PREV-PITCH-LEADING will have
stored 83, and PREV-PITCH-CLASS-LEADING will
have stored ((2 7 11) (2 5 7 9 11)). This will
result in measure 2 and 4 being ranked highest
according to both pitch and pitch-class, and measure 6
and the cadence close according to pitch-class, while
measure 6 is also quite close according to pitch. This
weighted choice will give a degree of freedom in the
decision that is needed to generate pieces with an
element of surprise. The music will not get stuck in
repetitive loops, but it will find the closest possible
continuation when no perfect match is available. We can
still find a close match in this way if the third constraint
eliminates all the obvious choices that are available;
e.g., because a jump is requested to the musical
elements of another composer, who might not use the
same pitch-classes and pitches.
We are currently exploring other possibilities with
extra constraints and transformations on music that will
generate music with repeated similarities (such as
“unifications” [9, 10]), and larger structures such as the
generation of rondos and variations, while still adhering
in real-time to the demands of the EEG.
Figure 4 shows an example output with elements
from the musical style of Robert Schumann and Ludwig
van Beethoven. In this example the EEG jumped back
and forth from bar to bar between the two styles. The
harmonic and melodic distances are quite large from bar
to bar, but still they are the optimal choices in the set of
chosen elements from the two composers.

Assuming that there are also musical elements
available from composers other than SCHU, the first
constraint will limit the options to all incipient measures
from all musical elements from all composers. The
second constrains will then limit the options according
to the current EEG analysis to the composer that is
associated with the current EEG activity, as follows:
((CLOSE 'PITCH 'PREV-PITCH-LEADING)
(CLOSE 'PITCH-CLASS
'PREV-PITCH-CLASS-LEADING)
(EQUAL 'COMPOSER EEG-SET-COMPOSER))

In the given phrase structure, the rule that follows
from BAR then defines the constraints put upon a valid
continuation of the music. These constrains will limit
the available options one by one and will order them
according to the defined rule preferences. The CLOSE

Figure 4. An example of a generated mixture of
Robert Schumann and Ludwig van Beethoven.

3.

THE DEMONSTRATION SYSTEM

The demonstration system falls into the category of BCI
computer-oriented systems [18]. These systems rely on
the capacity of the users to learn to control specific
aspects of their EEG, affording them the ability to exert
some control over events in their environments.
Examples have been shown where subjects learn how to
steer their EEG to select letters for writing words on the
computer screen [7]. However, the motivation for this
demonstration departed from a slightly different angle
from other BCI systems. We aimed for a system that
would make music by “guessing” the meaning of the
EEG of the subject rather than a system for explicit
control of music by the subject. Learning to steer the
system by means of biofeedback would be possible, but
we did not investigate this possibility systematically yet.
We acknowledge unreservedly that the notion of
“guessing the meaning of the EEG” here is rather
simplistic. Nevertheless we took the risk of suggesting
this notion because it is a plausible notion: it is based on
the assumption that neurophysiological information can
be associated with specific mental activities [2, 24].
Continual progress in the field of Cognitive
Neuroscience of Music is increasingly substantiating
this assumption [23].

outside the scope of this paper. It suffices to say that we
are not looking for signals emanating from specific
cortical sites; rather, the idea is to sense the EEG over
the whole surface of the cortex. The electrodes are
plugged into a biosignal amplifier and a real-time
acquisition system. The analysis module is programmed
in Matlab/Simulink [17] to perform power spectrum and
Hjorth analyses in real-time. The analysis module
generates two streams of control parameters. One stream
contains information about the most prominent
frequency band in the signal and is used to generate the
music. The other stream contains information about the
complexity of the signal and is used to control the tempo
(beat) and dynamics (loudness) of the performance. The
generative music module is implemented in Max/MSP
and Common Lisp. (A newer version of the system is
being implemented in Miller Puckette’s PD.)
The present demonstration activates generative rules
for two different styles of music, depending on whether
the EEG indicates salient low-frequency or highfrequency components (or EEG rhythms) in the
spectrum of the EEG. Every time it has to produce a bar,
it checks the power spectrum of the EEG at that moment
and activates the generative rules accordingly.

Figure 6. The demonstration system in action using
a Disklavier piano.
Figure 5. The demonstration system runs on two
computers. The laptop performs the EEG analysis
with Matlab/Simulink and the Macintosh generates
the music with Max/MSP and Common Lisp. The
units under the laptop are the EEG amplifiers.
The system is programmed to look for information
in the EEG signal and match the findings with assigned
generative musical processes corresponding to different
musical styles. As mentioned in the previous section,
these assignments are arbitrary. An example could be: if
the system detects prominent alpha rhythms in the EEG,
then it might activate assigned processes that generate
musical passages in the style of Robert Schumann’s
piano works.
The EEG is sensed with seven pairs of gold EEG
electrodes on the scalp, forming a bipolar montage. A
discussion for the rationale of this configuration falls

The system is initialised with a reference tempo
(e.g., 120 beats per minute), which is constantly
modulated by the signal complexity analysis (Hjorth
analysis). The system sends out MIDI information for
performance on a Disklavier piano, manufactured by
Yamaha (Figures 5 and 6).
4.

CONCLUDING DISCUSSION

The work presented in this paper is the result of intense
multidisciplinary research, ranging from neuroscience
and medical engineering to music technology and
composition. Our research work owes an historical debt
to the pioneering works of people such as David
Rosenboom, Richard Teitelbaum and Alvin Lucier, but
extends those works with new possibilities for much
finer granularity of control over real-time musical
processes.

Research into brain-computer music interfacing is an
interesting arena for the development of new devices for
performance and composition. However, with this
research we are primarily interested in opening up new
possibilities in recreational and therapeutic devices for
people with physical and neurological disabilities.
There are various music-making devices available
for those with disabilities, and even though these
devices have proved to work very effectively, they often
do not allow as much control for those with severe
physical disabilities. At present, access music tutors use
gesture devices and adapted accessible technology to
make this possible, which achieve excellent results. For
people with severe physical disabilities, however,
having complete control of the environment created for
them by the facilitator can sometimes prove difficult.
For many with disabilities, EEG signals could be the
only option of control and sometimes with others be a
more reliable one, due to the nature of their disability.
At present, our system is being tested and assessed
in professional recreational activities by a music
facilitator. The results of these tests and assessments
will be crucial to guide further developments. In the
flowing paragraphs we briefly discuss some concluding
issues that emerged during the research.
4.1. BCMI vs. Hard BCI Research
The BCI research community understands that a BCI
system is a system that allows for the control of a
machine by explicitly thinking the task(s) in question;
e.g., control a robotic arm by thinking explicitly about
moving an arm. This is a very difficult problem. The
system presented in this paper does not address this type
of explicit control. This would be even more difficult in
the case of music.
However, we stress that we are not interested in a
system that plays a melody by thinking the melody
itself. Rather, we are furnishing our systems with
Artificial Intelligence in order to allow them make their
own interpretation of the meaning of the EEG patterns.
Such machine-interpretations may not always be
accurate or realistic, but this is exactly the type of manmachine interaction that we are addressing in our work.
4.2. Training
In order to have greater control over the system, we are
developing methods to train subjects to achieve specific
EEG patterns to control musical algorithms. We have
initial evidence that this can be made possible using a
technique known as biofeedback. Biofeedback is when
biological information or signals are monitored
electronically, which in turn feedback information about
our body or physiological state. This information is
often displayed through audio-visual stimuli. As a result
the subject can learn to modify these signals and
subsequently learn to gain greater control of the
biological signals. Biofeedback technology is used to
treat and control a number of conditions; examples

include migraine headaches and epilepsy. In addition it
has been used for artistic expression by composers such
as David Rosenboom through music, performance and
visual art [25, 26, 27].
4.3. Deciphering the EEG
Although powerful mathematical tools for analysing the
EEG already exist, we still lack a good understanding of
their analytical semantics in relation to musical
cognition. However, continual progress in the field of
cognitive neuroscience [23] is improving this scenario
substantially. Once these issues are better understood we
will be able to program our device to recognise patterns
of cognitive activity in the brainwaves and activate
appropriate musical algorithms associated with such
patterns. Preliminary work in this regard has been
reported in [18, 19].
4.4. Ergonomics
The non-ergonomic nature of the electrode technology
for sensing the EEG is an aspect that needs to be
addressed in future research. The current system is
awkward to wear and uncomfortable. There are various
possibilities for innovations in the hardware design of
EEG capture devices. Inexpensive auto-scanning / autonegotiating wireless chips are now available and could
be placed on the head along with the small
preamplifiers. It is thus possible to build wearable EEG
amplifiers with built-in signal processing and wireless
data transmission. The possibility of using other sensing
and brain imaging technologies also needs to be
addressed.
4.5. Quality of the Music
We acknowledge that the music produced by the system
is of limited appeal for those interested in contemporary
music. Furthermore, the pieces produced by our
computer-replication of musical style system may not
always sound convincing to discerning listeners.
However, we decided to adopt the ATN-like approach
developed by David Cope [7, 8] as a starting point for
this research because ATN grammars are well
understood and their use in music is well documented.
Nevertheless, we are studying the possibility of using
other interesting machine learning and generative
techniques such as those proposed by Barbar et al. [4],
Dubnov et al. [11], and Assayag and Dubnov (Factor
Oracles) [3].
We did try our system with more adventurous and
experimental compositional practices (cellular automata,
stochastic schemes, etc.). However, we decided to stick
to a more traditional pragmatic approach to musical
composition, at least at this stage of the project. It
proved to be less difficult to demonstrate the merits of
our research to the scientific and medical community
when the system produced music in styles that were
more popularly known.

5.

REFERENCES

[1] Adrian, E.D., and Matthews, B.H.C. (1934),
"The Berger Rhythm: Potential Changes from
the Occipital Lobes in Man." Brain 57(4): 35585.
[2] Anderson, C. and Sijercic, Z. (1996),
“Classification of EEG signals from four
subjects during five mental tasks”, Solving
Engineering Problems with Neural Networks:
Proceedings of the Conference on Engineering
Applications in Neural Networks (EANN’96),
pp. 507-414.
[3] Assayag, G. and Dubnov, S. (2004). “Using
Factor Oracles for Machine Improvisation”,
Soft Computing 8(9): 604-610.
[4] Barbar, K., Beurivé, A. and DesainteCatherine,
M.
(1998).
“Structures
hiérarchiques pour la composition assistée par
ordinateur”, M. Chemillier and F. Pachet
(Eds.), Recherches et applications en
informatique musicale. Paris: Hermès, 1998.
[5] Berger, H. (1969), “On the Electroencephalogram of Man”, The Fourteen Original
Reports on the Human Electroencephalogram,
Electroencepha-lography and Clinical Neurophysiology,
Supplement No. 28.
Amsterdam: Elsevier.
[6] Besson, M. and Faita, F. (1995), “An eventrelated potential (ERO) study of musical
expectancy: Comparison of musicians with
non-musicians”, Journal of Experimental
Psychology:
Human
Perception
and
Performance 21:1278-1296.
[7] Birbaumer, N., Ghanayin, N., Hinterberger, T.,
Iversen, I., Kotchoubey, B., Kubler, A.,
Perelmeouter, J., Taub, E. and Flor, H. (1999),
“A spelling device for the paralysed”, Nature
398:297-298.
[8] Brouse, A. 2004, “Petit guide de la musique
des ondes cérébrales”, Horizon 0, No. 15.
http://www.horizonzero.ca,
Accessed
31
January 2005.
[9] Cope, D. 2001. Virtual Music. Cambridge,
MA: The MIT Press.

[13] Janata, P. and Petsche, H. (1993), “Spectral
analysis of the EEG as a tool for evaluating
expectancy violations of musical contexts”,
Musical Perception 10(3):281-304.
[14] Koelsch, S., Schroger, E., Gunter, T.C. (2002),
“Music matters: Preattentive musicality of the
human brain”, Psychophysiology 39:38-48.
[15] Kohonen, T., Laine P., Tiits, K and Torkkola,
K. (1991), “A Nonheuristic Automatic
Composing Method”, P. Todd and D. G. Loy
(Eds.), Music and Connectionism. Cambridge
(MA): The MIT Press.
[16] Lucier, A. (1976), “Statement On: Music for
Solo Performer”, D. Rosenboom (Ed.),
Biofeedback and the Arts, Results of Early
Experiments. Vancouver: Aesthetic Research
Center of Canada Publications.
[17] Mathworks
(2004),
The
MathWorks,
http://www.mathworks.com, Acessed 18 June
2004.
[18] Miranda, E.R., Sharman, K., Kilborn, K. and
Duncan, A. (2003), “On Harnessing the
Electroencephalogram
for
the
Musical
Braincap”, Computer Music Journal 27(2):80102.
[19] Miranda, E. R., Roberts, S. and Stokes, M.
(2004). "On Generating EEG for Controlling
Musical Systems", Biomedizinische Technik
49(1):75-76.
[20] Misulis, K.E. (1997), Essentials of Clinical
Neurophysiology.
Boston,
Massachusetts:
Butterworth-Heinemann.
[21] Näätänen, R. (1990), “The role of attention in
auditory information processing as revealed by
event-related potentials and other brain
measures of cognitive function”, Behavioral
and Brain Sciences 13:201-288.
[22] Niedermeyer, E. and Lopes da Silva, F. H.
(Eds.) (1987) Electroencephalography (2nd
edition). Munich: Urban and Schwartzenberg.
[23] Peretz, I. and Zatorre, R.J. (2003), The
Cognitive Neuroscience of Music. Oxford:
Oxford University Press.

[10] Cope, D. 1996. Experiments in Musical
Intelligence. Madison, WI: A-R Editions Inc.

[24] Petsche, H. and Etlinger, S.C. (1998), EEG and
Thinking. Vienna: Austrian Academy of
Sciences.

[11] Dubnov, S., Assayag, G., Lartillot, O. and
Bejerano, G. (2003). “Using Machine-Learning
Methods for Musical Style Modeling”, IEEE
Computer 36(10): 73-80.

[25] Rosenboom, D. (Ed.) (1975), Biofeedback and
the Arts, Results of Early Experiments.
Vancouver: Aesthetic Research Center of
Canada Publications.

[12] Hjorth, B. (1970), “EEG analysis based on time
series properties”, Electroencephalo-graphy
and Clinical Neurophysiology 29:306-310.

[26] Rosenboom, D. (1990), Extended Musical
Interface with the Human Nervous System,
Leonardo Monograph Series No. 1. Berkeley,

California: International Society for the Arts,
Science and Technology.
[27] Rosenboom, D. (1990), “The Performing
Brain”. Computer Music Journal 14(1):48-65.
[28] Teitelbaum, R. (1976), “In Tune: Some Early
Experiments in Biofeedback Music (19661974)”, D. Rosenboom (Ed.), Biofeedback and
the Arts, Results of Early Experiments.
Vancouver: Aesthetic Research Center of
Canada Publications.
[29] Tervaniemi,
M. (1999), “Pre-Attentive
Processing of Musical Information in the
Human Brain”. Journal of New Music
Research 28(3):237-245.
[30] Vidal, J.J. (1973), "Toward Direct BrainComputer Communication", L. J. Mullins
(Ed.), Annual Review of Biophysics and
Bioengineering pp. 157—80.
[31] Wolpaw, J., McFarland, D., Neat, G., Forneris.
C. (1991), "An Eeg-Based Brain-Computer
Interface
for
Cursor
Control",
Electroencephalography
and
Clinical
Neurophysiology 78(3):252-9.
6.

APPENDIX

An excerpt from a database of musical elements where:
CO = composer (SCHU = Robert Schumann.), P-CLASS
= pitch class, P = pitch, PCL = pitch-class leading, PL =
pitch leading and TPE = type.
ID
CO
P-CLASS
P
PCL
PL
TPE

SCHU-1-1-CAD
SCHU
((0 2 7)(0 2 4 5 7 11))
74
((0 4 9)(0 2 4 5 7 9 11))
76
CAD

ID
CO
P-CLASS
P
PCL
PL
TPE

SCHU-1-1-MEA-6
SCHU
((5 9)(0 5 7 9))
81
((0 2 7)(0 2 4 5 7 11))
74
BAR

ID
CO
P-CLASS
P
PCL
PL
TPE

SCHU-1-1-MEA-5
SCHU
((0 4)(0 4 7))
76
((5 9)(0 5 7 9))
81
BAR

ID
CO

SCHU-1-1-MEA-4
SCHU

P-CLASS
P
PCL
PL
TPE

((0 4)(0 3 4 6 7 9))
83
((0 4)(0 4 7))
76
BAR

ID
CO
P-CLASS
P
PCL
PL
TPE

SCHU-1-1-MEA-3
SCHU
((0 4)(0 3 4 6 7 9))
76
((2 7 11)(2 5 7 9 11))
83
BAR

ID
CO
P-CLASS
P
PCL
PL
TPE

SCHU-1-1-MEA-2
SCHU
((2 7 11)(2 5 7 9 11))
83
((0 4)(0 3 4 6 7 9))
76
BAR

ID
CO
P-CLASS
P
PCL
PL
TPE

SCHU-1-1-MEA-1
SCHU
((0 4)(0 3 4 6 7 9))
76
((2 7 11)(2 5 7 9 11))
83
INC

