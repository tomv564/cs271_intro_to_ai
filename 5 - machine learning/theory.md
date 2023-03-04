### Overview

**What?**

Parameters, structure, hidden concept

**What From?**

Supervised or unsupervised learning, reinforcement learning

**What for?**

Prediction, diagnostics, summarization

**How?**

Passive (observer), active (participant), online, offline (after data generation)

**Outputs?**

Classification regression

**Details**

Generative vs discriminative 

### Supervised Learning

feature vector => target label

x1 x2 x3 xn -> Y 

(factors) -> (will person default?)
x21 .. x2n -> Y2
xm1 .. xmn -> Ym

until f(Xm) = Ym

#### Occams Razor

Choose least complex hypothesis.

Fit <-----> Complexity

Factor of training data error and overfitting error - there is a balance.

#### Spam Filtering

Human input: the spam/not spam buttons

Bag of words: word & usage count

Maximum likelihood that a message is spam

From sample SSSHHHHH (3 spam / 8 total messages)= ...

P(S) = pi

Getting best fit value for sample:

P(Yi) = pi if yi = S | 1-pi if yi = H

Rewrite as 11100000

P(Yi) = pi^yi * (1-pi)^(1-yi)

P(data)  is product of all instances i:

pi ^ count(yi=1) * (1 - pi) ^ count(yi = 0)

      (3)                       (5)
      
mathmathmath: answer is 3/8.

Conclusion: using enumeration is an accurate estimation of Maximum Likelihood.

#### Relation to Bayes Network

words w1, w2, w3, w4 cause SPAM

using a dictionary of 12 words, how many parameters?
P(SPAM) = 1
P(w1-11|SPAM) = 11
P(w1-11|^SPAM) = 11

= 23 parameters

given "secret" how to calculate probability is spam?

Use Bayes rule

```
P(SPAM|M) = P(M|SPAM)P(SPAM) / (P(M|SPAM)P(SPAM) + P(M|HAM)P(HAM)
= 1/9 * 3/8 / ( ( 1/9 * 3/8 ) + (1/15 * 5/8) )
```

What if word is not in SPAM list?
probability drops to 0 - overfitting.

#### Laplace Smoothing

Replace ML with:

count(x) / N

add k to count, then normalize for this K

`LS(k) p(x) = count(x) + k / ( N + k|x| )`

|x| is the number of values that the variable x can take on.

k is a smoothing parameter.

And N is the total number of occurrences of x (the variable, not the value) in the sample size.

Using laplace smoother:

P(spam) = (3+1) / (8+2) = 2/5
P(ham) = (5+1) / (8+2) = 3/5

on "Today"

P("today"|SPAM) = (0+1) / (9+12) = 1/21 // 12 words in the dictionary
P("today"|HAM) = (2+1) / (15+12) = 3/27 = 1/9 

#### Summary

Naive Bayes rule, bag of words, laplace smoother

#### Digit Recognition

Mapping pixels as inputs is inaccurate as shifted images appear fundamentally different.

Input smoothing (convolver, gaussian) takes neighbouring pixels into account.

#### Overfitting prevention

Occam's Razor - tradeoff between simplicity and smooth
Selecting k for laplace is one example


#### Cross validation

Divide training data into Train, Crossvalidate, Test
80%, 10%, 10%
Train - find parameters
CV - find k, repeat Train
Test - validate model

Don't want test data to become part of training data because you risk overfitting to the test data.

### Supervised Learning

We have used classification so far with Bayes nets
Regression is useful for prediction (which Bayes nets cannot do)


#### Linear Regression

data:

X11 ... X1n -> y1
...
Xm1 ... Xmn -> ym


Given a linear function f(x) = ax + b, find  a and b

#### Loss minimalization

Loss function l(x) = sum all ( yj - f(xj) ) ^ 2



