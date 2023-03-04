### Complementary probability 

if event has probability P, then complementary event has probability `1-P`

### Independence

If X independent from Y, then to calculate the **joint probability**  of both **marginals**:

`P(X,Y) = P(X) * P(Y)`

### Multiple dependent variables

Heads/Tails, second coin loaded

```
P(X1=T) = 0.5
P(X2=H|X1=H) = 0.9
P(X2=T|X1=T) = 0.8
```
What is probability that second coin is Heads?

To gather all the cases when X2 is H, we need to invert the second condition: `P(X2=H|X1=T) = 1 - 0.8 = 0.2`

Then we can add all the X2=H outcomes:
```
P(X2=H) 
= P(X2=H|X1=H)*P(X1=H) + P(X2=H|X1=T)*P(X1=T)
= 0.9 * 0.5 + 0.2 * 0.5
= 0.55

```

### Total probability

`P(Y) = sum of all i over (P(Y|X=i) * P(X=i)`

Combined with complementary probability:

`P(^X|Y) = 1 - P(X|Y)`


### Calculating inverse probability

Probability of having cancer:

`P(C) = 0.01` => `P(^C) = 0.99`

Probabilities of positive test results:

`P(+|C) = 0.9` => `P(-|C) = 0.1`

`P(+|^C) = 0.2` => `P(-|^C) = 0.8`

Given these, calculate Joint Probabilities:

```
P(+,C) = 0.009
P(-,C) = 0.001
P(+,^C) = 0.2 * 0.99 = 0.198
P(-,^C) = 0.8 * 0.99 = 0.792 
```

Then we can determine likelihood of having cancer based on test results. Basically: outcome of condition we're interested in over sum of all probabilities for that outcome:

```
P(C|+) 
= P(+,C) / ( P(+,C) + P(-,C) ) 
= 0.009  / ( 0.009 + 0.198 )
```


### Bayes Rule

A causes B
But we are often not interested in P(B|A).
Given that we measured B, we want to know the probability of A **(diagnostic reasoning)**

Posterior: `P(A|B)`

is equal to ( likelihood * prior ) / marginal likelihood:

```
( P(B|A) * P(A) ) / P(B)
```

But we often don't have P(B), so we expand using total probability

```
P(B) = sum of all i  over P(B|A=i) * P(A=i)
```

Cancer example:

```
P(C|+) 
= ( likelihood * prior ) / marginal likelihood
= ( P(+|C) * P(C) ) / P(+|C)*P(C) + P(+|^C)*P(^C)
= ( 0.9 * 0.01 ) /  ( 0.9*0.01 + 0.2*0.99)
```

Condensing this:

Because `P(A|B) + P(^A|B) = 1`

We can calculate a pseudo probability for both:

```
P'(A|B) = P(B|A)*P(A)
P'(^A|B) = P(B|^A)*P(^A)
```
And a normalizer n:

` n = 1 / ( P'(A|B) + P'(^A|B) ) `

Allowing us to calculate P(A|B) without knowing P(B):

`P(A|B) = n * P'(A|B)`


### Confounding Cause

A causes B and C

B and C are fully independent:

```
P(B|C) = P(B)
P(C|B) = P(C)
```


Example: Probability I am happy given a raise or that it's sunny

```
P(S) = 0.7
P(R) = 0.01
```

```
P(H|S,R) = 1
P(H|^S,R) = 0.9
P(H|S,^R) = 0.7
P(H|^S,^R) = 0.1
```

`P(R|S) = 0.01`  because of conditional independence


### Explaining Away

Knowing R means we discredit S: if we know you got a raise, we don't think it's because it is sunny.

### D-Seperation

Knowledge of a node between two nodes renders the nodes independent.
Except when two nodes are causes to a single outcome, then knowledge of the outcome renders them dependent (see Explaining Away)!

