import random
import matplotlib.pyplot as plt
import pandas as pd

# Definindo TODAS as perguntas e opções
perguntas = {
    "avaliacao_atendimento": {
        "pergunta": "Como você avalia, em geral, o atendimento que costuma receber em lojas ou serviços?",
        "opcoes": ["Excelente", "Bom", "Regular", "Ruim", "Péssimo"]
    },
    "valoriza_atendimento": {
        "pergunta": "O que você mais valoriza em um bom atendimento?",
        "opcoes": ["Ser atendido com rapidez", "Ser tratado com educação e respeito", "Que o atendente saiba explicar bem os produtos/serviços", "Que o atendente resolva problemas com eficiência", "Que o ambiente seja agradável"],
        "multipla_escolha": True
    },
    "atitude_inaceitavel": {
        "pergunta": "Qual dessas atitudes você considera inaceitável em um atendente?",
        "opcoes": ["Falar no celular durante o atendimento", "Ser rude ou mal-humorado", "Não saber responder suas dúvidas", "Ignorar sua presença", "Todas as anteriores"]
    },
    "experiencia_ruim": {
        "pergunta": "Já teve alguma experiência ruim de atendimento?",
        "opcoes": ["Sim", "Não"]
    },
    "experiencia_boa": {
        "pergunta": "E uma experiência muito boa?",
        "opcoes": ["Sim", "Não"]
    },
    "escutar_cliente": {
        "pergunta": "Você acredita que escutar bem o cliente faz diferença no atendimento?",
        "opcoes": ["Sim", "Não", "Talvez"]
    },
    "lidar_cliente_impaciente": {
        "pergunta": "O que você faria se estivesse no lugar de um atendente lidando com um cliente impaciente?",
        "opcoes": ["Tentaria conversar com calma e explicar a situação", "Ignoraria o cliente", "Chamaria um supervisor", "Outro"]
    },
    "influencia_decisao": {
        "pergunta": "Você acha que o bom atendimento influencia sua decisão de voltar a comprar ou usar o serviço?",
        "opcoes": ["Sim, sempre", "Às vezes", "Não influencia"]
    },
    "elogiou_atendente": {
        "pergunta": "Você já elogiou um atendente por um bom atendimento?",
        "opcoes": ["Sim", "Não", "Não me lembro"]
    },
    "preco_vs_atendimento": {
        "pergunta": "Para você, o que é mais importante: preço baixo ou bom atendimento?",
        "opcoes": ["Preço baixo", "Bom atendimento", "Os dois igualmente"]
    }
}

# Número de votos a simular
num_votos = 3

# Dicionário para armazenar os resultados
resultados = {}
for chave in perguntas.keys():
    resultados[chave] = {opcao: 0 for opcao in perguntas[chave]["opcoes"]}

# Simular os votos
for _ in range(num_votos):
    for chave, info in perguntas.items():
        if info.get("multipla_escolha"):
            # Escolhe aleatoriamente até 2 opções (conforme a pergunta)
            num_escolhas = random.randint(1, 2)
            opcoes_escolhidas = random.sample(info["opcoes"], k=num_escolhas)
            for opcao in opcoes_escolhidas:
                resultados[chave][opcao] += 1
        else:
            # Escolhe uma única opção
            opcao_escolhida = random.choice(info["opcoes"])
            resultados[chave][opcao_escolhida] += 1

# Exibir os resultados e gerar os gráficos
for chave, dados in resultados.items():
    print(f"\n--- Resultados para a pergunta: '{perguntas[chave]['pergunta']}' ---")
    
    # Criar um DataFrame para facilitar a visualização e a plotagem
    df = pd.DataFrame(list(dados.items()), columns=['Opção', 'Votos'])
    print(df)
    
    # Gerar o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(df['Opção'], df['Votos'], color='skyblue')
    
    plt.title(perguntas[chave]['pergunta'])
    plt.xlabel('Opções')
    plt.ylabel('Número de Votos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()