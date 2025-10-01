# On_Making_Music_with_Artificial_Life_Mod

Converted from: On_Making_Music_with_Artificial_Life_Mod.pdf
Date: 2025-08-19

---

Consciousness Reframed 2003

On Making Music with Artificial Life Models
Eduardo Reck Miranda
Summary: Our planet is a pulsating body inhabited by vibrating creatures and things. We are oscillatory beings resonating
in a myriad of vibrating frequencies: both natural (brainwaves, heartbeat, ocean tides, and so forth) and artificial
(telecommunications signals, radio, etc.). I am interested in the acoustics of the interplay between the artificial and the
natural worlds, and in particular with the idea of composing music with the aid of a computer. To this end, I am
investigating ways to make computational models of biological systems audible in order to make music with them. This
paper introduces two systems of my own design, which uses cellular automata to compose music and synthesise sounds.
Keywords: Computer Music, Generative Music, Granular Synthesis, Artificial Life, Cellular Automata.
Introduction
Perhaps one the greatest achievements of Artificial Intelligence (AI) to date lies in the construction of machines that
can compose music of incredibly good quality. One must not forget, however, that these AI systems are good at mimicking
well-known musical styles. They are either hard-wired to compose in a certain style or able to learn how to imitate a style by
looking at patterns in a bulk of training examples. Such systems are therefore good for imitating composers or musical
styles that are well established, such as medieval, baroque or jazz [7]. Conversely, issues as to whether computers can create
new kinds of music is much harder to study, because in such cases the computer should neither be embedded with particular
models at the outset nor learn from carefully selected examples. Furthermore, it is hard to judge what the computer creates in
such circumstances because the results normally sound very strange to us. We are often unable to judge these computergenerated pieces because they tend to lack those cultural references that we normally hold on to when appreciating music.
One plausible approach to these problems is to program the computer with abstract models that embody our
understanding of the dynamics of some compositional processes. Since the invention of the computer, many composers tried
out mathematical models, which were thought to embody musical composition processes, such as combinatorial systems,
stochastic models and fractals [1, 9, 10]. Some of these trials produced interesting music and much has been learned about
using mathematical formalisms and computer models in composition. The potential of artificial life models is therefore a
natural progression for computer-generated music. By artificial life models here I mean those computational paradigms
whereby the algorithms display some form of emergent behaviour that resembles a biological phenomena of some kind; for
example, cellular automata models, generic algorithms, autonomous agents systems and adaptive games to cite but a few.
This will become clearer in then next paragraphs where I introduce CAMUS and Chaosynth, two cellular automata-based
music systems of my own design.
Listening to the Propagation of Artificial Life Patterns
CAMUS uses two simultaneous cellular automata to generate musical forms: the Game of Life and Demon Cyclic
Space. Due to limitations of space, we will briefly introduce only the role of the Game of Life in its generative process.
More information on CAMUS can be obtained in a recent paper that appeared in the Computer Music Journal [2].
The Game of Life is a two-dimensional CA that attempts to model a colony of simple virtual organisms. In theory,
the automaton is defined on an infinite square lattice. For practical purposes, however, it is normally defined as consisting of
a finite m ¥ n array of cells, each of which can be in one of two possible states: alive represented by the number one, or dead
represented by the number zero. On the computer screen, living cells are coloured as black and dead cells are coloured as
white. The state of the cells as time progresses is determined by the state of their eight nearest neighbouring cells. There are
essentially four rules that determine the fate of the cells at the next tick of the clock:
•Birth: A cell that is dead at time t becomes alive at time t + 1 if exactly three of its neighbours are alive at time t;
•Death by overcrowding: A cell that is alive at time t will die at time t + 1 if four or more of its neighbours are alive
at time t;
•Death by exposure: A cell that is alive at time t will die at time t + 1 if it has one or none live neighbours at time t;
•Survival: A cell that is alive at time t will remain alive at time t + 1 only if it has either two or three live
neighbours at time t.
Whilst the environment, represented as E, is defined as the number of living neighbours that surround a particular live
cell, a fertility coefficient, represented as F, is defined as the number of living neighbours that surround a particular dead
cell. Note that both the environment and fertility vary from cell to cell and indeed from time to time as the automaton
evolves. In this case, the life of a currently living cell is preserved whenever 2 £ E £ 3 and a currently dead cell will be
reborn whenever 3 £ F £ 3. Clearly, a number of alternative rules can be set. The general form for such rules is (Emin, E max,
Fmin and Fmax) where Emin £ E £ E max and Fmin £ F £ F max. The CAMUS implementation of the Game of Life algorithm
enables the user to design rules beyond Conway's original rule. However rules other than (2, 3, 3, 3) may exist, but not all
of them produce interesting emergent behaviour.
CAMUS uses a Cartesian model in order to represent a triple of notes. In this context, a triple is an ordered set of
three notes that may or may not sound simultaneously. These three notes are defined in terms of the distances between them,
or intervals in music jargon. The horizontal co-ordinate of the model represents the first interval of the triple and the vertical
co-ordinate represents its second interval.

To begin the musical generation process, the CA is set up with an initial random configuration and is set to run.
When the Game of Life automaton arrives at a live cell, its co-ordinates are taken to estimate the triple from a given lowest
reference note. For example, if a cell at the position (5, 5) is alive then it will generate a triple of notes. The co-ordinates (5,
5) describe the intervals of the triple: a fundamental pitch is given, then the next note will be at five semitones above the
fundamental and the last note ten semitones above the fundamental. Although the cell updates occur at each time step in
parallel, CAMUS plays the live cells column by column, from top to bottom. Each of these musical cells has its own
timing, but the notes within a cell can be of different lengths and can be triggered at different times. Once the triple of notes
for each cell has been determined, the states of the neighbouring cells in the Game of Life are used to calculate a timing
template, according to a set of temporal codes. More information about this temporal codification can be found in a paper
that appeared in Interface (now called Journal of New Music Research) [3].
Listening to Organised Chaos
Chaosynth is essentially a granular synthesiser [4,5]. Granular synthesis works by generating a rapid succession of
very short sound bursts called granules (e.g. 35 milliseconds long) that together form larger sound events. The results tend
to exhibit a great sense of movement and sound flow. This synthesis technique can be metaphorically compared with the
functioning of a motion picture in which an impression of continuous movement is produced by displaying a sequence of
slightly different images (sound granules in our case) at a rate above the scanning capability of the eye. So far, most of these
systems have used stochasticity to control the production of the granules; for example, to control the waveform and the
duration of the individual granules. Chaosynth uses a different method: it uses cellular automata. The CA used in Chaosynth
tends to evolve from an initial random distribution of cells in the grid, towards an oscillatory cycle of patterns.
The behaviour of this CA resembles the way in which most of the natural sounds produced by some acoustic
instruments evolve: they tend to converge from a wide distribution of their partials (for example, noise) to oscillatory
patterns; for example, a sustained tone. Chaosynth’s CA can be thought of as a grid of identical electronic circuits called
cells. At a given moment, cells can be in any one of the following conditions: quiescent, depolarised or burned. A cell
interacts with its neighbours (4 or 8) through the flow of electric current between them. There are minimum (Vmin) and
maximum (Vmax) threshold values which characterise the condition of a cell. If its internal voltage (Vi) is under Vmin, then
the cell is quiescent (or polarised). If it is between Vmin (inclusive) and Vmax values, then the cell is being depolarised. Each
cell has a potential divider which is aimed at maintaining Vi below Vmin. But when it fails (that is, if Vi reaches Vmin) the
cell becomes depolarised. There is also an electric capacitor, which regulates the rate of depolarisation. The tendency,
however, is to become increasingly depolarised with time. When Vi reaches Vmax, the cell fires and becomes burned. A
burned cell at time t is automatically replaced by a new quiescent cell at time t + 1.
Each sound granule produced by Chaosynth is composed of several spectral components. Each component is a
waveform produced by a digital oscillator (i.e., a lookup sampling table containing one cycle of a waveform) which needs
two parameters to function: frequency and amplitude. The CA controls the frequency and duration values of each granule (the
amplitude values are set up via another procedure). The values (i.e., the colours) of the cells are associated to frequencies and
oscillators are associated to a number of cells. The frequencies of the components of a granule at time t are established by the
arithmetic mean of the frequencies associated with the values of the cells associated with the respective oscillators. Suppose,
for example, that each oscillator is associated with 9 cells and that at a certain time t, 3 cells correspond to 110 Hz, 2 to 220
Hz and the other 4 correspond to 880 Hz. In this case, the mean frequency value for this oscillator at time t will be 476.66
Hz. The user can also specify the dimension of the grid, the amount of oscillators, the allocation of cells to oscillators, the
allocation of frequencies to CA values, and various other CA-related parameters. The duration of a whole sound event is
determined by the number of CA iterations and the duration of the particles; for example, 100 iterations of 35 millisecond
particles results in a sound event of 3.5 seconds of duration.
Discussion and conclusion
A number of professional pieces were composed using CAMUS-generated material, such as Entre o Absurdo e o
Mistério [8], for chamber orchestra, and the second movement of the string quartet Wee Batucada Scotica [6]. Chaosynth
also proved to be a successful experiment in the sense that it is able to synthesise a large amount of unusual sounds that are
normally not found in the real acoustic world, but nonetheless sound pleasing to the ear. As an example of an electroacoustic
piece composed using the sounds of Chaosynth I cite Olivine Trees, which has recently been awarded the bronze medal at the
International Luigi Russolo Electroacoustic Music Competition in Italy (the recordings of all these pieces are available by
request). The results of the CA experiments are very encouraging, as they are good evidence that both musical sounds and
abstract musical forms might indeed share similar organisational principles with cellular automata.
In general, I found that Chaosynth produced more interesting results than CAMUS. I think that this might be due to
the very nature of the phenomena in question. The inner structures of sounds seem more susceptible to CA modelling than
large musical structures. As music is primarily a cultural phenomenon, in the case of CAMUS I think that one would need
to add generative models that take into account the dynamics of social formation and cultural evolution. In this case, one
should find modelling paradigms where phenomena (in our case musical processes and forms) can emerge autonomously. I
am currently working on a number of experiments whereby I am trying to simulate the emergence of musical forms in a
virtual community of simple entities, or ‘software agents; in computer science jargon. Should such experiments corroborate
my hypothesis that one can improve computer composition systems considerably by including mechanisms that take into
account the dynamics of cultural evolution and social interaction, then I believe that over the next few years we will be
listening to a new generation of much improved intelligent composing systems.
References
[1] Dodge, T. and Jerse, T. A., Computer Music: Synthesis, Composition and Performance, Schirmer Books, 1985.
[2] McAlpine, K, Miranda, E. R. and Hoggar, S., “Making Music with Algorithms: A Case-Study System”, Computer
Music Journal, Vol 23 No. 2, 1999.
[3] Miranda, E. R., “Cellular Automata Music: An Interdisciplinary Project”, Interface/Journal of New Music Research,
Vol.22, No. 1, 1993.

[4] Miranda, E. R., “Granular Synthesis of Sounds by Means of a Cellular Automaton”, Leonardo, Vol. 28, No. 4, 1995.
[5] Miranda, E. R., Computer Sound Synthesis for the Electronic Musician, Focal Press, 1998.
[6] Miranda, E. R., Wee Batucada Scotica, musical score, Goldberg Ediçöes Musicais, 1998.
[7] Miranda, E. R., (Ed.) Readings in Music and Artificial Intelligence, Gordon and Breach/Harwood Academic Publishers,
2000.
[8] Miranda, E. R., Entre o Absurdo e o Mistério, musical score, Goldberg Ediçöes Musicais, 2001.
[9] Worral, D., “Studies in metamusical methods for sound image and composition”, Organised Sound, Vol. 1, No. 3,
1996.
[10] Xenakis, I., Formalized Music, Indiana University Press, 1971.
Eduardo Reck Miranda is a Reader in Artificial Intelligence and Music at the University of Plymouth, UK. He is a leading
research scientist and a composer of international reputation. He received an MSc in Music Technology from the University
of York and went on to the University of Edinburgh, where in 1994 he obtained his PhD in Music with important
contributions in the fields of musical knowledge representation, machine learning of music and software sound synthesis. In
1994 he was awarded a research fellowship at the Edinburgh Parallel Computing Centre (EPCC), where he developed
Chaosynth, a granular synthesis software that uses evolutionary computing techniques for generating complex sound spectra.
In 1998, Dr. Miranda moved to France, to take up a research position at Sony Computer Science Laboratory. At Sony he
conducted research aimed at gaining a better understanding of the fundamental cognitive mechanisms employed in soundbased communication systems, with particular focus on the evolution of the human ability to speak and the role of our
musical capacity in the development of spoken languages. His compositions have been broadcast and performed in
prestigious concerts and festivals worldwide, including Festival Música Viva (Lisbon, 1999, 2000), Computer Music
Festival in Seoul (Seoul, 1998, 1999, 2001) and International Computer Music Conference (Gothenburg 2002, Hong Kong
1996), to cite but a few. Email: <eduardo.miranda@plymouth.ac.uk>. URL: http://neuromusic.soc.plymouth.ac.uk.

