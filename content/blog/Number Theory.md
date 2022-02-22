+++
title = "Number Theory"
date = "2021-09-17"
author = "Gautam, Anirudha"
description = ""
weight = 6
+++

## GCD and LCM

GCD of say _n_ numbers is the greatest number which divides each of the _n_ numbers. LCM of _n_ numbers is the smallest number that can be divided by each of the _n_ numbers. These definitions are well known to most of the readers. It is also quite obvious to see that
$$
\begin{align}
gcd(a_1, a_2, \ldots, a_n) &= gcd(gcd(a_1, a_2), a_3, \ldots, a_n) \\\\
gcd(a,b) &= gcd(b,a) \\\\
gcd(0,a) &= a \\\\
\text{lcm}(a,b)\cdot\text{gcd}(a,b) &= ab
\end{align}
$$
So once either one of GCD and LCM is known, calculating the other is not difficult. Turns out that finding the GCD is easier than finding the LCM. But, how do we calculate the GCD of two numbers?

### Task: Find GCD of two numbers $a,b$

#### Approach 1:

Iterate over all positive integers less than $\text{min}(a,b)$​ and find the largest number that divides both $a$ and $b$. So that would take $O(\text{min}(a,b))$​​ time to find the GCD.  However, this is not a _fast_ algorithm.

#### Approach 2 (Euclidean Algorithm):

Suppose we have two positive integers $a$ and $b$ with $a>b$ and the task is to find the GCD. The Euclidean Algorithm is as follows:

1) Divide $a$ by $b$​. You get a quotient $q_1$ and a remainder $r_1$.
$$
a = bq_1 + r_1
$$

2) If $r_1 = 0$​, then we're done. The GCD of $a, b$ is $b$.
3) Else, replace $a$ with $b$ and $b$ with $r_1$​ and go to Step 1.

In other words, you do a series of divisions until you have a zero remainder
$$
\begin{align}
a &= bq_1 + r_1\\\\
b &= r_1q_2 + r_2\\\\
r_1 &= r_2q_3 + r_3\\\\
&\vdots \;\;\;\;\;\; \vdots\\\\
r_{n-2} &= r_{n-1}q_n + r_n\\\\
r_{n-1} &= r_nq_{n+1} 
\end{align}
$$
Then, $r_n$ is the GCD of $a, b$. 

Let's now find the GCD of $4840$ and $1512$ using Euclidean Algorithm.
$$
\begin{align}
4840 &= 1512 \times 3 + 304 \\\\
1512 &= 304 \times 4 + 296\\\\
304 &= 296 \times 1 + 8\\\\
296 &= 8 \times 37
\end{align}
$$
Hence $8$ is the GCD of $4840$ and $1512$.

A sample C++ implementation of the Euclidean algorithm:

```cpp
int gcd(int a, int b)
{
    if(a==0)
        return b;
    if(b==0)
        return a;
    else if(a>=b)
        return gcd(b, a%b);
    else
        return gcd(a, b%a);
}
```

This algorithm works in $O(log(\text{min}(a,b)))$ time and hence, is very fast for computing GCD of large numbers. So now we have a tool to compute the GCD of two numbers. Readers who are not comfortable with implementing your own GCD function can use `__gcd(int a, int b)` (defined in header `<algorithm>`) or `std::gcd(int a, int b)` (defined in header `<numeric>`).

#### Resources

- Check [this link](https://cp-algorithms.com/algebra/euclid-algorithm.html) for a more detailed explanation on how Euclidean Algorithm works and why it runs in $O(log(\text{min}(a,b)))$ time.

- Check out [this link](https://medium.com/i-math/why-does-the-euclidean-algorithm-work-aaf43bd3288e) to have a visual understanding of what Euclidean Algorithm is
- Check [geeksforgeeks](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/) for implementations of Euclidean Algorithm in different languages.

#### Problems

- [GCD and LCM](https://www.codechef.com/problems/FLOW016)
- [Common Divisors](https://codeforces.com/contest/1203/problem/C)
- [Complicated GCD](https://codeforces.com/problemset/problem/664/A)
- [Round Corridor](https://codeforces.com/contest/1200/problem/C)
- [Epic Game](https://codeforces.com/contest/119/problem/A)
- [Enigmath](https://www.spoj.com/problems/ENIGMATH/)

#### Additional Resources

- Check out the [Extended Euclidean Algorithm](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/) (Not really used much in CP) 
  - Go through this [link](https://cp-algorithms.com/algebra/extended-euclid-algorithm.html) to have a better understanding of the Extended Euclidean Algorithm.
  - Check out this [link](https://math.libretexts.org/Courses/Mount_Royal_University/MATH_2150%3A_Higher_Arithmetic/4%3A_Greatest_Common_Divisor_least_common_multiple_and_Euclidean_Algorithm/4.2%3A_Euclidean_algorithm_and__Bezout%27s_algorithm) for more numerical examples.
  - Problems on EEA: [Euclid Problem](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1045), [Border](https://codeforces.com/contest/1011/problem/E).

- Additional Problems on GCD
  - [Mike and gcd problem](https://codeforces.com/contest/798/problem/C)
  - [Vasya's Function](https://codeforces.com/contest/837/problem/E)
  - [Optimal Denomination](https://www.codechef.com/JULY21C/problems/MINNOTES) (Note that GCD can crop up in literally any problem XD)
  - [HUGE GCD](https://www.spoj.com/problems/HG/)
  - (add more here)

## Primes

A prime number (or prime in short) is a positive integer having exactly two factors : $1$ and  itself. Numbers which are not prime are called composite numbers. We don't count $1$ as a prime.

### Task: Check whether a number is a prime

#### Approach 1:

Brute force. Iterate from $i=2$ to $n-1$  and check if $i$ divides $n$. Time Complexity: $O(n)$

#### Approach 2:

If you're smart enough, you'll know that anything more than $n/2$ and less than $n$ cannot divide $n$. So, iterating from $i=2$ to $n/2$ would do good. Even though the number of computations are cut down by half, the time complexity is still $O(n)$.

#### Approach 3:

If $n$ was composite, it would have at least one divisor $d$, with $1 < d \leq \sqrt n$. (Think why. If all the divisors of $n$ were more than $\sqrt n$, then product of two such divisors would be more than $n$) So iterate from $i=2$ to $\sqrt n$ and check if $i$ divides $n$. Time complexity: $O(\sqrt n)$.

Sample implementation:

```c++
bool checkPrime(int n)
{
    if(n==1)
        return false;
    if(n==2||n==3)
        return true;
    for(int i = 2; i*i<=n; i++)
    {
        if(n%i==0)
            return false;
    }
    return true;
}
```

There are also some more primality tests (Fermat's Primality test, Miller-Rabin Primality test, etc), but they are only probabilistic primality tests. For example, Fermat's Primality test would classify the number $561 = 3 \times 5 \times 11$ as a prime number. You can read more about them [here](https://cp-algorithms.com/algebra/primality_tests.html).

So now we have an algorithm to check whether a number is a prime. How about we try to find all primes till $10^8$.

### Task: Find all primes till $n$

#### Approach 1:  {#approach-1}

Iterate from $i=1$ to $n$ and use `checkPrime(i)` function defined above that works in $\sqrt i$ for each iteration. Time complexity of this algorithm is $O(n \sqrt n)$. Not bad. But solving [this problem](https://www.spoj.com/problems/TDPRIMES/) where $n$ can be as high as $10^8$ would take about $2.78$ hours to complete! (Assuming $10^8$ operations are processed every second, this speed might be different for different computers) We need a better algorithm.

#### Approach 2 (Sieve of Eratosthenes){#approach-soe}:

This technique is used by most elementary/middle schoolers to count number of primes less than $100$ (In case, you are hearing this for the first time, watch [this video](https://www.youtube.com/watch?v=klcIklsWzrY) from Khan Academy or [this nice GIF](https://en.wikipedia.org/wiki/File:Sieve_of_Eratosthenes_animation.gif) from wikipedia to understand what SoE is). Basically, in this algorithm, we use the fact that multiples of a number more than $1$ can only be composite numbers. Once we know that $p$ is a prime number, we can "strike off" numbers like $2p, 3p, 4p \ldots$ and skip checking whether they're primes because we know that they're composite. This technique sieves out the primes and hence the name. 

It also turns out that once we know that $p$ is a prime, striking off multiples of $p$ starting from $p^2$ would be enough. This is because all the multiples of $p$ which are less than $p^2$ would have been a multiple of another prime $q < p$, so such multiples would have been already struck off. 

Here's a sample implementation of SoE in C++:

```cpp
int N = 1000000; //N is size of the input, generally millions or greater than that
bool prime[N];
for(int i = 0; i<=N; i++)
	prime[i] = true; //Initialise every number as a prime.

prime[1] = prime[0] = false; //0 and 1 aren't primes. It doesnt really matter tbh.

for(int i = 2; i*i<=N; i++)
{
	if(prime[i])
	{
        for(int j = i; i*j<=N; j++)
        	prime[i*j]= false;	//all multiples of i from i^2 are composite
    }
}
```

This algorithm works in $O(n\log \log n)$ time (Check [this](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html#toc-tgt-1) for the proof). This is a really great optimisation from [Approach 1](#approach-1) which runs in $O(n\sqrt n)$. 

##### Resources

- Check out [this video](https://www.youtube.com/watch?v=klcIklsWzrY) on SoE from Khan Academy. 
- Check out [this page](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html) to see a detailed explanation and an implementation of SoE.
- Checkout [GeeksforGeeks](https://www.geeksforgeeks.org/sieve-of-eratosthenes/) 

##### Problems

1) [Conjecture of Paul Erdos](https://www.spoj.com/problems/HS08PAUL/)
2) [Primal Fear](https://www.spoj.com/problems/VECTAR8/)
3) [Noldbach Problem](https://codeforces.com/contest/17/problem/A)
4) [Prime Matrix](https://codeforces.com/problemset/problem/271/B)
5) Remaining problems from [here](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html#toc-tgt-9)

We've seen a fast algorithm to find all primes in $[1, n]$. How about find all primes in $[m,n]$?

### Task: Find all primes in $[m,n]$

#### Approach 1: 

Use SoE to find all the primes till $n$. This runs in $O(n\log \log n)$ time.

Approach 1 seems to be a very good option. However, this approach cannot solve [this problem](https://www.spoj.com/problems/PRIME1/) in the given time limit. The problem here is that for large $n$, we take more time to find all the primes till $n$, but in reality we only require primes greater than or equal to $m$. 

#### Approach 2:

We now use our [previous approach](#approach-1) of finding whether a number is a prime in $O(\sqrt n)$ time. This approach solves the problem in just enough time!

We see that for finding all the primes till a natural number $n$, SoE is faster than finding whether each number is a prime. But for finding primes between two numbers $m,n$, with $m-n<<n$, finding whether is number is a primes does better than SoE. The takeaway from this is that, while certain algorithms seem to have better time complexity, it is always better to keep in mind all the possible approaches we could take to solve a given problem. 

#### Approach 3 (Segmented Sieve of Eratosthenes):

By striking off the composite numbers in $[m,n]$, we are remained with only primes. We use the fact that all the composite numbers in $[m,n]$ are multiples of primes in $[1,\sqrt n]$. Hence, by finding all the primes in $[1,\sqrt n]$, we can "strike off" all the composite numbers in $[m,n]$ and thereby find all the primes. 

##### Resources

1) Read more about SSoE [here](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html#toc-tgt-6). Though the time complexity doesn't reduce, the space complexity reduces considerably from $O(n)$ to $O(\sqrt n + S)$.
2) http://translate.google.com/translate?hl=en&sl=auto&tl=en&u=https%3A%2F%2Fprodeportiva.wordpress.com%2F2013%2F02%2F11%2Fcriba-de-eratostenes%2F&sandbox=1

## Additional Resources

1) http://pag.iitr.ac.in/blog/Number-theory-basics
2) https://artofproblemsolving.com/community/c90633h1291397
3) https://codeforces.com/blog/entry/49494
