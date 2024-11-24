# Usar uma imagem base do Python 3.9 slim
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação para o contêiner
COPY . .

# Expor a porta 80 para acesso externo
EXPOSE 80

# Executar a aplicação
CMD ["python", "app.py"]
