# Simulador de Votos de Pesquisa

Este projeto é um script em Python que simula a coleta de votos para uma pesquisa de opinião sobre atendimento ao cliente. Ele gera dados aleatórios para cada pergunta e, em seguida, cria gráficos para visualizar os resultados, como se a pesquisa tivesse sido respondida por 3 pessoas.

# 📝 Descrição

## O código foi desenvolvido para:

- *Simular Votos:* Adicionar votos aleatórios a cada opção de resposta em uma série de perguntas sobre atendimento ao cliente.

- *Analisar Dados:* Organizar os votos simulados em um formato tabular (*DataFrame*) para facilitar a análise.

- *Gerar Gráficos:* Criar um gráfico de barras para cada pergunta, permitindo uma visualização clara e imediata de como os votos foram distribuídos.

Este script é útil para demonstrar como dados de pesquisa podem ser coletados e visualizados, sem a necessidade de um conjunto de dados real.

# ⚙️ Pré-requisitos
## Para executar este código, você precisa ter as seguintes bibliotecas Python instaladas:

"""matplotlib"""

'''pandas'''

## Se você ainda não as tem, instale-as usando o *pip*:

'''pip install matplotlib pandas'''

# 🚀 Como Usar

* Copie o Código: Salve o código fornecido em um arquivo chamado simulador_pesquisa.py.

* Execute o Script: Abra seu terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute-o com o Python:

'''python simulador_pesquisa.py'''

* Visualize os Resultados: Após a execução, o script irá imprimir os resultados em texto no terminal e, em seguida, abrirá uma janela com os gráficos gerados. Cada gráfico representa uma pergunta da pesquisa, mostrando a distribuição dos 3 votos simulados. Feche um gráfico para que o próximo seja exibido.

# 🛠️ Personalização
Você pode facilmente modificar o comportamento do script:

- *Alterar o Número de Votos:* Mude o valor da variável *num_votos* no início do código para simular um número diferente de participantes. Por exemplo, para simular 10 votos, altere a linha para:

'''num_votos = 10'''

- *Adicionar Novas Perguntas:* Você pode incluir mais perguntas ou modificar as existentes no dicionário *perguntas*. Certifique-se de manter o formato *{"pergunta": "...", "opcoes": ["..."]}* e adicione a chave *"multipla_escolha": True* se a pergunta permitir mais de uma resposta.