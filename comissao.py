#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programa para calcular comissão sobre vendas
Baseado no algoritmo original: comissao.alg
"""

def calcular_comissao():
    # Leitura dos dados de entrada
    salario_base = float(input("Digite o salário-base: "))
    valor_venda = float(input("Digite o valor de vendas: "))
    
    # Inicializa a comissão
    comissao = 0
    
    # Cálculo da comissão conforme a faixa de vendas
    if valor_venda < 55000:
        comissao = 100
    elif valor_venda <= 100000:
        comissao = valor_venda * 0.02
    else:  # valor_venda > 100000
        comissao = 5000
    
    # Calcula o salário final
    salario_final = salario_base + comissao
    
    # Exibe os resultados
    print(f"Comissão: {comissao:.2f}")
    print(f"Salário final: {salario_final:.2f}")


if __name__ == "__main__":
    calcular_comissao()
