# ⚡ Calculadora de Consumo Elétrico Inteligente

A **Calculadora de Consumo Elétrico Inteligente** é um script em Python desenvolvido para estimar o consumo de energia (em kWh) e o custo financeiro mensal de qualquer eletrodoméstico. 

Este sistema permite personalizar a potência do aparelho, as horas diárias de utilização e a quantidade de dias de uso no mês. Isso possibilita calcular com precisão tanto aparelhos de uso contínuo (como geladeiras) quanto de uso pontual (como máquinas de lavar roupas e lava-louças).

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## 🧮 Fórmulas Utilizadas

O programa realiza a conversão da potência de Watts para Quilowatts e calcula os custos com base na tarifa média configurada:

1. **Consumo Diário (kWh):**
   $$\text{Consumo Diário} = \frac{\text{Potência (W)} \times \text{Horas de Uso}}{1000}$$

2. **Consumo Mensal (kWh):**
   $$\text{Consumo Mensal} = \text{Consumo Diário} \times \text{Dias de Uso no Mês}$$

3. **Custo Mensal Estimado (R$):**
   $$\text{Custo Mensal} = \text{Consumo Mensal} \times 0.95$$
   *(Considerando a tarifa fixa de R$ 0,95 por kWh)*

## 🚀 Como Executar o Programa

### Pré-requisitos
* Ter o **Python** instalado em sua máquina.

### Passo a Passo

1. **Clone ou baixe o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

```

2. **Acesse a pasta do projeto via terminal:**
```bash
cd seu-repositorio

```

3. **Execute o script Python:**
```bash
python calculadora.py

```

4. **Siga as instruções na tela:**
Insira o nome do aparelho, potência (W), tempo de uso diário (h) e os dias de uso no mês quando solicitado.

## 👨‍💻 Autor

Desenvolvido por **Lucas Fersa**.

```

```