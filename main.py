import random
from datetime import datetime

# Função para distribuir os coroinhas de acordo com a pauta da missa
def distribuir_coroinhas(nomes_coroinhas, pauta, coroinhas_servidos, impedimentos, periodo, data_missa, escalados_na_mesma_data):
    funcoes = {
        "solene": {"Turíbulo": 1, "Naveta": 1, "Vela": 6, "Missal": 1, "Microfone": 1, "Credencia": 1},
        "comum": {"Vela": 2, "Missal": 1, "Credencia": 3}
    }

    if pauta.lower() not in funcoes:
        print("Pauta inválida. Por favor, escolha 'solene' ou 'comum'.")
        return None

    funcoes_missa = funcoes[pauta.lower()]

    # Embaralhar os nomes dos coroinhas para distribuição aleatória
    random.shuffle(nomes_coroinhas)

    # Verificar se há coroinhas suficientes para as funções
    if len(nomes_coroinhas) < sum(funcoes_missa.values()):
        print("Não há coroinhas suficientes para todas as funções.")
        return None

    # Inicializar o registro de coroinhas servidos para esta pauta
    for coroinha in nomes_coroinhas:
        if coroinha not in coroinhas_servidos:
            coroinhas_servidos[coroinha] = 0

    # Distribuir os coroinhas nas funções para a missa
    distribuicao_missa = {}
    for funcao, qtd_coroinhas in funcoes_missa.items():
        coroinhas_disponiveis = [
            coroinha for coroinha in nomes_coroinhas 
            if coroinhas_servidos[coroinha] < 2 and not verifica_impedimento(coroinha, impedimentos, periodo, data_missa)
            and coroinha not in escalados_na_mesma_data
        ]

        # Se não houver coroinhas suficientes disponíveis, interromper a distribuição
        if len(coroinhas_disponiveis) < qtd_coroinhas:
            print(f"Não há coroinhas suficientes disponíveis para a função {funcao}.")
            return None

        # Atribuir coroinhas para a função atual
        coroinhas = random.sample(coroinhas_disponiveis, qtd_coroinhas)
        for coroinha in coroinhas:
            coroinhas_servidos[coroinha] += 1
            escalados_na_mesma_data.add(coroinha)

        distribuicao_missa[funcao] = coroinhas

    return distribuicao_missa

# Função para verificar se o coroinha tem impedimento para servir em um determinado período ou data
def verifica_impedimento(coroinha, impedimentos, periodo, data_missa):
    if coroinha not in impedimentos:
        return False

    # Verifica se o coroinha tem impedimento para o dia da semana ou a data específica
    dias_nao_pode = impedimentos[coroinha]["dias"]
    datas_nao_pode = impedimentos[coroinha]["datas"]

    # Verifica se o coroinha tem impedimento no período (dia da semana)
    if periodo.lower() in dias_nao_pode:
        return True

    # Verifica se o coroinha tem impedimento na data específica
    if data_missa in datas_nao_pode:
        return True

    return False

# Função para criar a escala para uma missa
def criar_escala():
    coroinhas_servidos = {}

    # Perguntar o número de pautas, quantas serão comuns e quantas serão solenes
    num_pautas = int(input("Quantas pautas você deseja criar? "))
    num_comum = int(input("Quantas pautas serão comuns? "))
    num_solene = num_pautas - num_comum

    print(f"Você escolheu {num_comum} pautas comuns e {num_solene} pautas solenes.")

    # Receber os nomes dos coroinhas e seus impedimentos
    nomes_coroinhas = []
    impedimentos = {}  # Dicionário para armazenar os impedimentos de cada coroinha

    while True:
        nome = input("Digite o nome do coroinha (ou deixe em branco para encerrar): ").strip()
        if not nome:  # Caso o usuário não insira nome, encerra a entrada
            break
        nomes_coroinhas.append(nome)
        coroinhas_servidos[nome] = 0  # Inicialmente, cada coroinha não serviu em nenhuma missa

        # Perguntar se o coroinha tem algum impedimento
        tem_impedimento = input(f"O coroinha {nome} tem algum impedimento para servir? (sim ou não): ").strip().lower()

        if tem_impedimento == "sim":
            # Perguntar o motivo do impedimento
            motivo_impedimento = input(f"Qual o motivo do impedimento para o coroinha {nome}? ").strip()

            # Perguntar os dias específicos que ele não pode servir
            dias_nao_pode = input(f"Quais dias da semana o coroinha {nome} NÃO PODE servir? (quinta-feira, domingo de manhã, domingo à noite):\n").strip().lower()

            # Perguntar as datas específicas em que o coroinha não pode servir
            datas_nao_pode = input(f"Quais datas o coroinha {nome} NÃO PODE servir (formato: DD/MM/AAAA)? Caso não tenha datas, deixe em branco.\n").strip()

            # Armazenar o impedimento com o motivo, os dias e as datas
            impedimentos[nome] = {
                "motivo": motivo_impedimento,
                "dias": set(dias_nao_pode.split(",")),
                "datas": set(datas_nao_pode.split(","))
            }
        else:
            # Se não tiver impedimento, considera-se disponível para todos os dias
            impedimentos[nome] = {
                "motivo": None,
                "dias": set(),
                "datas": set()
            }

    # Exibir os impedimentos dos coroinhas
    print("\nImpedimentos dos coroinhas:")
    for coroinha, dados in impedimentos.items():
        if dados["motivo"]:
            dias = ', '.join(dados["dias"])
            datas = ', '.join(dados["datas"])
            print(f"{coroinha}: Motivo: {dados['motivo']}, Não pode servir nos dias: {dias}, Não pode servir nas datas: {datas}.")
        else:
            print(f"{coroinha}: Sem impedimentos, pode servir em qualquer dia.")

    # Perguntar o número de missas
    num_missas = num_pautas  # Usaremos o mesmo número de pautas

    # Gerar as pautas
    pautas = []
    for i in range(num_pautas):
        pauta = "comum" if i < num_comum else "solene"
        pautas.append(pauta)

    # Perguntar o horário de ensaio/organização, que será o mesmo para todas as missas
    while True:
        horario_organizacao_ensaio = input("Digite o horário da organização e do ensaio (será o mesmo para todas as missas): ").strip()
        if horario_organizacao_ensaio:
            break
        else:
            print("O horário da organização e do ensaio não pode ficar em branco.")

    # Agora, distribuir os coroinhas para as missas
    coroinhas_servidos_por_periodo = {'Manhã': [], 'Noite': []}

    for i, pauta in enumerate(pautas):
        # Gerar duas pautas com o mesmo nome, uma para a manhã e outra para a noite
        nome_missa = input("Digite o nome da missa: ").strip()
        data_missa = input("Digite a data da missa (DD/MM/AAAA): ").strip()

        # Túnica
        tunica = "Romana" if pauta == "solene" else "Branca"

        # Inicializar o conjunto para rastrear os coroinhas escalados para a mesma data
        escalados_na_mesma_data = set()

        # Criar as duas pautas para cada missa: uma para a manhã e outra para a noite
        for periodo in ["Manhã", "Noite"]:
            print(f"\n--- {nome_missa} ({periodo}) ---")
            print(f"Data: {data_missa}")
            print(f"Horário da Organização e Ensaio: {horario_organizacao_ensaio}")
            print(f"Pauta: {pauta.capitalize()} - {periodo}")
            print(f"Túnica: {tunica}")

            # Distribuir os coroinhas para a missa
            distribuicao_missa = distribuir_coroinhas(nomes_coroinhas, pauta, coroinhas_servidos, impedimentos, periodo, data_missa, escalados_na_mesma_data)

            if distribuicao_missa:
                print("\nDistribuição dos coroinhas para a missa:")
                for funcao, coroinhas in distribuicao_missa.items():
                    print(f"{funcao}: {', '.join(coroinhas)}")

                # Registrar os coroinhas que serviram no período
                coroinhas_servidos_por_periodo[periodo].extend([coroinha for coroinha in distribuicao_missa['Vela']])

# Iniciar o processo de criação de escala
criar_escala()
