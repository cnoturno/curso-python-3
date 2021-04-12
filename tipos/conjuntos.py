# print({1, 2, 3})
print(type({1, 2, 3}))
conj = {1, 2, 3, 3, 3, 3, 3}
print(conj)
print(len(conj))

####################################

a = {1, 2, 3}
type(a)
# a[0]
a = set('coddddd3r')
print(a)
print('3' in a, 4 not in a)
{1, 2, 3} == {3, 2, 1, 3,}

# Operações
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2)
c1
c2 <= c1
c1 >= c2

{1, 2, 3} - {2}
c1 - c2
c1 -= {2}
c1