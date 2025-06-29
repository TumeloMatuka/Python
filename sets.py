#Sets
'''
my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(2)
print(my_set)
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union
set_union = set1.union(set2)
print(set_union)

#intersection
set_intersection = set1.intersection(set2)
print(set_intersection)

#difference
set_difference = set1.difference(set2)
print(set_difference)