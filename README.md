# Checking if images are manipulated using Benford's law

## The discovery and rediscovery of Benford’s law
Simon Newcomb (March 12, 1835 – July 11, 1909) was a Canadian–American astronomer, applied mathematician and autodidactic polymath, who was Professor of Mathematics in the United States Navy and at Johns Hopkins University.

Simon was going through a set of logarithmic books and he saw this weird phenomenon, the first few pages were worn out and the wear decreased as he moved along the pages. Logarithmic books are what people used before the invention of digital calculators and computers, to go through sets of multiplcation to ease up their task. So only first few pages being worn out meant that most of the numbers people were dealing with started with a 1,2,3 and so on. 

Simon thought this would be some weird concidence and so referred to all possible logarithmic books that he could and all of the test proved the same thing, he wrote a paper about this in 1881. His finding were discarded by the scientific community of his time.

Then years later in 1938 a physicist named Frank Benford rediscovered Newcomb's work and referred to them in his paper titled "The Law of Anomalous Numbers", while collecting more proofs that the natural world followed this pattern.

Frank applied this theory on wide variety data sets like - electricity bills, street addresses, stock prices, house prices, population numbers, death rates, lengths of rivers, and physical and mathematical constants. And, they all followed Benford's law.


## What is Benford's law (In Short)
Benford’s law, a.k.a. Newcomb–Benford law, the law of anomalous numbers, or the first digit law, states that the frequency of occurrence of the leading digits in naturally occurring numerical distributions is predictable and nonuniform but more close to a power law distribution. According to this law any given number is 6 times likely to start with 1 than 9. Though this may sound very illogical, and most people would expect a uniform distribution U(1,9), where all have the same (11.1%) probabilty of showing up in the first slot, it so happens to be the rythm of the universe.

## Formula
```Pr(D1=d) = log10(1 + 1/d)```

## What are we going to do?
    1: We are trying to apply Benford's law to images to see if they have been manipulated with or not.
    2: Later we would apply the same law on multiple data-sets
    (This is a purely a `for curiousity` project :) )

## First test - Check images for manipulation
Here's the result of the first test
Manipulated image graph - example 1 (img_manipulated_ex1.jpg)
![Manipulated image graph](https://raw.githubusercontent.com/rohitnairtech/benfords_law/master/ex1.png)

Unmanipulated image graph - example 2 (img_original_ex2.jpg)
![Unmanipulated image graph](https://raw.githubusercontent.com/rohitnairtech/benfords_law/master/ex2.png)