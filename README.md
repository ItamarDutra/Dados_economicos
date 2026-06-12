# Captura de Valores de Moedas em Tempo Real

## 📋 Resumo do Projeto
Uma empresa que realiza investimentos no exterior precisa saber o valor exato do Dólar e do Euro para registrar o valor convertido de suas compras. Antes, era necessário buscar essa cotação manualmente no momento de cada transação e registrar o valor em planilhas.

Com a conclusão deste projeto, todo esse processo de captura foi automatizado. Agora, a extração e a filtragem dos dados são feitas em apenas 2 segundos, eliminando o trabalho manual e garantindo uma margem de erro nula no registro dos valores.

## 🛠️ Ferramentas Utilizadas

* **Requests:** Utilizada para conectar com uma API financeira e capturar de forma dinâmica os dados brutos das moedas em tempo real.
* **Pandas:** Utilizada para transformar o formato bruto recebido da API (JSON) em uma tabela organizada (DataFrame). Com ela, filtrei apenas as colunas estritamente necessárias para o negócio e exportei o resultado limpo em um arquivo CSV.
* **Git / GitHub:** Utilizados para o controle de versão do código, garantindo um desenvolvimento seguro por meio de commits e servindo como vitrine para o projeto.

## 🚀 Como Executar o Projeto

Para rodar este script na sua máquina, você precisará do Python instalado e seguir os passos abaixo no seu terminal:

1. Clone este repositório para a sua máquina local utilizando o comando "git clone" acompanhado do link deste projeto.

2. Instale as bibliotecas necessárias digitando o comando:
pip install requests pandas

3. Obtenção da Chave: Acesse o site da AwesomeAPI (https://economia.awesomeapi.com.br) para criar a sua conta gratuita e obter a sua chave de API (Token).

4. Configuração de Segurança: Para não expor sua chave no código, defina-a como uma variável de ambiente antes de rodar o script.
- No Windows: set API_KEY=sua_chave_aqui
- No Linux/Mac: export API_KEY=sua_chave_aqui

5. Execute o script principal de extração digitando o comando:
python extract.py

Após a execução, um arquivo chamado Tabela_valor_eur_usd será gerado automaticamente na pasta do projeto.

---
📬 Conecte-se comigo: [https://www.linkedin.com/in/itamar-dutra](https://www.linkedin.com/in/itamar-dutra)