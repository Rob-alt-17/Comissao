# Calculadora de Comissão sobre Vendas 💰

Um programa simples que calcula a comissão de vendas com base no valor total vendido e retorna o salário final do vendedor.

## 📋 Descrição

Este projeto calcula automaticamente a comissão de um vendedor de acordo com as seguintes faixas:

| Faixa de Vendas | Comissão |
|---|---|
| Menos de R$ 55.000 | R$ 100 (fixo) |
| De R$ 55.000 a R$ 100.000 | 2% do valor de vendas |
| Acima de R$ 100.000 | R$ 5.000 (fixo) |

O salário final é calculado como: **Salário Base + Comissão**

## ✨ Funcionalidades

- Cálculo automático da comissão de vendas
- Aplicação das regras de negócio conforme a faixa de vendas
- Cálculo do salário final
- Interface simples via terminal


### 📸 Demonstração da execução

<p align="center">
  <img src="https://github.com/user-attachments/assets/2c4bf5b1-417d-49fd-b8f5-3a3ba8e98489"
       alt="Demonstração da execução do programa"
       width="500">
</p>

## 🚀 Como Usar

### Pré-requisitos
- Python 3.6+

### Executar o programa

```bash
python3 comissao.py
```

Você será solicitado a inserir:
1. O salário-base
2. O valor de vendas

### Exemplo de uso:

```text
Digite o salário-base: 5000
Digite o valor de vendas: 80000

Comissão: 1600.00
Salário final: 6600.00
```

## 📁 Arquivos do Projeto

- `comissao.py` - Versão em Python (recomendada para testes)
- `comissao.alg` - Versão em Portugol/Visualg (algoritmo original)
- `README.md`- Documentação do projeto

## 📊 Casos de Teste

Teste o programa com os seguintes cenários:

| Salário Base | Valor Vendas | Comissão Esperada | Salário Final |
|---|---|---|---|
| 1000 | 30000 | 100.00 | 1100.00 |
| 1000 | 75000 | 1500.00 | 2500.00 |
| 1000 | 150000 | 5000.00 | 6000.00 |
| 2000 | 55000 | 1100.00 | 3100.00 |
| 2500 | 100000 | 2000.00 | 4500.00 |

## 🔄 Conversão de Linguagens

Este projeto foi desenvolvido originalmente em **Portugol (Visualg)** como exercício de lógica de programação e posteriormente convertido para **Python**, preservando a mesma regra de negócio para facilitar testes e evolução do código.

A regra de negócio foi mantida durante a conversão, alterando apenas a sintaxe da linguagem.

### Linguagem Original (Portugol)
```algol
se (valorVenda >= 55000) e (valorVenda <= 100000) entao
   comissao <- valorVenda * 0.02
fimse
```

### Python
```python
elif valor_venda <= 100000:
    comissao = valor_venda * 0.02
```

## 💻 Tecnologias

- Python 3
- Portugol (Visualg)
- Script de console
- Bibliotecas padrão do Python

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e prática de lógica de programação e Python.
