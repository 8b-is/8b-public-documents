# Application_of_Pulsed_Melodic_Affective

Converted from: Application_of_Pulsed_Melodic_Affective.pdf
Date: 2025-08-19

---

Application of Pulsed Melodic Affective Processing to
Stock Market Algorithmic Trading and Analysis
Alexis Kirke1 and Eduardo Miranda1
1

Interdisciplinary Centre for Computer Music Research, School of Humanities, Music and
Performing Arts, Faculty of Arts, University of Plymouth,
Drake Circus, Plymouth, UK
{Alexis.Kirke, Eduardo.Miranda}@Plymouth.ac.uk
Abstract. The application of Pulsed Melodic Affective Processing (PMAP) to
stock market analysis and algorithmic trading is examined. PMAP utilizes
musically-based pulse sets (“melodies”) for processing – capable of
representing affective states. Affective processing and affective input/output is
now considered to be a key tool in artificial intelligence and computing.
However in the designing of processing elements (e.g. bits, bytes, floats, etc),
engineers have primarily focused on the processing efficiency and power.
Having defined these elements, they then go on to investigate ways of making
them perceivable by the user/engineer. But the extremely active and productive
area of Human-Computer Interaction - and the increasing complexity and
pervasiveness of computation in our daily lives – supports the idea of a
complementary approach in which computational efficiency and power are
more balanced with understandability to the user/engineer. PMAP provides the
potential for a person to tap into the affective processing path to hear a sample
of what is going on in that computation, as well as providing a simpler way to
interface with affective input/output systems. In this paper PMAP will be
applied to a simple algorithmic trading system based on an affective model of a
simulated stock market.
Keywords: Human-Computer Interaction, Music, Affective, Boolean Logic,
Neural Networks, Behavioural Finance, Algorithmic Trading, Stock Market

1 Introduction
Pulsed melodic affective processing involves the use of music as a processing tool
for affective computation in artificial systems. It has been shown that affective states
(emotions) play a vital role in human cognitive processing and expression [1]. The
field of Behavioral finance has highlighted the importance of emotions in finance and
markets [2]. This paper proposes the application of PMAP in stock market trading and
analysis.
Affective state processing has been incorporated into previous artificial
intelligence processing and robotics [3]. The issue of developing systems with
affective intelligence which also provide for greater user-transparency, is a key

element discussed in this paper. Music has often been described as a language of
emotions [4]. There has been work into automated systems which communicate
emotions through music [5] and which detect emotion embedded in music based on
musical features [6]. Hence the general features which express emotion in western
music are known.
Before introducing these, affective representation will be briefly discussed. The
dimensional approach to specifying emotion utilizes an n-dimensional space made up
of emotion “factors”. Any emotion can be plotted as some combination of these
factors. For example, in many emotional music systems [7] two dimensions are used:
Valence and Arousal. In that model, emotions are plotted on a graph (see Figure 1)
with the first dimension being how positive or negative the emotion is (Valence), and
the second dimension being how intense the physical arousal of the emotion is
(Arousal). For example “Happy” is high valence high arousal affective state, and
“Stressed” is low valence high arousal state.
Figure 1: The Valence/Arousal Model of Emotion

Previous research [8] has suggested that a main indicator of valence is musical key
mode. A major key mode implies higher valence, minor key mode implies lower
valence. For example the overture of The Marriage of Figaro opera by Mozart is in a
major key; whereas Beethoven’s melancholy “Moonlight” Sonata movement is in a
minor key. It has also been shown that tempo is a prime indicator of arousal, with
high tempo indicating higher arousal, and low tempo - low arousal. For example:
compare Mozart’s fast overture above with Debussy’s major key but low tempo
opening to “Girl with the Flaxen Hair”. The Debussy piano-piece opening has a
relaxed feel – i.e. a low arousal despite a high valence.
Affective Computing [9] focuses on robot/computer affective input/output.
Whereas an additional aim of PMAP is to develop data streams that represent such
affective states, and use these representations to internally process data and compute
actions. The other aim of PMAP is more related to Picard’s work – to aid easier
sonification of affective processing [10] for transparency in HCI, i.e. representing
non-musical data in musical form to aid its understanding. Related sonification

research has included tools for using music to debug programs [11]. There have also
been a number of papers published on sonification [12][13] of stock market data, but
not from an affective point of view, nor with a unified data stream for processing and
sonification.

2 PMAP Representation of Affective State
Pulsed melodic affective processing is a method of representing affective state
using music. In PMAP the data stream representing affective state is a series of pulses
of 10 different levels with a varied pulse rate. This rate is called the “Tempo”. The
pulse levels can vary across 12 values. The important values are:
1,3,4,5,6,8,9,10,11,12 (for pitches C,D,Eb,E,F,G,Ab,A,Bb,B – we assume all
melodies are in C). These values represent a valence (positivity or negativity of
emotion). Values 4, 9 & 11 represent negative valence (Eb, Ab, Bb are part of C
minor) e.g. sad; and values 5, 10,& 12 represent positive valence (E, A, B are part of
C major), e.g. happy. The other pitches are taken to be valence-neutral. For example a
PMAP
stream
of
say
[1,1,4,4,2,4,4,5,8,9]
(which
translates
as
C,C,Eb,Eb,C#,Eb,Eb,E,G,Ab) would be principally negative valence since most of
the notes are in the minor key of C. It is understood that these key modes can become
ambiguous, particularly in terms of relative keys. It is expected that they will tend to
be more accurate for more extreme valence values (i.e. those furthest from 0).
The pulse rate of a stream contains information about arousal. So
[1,1,4,4,2,4,4,5,8,9] transmitted at maximum pulse rate, could represent maximum
arousal and low valence, e.g. “Anger”. Similarly [10,8,8,1,2,5,3,1] (which translates
as A,G,G,C,D,E,C,C) transmitted at a quarter of the maximum pulse rate could be a
positive valence, low arousal stream, e.g. “Relaxed” (because it is in the major key of
C). If there are two modules or elements both with the same affective state, the
different note groups which go together to make up that state representation can be
unique to the object generating them. This allows other objects, and human listeners,
to identify where the affective data is coming from.
In performing some of the analysis on PMAP, it is convenient to utilize a
parametric form, rather than the data stream form. The parametric form represents a
stream by a Tempo-value variable and a Key-value variable, which can vary
continuously as Arousal and Valence vary.

3 Affective Market Mapping
PMAP has been applied to affective processing in a multi-robot security system,
and to a text emotion detection system [14]. The first of these was achieved by
designed a set of “musical” logic circuits. The second involved a neural network
based on musical neurons or “Murons”, whose weights adjust tempo and key mode,
and which learned by gradient descent. There are 3 elements which suggest PMAP
may have potential in the stock markets: a simple market-state mapping (described
below), the incorporation of trader, client and news article “sentiment” into what is an
art as well as a science, and a natural sonification for eyes-free HCI in busy
environments. The Affective Market Mapping (AMM) involves mapping stock
movements onto a PMAP representation. Such a mapping would allow PMAP
processing to interact with stock market data and be used for algorithmic trading. One
mapping that was initially considered was a risk / return mapping – letting risk be

mapped onto arousal / tempo, and return be mapped onto valence / key mode.
However this does not give an intuitively helpful result. For example it implies that a
high arousal high valence stock (high risk / high return) is “happy”. However this
entirely depends on the risk profile of the investor / trader. So a more flexible
approach – and one that is simpler to implement - for the AMM is:
1. Key mode (valence) is proportional to Market Imbalance.
2. Tempo (arousal) is proportional to Number of Trades per Second.
These can refer to a single stock, a group of stocks, or a whole index. Consider a
single stock S. The Market Imbalance Z in a time period dT is the total number of
shares of buying interest in the market during dT minus the total number of shares of
selling interest during dT. This information is not publically available, but can be
approximated. For example it can be calculated as in [15] - the total number of buyinitiated sales minus the total number of sell-initiated trades (normalized by the
Average Daily Volume for S); with a trade is defined as buy initiated if it happens on
an uptick in the market price of stock S, and sell-initiated if it happens on a downtick
(the “tick algorithm”). If there are as many buyers as sellers in stock S then it is
balanced and its market imbalance Z will be 0. If there are a large number of buyers
and not enough sellers (e.g. in the case where positive news has been released about
the stock) the imbalance will become positive.
To generate a melody from a stock, simply have a default stream of non-key notes
at a constant or uniformly random rate; and every time there is a trade add a major
key note for a buy initiated trade and a minor key note for a sell initiated trade. So for
example, if a stock is being sold off rapidly due to bad news, it will have a negative
market imbalance and a high trading rate – which will be represented in PMAP as a
minor key and high tempo – earlier labelled as “angry”. Stocks trading up rapidly on
good news will be “happy”, stocks trading up slowly in a generally positive market
will be “relaxed”. The resulting PMAP stream matches what many would consider
their affective view of the stock.

6 Simulation
To examine a simple processing usage of the Affective Market Mapping and PMAP
a basic algorithmic trading system will be implemented. Algorithmic Trading has
become extremely prominent in the markets in the last few years [16], but we are not
aware of any work which focuses on affectivity. To examine this approach, a simple
stock market order book simulation has been developed. The market contains a single
stock whose initial price is $100. Orders arrive at the market at a constant rate of one
every 10 minutes. The stock has an Average Daily Volume of around 40000 shares.
Each trade can be a buy or sell order with a probability p of being a buy order and 1-p
of being a sell-order. The order book can contain up to 30 buy orders and 30 sell
orders. Each order is uniformly randomly sized. The market price p(t) evolves based
on whether an order is a buy or sell order, the order size, and a price volatility
parameter.
p(t) = p(t-1) + priceDriftFactor.orderSize.orderPrice / ADV
- volatility+ 2.r.volatility

The level at which a simulated order is priced is the market price p(t) with a certain
deviation of % size defined by a parameter priceFluctFactor. Once the book has filled
up with arriving orders, new orders overwrite the oldest ones. Although in the
simulation it is known precisely whether the order is a buy or sell order, the tick
algorithm is still used to estimate the order side for the affective market mapping. The
accuracy of this estimation will depend on the size of the random price fluctuations in
orders and the market price volatility – i.e. the higher the volatility and fluctuation
parameters, the less accuracy the tick algorithm with exhibit. For the simulation
detailed here volatility was set to 0.02, priceDriftFactor to 0.005 and
priceFluctFactor to 0.001. This led to the tick algorithm being on average about 75%
accurate. In other words about 75% of orders were correctly classified. If volatility is
increased to 0.005, the accuracy drops to around 60%.
To see how this model functions with the affective marking mapping, consider the
prices of a month’s worth of trading shown on the left hand side of Figure 2, where
maximum order size is 1000 shares. This month is a “neutral” month – in other words
the probability of a buy order is equal to the probability of a sell order. The right hand
side of Figure 2 shows a month where there is a constant probability of 70% of a sell
order arriving, and of 30% of a buy order arriving. The left side of Figure 3 shows the
valence calculated for this “selling month”. The higher valences are equivalent to a
more clearly major key mode and the lower valences to a more clearly minor key
mode. (Note in the following discussions valence and arousal are used
interchangeably with key mode and tempo. This is for simplicity - rather than
constructing a melodic stream.) The first thing to observe is that the valence is usually
negative, with a mean valence of -0.34. There are 5 sections where it goes above 0,
but then there are also local maxima in the globally falling stock price in Figure 2.
Figure 2: Stock Price in dollars in a “Neutral” Month; and in a “Selling Month” (x-axis is
simulation time steps)

It is much clearer to see patterns of behaviour if both key-mode and tempo are
plotted as valence and arousal, as in Figure 4. The right hand of Figure 3 shows a
market event which begins with a relative relaxed trading in the stock just above
$100, followed by a rapid rise in the stock price due to an increase in buy order
probability. This is followed by another period of stable price trading just below $104,
then for some reason the stock starts to fall with increasing rapidity back to just above
$100. This is done by setting the buy probabilities to 0.5, 0.75, 0.5, 0.25 respectively;

and setting average order amounts to 1000, 2000, 1500, and then during the selling
period to 1500 and then 4000. Looking now at how this is reflected in the affective
market model, we can observe the left hand of Figure 4. To clarify this further an
average version is shown in the right hand side of Figure 4, averaged over 50 runs.
Figure 3: Valence of Stock Price in the “Selling” Month; and Price during “Event” (x-axis
is simulation time steps)

The stock begins at the far left of the diagram with a low arousal and neutral
valence due to the slow build of the order book (which starts from empty). One can
then observe at least 5 “emotional regimes” that the market moves through, as the
arousal/valence line is followed by eye moving from the far left to the far right of the
diagram:
1.
2.

3.
4.
5.

“Relaxed” – after the arousal builds up there is a regime around 0.02 arousal at
the left of the diagram.
“Joyful”/”Excited” – this is the region of maximum valence / key-value and
with significantly increase arousal / tempo, during which the stock price is
rising more rapidly.
“Happy” – The market rise is slowing down as it approaches $104
“Sad” – The market starts to go down slowly.
“Angry”/”Fearful” – At around $102.50 the stock begins to fall rapidly.
Figure 4: Affective Market Model of Stock event; and Mean Affective Market Model
averaged over 50 Stock events

An interesting element to observe concerning these regimes is that they are audible
since if sound is played with the relevant key-value and tempo the music will – for
western listeners - have the affective communication (approximately) of: “Relaxed”,
“Excited”, “Happy”, “Sad”, and “Fearful” [5].
To examine how the AMM might be used in algorithmic trading, consider a simple
rule:
If keymode > trigger then buy stock quantity proportional to tempo
If keymode <-trigger then sell short the stock with quantity proportional to tempo
Using this rule and the above market model, with a trigger value of 0.1, trading
simulations were run (once again substituting valence for key-mode, and arousal for
tempo). When the trigger kicked in a stock quantity of 50xArousal was traded. So an
arousal of 0 would lead to a trade of 0 shares, an arousal of 2 would lead to a trade of
100 shares. The results are shown in Table 1, each cell gives the average profit from
50 experiments.
Table 1: Profits for the Strategy
Trigger
0.6
0.6
0.4
0.4
0.1
0.1

Arousal-based
Trade Size?
Y
N
Y
N
Y
N

Trigger Strategy
Profit
$4,515
$9,109
$21,618
$18,333
$15,609
$18,235

Random Strategy
Profit
$671
-$244
$17
$76
$1,843
-$103

The Random strategy trades with approximately the same frequency as the Trigger
Strategy but at randomize times and random order sizes. Column 2 is included so as
to compare trading a fixed amount, with trading an amount decided by arousal level.
It can be seen that the trigger strategy outperforms the random strategy, and that a full
valence / arousal strategy (where trade size is based on arousal) outperforms a
valence-only strategy. Another interesting element of the arousal-based order size is
that order sizes will tend to be closer to the immediate market volumes, which may
tend to reduce transaction costs. Note that algorithmic strategies such as the above
could be embedded in Music Logic circuits and Musical Neural Networks [14],
allowing them to interact with other PMAP functionality such as sentiment analysis of
news text feeds.
In theory the above stock market methodologies could all have been derived purely
based on valence and arousal, without mentioning tempo and key mode. However
PMAP is designed to simplify the sonification of internal processing [14]. So this
work is designed to show another area where PMAP can be applied, rather than to
address specifically how the sonification of internal processing has particular benefits
in stock market computations. But there is also a benefit which stands out here in the
use of PMAP – it incorporates a sonification of the market. The melodies provide a
natural sonification of stock movements – a useful factor for traders whose eyes are
already too busy [13]. One can also consider the harmonic relationship between two
stocks, or between a stock and the market. There may be PMAP methods developable

such that if stocks start to create cross-dissonance where once was consonance (e.g.
one becomes more major as the other stays minor) then this indicates a potential
divergence in any correlated behaviour.

8 Conclusions
This paper has introduced the concept of PMAP and given an initial proof of
concept of a stock market application. PMAP is a complementary approach in which
computational efficiency and power are more balanced with understandability to
humans (HCI); and which can naturally address rhythmic and affective processing. Its
application in stock markets requires significant further work before these very initial
experiments. For example, it needs to be tested against real stock market data, and
trading profits need to include the factoring in of transaction costs. There also need to
be cross-comparisons with other standard algorithmic trading approaches. Finally
there should be listening tests analysing the audible information content in the
processing and the market mapping.
There are a significant number of issues to be further addressed with PMAP itself,
a key one being is the rebalance between efficiency and understanding useful and
practical, and also just how practical is sonification? The valence/arousal coding
provides simplicity, but is it sufficiently expressive while remaining simple? Similarly
it needs to be considered if a different representation than tempo/key mode be better
for processing or transparency. PMAP also has a close relationship to Fuzzy Logic
and Spiking Neural Networks – so perhaps it can adapted based on lessons learned in
these disciplines. And finally, most low level processing is done in hardware – so
issues of how PMAP hardware is built need to be investigated.

References
1.

Malatesa, L., Karpouzis, K., Raouzaiou, A.: Affective intelligence: the human face of AI,
In Artificial intelligence, Springer-Verlag (2009).
2. Davies, G.B, De Servigny, A.: Behavioral Investment Management: An Efficient
Alternative to Modern Portfolio Theory, McGraw-Hill (2012).
3. Banik, S., Watanabe, K., Habib, M., Izumi, K.: Affection Based Multi-robot Team Work,
In Lecture Notes in Electrical Engineering, pp. 355--375 (2008).
4. Cooke, D.: The Language of Music. Oxford University Press (1959).
5. Livingstone, S.R., Muhlberger, R., Brown, A.R., Loch, A.: Controlling Musical
Emotionality: An Affective Computational Architecture for Influencing Musical
Emotions. Digital Creativity, Vol. 18, No. 1, pp. 43--53 (2007).
6. Kirke, A., Miranda, E.: Emergent construction of melodic pitch and hierarchy through
agents communicating emotion without melodic intelligence, In Proceedings of 2011
International Computer Music Conference (ICMC 2011), ICMA (2011).
7. Kirke, A., Miranda, E.: A Survey of Computer Systems for Expressive Music
Performance, ACM Surveys, Vol. 42, No. 1, pp. 1--41 (2009).
8. Juslin, P.: From Mimesis to Catharsis: expression, perception and induction of emotion in
music, In Music Communication, pp. 85--116, Oxford University Press (2005).
9. Picard, R.: Affective Computing: Challenges, International Journal of Human-Computer
Studies, Vol. 59, No. 1-2, pp. 55--64 (2003).
10. Cohen, J.: Monitoring Background Activities, In Auditory Display: Sonification,
Audification, and Auditory Interfaces, pp. 499--531 (1994).
11. Vickers, P., Alty, J.: Siren songs and swan songs debugging with music. Communications
of the ACM, Vol. 46, No. 7, pp. 87--92 (2003).

12. Worral, D.: The use of sonic articulation in identifying correlation in capital market
trading data, In Proceedings of the 15th International Conference on Auditory Display
(2009).
13. Cifariello, F., At F.: sMAX: A Multimodal Toolkit for Stock Market Data Sonification, In
Proceedings of the 10th International Conference on Auditory Display (2004).
14. Kirke, A., Miranda, E.: Pulsed Melodic Processing - Using Music for natural Affective
Computation and increased Processing Transparency, In Music and Human-Computer
Interaction, Springer Verlag (2012).
15. Kissell, R., Glantz, M.,: Optimal Trading Strategies, Amacom (2003).
16. Pole, A.: Algorithmic Trading and Statistical Arbitrage. Trading, Vol. 2, No. 1, pp. 79—
87 (2007).

