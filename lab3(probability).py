import numpy as np
import random
import itertools

def generate_cards():
    suits = ['S','H','D','C']
    faces = list(range(2, 11)) + ["J", "Q", "K", "A"]
    return list(map(lambda x: str(x[0]) + x[1],itertools.product(faces, suits)))

#print (generate_cards())

def shuffle_cards(cards):
    for i in range(len(cards)-1,1,-1):
        j = random.randint(0,i)
        cards[i],cards[j] = cards[j],cards[i]
    return cards

#print (shuffle_cards(generate_cards()))

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))
#----------------------------------------------------------

#changing the original python function
# FROM: returning tuple
# TO: returning list 
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = list(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield list(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield list(pool[i] for i in indices[:r])
                break
        else:
            return



#-----------------------------------------------------------

def get_combinations(numbers, k):
  comb = []
  for i in range(len(numbers)):
      comb += itertools.combinations(numbers,k)
  return comb

numbers = np.random.uniform(-10, 10, 20)
#print(numbers)

#print(take(4,get_combinations(numbers, 4)))
#Display all anagrams of a given word
def anagrams(word):
    words = permutations(word)
    return list(map(lambda x : ''.join(x), words))

print (take(4,anagrams("word")))
