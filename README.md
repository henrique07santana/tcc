# SEMINÁRIO INTEGRADOR EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
## Henrique de Souza Santana, Hugo Mello Neto, Marcos Paulo Hauer

### Pre-reqs
* Python 3.7
* requirements.txt
  * instalação: pip install -r requirements.txt
  
### Arquivos
* main.py - estrutura de menus e chamada de funções
* passenger.py, booking.py, station.py, vehicle.py - módulos com funções e telas
* seat.py - exemplo para ser usado na reserva e/ou nos veículos para reservar/mostrar assentos (utiliza o arquivo data.txt)

### Diagrama de Classes

![Diagrama](https://github.com/mhauer71/tcc/blob/master/SeatReservation.png?raw=true)

### TODO
Como o professor está pedindo no fórum:  
*Reiterando que a próxima tarefa (etapas 3 e 4), a ser entregue até 27/05/2020, corresponde aos relatórios e telas do software que está sendo desenvolvido nesta disciplina. Portanto, ao entregar essa tarefa (até 27/05/2020),  vcs devem postar um arquivo "pdf" contendo somente uma breve descrição e o lay-out para cada tela e relatório implementado. Cabe ressaltar que não são necessárias todas as telas e relatórios, mas somente aqueles que vcs conseguirem implementar, tentando priorizar os que julguem ser os mais importantes. Eu sei da dificuldade de todos, portanto implementem dentro da possibilidade de cada grupo.*  
então vou listar por ordem de prioridade o que acho que precisamos fazer:
* Tela de inclusão de agendamentos ( adaptando o código do seat.py)
* Tela de inclusão de passageiros 
* Tela de listagem de passageiros
* Tela de listagem de agendamentos
* Tela de inclusão de veículos 
* DAO para acesso ao banco (MySQL)
* Ligação das telas com o banco (efetiva inserção, edição e relatórios)

Como ele não está pedindo o código nesse passo da tarefa para o dia 27/05, acho que podemos focar na parte visual para enviarmos, mas já preparando um código enxuto pra gerar as mesmas pq acho que isso será pedido na etapa 4, no dia 16/06.  
Vou preparar um ambiente com Dockerfile e docker-compose pra já incluir um banco MySql pra gente ter facilidade pra testar e desenvolver.
