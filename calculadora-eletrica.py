# Calculadora de consumo elétrico inteligente
# Autor: Lucas Fersa

# Entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
tempo = float(input("Digite o tempo de uso do aparelho em horas (h): "))
dias_uso = int(input("Digite o número de dias de uso por mês: "))

# Cálculo do consumo em kWh
consumo_diario = (potencia * tempo) / 1000
consumo_mensal = consumo_diario * dias_uso
custo_mensal = consumo_mensal * 0.95  # Custo do kWh em reais em agosto (R$ 0,95)

# Saída
print(f"\nO consumo mensal do aparelho {aparelho} é de {consumo_mensal:.2f} kWh.")
print(f"O custo mensal estimado para o uso do aparelho {aparelho} é de R$ {custo_mensal:.2f}.")