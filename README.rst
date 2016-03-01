========================================================================
An Efficient Way to Generate Bernoulli Random Variables with a Fair Coin
========================================================================

Problem Description
===================

Generate a Bernoulli random variable :math:`X` with :math:`P[X=1]=p` and :math:`P[X=0]=1-p` by flipping a fair coin


Algorithm
=========

Without losing generality, assume :math:`p=0.a_1a_2a_3\ldots a_n, a_i∈\{0, 1\}`. If we have a uniform random variable :math:`Y` with a probability density function of :math:`f_Y(y)=1, 0≤ y<1`. We can generate :math:`X` as follows:

.. math::

    X=\begin{cases} 1 & Y<p \\
    0 & Y>p \end{cases} 

We can generate :math:`Y` by flipping a fair coin repeatedly. Let :math:`Y=0.B_1B_2B_3\ldots, B_i∈\{0, 1\}`,


.. math::

    B_i=\begin{cases} 0 & i\textrm{th flip is “head”} \\
    1 & i\textrm{th flip is “tail”} \end{cases} 


In order to decide whether :math:`Y` is greater or less than :math:`p`, we need to generate the binary expansion of :math:`Y` bit by bit and compare them with the corresponding bits of :math:`p`.  Once we find the smallest :math:`k` such that :math:`a_k\neq B_k`, we will stop flipping the coin. Then, :math:`X` can be generated as follows:


.. math::

    X=\begin{cases} 1 & \textrm{if }a_i=B_i,i=1,2,\ldots k-1\textrm{ and }B_k<a_k,k\leq n \\
    0 & \textrm{if }a_i=B_i,i=1,2,\ldots k-1\textrm{ and }B_k>a_k,k\leq n\\ 
    0 & \textrm{if }a_i=B_i,i=1,2,\ldots n \end{cases} 


Note that when the comparison reaches the end of binary expansion of :math:`p`, i.e., the first :math:`n` bits of :math:`p` are the same as the first :math:`n` bits of :math:`Y`, we know that :math:`Y` will be greater than :math:`p` eventually since it has an infinite expansion. Therefore, we can set :math:`X` as :math:`0` and stop flipping the coin.


Based on the algorithm above, the probability of the number of flips required is the following:

.. math::

    P\left[\textrm{# of flips}=k\right]=\begin{cases} \left(\frac{1}{2}\right)k & k<n \\
    \left(\frac{1}{2}\right)n & k=n \end{cases}

 
We have the expected number of flips:

.. math::

    E\left[\textrm{# of flips}\right]=\sum_{k=1}^{n-1}k\cdot\left(\frac{1}{2}\right)^{k}+n\cdot\left(\frac{1}{2}\right)^{n}=2-\left(\frac{1}{2}\right)^{n-1}

For :math:`p=0.5`, the length of its binary expansion :math:`n=1`, and thus the expected number of flips is :math:`1`. For :math:`p=0.625` (its :math:`n=3`), the expected number of flips is :math:`1.75`. When :math:`n\rightarrow\infty`, e.g., :math:`p=\frac{5}{7}`, the expected number of flips will be :math:`2`.