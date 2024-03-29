# 🌟 Consulta de Bolsas do FNDE 🌟
[📦 PyPI](https://pypi.org/project/bolsasfnde/)

Bem-vindo ao projeto **Consulta de Bolsas do FNDE**. Esta biblioteca foi criada para simplificar o processo de verificação do status da concessão de bolsas através do site do Fundo Nacional de Desenvolvimento da Educação (FNDE).

## 💡 Como Funciona?

O algoritmo faz uma requisição para um endpoint do FNDE usando o CPF do bolsista. Obtendo um hash com algumas informações do bolsista, mas o interessante é usar o hash para obter a informação o histórico de bolsas recebidas. Quando o hash é enviado a outro endpoint, obtemos um json com o histórico de bolsas que recebe um tratamento para deixar legível e permite descobrir se a bolsa caiu.

## 🚀 Instalação Rápida

Para começar, siga estes passos simples:

1. **Instale usando o pip:**
   ```bash
   python3 -m pip install bolsasfnde
   ````
   ou Clone e instale localmente:
   ```bash
   git clone https://github.com/asm444/bolsas-fnde.git && python3 -m pip install -e bolsas-fnde
   ```
2. **Execute a biblioteca com**
   ```bash
   python3 -m bolsasfnde
   ```
##  💡Execução Manual

Clone o repositório
   ```bash
   git clone https://github.com/asm444/bolsas-fnde.git
   ```
instale as dependências 
   ```bash
   python3 -m pip install requests
   ```
e execute o algoritmo
   ```bash
   cd bolsas-fnde ; python3 main.py
   ```
e após a primeira consulta, as próximas consultas podem ser feitas ao executar o main.py com
   ```bash
   python3 main.py
   ```
