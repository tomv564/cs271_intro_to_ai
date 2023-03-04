### Categories of variables

Not input/output

Evidence -> hidden -> query variables
Bayes nets can be reversed in any direction
Anything can become evidence/query/hidden.

### Enumeration

Going through all possibilities and adding them up

Given: 
B (burglary) and E (earthquake)
Cause:
A (alarm) to go off
Causes:
J (john) and M (mary) to call.

Possibility there was a burglary given john and mary called:

Convert to unconditional probability:

```
P(+b|+j,+m)
= P(+b,+j,+m) / P(+j,+m)

```

Sum on all occurances of dependent variables:

`SumE(SumA(P(+b,+j,+m,e,a))`

Rewrite expression as product of all variables in Bayes net:

`f(e,a) = SumE{ SumA{ P(+b)* P(e)* (P(a|+b,e) * P(+j|a) * P(+m|a) } }`

Then the result can be calculated as a sum of four combinations:

`f(+e,+a) + f(+e, ^a) + f(^e, +a) + f(^e,^a)`

Look up the result of each in the probability tables, fill in, add up, then divide by similarly expanded P(+j,+m) to normalize

### Pulling out terms

P(+b) always the same:

```
SumE{ SumA{ P(+b)* P(e)* (P(a|+b,e) * P(+j|a) * P(+m|a)
= P(+b) * SumE{ SumA{ P(e)* (P(a|+b,e) * P(+j|a) * P(+m|
```

P(e) doesn't depend on a
```
= P(+b) * SumE{ P(e) * SumA{ (P(a|+b,e) * P(+j|a) * P(+m|
```

Less columns to repeatedly compute, but still many rows in table.

### Maximize Independence

When setting up dependencies from effect to cause (from John and Mary to Earthquake and Burglary), more dependencies arise.

Bayes networks are most compact when variables are listed from cause to effect.

### Variable elimination

Example:

R (raining) -> T (traffic) -> L (late for appointment)

Will I be late?

```
P(+l) = SumR { SumT { P(r) * P(t|r) * P(+l|t)
```

1. Joining factors

Combine T and R by multiplying their probabilities in the table
P(r,t)

2. Elimination (summing out / marginalization)

Convert P(r,t) to just P(t) by summing all the +t and ^t rows.

3. Join the other tables by multiplying again

Gives a single node network with table P(T,L) 

### Approximate Inference: Sampling

Example: tallying Heads/Tails outcomes of two different coins

Less work to compute, gets accurate with large enough sample size.

Start at the cause, generate random outcome

Apply random values and look up outcome on hidden values

Occurrance of query value in sample size (if large enough) becomes true probability.

#### Conditional probability

Network: Cloudy causes Sprinkler and Rain cause WetGrass

Reject samples that don't match the conditional probability

eg. P(w|-c), remove all +c samples.

this is called **rejection sampling**

But this ends up rejecting a lot of samples.

#### Likelihood weighting

Fix the evidence variables (eg R must be positive) 
The resulting set is inconsistent.
Fixable by assigning probability to each sample:

eg. `P(R|+S, +W)`

A sample for (+c,+s,+r,+w) would have a weight of 
0.1 (from Sprinkler table) * 0.99 ( from Rain table) = 0.099

This makes the sampling also consistent.

BUT: If random sampling is used for a cause variable (eg c) when the dependent variables are also controlled, some of its values will be inconsistent with the dependent outcomes.

#### Gibbs Sampling

Markov chain monte carlo (MCMC)

Resample one variable at a time conditioning on all others.

+c +s -r -w
+c -s -r -w
+c -s +r -w


