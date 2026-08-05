# Calculadora de Comissão sobre Vendas 💰

Um programa simples para calcular a comissão de vendas baseada no valor total de vendas e adicionar ao salário base.

## 📋 Descrição

Este projeto calcula automaticamente a comissão de um vendedor de acordo com as seguintes faixas:

| Faixa de Vendas | Comissão |
|---|---|
| Menos de R$ 55.000 | R$ 100 (fixo) |
| De R$ 55.000 a R$ 100.000 | 2% do valor de vendas |
| Acima de R$ 100.000 | R$ 5.000 (fixo) |

O salário final é calculado como: **Salário Base + Comissão**

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

```
Digite o salário-base: 1000
Digite o valor de vendas: 75000
Comissão: 1500.00
Salário final: 2500.00
```

## 📁 Arquivos do Projeto

- `comissao.py` - Versão em Python (recomendada para testes)
- `comissao.alg` - Versão em Portugol/Visualg (algoritmo original)
- `README.md` - Este arquivo

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

O código foi convertido de **Portugol/Visualg** para **Python** para facilitar testes e integração com CI/CD.

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

- **Linguagem**: Python 3
- **Tipo**: Script console
- **Dependências**: Nenhuma (usa apenas bibliotecas padrão)
