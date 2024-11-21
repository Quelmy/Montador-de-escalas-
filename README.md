# Sistema de Distribuição de Coroinhas para Missas

Este sistema ajuda a criar escalas de coroinhas para missas, levando em consideração as funções a serem desempenhadas (como turíbulo, vela, missal, etc.), os impedimentos dos coroinhas (datas específicas, dias da semana), e os horários das missas.

### Funcionalidades
1. **Cadastro de Coroinhas**: Permite o cadastro de coroinhas e seus impedimentos (dias da semana e datas específicas em que não podem servir).
2. **Criação de Pautas**: Permite a criação de pautas para missas, definindo se são comuns ou solenes.
3. **Distribuição de Coroinhas**: Os coroinhas são distribuídos aleatoriamente para funções de acordo com a pauta da missa, respeitando os impedimentos e os coroinhas já escalados para a mesma data.
4. **Escala de Missas**: O sistema permite gerar escalas para diferentes missas, definindo funções e distribuindo coroinhas para cada missa, tanto no período da manhã quanto à noite.
5. **Controle de Impedimentos**: O sistema verifica os impedimentos dos coroinhas e distribui as funções apenas para aqueles que estão disponíveis.

### Como Usar

1. **Cadastro de Coroinhas**:
   - O sistema solicitará os nomes dos coroinhas.
   - Para cada coroinha, será perguntado se ele possui algum impedimento (dias da semana ou datas específicas que não pode servir).

2. **Criação de Pautas**:
   - Você informará o número total de missas e o número de missas solenes e comuns.
   - O sistema permitirá a criação de missas de acordo com as pautas selecionadas (solene ou comum).

3. **Distribuição de Coroinhas**:
   - O sistema irá distribuir os coroinhas para as missas, de acordo com a pauta (solene ou comum) e o número de coroinhas necessários para cada função.
   - Ele leva em consideração os impedimentos e a disponibilidade de cada coroinha.

4. **Visualização da Escala**:
   - Após a distribuição, o sistema mostrará a lista de coroinhas escalados para cada função na missa.

### Exemplos de Funcionamento

1. **Cadastro de Coroinhas**:
   ```
   Digite o nome do coroinha (ou deixe em branco para encerrar): João
   O coroinha João tem algum impedimento para servir? (sim ou não): sim
   Qual o motivo do impedimento para o coroinha João? Trabalho
   Quais dias da semana o coroinha João NÃO PODE servir? quinta-feira, domingo de manhã
   Quais datas o coroinha João NÃO PODE servir (formato: DD/MM/AAAA)? 24/12/2024, 25/12/2024
   ```

2. **Criação de Missas**:
   ```
   Quantas pautas você deseja criar? 3
   Quantas pautas serão comuns? 2
   Você escolheu 2 pautas comuns e 1 pauta solene.
   ```

3. **Distribuição de Coroinhas**:
   ```
   --- Missa de Natal (Manhã) ---
   Data: 25/12/2024
   Horário da Organização e Ensaio: 08:00
   Pauta: Solene - Manhã
   Túnica: Romana
   Distribuição dos coroinhas para a missa:
   Turíbulo: João
   Naveta: Maria
   Vela: Ana, Lucas, Pedro, João
   Missal: Clara
   Microfone: Sofia
   Credencia: Paulo
   ```

### Requisitos

Este script foi desenvolvido utilizando o Python 3.x e usa as bibliotecas padrão (`random`, `datetime`).

### Instruções para Execução

1. Certifique-se de que você tenha o Python 3.x instalado no seu computador.
2. Copie e cole o código em um arquivo chamado `distribuir_coroinhas.py`.
3. Execute o script no terminal ou IDE Python de sua preferência:
   ```
   python distribuir_coroinhas.py
   ```

### Considerações

- **Impedimentos**: Cada coroinha pode ter impedimentos específicos para dias da semana ou datas. O sistema vai respeitar esses impedimentos ao distribuir as funções.
- **Funções e Pautas**: Para missas solenes, são necessárias funções adicionais (como turíbulo e naveta). Para missas comuns, são funções mais simples, como vela e missal.

### Possíveis Melhorias

- Adicionar suporte para exportar a escala de coroinhas para um arquivo CSV ou PDF.
- Adicionar uma interface gráfica (GUI) para facilitar o uso do sistema.

---

Esse README fornece uma visão geral de como utilizar o sistema, suas funcionalidades e como o código pode ser adaptado ou expandido no futuro.
