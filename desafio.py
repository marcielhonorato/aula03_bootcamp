CONSTANTE_BONUS = 1000

nome_valido : bool = False
salario_valido : bool = False
bonus_valido : bool = False

while nome_valido is not True:
# Solicita ao usuário que digite seu nome
    try:
        nome_usuario : str = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome_usuario) == 0:
            print("O nome não pode ficar vazio")

        # Verifica se há números no nome
        elif nome_usuario.isdigit():
            print("O nome não deve conter números.")

        # Verifica se há mais de 3 letras ou caractere inválido digitados para nome
        elif len(nome_usuario) < 3:
            print("Você digitou menos de 3 letras ou caractere inválido para nome")
        else:
            nome_valido = True
            print(f"Nome válido: {nome_usuario}")
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário Converte a entrada para um número de ponto flutuante
while salario_valido is not True:
    try:
        salario_usuario : float = float(input("Digite o valor do salário: "))
        if salario_usuario < 0:
            print("O valor digitado precisa ser positivo")
        else:
            salario_valido = True
    except ValueError:
        print("Erro. Parece que não foi digitado um valor númerico/nada")
  

# Solicita ao usuário que digite o valor do bônus recebido Converte a entrada para um número de ponto flutuante
while bonus_valido is not True:
    try:
        bonus_usuario : float = float(input("Digite o valor do bônus em %: "))
        if bonus_usuario < 0:
            print("O valor digitado precisa ser positivo")
        else:
            bonus_valido = True
    except ValueError:
            print("Erro. Parece que não foi digitado um valor númerico ou nada")

# 4) Calcule o valor do bônus final

valor_do_bonus : float = CONSTANTE_BONUS + (salario_usuario * bonus_usuario)

# Imprima cálculo do KPI para o usuário

print(f"O usuario {nome_usuario}, recebeu um bônus de R$ {valor_do_bonus}")

# Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"O usuario {nome_usuario}, com um salário de R$ {salario_usuario}, recebeu um bônus {bonus_usuario}% equivalente a R$ {salario_usuario * bonus_usuario} do salário + R$ {CONSTANTE_BONUS}, total de: R${valor_do_bonus + salario_usuario}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
    # Utilizar numeros por engano no nome, para a nossa regra não serve
    # Colocar ',' em variavel do tipo float, quebrará o programa
    # O programa aceita valores negativos, para a nossa regra não serve
    