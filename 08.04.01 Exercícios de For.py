#!/usr/bin/env python
# coding: utf-8

# ## 1. Criando um Registro de Hóspedes
# 
# Sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:
#
# 1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
# 2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
# 3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:
quarto = [
    ['João', 'cpf:00000000000'],
    ['Julia', 'cpf:11111111111'],
    ['Marcus', 'cpf:22222222222'],
    ['Maria', 'cpf:33333333333'],
]
#Código

np = int(input("Quantos hospedes?"))
quarto = []
for i in range(np):
    index = str(i+1)
    cpf = input(index + "º CPF" )
    nome = str(input(index + "º Nome",))
    hospede = [nome, "cpf:{}".format(cpf)]
    quarto.append(hospede)
    
print(quarto)

print("--"*6)


# ## 2. Análise de Vendas
# 
# Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
# 
# Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
#Código

for nome, valor in vendas:
    if valor > meta:
        print("O/A vendedor(a) {} bateu a meta vendendo {}".format(nome, valor))

print("--"*6)

# ## 3. Comparação com Ano Anterior
# 
# Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.


produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

#Código

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        print("{}\n 2019:{}\n 2020:{}\nEm 2020 o crescimento foi de: {:2.1%}\n".format(produto, vendas2019[i],vendas2020[i], vendas2020[i]/vendas2019[i]-1))

print("--"*14)


