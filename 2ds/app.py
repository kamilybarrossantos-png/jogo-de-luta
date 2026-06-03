# Solicita ao usuário que digite o seu peso. 
# O 'input' lê a resposta como texto, e o 'float' converte esse texto para um número decimal.
peso = float(input("Digite o seu peso em kg (ex: 70.5): "))

# Solicita ao usuário que digite a sua altura.
# Novamente, o 'float' é usado porque a altura tem casas decimais (ex: 1.75).
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

# Calcula o IMC aplicando a fórmula matemática: peso dividido pela altura ao quadrado.
# Em Python, o símbolo '**' é usado para exponenciação (altura ** 2 significa altura ao quadrado).
imc = peso / (altura ** 2)

# Exibe na tela o valor do IMC calculado.
# O ': .2f' formata o número para exibir apenas duas casas decimais, deixando o visual mais limpo.
print(f"\nSeu IMC calculado é: {imc:.2f}")

# A partir daqui, começam as estruturas condicionais (if, elif, else) para classificar o resultado.
# Se o IMC for menor que 18.5, o programa entra neste bloco.
if imc < 18.5:
    print("Classificação: Abaixo do peso.")

# Se não for menor que 18.5, verifica se está entre 18.5 (inclusivo) e 24.9.
elif 18.5 <= imc <= 24.9:
    print("Classificação: Peso normal.")

# Se não caiu nas opções anteriores, verifica se está entre 25.0 e 29.9.
elif 25.0 <= imc <= 29.9:
    print("Classificação: Sobrepeso.")

# Verifica se o IMC indica Obesidade Grau I (entre 30.0 e 34.9).
elif 30.0 <= imc <= 34.9:
    print("Classificação: Obesidade Grau I.")

# Verifica se o IMC indica Obesidade Grau II (entre 35.0 e 39.9).
elif 35.0 <= imc <= 39.9:
    print("Classificação: Obesidade Grau II.")

# Se o valor não se encaixou em nenhuma das condições acima (ou seja, é 40 ou maior).
else:
    print("Classificação: Obesidade Grau III (Mórbida).")