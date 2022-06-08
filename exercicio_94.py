# ler nome, sexo e idade - isso é um dicionario
# adicionar os dados a uma lista
# A) Quantas pessoas foram cadastradas
# B) Média da idade do grupo
# C) lista com as mulheres
# D) lista de pessoas com idade acima da média

pessoa = {}
lista = []
listam = []
lista_media = []
soma = 0

while True:
    pessoa['nome'] = str(input('Qual o nome? ')).strip()
    pessoa['sexo'] = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] not in "MmFf":
        pessoa['sexo'] = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if pessoa['sexo'] in"Ff":
        listam.append(pessoa['nome'])

    pessoa['idade'] = int(input('Qual a sua idade? '))
    soma = soma + pessoa['idade']
    lista.append(pessoa.copy())
    opcao = str(input('Gostaria de cadastrar outra pessoa? [S/N] ')).strip().upper()[0]
    while opcao not in 'SsNn':
        opcao = str(input('Gostaria de cadastrar outra pessoa? [S/N] ')).strip().upper()[0]
    if opcao in "Nn":
        break

media = (soma) / (len(lista))
for p in range(0, len(lista)):
    if lista[p]['idade'] > media:
        lista_media.append(lista[p]['nome'])
print(f'\nAs pessoas que têm a idade acima da média são:')
print('-='*30)
for p in lista_media:
    print(p)
print('\nAs mulheres cadastradas são:')
print('-='*30)
for p in listam:
    print(f'{p}')
print(f'\nA média de idade é de {media} anos.')
print(f'O número de pessoas cadastradas foi {len(lista)}.')
