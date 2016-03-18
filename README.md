#FibonacciBases
FibonacciBases is an original project by a college student exploring her/their old love for Number Theory by programming in Python and R.

### Background
My focus is in the one’s (10^0) digit of the Fibonacci numbers. In the decimal Fibonacci numbers, there are only ten digits (0 through 9) that show up in the one’s digit. Because of the finite values the one’s digit can take, I was curious if there could be a cycle that repeated in the one’s digit. Sure there was. Using modular arithmetic, after scribbling sixty numbers in my notebook, I found the digits returned to the 0 and 1 that it began from. I regretted beginning my investigation in base-10, because I realized the smaller bases and even hexadecimal required a shorter sequence of integers before repeated itself. For example, base-4 and base-7 both repeated their one’s digits after 24 integers. This means, I summed 23 pairs of integers before arriving back to 0 and 1. But there are actually 36 permutations of two base-4 digits and 81 permutations of two base-7 digits. The one’s digit sequence does not grow exponentially.

From here on and in my programs, I will refer to this one’s digit sequence as the **Fibonacci Sequence** for convenience.
The **sequence length** is the number of integers the one's digit takes on before repeating its Fibonacci Sequence.
The **number of pairs** in each sequence is the number of consecutive integers in the sequence I have to add in order to yield the next one (or simply, it is the length minus one).
The **total possible pairs** refers to the permutations of two digits in each base (which is simply the square of the base).

fibbase.py is the Python program to calculate all of the Fibonacci Sequences for a list of bases.
FibonacciBases.rmd is the annotated R code segments to analyze the data of the sequence lengths, number of pairs, and total possible pairs.