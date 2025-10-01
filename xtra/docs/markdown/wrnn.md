# Traveling Waves Encode the Recent Past and Enhance Sequence Learning

**Published as a conference paper at ICLR 2024**

## Authors

- **T. Anderson Keller*** - The Kempner Institute for the Study of Natural and Artificial Intelligence, Harvard University, USA
- **Lyle Muller** - Department of Mathematics, Western University, CA
- **Terrence Sejnowski** - Computational Neurobiology Lab, Salk Institute for Biological Studies, USA
- **Max Welling** - Amsterdam Machine Learning Lab, University of Amsterdam, NL

*Correspondence: T.Anderson.Keller@gmail.com, work completed while part of the UvA-Bosch Delta Lab.

## Abstract

Traveling waves of neural activity have been observed throughout the brain at a diversity of regions and scales; however, their precise computational role is still debated. One physically inspired hypothesis suggests that the cortical sheet may act like a wave-propagating system capable of invertibly storing a short-term memory of sequential stimuli through induced waves traveling across the cortical surface, and indeed many experimental results from neuroscience correlate wave activity with memory tasks. To date, however, the computational implications of this idea have remained hypothetical due to the lack of a simple recurrent neural network architecture capable of exhibiting such waves. In this work, we introduce a model to fill this gap, which we denote the Wave-RNN (wRNN), and demonstrate how such an architecture indeed efficiently encodes the recent past through a suite of synthetic memory tasks where wRNNs learn faster and reach significantly lower error than wave-free counterparts. We further explore the implications of this memory storage system on more complex sequence modeling tasks such as sequential image classification and find that wave-based models not only again outperform comparable wave-free RNNs while using significantly fewer parameters, but additionally perform comparably to more complex gated architectures such as LSTMs and GRUs.

## 1. Introduction

Since the earliest neural recordings (Caton, 1875; Beck, 1890), neural oscillations and the spatial organization of neural activity have persisted as topics of great interest in the neuroscience community. Consequently, a plethora of hypothesized potential functions for these widely observed phenomena have been put forth in the literature. For example: Pitts & McCulloch (1947) propose that alpha oscillations perform 'cortical scanning' akin to radar; Milner (1974) suggests that synchrony may serve to segregate the visual scene and 'bind' individual features into cohesive objects; Engel et al. (2001) suggest brain-wide oscillations serve as 'top-down' stored knowledge and contextual influence for local processing; Raghavachari et al. (2001) show theta is consistent with a gating mechanism for human working memory; Buzsáki et al. (2013) posit that oscillations form a hierarchical system that offers a syntactical structure for spike traffic; and Liebe et al. (2012) & de Mooij-van Malsen et al. (2023) implicate oscillatory coherence with the transfer of information on working memory tasks.

Recently, the advents of high density multi-electrode arrays and high resolution imaging have led to the discovery that many of the oscillations observed in the brain are better described as traveling waves of activity rather than precise zero-lag synchrony (Muller et al., 2018). For example, alpha and theta oscillations have been measured to precisely correspond to traveling waves in both the cortex and hippocampus of humans (Lubenov & Siapas, 2009; Lozano-Soldevilla & VanRullen, 2019; Zhang et al., 2018). Furthermore, it has become increasingly clear that wave-like dynamics are prevalent throughout the brain, from local (Muller et al., 2014) to global (Muller et al., 2016) scales, and across virtually all brain regions measured (Townsend et al., 2015; Gu et al., 2021b; Pang et al., 2023). Research has correlated wave activity with a range of functional roles rivaling oscillations in diversity and number, including: perceptual awareness (Davis et al., 2020); attentional scanning (Fries, 2023); information transfer (Rubino et al., 2006); motor control sequencing and topographic organization (Takahashi et al., 2011); integrating visual sensory signals with saccadic eye movements (Zanos et al., 2015); and coordinating and reconfiguring distinct functional regions (Xu et al., 2023).

Most relevant to the present study, significant work has shown correlations between wave dynamics and memory. For example: King & Wyart (2021) provide evidence that traveling waves propagating from posterior to anterior cortex serve to encode sequential stimuli in an overlapping 'multiplexed' manner; Sauseng et al. (2002) show that traveling theta oscillations propagate from anterior to posterior regions during retrieval from long-term memory; and Zabeh et al. (2023) show traveling beta waves in frontal and parietal lobes encode memory of recent rewards. As described by Muller et al. (2018), one way to understand the relation between traveling waves and memory comes from an analogy to physical wave systems. Specifically, non-dissipative wave-propagating systems can be shown to contain all information about past disturbances in a 'time-reversible' manner. In contrast, in a static wave-free 'bump' system, onset time of stimuli are tied to position, and therefore information about the sequential order of multiple inputs at the same position is lost. This is visualized in Figure 1, and is demonstrated experimentally in Section 3. Although an imperfect analogy to the brain, such ideas have inspired neuroscientists to suggest that the cortical surface may act like such a wave-propagating system to efficiently encode recent sequential inputs as a form of working memory. In this work, we propose a complimentary mechanistic understanding of the relation between traveling waves and memory by suggesting that a wave-propagating hidden state can be thought of like a register or 'stack' to which inputs are sequentially written or 'pushed'. The propagation of waves then serves to prevent overwriting of past input, allowing for superior invertible memory storage.

**Figure 1:** Three binary input signals (top), a corresponding wave-RNN hidden state (middle), and wave-free static bump system (bottom). At each timestep we are able decode both the onset time and channel of each input from the wave-RNN state. In the wave-free system, relative timing information is lost for inputs on the same channel, hindering learning and recall for sequential inputs.

In concert with these theories of potential function, an almost equal number of arguments have been put forth suggesting that traveling waves are 'epiphenomenal' or merely the inert byproduct of more fundamental causal neural processes without any causal power of their own. One driving factor behind the continuation of this controversy is a lack of sufficiently capable models which permit the study of the computational role of waves in a task-relevant manner. In the computational neuroscience literature, there exist large-scale spiking neural network (SNN) models which exhibit traveling waves of activity (Davis et al., 2021); however, due to the computational complexity of SNNs, such models are still not feasible to train on real world tasks. These models therefore lack the ability to demonstrate the implications of traveling waves on memory. In the machine learning community, Keller & Welling (2023) recently introduced the Neural Wave Machine which exhibits traveling waves of activity in its hidden state in the service of sequence modeling; however, due to its construction as a network of coupled oscillators, it is impossible to disassociate the memory-enhancing contributions of oscillations (as described by Rusch & Mishra (2021a)) from those of traveling waves.

In this work, we derive and introduce a simple non-oscillatory recurrent neural network (RNN) architecture which exhibits traveling waves in its hidden state and subsequently study the performance implications of these waves when compared directly with identical wave-free 'bump system' RNN counterparts. Ultimately, we find that wave-based models are able to solve sequence modeling tasks of significantly greater length, learn faster, and reach lower error than non-wave counterparts, approaching performance of more complicated state of the art architectures – thereby providing some of the first computational evidence for the benefits of wave-based memory systems. We therefore present our model as both a proof of concept of the computational role of wave-based memory systems, as well as a starting point for the continued development of such systems in the future.

## 2. Traveling Waves in Recurrent Neural Networks

In this section, we outline how to integrate traveling wave dynamics into a simple recurrent neural network architecture and provide preliminary analysis of the emergent waves.

### Simple Recurrent Neural Networks

In order to reduce potential confounders in our analysis of the impact of waves on memory, we strive to study the simplest possible architecture which exhibits traveling waves in its hidden state. To accomplish this, we start with the simple recurrent neural network (sRNN) defined as follows. For an input sequence {xₜ}ᵀₜ₌₀ with xₜ ∈ ℝᵈ, and hidden state h₀ = 0 & hₜ ∈ ℝᴺ, an sRNN is defined with the following recurrence: 

hₜ₊₁ = σ(Uhₜ + Vxₜ + b)

where the input encoder and recurrent connections are both linear, i.e. V ∈ ℝᴺˣᵈ and U ∈ ℝᴺˣᴺ, where N is the hidden state dimensionality and σ is a nonlinearity. The output of the network is then given by another linear map of the final hidden state: y = Whᵀ, with W ∈ ℝᵒˣᴺ.

### Wave-Recurrent Neural Networks

To integrate wave dynamics into the sRNN, we start with the simplest equation which encapsulates our goal, the one-dimensional one-way wave equation:

∂h(x, t)/∂t = ν ∂h(x, t)/∂x    (1)

Where t is our time coordinate, x defines the continuous spatial coordinate of our hidden state, and ν is the wave velocity. We can see that if we discretize this equation over space and time, with timestep Δt, defining h(x, t) = hₓₜ as the activation of the x'th neuron at timestep t, this is equivalent to multiplication of the hidden state vector with the following circulant matrix:

hₜ₊₁ = Σhₜ where Σ is a circulant shift matrix    (2)

where ν' = νΔt. A common linear operator which has a similar circulant structure to Σ is convolution. Specifically, assuming a single channel length 3 convolutional kernel u = [0, 1 − ν, ν], we see the following equivalence: u ⋆ hₜ₋₁ = Σhₜ₋₁, where ⋆ defines circular convolution over the hidden state dimensions N. Intuitively this can be thought of as a ring of neurons with shared recurrent local connectivity. We therefore propose to define the Wave-RNN (wRNN) with the following recurrence:

hₜ₊₁ = σ(u ⋆ hₜ + Vxₜ + b)    (3)

In practice we find that increasing the number of channels helps the model to learn significantly faster and reach lower error. To do this, we define u ∈ ℝᶜˣᶜˣᶠ where c is the number of channels, and f is the kernel size, and we reshape the hidden state from a single N dimensional circle to c separate n = ⌊N/c⌋ dimensional circular channels (e.g. h ∈ ℝᶜˣⁿ). For the activation σ, we follow recent work which finds that linear and rectified linear activations have theoretical and empirical benefits for long-sequence modeling (Le et al., 2015; Orvieto et al., 2023). Finally, similar to the prior work with recurrent neural networks (Gu et al., 2022), we find careful initialization can be crucial for the model to converge more quickly and reach lower final error. Specifically, we initialize the convolution kernel such that the matrix form of the convolution is exactly that of the shift matrix Σ for each channel separately, with ν = 1. Furthermore, we find that initializing the matrix V to be all zero except for a single identity mapping from the input to a single hidden unit to further drastically improve training speed. Intuitively, these initializations combined can be seen to support a separate traveling wave of activity in each channel, driven by the input at a single source location. Pseudocode detailing these initializations can be found in Appendix B, and an ablation study can be found in Table 4.

### Baselines

In order to isolate the effect of traveling waves on model performance, we desire to pick baseline models which are as similar to the Wave-RNN as possible while not exhibiting traveling waves in their hidden state. To accomplish this, we rely on the Identity Recurrent Neural Network (iRNN) of Le et al. (2015). This model is nearly identical to the Wave-RNN, constructed as a simple RNN with σ = ReLU, but uses an identity initialization for U. Due to this initialization, the iRNN can be seen to be nearly analogous to the 'bump system' described in Figure 1, where activity does not propagate between neurons but rather stays as a static/decaying 'bump'. Despite its simplicity the iRNN is found to be comparable to LSTM networks on standard benchmarks, and thus represents the ideal highly capable simple recurrent neural network which is comparable to the Wave-RNN. We note that, as in the original work, we allow all parameters of the matrix U to be optimized.

### Visualization of Traveling Waves

Before we study the memory capabilities of the wRNN, we first demonstrate that the model does indeed produce traveling waves within its hidden state. To do this, in Figure 2, for the best performing (wRNN & iRNN) models on the Sequential MNIST task of the proceeding section, we plot in the top row the activations of our neurons (vertical axis) over time (horizontal axis) as the RNNs process a sequence of inputs (MNIST pixels). As can be seen, there are distinct diagonal bands of activation for the Wave-RNN (left), corresponding to waves of activity propagating between hidden neurons over time. For the baseline simple RNN (iRNN) right, despite sorting the hidden state neurons by 'onset time' of maximum activation to uncover any potential traveling wave activity, we see no such bands exist, but instead stationary bumps of activity exist for a duration of time and then fade. In the bottom row, following the analysis techniques of Davis et al. (2021), we plot the corresponding 2D Fourier transform of the above activation time series. In this plot, the vertical axis corresponds to spatial frequencies while the horizontal axis corresponds to temporal frequencies. In such a 2D frequency space, a constant speed traveling wave (or general moving object (Mahmoud et al., 1988)) will appear as a linear correlation between space and time frequencies where the slope corresponds to the speed. Indeed, for the Wave-RNN, we see a strong band of energy along the diagonal corresponding to our traveling waves with velocity ≈ 1 unit/timestep; as expected, for the iRNN we see no such diagonal band in frequency space. In Appendix C Figure 10 we show additional visualizations of waves propagating at multiple different speeds simultaneously within the same network, demonstrating flexibility of learned wave dynamics. Further, in Appendix C Figure 18, we show how the wave dynamics change through training for a variety of different initializations and architectures. We see that even in wRNN models with random recurrent kernel u initializations, although waves are not present at initialization, they are learned through training in the service of sequence modeling, indicating they are a valuable solution for memory tasks.

**Figure 2:** Visualization of hidden state (left) and associated 2D Fourier transform (right) for a wRNN (top) and iRNN (bottom) after training on the sMNIST task. We see the wRNN exhibits a clear flow of activity across the hidden state (diagonal bands) while the iRNN does not. Similarly, from the 2D space-time fourier transform, we see the wRNN exhibits significantly higher power along the diagonal corresponding to the wave propagation velocity of 1 unit/step (Mahmoud et al., 1988).

## 3. Experiments

In this section we aim to leverage the model introduced in Section 2 to test the computational hypothesis that traveling waves may serve as a mechanism to encode the recent past in a wave-field short-term memory. To do this, we first leverage a suite of frequently used synthetic memory tasks designed to precisely measure the ability of sequence models to store information and learn dependencies over variable length timescales. Following this, we use a suite of standard sequence modeling benchmarks to measure if the demonstrated short-term memory benefits of wRNNs persist in a more complex regime. For each task we perform a grid search over learning rates, learning rate schedules, and gradient clip magnitudes, presenting the best performing models from each category on a held-out validation set in the figures and tables. In Appendix B we include the full ranges of each grid search as well as exact hyperparameters for the best performing models in each category.

### Copy Task

As a first analysis of the impact of traveling waves on memory encoding, we measure the performance of the wRNN on the standard 'copy task', as frequently employed in prior work (Graves et al., 2014; Arjovsky et al., 2016; Gu et al., 2020b). The task is constructed of sequences of categorical inputs of length T + 20 where the first 10 elements are randomly chosen one-hot vectors representing a category in {1, . . . 8}. The following T tokens are set to category 0, and form the time duration where the network must hold the information in memory. The next token is set to 9, representing a delimiter, signaling the RNN to begin reproducing the stored memory as output, and the final 9 tokens are again set to category 0. The target for this task is another categorical sequence of length T + 20 with all elements set to category 0 except for the last 10 elements containing the initial random sequence of the input to be reproduced. At a high level, this task tests the ability for a network to encode categorical information and maintain it in memory for T timesteps before eventually reproducing it. Given the hypothesis that traveling waves may serve to encode information in an effective 'register', we hypothesize that wave-RNNs should perform significantly better on this task than the standard RNN. For each sequence length we compare wRNNs with 100 hidden units per channel and 6 channels (n = 100, c = 6) with two baselines: iRNNs of comparable parameter counts (n = 100 ⇒ 12k params.), and iRNNs with comparable numbers of activations/neurons (n = 625) but a significantly greater parameter count (⇒ 403k params.). In Figure 3, we show the performance of the best iRNNs and wRNNs, obtained from our grid search, for T = {0, 30, 80}. We see that the wRNNs achieve more than 5 orders of magnitude lower loss and learn exponentially faster for all sequence lengths. Furthermore, we see that the iRNN with (n = 625) still fails to perform even close to the wRNN despite having an equivalent number of activations and nearly 40 times more parameters. From the visualization of the model outputs in Figure 4, we see that the iRNN has trouble holding items in memory for longer than 10 timesteps, while the comparable wRNN has no problem copying data for up to 500 timesteps. Ultimately, this experiment demonstrates exactly the distinction between traveling wave and static systems illustrated in Figure 1 – the iRNN (static) system is unable to accurately maintain the relative order of sequence elements that have the same input encoding, while the wRNN wave field has no problem encoding both timing and position, facilitating decoding.

**Figure 3:** Copy task with lengths T={0, 30, 80}. wRNNs achieve > 5 orders of magnitude lower loss than iRNNs with approximately equal number of parameters (n = 100) and activations (n = 625).

**Figure 4:** Examples from the copy task for wRNN (n=100, c=6) and iRNN (n=625). We see the iRNN loses significant accuracy after T=10 while the wRNN remains perfect at T=480 (MSE ≈ 10⁻⁹).

### Adding Task

To bolster our findings from the copy task, we employ the long-sequence addition task originally introduced by Hochreiter & Schmidhuber (1997). The task consists of a two dimensional input sequence of length T, where the first dimension is a random sample from U([0, 1]), and the second dimension contains only two non-zero elements (set to 1) in the first and second halves of the sequence respectively. The target is the sum of the two elements in the first dimension which correspond to the non-zero indicators in the second dimension. Similar to the copy task, this task allows us to vary the sequence length and measure the limits of each model's ability. The original iRNN paper (Le et al., 2015) demonstrated that standard RNNs without identity initialization struggle to solve sequences with T > 150, while the iRNN is able to perform equally as well as an LSTM, but begins to struggle with sequences of length greater than 400 (a result which we reconfirm here). In our experiments depicted in Figure 5 and Table 1, we find that the wRNN not only solves the task much more quickly than the iRNN, but it is also able solve significantly longer sequences than the iRNN (up to 1000 steps). In these experiments we use an iRNN with n = 100 hidden units (10.3k parameters) and a wRNN with n = 100 hidden units and c = 27 channels (10.29k parameters).

**Figure 5:** wRNN and iRNN Training curves on the addition task for three different sequence lengths (100, 400, 1000). We see that the wRNN converges significantly faster than the iRNN on all lengths, achieves lower error, and can solve tasks which are significantly longer.

**Table 1:** Long sequence addition task for different sequence lengths. The wRNN finds the task solution (defined as MSE ≤ 5 × 10⁻²) multiple orders of magnitude quicker and is able to solve much longer tasks than the iRNN. The × indicates the model never solved the task after 60k iterations.

| Seq. Length (T) | 100 | 200 | 400 | 700 | 1000 |
|-----------------|-----|-----|-----|-----|------|
| iRNN Test MSE | 1 × 10⁻⁵ | 4 × 10⁻⁵ | 1 × 10⁻⁴ | 0.16 | 0.16 |
| Solved Iter | 14k | 22k | 30k | × | × |
| wRNN Test MSE | 4 × 10⁻⁶ | 2 × 10⁻⁵ | 4 × 10⁻⁵ | 8 × 10⁻⁵ | 6 × 10⁻⁵ |
| Solved Iter. | 300 | 1k | 1k | 3k | 2k |

### Sequential Image Classification

Given the dramatic benefits that traveling waves appear to afford in the synthetic memory-specific tasks, in this section we additionally strive to measure if waves will have any similar benefits for more complex sequence tasks relevant to the machine learning community. One common task for evaluating sequence models is sequential pixel-by-pixel image classification. In this work we specifically experiment with three sequential image tasks: sequential MNIST (sMNIST), permuted sequential MNIST (psMNIST), and noisy sequential CIFAR10 (nsCIFAR10). The MNIST tasks are constructed by feeding the 784 pixels of each image of the MNIST dataset one at a time to the RNN, and attempting to classify the digit from the hidden state after the final timestep. The permuted variant applies a random fixed permutation to the order of the pixels before training, thereby increasing the task difficulty by preventing the model from leveraging statistical correlations between nearby pixels. The nsCIFAR10 task is constructed by feeding each row of the image (32×3 pixels) flattened as vector input to the network at each timestep. This presents a significantly higher input-dimensionality than the MNIST tasks, and additionally contains more complicated sequence dependencies due to the more complex images. To further increase the difficulty of the task, the sequence length is padded from the original length (32), to a length of 1000 with random noise. Therefore, the task of the model is not only to integrate the information from the original 32 sequence elements, but additionally ignore the remaining noise elements. As in the synthetic tasks, we again perform a grid search over learning rates, learning rate schedules, and gradient clip magnitudes. Because of our significant tuning efforts, we find that our baseline iRNN results are significantly higher than those presented in the original work (98.5% vs. 97% on sMNIST, 91% vs. 81% on psMNIST), and additionally sometimes higher than many 'state of the art' methods published after the original iRNN. In the tables below we indicate results from the original work by a citation next to the model name, and lightly shade the rows of our results.

**Figure 6:** sMNIST (left) and psMNIST (right) training curves for the iRNN & wRNN. The wRNN trains much faster and is virtually unaffected by the sequence permutation, while the iRNN suffers.

**Table 2:** sMNIST & psMNIST test accuracy, sorted by psMNIST score. Baseline values from multiple cited sources.

| Model | sMNIST | psMNIST | n / #θ |
|-------|--------|---------|--------|
| uRNN[1] | 95.1 | 91.4 | 512 / 9k |
| iRNN | 98.5 | 92.5 | 256 / 68k |
| LSTM[2] | 98.8 | 92.9 | 256 / 267k |
| GRU[2] | 99.1 | 94.1 | 256 / 201k |
| NWM[8] | 98.6 | 94.8 | 128 / 50k |
| IndRNN (6L)[3] | 99.0 | 96.0 | 128 / 83k |
| Lip. RNN[6] | 99.4 | 96.3 | 128 / 34k |
| coRNN[7] | 99.3 | 96.6 | 128 / 34k |
| LEM[2] | 99.5 | 96.6 | 128 / 68k |
| wRNN (16c) | 97.6 | 96.7 | 256 / 47k |
| URLSTM[4] | 99.2 | 97.6 | 1024 / 4.5M |
| wRNN + MLP | 97.5 | 97.6 | 256 / 420k |
| FlexTCN[5] | 99.6 | 98.6 | - / 375k |

In Table 2, we show our results in comparison with existing work on the sMNIST and psMNIST. Despite the simplicity of our proposed approach, we see that it performs favorably with many carefully crafted RNN and convolutional architectures. We additionally include wRNN + MLP, which is the same as the existing wRNN, but replaces the output map W with a 2-layer MLP. We see this increases performance significantly, suggesting the linear decoder of the basic wRNN may be a performance bottleneck. In Figure 6 (left), we plot the training accuracy of the best performing wRNN compared with the best performing iRNN over training iterations on the sMNIST dataset. We see that while the iRNN reaches a slightly higher final accuracy (+0.9%), the wRNN trains remarkably faster at the beginning of training, taking the iRNN roughly 50 epochs to catch up. On the right of the figure, we plot the models' performance on the permuted variant of the task (psMNIST) and see the performance of the Wave-RNN is virtually unaffected, while the simple RNN baseline suffers dramatically. Intuitively, this performance difference on the permuted task may be seen to come from the fact that by directly encoding the input into the wave-field 'buffer', the wRNN is able to learn to classify sequences invariant of the ordering or permutations of the input (through the fully-connected readout matrix W), while the iRNN has no such buffer and thus struggles to encode sequences with less temporal structure.

**Figure 7:** Num. parameters vs. accuracy for wRNNs & iRNNs on psMNIST.

We note that in addition to faster training and higher accuracy, the wRNN model additionally exhibits substantially greater parameter efficiency than the iRNN due to its convolutional recurrent connections in place of fully connected layers. To exemplify this, in Figure 7 we show the accuracy (y-axis) of a suite of wRNN models plotted as a function of the number of parameters (x-axis). We see that compared with the iRNN, the wRNN reaches near maximal performance with significantly fewer parameters, and retains a performance gap over the iRNN with increased parameter counts.

Finally, to see if the benefits of the wRNN extend to more complicated images, we explore the noisy sequential CIFAR10 task. In Figure 8 we plot the training curves of the best performing models on this dataset, and see that the Wave-RNN still maintains a significant advantage over the iRNN in this setting. In Table 3, we see the performance of the wRNN is ahead of standard gated architectures such as GRUs and LSTMs, but also ahead of more recent complex gated architectures such as the Gated anti-symmetric RNN (Chang et al., 2019). We believe that these results therefore serve as strong evidence in support of the hypothesis that traveling waves may be a valuable inductive bias for encoding the recent past and thereby facilitate long-sequence learning.

**Figure 8:** Training curves on noisy sequential CIFAR10. We again see the wRNN trains faster and reaches higher accuracy than the wave-free model.

**Table 3:** Test set accuracy on the noisy sequential CIFAR dataset sorted by performance. Baseline values from cited sources.

| Model | Acc. | # units / params |
|-------|------|------------------|
| LSTM [1] | 11.6 | 128 / 116k |
| GRU [1] | 43.8 | 128 / 88k |
| anti-sym. RNN [2] | 48.3 | 256 / 36k |
| iRNN | 51.3 | 529 / 336k |
| Incremental RNN [3] | 54.5 | 128 / 12k |
| Gated anti-sym. RNN [2] | 54.7 | 256 / 37k |
| wRNN (16c) | 55.0 | 256 / 435k |
| Lipschits RNN [4] | 57.4 | 128 / 46k |
| coRNN [5] | 59.0 | 128 / 46k |
| LEM [1] | 60.5 | 128 / 116k |

### Ablation Experiments

Finally, we include ablation experiments to validate the architecture choices for the Wave-RNN. For each of the results reported below, we again grid search over learning rates, activation functions, initializations, and gradient clipping values. In Table 4, we show the performance of the wRNN on the copy task as we ablate various proposed components such as convolution, u-shift initialization, and V initialization (as described in Section 2). At a high level, we see that the wRNN as proposed performs best, with u-shift initialization having the biggest impact on performance, allowing the model to successfully solve tasks greater than length T = 10. In addition to ablating the wRNN, we additionally explore initializing the iRNN with a shift initialization (U = Σ) and sparse identity initialization for V to disassociate these effects from the effect of the convolution operation. We see that the addition of Σ initialization to the iRNN improves its performance dramatically, but it never reaches the same level of performance of the wRNN – indicating that the sparsity and tied weights of the convolution operation are critical to memory storage and retrieval on this task.

**Table 4:** Ablation test results (MSE) on the copy task. Best results are bold, second best underlined.

| Model | Sequence Length (T) ||||
|-------|---|---|---|---|
| | 0 | 10 | 30 | 80 |
| wRNN | **9 × 10⁻¹²** | **1 × 10⁻¹⁰** | **8 × 10⁻¹¹** | **1 × 10⁻¹¹** |
| - V-init | 1 × 10⁻¹¹ | 2 × 10⁻¹¹ | 4 × 10⁻¹⁰ | 4 × 10⁻¹¹ |
| - u-shift-init | 5 × 10⁻¹¹ | 3 × 10⁻¹⁰ | 7 × 10⁻⁴ | 6 × 10⁻⁴ |
| - V-init - u-shift-init | 8 × 10⁻¹⁰ | 1 × 10⁻⁴ | 3 × 10⁻⁴ | 7 × 10⁻⁴ |
| iRNN (n=100) | 1 × 10⁻⁴ | 3 × 10⁻³ | 2 × 10⁻³ | 1 × 10⁻³ |
| + Σ-init | <u>1 × 10⁻⁸</u> | <u>1 × 10⁻⁷</u> | <u>2 × 10⁻⁷</u> | <u>2 × 10⁻⁵</u> |
| + Σ-init + V-init | 1 × 10⁻⁷ | 1 × 10⁻⁷ | 1 × 10⁻⁶ | 8 × 10⁻⁶ |

## 4. Discussion

In this work we have discussed theories from neuroscience relating traveling waves to working memory, and have provided one of the first points of computational evidence in support of these theories through experiments with our Wave-RNN – a novel minimal recurrent neural network capable of exhibiting traveling waves in its hidden state. In the discussion below we include a brief summary of related work, limitations, and future work, with an extended survey of related work in Appendix A.

### Related Work

As mentioned in the introduction, most related to this work in practice, Keller & Welling (2023) showed that an RNN parameterized as a network of locally coupled oscillators (NWM) similarly exhibits traveling waves in its hidden state, and that these waves served as a bias towards learning structured representations. This present paper can be seen as a reduction of the Keller & Welling (2023) model to its essential elements, allowing for a controlled study of hypotheses relating traveling waves and memory. Additionally, we see in practice that this reduction sometimes improves performance, as on the psMNIST task in Table 2, where the wRNN outperforms the NWM.

Another related line of work proposes to solve long-sequence memory tasks by taking inspiration for biological 'time-cells' (Jacques et al., 2021; 2022). The authors use temporal convolution with a set of exponentially scaled fixed kernels to extract a set of time-scale-invariant features at each layer. Compared with the wRNN, the primary conceptual difference is the logarithmic scaling of time features which is purported to increase efficiency for extremely long time dependencies. As we demonstrate in Appendix Fig. 10, however, the wRNN is also capable of learning waves of multiple speeds, and therefore with proper initialization may also exhibit a logarithmic scaling of time-scales.

Similar in results to our work, Chen et al. (2022) demonstrated that in a predictive RNN autoencoder learning sequences, Toeplitz connectivity emerges spontaneously, replicating multiple canonical neuroscientific measurements such as one-shot learning and place cell phase precession. Our results in Figure 18 further support these findings that with proper training and connectivity constraints, recurrent neural networks can learn to exhibit traveling wave activity in service of solving a task.

Finally, we note that the long-sequence modeling goal of this work can be seen as similar to that of the recently popularized Structured State Space Models (S4, HIPPO, LSSL) (Gu et al., 2022; 2020a; 2021a). In practice the recurrent connectivity matrix of the wRNN is quite different than the HiPPO initialization pioneered by these works, however we do believe that linear recurrence may be an equivalently useful property for wRNNs. Importantly, however, the H3 mechanism of Fu et al. (2023) does indeed include a 'shift SSM' with a toeplitz structure very similar to that of the wRNN. However, this shift initialization was subsequently dropped in following works such as Hyena and Mamba (Poli et al., 2023; Gu & Dao, 2023). In future work we intend to explore this middle ground between the wRNN and state space models as we find it to likely be fruitful.

### Limitations & Future Work

The experiments and results in this paper are limited by the relatively small scale of the models studied. For example, nearly all models in this work rely on linear encoders and decoders, and consist of a single RNN layer. Compared with state of the art models (such as S4) consisting of more complex deep RNNs with skip connections and regularization, our work is therefore potentially leaving significant performance on the table. However, as described above, beginning with small scale experiments on standard architectures yields alternative benefits including more accurate hyperparameter tuning (due to a smaller search space) and potentially greater generality of conclusions. As the primary goal of this paper was to demonstrate the computational advantage of traveling waves over wave-free counterparts on memory tasks, the tradeoff for small scale was both necessary and beneficial. In future work, we plan to test the full implications of our results for the machine learning community and integrate the core concepts from the wRNN into more modern sequence learning algorithms, such as those used for language modeling.

We note that the parameter count for the wRNN on the CIFAR10 task is significantly higher than the other models listed in the table. This is primarily due to the linear encoder mapping from the high dimensionality of the input (96) to the large hidden state. In fact, for this model, the encoder V alone accounts for > 90% of the parameters of the full model (393k/435k). If one were to replace this encoder with a more parameter efficient encoder, such as a convolutional neural network or a sparse matrix (inspired by the initialization for V), the model would thus have significantly fewer parameters, making it again comparable to state of the art. We leave this addition to future work, but believe it to be one of the most promising approaches to improving the wRNN's general competitiveness.

Finally, we believe this work opens the door for significant future work in the domains of theoretical and computational neuroscience. For example, direct comparison of the wave properties of our model with neurological recordings (such as those from (King & Wyart, 2021)) may provide novel insights into the mechanisms and role of traveling waves in the brain, analogous to how comparison of visual stream recordings with convolutional neural network activations has yielded insights into the biological visual system (Cadieu et al., 2014).

## Acknowledgments and Disclosure of Funding

We would like to thank the creators of Weight & Biases (Biewald, 2020) and PyTorch (Paszke et al., 2019). Without these tools our work would not have been possible. We thank the Bosch Center for Artificial Intelligence for funding T. Anderson Keller for the initial stages of this project, and The Kempner Institute for funding him through the final stages of the project.

## References

[The paper contains 59 references which I can include if needed - they span from Arjovsky et al. (2016) to Zanos et al. (2015)]

## Appendices

The paper includes extensive appendices (A through C) containing:
- **Appendix A:** Related Work
- **Appendix B:** Experiment Details (including pseudocode, hyperparameters, and grid search specifications)
- **Appendix C:** Additional Results (including performance means & standard deviations, multiple visualizations, and ablation studies)

---
