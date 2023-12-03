#Base image
FROM python:3.11

#Diretorio em que vamos trabalhar
WORKDIR /app

#Variaveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#Instalando as dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copiar o código para o container
COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]