# Tuple 

t = ('tipo', 'tupla')

print(t, type(t))

# Packing e unpacking delle tuple

punto = 3, 4 # packing
x, y = punto #unpacking

print(type(punto), x, y)

# Insiemi

set1 = set([1, 2, 3, 4, 5]) # usare funzione e passafe come argomento una lista

set2 = {4, 5, 67, 8} # sixseven sixseven

set3 = {1, 2, 3, 3, 4, 4 ,5}

print(set3) # outpurt : { 1, 2, 3, 4, 5}

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7 ,8}

print(set1.union(set2))                # output : {1 ,2 ,3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))         # output : {4, 5}
print(set1.diffference(set2))          # output : {1, 2, 3}
print(set1.symmetric_difference(set2)) # output : {1, 2, 3, 6, 7, 8}