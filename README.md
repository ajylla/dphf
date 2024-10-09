# DPHF (Double Pendulum Hash Function)

![](https://upload.wikimedia.org/wikipedia/commons/e/e4/Double_pendulum_predicting_dynamics.gif "Source: https://commons.wikimedia.org/wiki/File:Double_pendulum_predicting_dynamics.gif")

[Hash functions](https://en.wikipedia.org/wiki/Hash_function) are functions that take as input some arbitrary 
length of data, and outputs a fixed length *hash*. Among other things, professional hash functions have the 
attribute that a slight change in the input data results in a drastic change at the output. This behaviour is 
also seen in physics; the double pendulum is a system that is very sensitive to the initial parameters, and a 
slight change in, say, the angle of one of the pendulums might result in very different behaviour as the system 
evolves. As such, I thought it might be a fun idea to combine the two and create my own hash function that depends 
on computations of the double pendulum to produce its output.

---

*Disclaimer:*

*You're welcome to do with the code as you wish but do NOT use it in any application where robustness and/or 
correctness is required.*

---

The function numerically solves the pair of differential equations that emerge from the double pendulum system[^1]. 
This is done using SciPy's [`solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) function. The initial values for the problem are generated from the input data.

## Goals for the function

This project is not a very serious exercise, thus I was not concerned with the details.

The conditions that I wanted my function to satisfy (which it more or less does) are as follows:

- Produce a fixed-length output for any arbitrary length input.
- Produce the same output for the same input.
- Have a *decent* collision resistance, that is, mostly produce unique hashes
for unique inputs.
- Produce greatly different outputs for two slightly different inputs.

There conditions are reflected in the tests I wrote for the function.

## Usage

Run: `python dphf.py <your string>`

## DPHT (Double Pendulum Hash Table)

See also folder dpht/ which implements a hash table using the DPHF as its hash function.

[^1]: See for example this: https://www.myphysicslab.com/pendulum/double-pendulum-en.html
