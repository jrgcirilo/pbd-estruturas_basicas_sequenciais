salario_base=float(input("Digite o salário base"))
gratificacao=salario_base*0.05
imposto=salario_base*0.07
salario_a_receber=salario_base+gratificacao-imposto
print(salario_a_receber)