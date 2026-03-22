n = int(input())

print(n)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    qtd = n // nota
    print('{} nota(s) de R$ {},00'.format(qtd, nota))
    n = n % nota