#Exercício 1: Verificação de Qualidade de Dados. 
#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
#Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

    # quantidade = -16

    # preco = -10.00

    # if quantidade > 0 and preco > 0:
    #     print(f"Dados válidos")
    # else: 
    #     print(f"Dados inválidos")
 
#Exercício 2: Classificação de Dados de Sensor
#Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'.
#Considerando que: Temperatura < 18°C é 'Baixa' | Temperatura >= 18°C e <= 26°C é 'Normal' | Temperatura > 26°C é 'Alta'

    # temperatura = 21

    # if temperatura < 18:
    #     print(f"Temperatura Baixa")
    # elif 18 <= temperatura <= 26:
    #     print(f"Temperatura Normal")
    # else:
    #     print(f"Temperatura Alta")

#Exercício 3: Filtragem de Logs por Severidade
#Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'.Dado um registro de log em formato de dicionário 
#como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

    # log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

    # if log['level'] == 'ERROR':
    #     print(log['message'] )

#Exercício 4: Validação de Dados de Entrada
#Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
#Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

    # idade = 15
    # email = "marciel@gmail.com"

    # if not 18 <= idade <= 65:
    #     print("Idade fora da faixa etária")
    # elif not '@' in email or not '.' in email:
    #     print("Email Inválido")
    # else:
    #     print("Dados de usuário válidos")

#Exercício 5: Detecção de Anomalias em Dados de Transações
#Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas.Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou 
#se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

    # transacao = {'valor': 12000, 'hora': 20}

    # if transacao['valor'] > 10000 or (transacao['hora'] < 9 or transacao['hora'] > 18):
    #     print("Transação suspeita")
    # else:
    #     print("Transação normal")

# #Exercício 6: Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

    # frase = "a raposa marrom salta sobre o cachorro preguiçoso, e o cachorro também salta sobe a raposa e corre"

    # split_palavras = frase.split(" ")

    # contador_palavras = {}

    # for palavra in split_palavras:
    #     if palavra in contador_palavras:
    #         contador_palavras[palavra] += 1
    #     else:
    #         contador_palavras[palavra] = 1
    # print(contador_palavras)

#7. Normalização de Dados
#Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

    # numeros = [10,20,30,40,50]
    # max_num = max(numeros)
    # min_num = min(numeros)

    # normalizados = [(x - min_num) / (max_num - min_num) for x in numeros]
    # print(normalizados)]

#8 Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

# print(usuarios_validos)

# 9. Extração de Subconjuntos de Dados
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

    # numeros = range(1, 30)

    # numero_pares = [numero for numero in numeros if numero % 2 ==0]

    # print(numero_pares)

# 10. Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# vlr_total_categoria = {}

# for venda in vendas:
#     categoria = venda["categoria"]    
#     valor = venda["valor"]
#     if categoria in vlr_total_categoria:
#         vlr_total_categoria[categoria] += valor
#     else:
#         vlr_total_categoria[categoria] = valor
# print(vlr_total_categoria)

# 11. Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

    # dados = []
    # entrada = ""

    # while entrada.lower() != "sair":
    #     entrada = input("Digite um valor (ou 'sair' para terminar): ")
    #     if entrada != 'sair':
    #         dados.append(entrada)
    # print(f"Valores digitados: {dados}")

# 12. Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

    # numero = int(input("Digite um numero de 1 a 10: "))

    # while numero < 1 or numero > 10:
    #     print(f"Número fora do intervalo")
    #     numero = int(input("Digite um numero de 1 a 10:"))
    # print("Número Válido!")

# 13. Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

    # pagina_atual = 1
    # paginas_totais = 5  # Simulação, na prática, isso viria da API

    # while pagina_atual < paginas_totais:
    #     print(f"Processando página {pagina_atual} de {paginas_totais}")
    #     pagina_atual += 1
    # print("Todas as páginas foram processadas.")

# 14. Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

    # tentativas_maximas = 5
    # tentativa = 1

    # while tentativa < tentativas_maximas:
    #     print(f"Tentando de conectar {tentativa} de {tentativas_maximas} ...")
    #     if False:
    #         print("Conexão bem-sucedida!")
    #         break
    #     tentativa += 1
    # else:
    #     print("Falha ao conectar após várias tentativas.")

# 15. Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.
    
itens = [1, 2, 3, "parar", 4, 5]
i = 0
while i < len(itens):
    if itens[i] == 'parar':
        print("Parada encontrada, encerrando o processamento.")
        break
    print(f"Processando item {itens[i]}...")
    i += 1