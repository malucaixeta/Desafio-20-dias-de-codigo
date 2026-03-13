codpeca1, numpecas1, valor1 = input().split()
codpeca2, numpecas2, valor2 = input().split()

total = int(numpecas1) * float(valor1) + int(numpecas2) * float(valor2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))