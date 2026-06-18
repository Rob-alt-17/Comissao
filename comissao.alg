algoritmo "Comissao"

var
   salarioBase, valorVenda, comissao, salarioFinal : real

inicio

   escreva("Digite o salario-base: ")
   leia(salarioBase)

   escreva("Digite o valor de vendas: ")
   leia(valorVenda)

   comissao <- 0

   se valorVenda < 55000 entao
      comissao <- 100
   fimse

   se (valorVenda >= 55000) e (valorVenda <= 100000) entao
      comissao <- valorVenda * 0.02
   fimse

   se valorVenda > 100000 entao
      comissao <- 5000
   fimse

   salarioFinal <- salarioBase + comissao

   escreval("Comissao: ", comissao)
   escreval("Salario final: ", salarioFinal)

fimalgoritmo
