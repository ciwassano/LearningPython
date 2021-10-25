#!/usr/bin/env python
# coding: utf-8

'''
Exercício - Mini Projeto de Análise de Dados

Temos os dados de 2019 de uma empresa de prestação de serviços.

- CadastroFuncionarios
- CadastroClientes
- BaseServiçosPrestados

O que queremos saber/fazer?

1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa? <br>
2. Qual foi o faturamento da empresa?<br>
3. Qual o % de funcionários que já fechou algum contrato?<br>
4. Calcule o total de contratos que cada área da empresa já fechou
5. Calcule o total de funcionários por área
6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?<br>

'''

# Importando as bases de dados

import pandas as pd

clientes_df = pd.read_csv("CadastroClientes.csv", sep=";", decimal=",")
funcionarios_df = pd.read_csv("CadastroFuncionarios.csv", sep=";", decimal=",")
servicos_df = pd.read_excel("BaseServiçosPrestados.xlsx")

# retirar colunas
servicos_df = base_servicos[["Codigo do Servico", "ID Funcionário", "ID Cliente", "Tempo Total de Contrato (Meses)"]]
display(servicos_df)
funcionarios_df = funcionarios_df.drop(["Estado Civil", "Cargo"], axis=1)

# 1 - Valor Total da Folha Salarial

funcionarios_df["Total da Folha Salarial"] = funcionarios_df["Salario Base"] + funcionarios_df["Impostos"] + funcionarios_df["Beneficios"] + funcionarios_df["VT"] + funcionarios_df["VR"]
display(funcionarios_df)

salario_total = funcionarios_df["Total da Folha Salarial"].sum()
print("O valor total da folha salarial foi de R${:,}".format(salario_total))


# ### 2 - Qual foi o faturamento da empresa?

clientes_df = clientes_df.merge(servicos_df, on="ID Cliente")

clientes_df["Faturamento anual"] = clientes_df["Valor Contrato Mensal"] * clientes_df["Tempo Total de Contrato (Meses)"]
display(clientes_df)

faturamento_total = clientes_df["Faturamento anual"].sum()
print("O faturamento total foi de R${:,}".format(faturamento_total))


# ###  3 - Qual o % de funcionários que já fechou algum contrato?

qtd_funcionarios_fechou = len(servicos_df["ID Funcionário"].unique())
qtd_funcionarios_total = len(funcionarios_df["ID Funcionário"])
print("O percentual de funcionários que fecharam contrato foi de {:.1%}".format(qtd_funcionarios_fechou/qtd_funcionarios_total))


# ###  4 - Calcule o total de contratos que cada área da empresa já fechou

contratosarea_df = servicos_df[["ID Funcionário", "Codigo do Servico"]].merge(funcionarios_df[["ID Funcionário", "Area"]], on="ID Funcionário")

display(contratosarea_df)
contratos_area = contratosarea_df["Area"].value_counts()
print(contratos_area)
contratos_area.plot(kind="bar")


# ### 5 - Calcule o total de funcionários por área

funcionarios_area = funcionarios_df["Area"].value_counts()
print(funcionarios_area)
funcionarios_area.plot(kind="bar")


# ###  6 - Qual o ticket médio mensal (faturamento médio mensal) dos contratos?

ticket_medio = clientes_df["Valor Contrato Mensal"].mean()
print("Ticket médio Mensal: R${:,}".format(ticket_medio))
