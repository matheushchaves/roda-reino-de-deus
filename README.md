# Roda do Reino de Deus

Aplicação Flask para avaliar diferentes áreas da vida espiritual e gerar um gráfico radar com os resultados.

## Sumário

- [Descrição](#descrição)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação e Execução](#instalação-e-execução)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição

A **Roda do Reino de Deus** é uma ferramenta interativa que permite aos usuários avaliar diferentes áreas de sua vida espiritual. Com base nas avaliações fornecidas, a aplicação gera um gráfico do tipo radar que visualiza as pontuações em cada área, ajudando na identificação de pontos fortes e áreas que precisam de desenvolvimento.

## Tecnologias Utilizadas

- **Python 3**
- **Flask** - Framework web para Python
- **HTML5 & CSS3**
- **Bootstrap 5** - Biblioteca front-end para estilização
- **Chart.js** - Biblioteca JavaScript para criação de gráficos
- **JavaScript** - Para manipulação do DOM e interatividade

## Como Executar o Projeto

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/)
- Um editor de código-fonte, como [Visual Studio Code](https://code.visualstudio.com/)

### Instalação e Execução

1. **Clone este repositório**

   ```bash
   git clone https://github.com/seu-usuario/roda-reino-de-deus.git
   ```

2. **Acesse a pasta do projeto no terminal**

   ```bash
   cd roda-reino-de-deus
   ```

3. **Crie um ambiente virtual (opcional, mas recomendado)**

   ```bash
   python -m venv venv
   ```

4. **Ative o ambiente virtual**

   - **No Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **No Unix/Linux/MacOS:**

     ```bash
     source venv/bin/activate
     ```

5. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

6. **Execute a aplicação**

   - Defina a variável de ambiente `FLASK_APP` (se necessário):

     ```bash
     export FLASK_APP=app.py         # No Unix/Linux/MacOS
     set FLASK_APP=app.py            # No Windows
     ```

   - Execute o servidor Flask:

     ```bash
     flask run
     ```

   - Ou, para modo de depuração:

     ```bash
     flask run --debug
     ```

7. **Acesse a aplicação no seu navegador**

   Abra o navegador e acesse:

   ```
   http://localhost:5000
   ```

## Como Usar

1. **Avalie cada área**

   - Na página inicial, você verá diferentes áreas da vida espiritual.
   - Para cada área, clique em uma nota de **1** (Muito Ruim) a **10** (Muito Bom) que represente sua autoavaliação naquela área.

2. **Envie suas respostas**

   - Após avaliar todas as áreas, clique no botão **"Enviar"** no final da página.

3. **Visualize os resultados**

   - Você será redirecionado para uma página que mostra um gráfico radar com suas pontuações em cada área.
   - A média geral das suas pontuações também será exibida.

4. **Reflexão e Ação**

   - Use o gráfico para identificar áreas que podem precisar de atenção e desenvolvimento.
   - Considere criar um plano de ação para melhorar nas áreas com pontuações mais baixas.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto, siga estes passos:

1. **Faça um fork deste repositório**

2. **Crie uma branch para sua feature**

   ```bash
   git checkout -b minha-nova-feature
   ```

3. **Commit suas alterações**

   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```

4. **Faça um push para a branch**

   ```bash
   git push origin minha-nova-feature
   ```

5. **Abra um Pull Request**

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
