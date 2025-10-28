taxaimposto = float (input("Digite a Taxa do Imposto:"))
custo = float (input(f"Digite o custo antes do Imposto:"))
preco_final = custo * (1 + taxaimposto / 100)

print("---------------------------------------")
print("| CÁLCULO DE PREÇO COM IMPOSTO |" )
print (f"Digite a taxa de imposto (%): {taxaimposto}")
print (f"Digite o custo do item (antes do imposto):{custo}")
print (f"Preço final com o Imposto : R$ {preco_final}")