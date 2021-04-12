# dicionario = objeto

aluno = {
  'nome': 'Pedro Henrique',
  'nota': 9.2,
  'ativo': True
}

print(type(aluno))
print(aluno['nome'])
print(aluno['nota'])
print(aluno['ativo'])
print(len(aluno))

####################################

pessoa = { 'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['INglês', 'Português'] }
type(pessoa)
dir(dict)
len(pessoa)

pessoa
pessoa['nome']
pessoa['idade']
pessoa['cursos']
pessoa['cursos'][1]
# pessoa[tag]
pessoa.keys()
pessoa.values()
pessoa.items()
pessoa.get('idade')
pessoa.get('get')
pessoa.get('tag', [])

####################################

pessoa = { 'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python'] }
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa
pessoa.pop('idade')

pessoa
pessoa.update({ 'idade': 40, 'sexo': 'M' })
pessoa
del pessoa['cursos']
pessoa
pessoa.clear()
pessoa