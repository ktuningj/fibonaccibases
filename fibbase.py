import csv
import pandas as pd

def leastSignificant(sum, base):
    """Takes the sum and returns only the one's place of its value in the chosen base."""
    return (sum % base)

def seqFib(base):
    """Generates the Fibonacci Sequence list of the chosen base (that must be an integer greater than 1 to make sense)."""
    fibs = [0,1]
    before = 0
    now = 1
    while not((before == (base-1)) and (now == 1)):
        # the sequence will repeat with last two integers becoming one less than the base and zero respectively
        nextinSequence = now + before
        ones = leastSignificant(nextinSequence, base)
        fibs.append(ones)
        before = now
        now = ones
    return fibs

def genFibData(nums):
    """Returns the bases used, the lengths of each Fibonacci Sequence, the number of pairs of the sequence, and the total number of possible unique pairs of integers."""
    base = []
    length = []
    pairs = []
    possible = []
    for n in nums:
        base.append(n)
        length.append(len(seqFib(n)))
        pairs.append(length[-1]-1)
        possible.append(n*n)
    return (base, length, pairs, possible)

def genFibDic(nums):
    fibs = {}
    fibs['base'] = genFibData(nums)[0]
    fibs['sequence length'] = genFibData(nums)[1]
    fibs['number of pairs'] = genFibData(nums)[2]
    fibs['total possible pairs'] = genFibData(nums)[3]
    return fibs

# dictionary should have a structure like this:
data = {'base': [list], 'sequence length': [list], 'number of pairs': [list], 'total possible pairs':[list]}

def genFibDataFrame(nums):
    data = genFibDic(nums)
    df = pd.DataFrame(data, columns=['base', 'sequence length', 'number of pairs', 'total possible pairs'])
    return df

def main():
    nums = []
    for n in range(2,3600):
        nums.append(n)
    df = genFibDataFrame(nums)
    df.to_csv('fibonaccibases.csv')

main()
