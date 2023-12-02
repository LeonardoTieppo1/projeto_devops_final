#Base image
FROM python:3.11

#Diretorio em que vamos trabalhar
WORKDIR /main

#Variaveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#Instalando as dependencias
COPY requirements.txt /main/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copiar o código para o container
COPY . /main/