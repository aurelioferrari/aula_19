jogador = {}
lista = []
lista_gols = []

while True:
    jogador['nome'] = str(input("Qual o nome do jogador? ")).strip().capitalize()
    partidas = int(input('Quantas partidas ele jogou? '))
    total = 0
    for j in range(0, partidas):
        gol = int(input(f'Quantos gols na {j+1}ª partida? '))
        lista_gols.append(gol)
        total = total + gol
    jogador['gols'] = lista_gols[:]
    jogador['total'] = total
    lista_gols.clear()
    lista.append(jogador.copy())
    opcao = str(input('Quer cadastrar mais um jogador? [S/N] ')).strip().upper()[0]
    while opcao not in "SsNn":
        opcao = str(input('Quer cadastrar mais um jogador? [S/N] ')).strip().upper()[0]
    if opcao in "Nn":
        break

for k in jogador.keys():
    print(f'  {k.upper():<15}', end="")
print()
for j in range(0, len(lista)):
    print(f'{j+1} {lista[j]["nome"]:<15}', end="")
    print(f'{str(lista[j]["gols"]):<15}', end="")
    print(f'{str(lista[j]["total"]):^15}')

while True:
    resp = int(input('\nDigite o código do jogador para ver seus dados ou 999 para sair.\n->'))
    if resp == 999:
        break
    if resp > len(lista):
        resp = int(input('\nCódigo incorreto. Digite o código do jogador para ver seus dados ou 999 para sair.\n->'))
    else:
        print(f'Estatísticas do jogador {lista[resp-1]["nome"]}')
        for i, g in enumerate(lista[resp-1]['gols']):
            print(f'No jogo {i+1} ele fez {g} gols.')

