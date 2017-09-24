# -*- coding: utf-8 -*-
"""
B351 - Assignment0 skeleton code
"""
import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
#**** Your Code goes here ****

def name_number():

    name = 'Renee Bialas'
    number = '0003256278'
    return name,number

def remove_dup(l):
    #new_list is the new list to add non duplicate items into
    new_list = []
    for item in l:
        if item not in new_list:
            new_list.append(item)
    return new_list

def substring(a,i,l):
    #a indicates character to be inserted
    #i indicates index position
    #l indicates list
    if i > len(l):
        l.append(a)
    else:
        l.insert(i, a)
    return l



def diag_add(d,l):
    #d = dimension of the square matrix
    #l = matrix values
    length = len(l)
    i = 0
    j = d-1
    diag1 = 0
    diag2 = 0

    while i < length:
        diag1 += l[i]
        i += d+1
    while j <= length-d:
        diag2 += l[j]
        j += d-1
    return max(diag1,diag2),min(diag1, diag2)

#****  End of your Code ****

#**** You can manually change the input to the functions below and test your codes****

def main():
    assert(compare(remove_dup(['a','c','a']),['c','a']))
    assert(compare(remove_dup([10,100,10000,10,100,10]),[10,100,10000]))
    print("Test cases passed for Remove Duplicates")

    assert (substring('d',10,['a','b','c'])==['a','b','c','d'])
    assert (substring('a', 2, ['c', 'd', 'b'])==['c','d','a','b'])
    print("Test cases passed for Substring")

    assert (diag_add(3,[2,2,2,2,2,2,2,2,2]) == (6,6))
    assert (diag_add(3,[1, 2, 3, 10, 12, 15, 20, 22, 25]) == (38,35))
    print ("passed all cases")


main()

#**** All the best ****
