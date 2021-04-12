# listas podem ser modificadas, tuplas não

nomes = ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')

print('Bia' in nomes)

print(nomes[0])
print(nomes[1:3])
print(nomes[1:-1])
print(nomes[2:])
print(nomes[:-2])

print(len(nomes))
print(type(nomes))
print(nomes)

####################################

tupla = tuple()
tupla = ()
type(tupla)
dir(tupla)
# help(tuple)
type(tupla)
tupla = ('um') # considera uma string
type(tupla)
tupla = ('um',) # tupla
type(tupla)
tupla[0]
# tupla[0] = 'novo'
cores = ('verde', 'amarelo', 'azul', 'branco')
cores[0]
cores[-1]
cores[1:]

cores.index('amarelo')
cores.count('azul')
len(cores)