#Base image
FROM python:3.11

#Diretorio em que vamos trabalhar
WORKDIR /app

#Variaveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Instalando as dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copiar o código para o container
COPY . /app/
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
