# JTSK-350112
# a1_p6.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
    Priority queue with list 
"""

def is_empty(pq):
    """
        check whether the pq has no elements
    """
    return pq == []

def insert_with_priority(pq, x, p):
    """
        add the element x to pq with a priority p
    """
    pq.append((x, p))

def pull_highest_priority_element(pq):
    """
        remove the element from pq that has the
        highest priority, and return it
    """
    if is_empty(pq):
        print("Priority Queue Underflow")
    else:
        min_el = pq[0]
        for i in pq:
            if i[1] < min_el[1]:
                min_el = i
        
        pq.remove(min_el)
        return min_el[0]

# main program
myList = []
insert_with_priority(myList, 5, 2)
insert_with_priority(myList, 3, 3)
insert_with_priority(myList, 13, 1)
insert_with_priority(myList, 6, 1)
print("Element = {}".format(pull_highest_priority_element(myList)))
print("Is empty = {}".format(is_empty(myList)))