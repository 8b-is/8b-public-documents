# Advanced_Prompt_Engineering_Methods_and

Converted from: Advanced_Prompt_Engineering_Methods_and.pdf
Date: 2025-08-19

---

Advanced Prompt Engineering Methods
and Techniques for Language Models
By Sebastian Schepis

Table of Contents:
Table of Contents:
Abstract:
1. Introduction
1.1 Background
1.2 Aim of the study
2. Methods and Techniques
2.1 Pseudocode-like syntax
2.2 Recursive prompts
2.3 Multi-entrant prompts
2.4 Prompts splitting the LLM's output input into multiple parts
2.5 Temperature parameter
2.6 Top_p parameter
3. Details and Discussion
3.1 Pseudocode-like syntax
3.2 Recursive prompts
3.3 Multi-entrant prompts
3.4 Prompts splitting the LLM's output input into multiple parts
3.5 Temperature parameter
3.6 Top_p parameter
4. Conclusion

2
2
2
2
2
2
3
3
3
3
3
3
4
4
4
5
6
6
7
7

Abstract:
Prompt engineering is an important aspect of utilizing language models to generate coherent
and contextually relevant text. This paper aims to provide an in-depth analysis of various
methods and techniques in prompt engineering, including the use of pseudocode-like syntax,
recursive prompts, multi-entrant prompts, and controlling the diversity of generated text using
temperature and top_p parameters. These techniques help users achieve consistent, coherent,
and diverse results when working with language models such as ChatGPT.

1. Introduction
1.1 Background
Language models have become an essential component of many natural language processing
applications. As their performance improves, so does the need for effective methods to generate
text that is both contextually relevant and coherent. This paper will explore various approaches
and techniques in prompt engineering, aiming to help users apply and improve these models in
various applications.

1.2 Aim of the study
This study aims to provide methods and techniques for effective prompt engineering when using
language models, focusing on achieving desired outcomes, improving efficiency, and effectively
controlling the output of the generated text.

2. Methods and Techniques
2.1 Pseudocode-like syntax
Using pseudocode-like syntax for deterministic tasks helps users avoid the need to use the
temperature parameter and makes the prompts more interpretable. This technique allows for a
more controlled outcome and reduces randomness in the generated text.

2.2 Recursive prompts
Recursive prompts generate text that is more coherent and consistent with the context of the
prompt. By looping through the generated text and considering its context during each iteration,
the model can provide a more in-depth and relevant response based on the input.

2.3 Multi-entrant prompts
Multi-entrant prompts enable the generation of text with output types that vary based on the
input type, allowing for a single prompt to generate multiple types of output. This technique
helps improve the efficiency of language model usage and enables more diverse results.

2.4 Prompts splitting the LLM's output input into multiple parts
Utilizing prompts that split the language model's output input into multiple parts allows the
generation of text that encompasses multiple perspectives on the same topic. This technique
yields a more complete and holistic understanding of the subject matter.

2.5 Temperature parameter
The temperature parameter controls the randomness of the generated text. Adjusting this
parameter affects the coherency and diversity of the text produced. A value between 0.8 and 1.1
is recommended for effective prompt engineering.

2.6 Top_p parameter
The top_p parameter influences the diversity of the generated text by controlling the selection of
more or less probable tokens. A value between 0.9 and 0.95 is suggested for achieving a
balance between coherence and diversity in generated text.

3. Details and Discussion
3.1 Pseudocode-like syntax
The use of pseudocode-like syntax allows users to more precisely communicate their intentions,
leading to more accurate generated text. This section will discuss the implementation and
impact of this approach while addressing strengths and limitations.
Let us examine a somewhat complex prompt, below, we render the same prompt in
natural-language and then re-render the prompt using a pseudocode-like format:
Natural language:
"Take the current input and and decompose it into a series of implementation tasks"
Pseudocode-like:
"decompose(input) -> implementation tasks"
Both of the prompts above are equivalent - but the second prompt takes less characters to
render and is just as precise and unambiguous as the first. As a bonus - because the prompt is
pseudocode, the AI model is already primed to generate formatted output.

3.2 Recursive prompts
This section will explore the application of recursive prompts, discussing their ability to maintain
coherence and consistency within generated text. Recursive prompts refer to the technique of
using the model's previous response as an input for generating the next response. By doing so,
the model takes context from its previous outputs, improving coherence and consistency.
Recursive prompts can be especially helpful when generating a list, explanation, or step-by-step
process.
Example:
Consider a situation where we want the model to generate a list of steps to bake a cake. The
initial prompt might look like this:
"Step 1 to bake a cake:"
The model's output might be:
"Preheat the oven to 350°F (180°C)."
Then, we use the model's output as part of the next prompt:
"Step 1 to bake a cake: Preheat the oven to 350°F (180°C).
Step 2:"
By doing this, we provide context for the model to generate the next step:
"Step 1 to bake a cake: Preheat the oven to 350°F (180°C).
Step 2: Grease and flour a cake pan."
This process can be continued to generate more steps while maintaining context and
coherence.

3.3 Multi-entrant prompts
Multi-entrant prompts are designed to generate different output types based on the input type
provided. This technique allows for greater flexibility and can be applied to a wide range of tasks
and use-cases.
Example:
Consider a prompt that asks the model to describe an animal based on a given input. We want
the model to generate a general description when provided with the animal's name and a more
detailed description when provided with a specific attribute.
Multi-entrant prompt:
"Describe {[Animal_Name: 'lion'], [Attribute: 'hunting abilities']}"
Output 1:
"Lions are large felines with a tawny coat and an impressive mane in adult males. They live in
groups called prides and are found in parts of Africa and India."
Output 2:
"A lion's hunting abilities are impressive as they rely on teamwork and communication. Working
together with the pride allows them to bring down large prey effectively, employing strategies
like flanking and ambushing."

3.4 Prompts splitting the LLM's output input into multiple parts
Prompts that split the language model's output input into multiple parts enable users to generate
text reflecting various perspectives on a single topic. This technique can be useful in developing
a well-rounded understanding of the subject or to compare different approaches.
Example:
Consider a scenario where we want the model to generate arguments both for and against a
topic, such as adopting a plant-based diet.
Initial prompt:
"Advantages and disadvantages of adopting a plant-based diet:
1. Advantages:
2. Disadvantages:"
Expected output:
"Advantages and disadvantages of adopting a plant-based diet:
1. Advantages:
- Improved health and lowered risk of chronic diseases
- Environmental sustainability
- Ethical treatment of animals
2. Disadvantages:
- Potential nutrient deficiencies
- Limited food options and social challenges
- Increased reliance on supplements"
This prompt type allows users to better understand and consider different perspectives on the
issue at hand.

3.5 Temperature parameter
The temperature parameter is crucial in controlling the randomness of the generated text.
Higher values (e.g., 1-1.1) will result in more creative and diverse text, while lower values (e.g.,
0-0.8) yield more focused and coherent text. Users should experiment with the temperature
parameter to achieve the desired balance of creativity and coherence in their prompts.

3.6 Top_p parameter
The top_p parameter helps control the diversity and coherence of the generated text by
selecting tokens based on probability. By using a top_p value between 0.9 and 0.95, users can
strike a balance between too much diversity (which might lead to incoherence) and too little
diversity (which might cause repetitive responses).

4. Conclusion
Effective prompt engineering methods and techniques are crucial in leveraging the full potential
of language models like ChatGPT. By understanding and employing methods such as
pseudocode-like syntax, recursive prompts, multi-entrant prompts, and fine-tuning temperature
and top_p parameters, users can achieve consistent, coherent, and diverse output, beneficial
for a wide array of natural language processing applications and tasks.

