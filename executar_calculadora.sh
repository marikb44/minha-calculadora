#!/bin/bash

echo "================================"
echo "   Iniciando a Calculadora...   "
echo "================================"

#Verificando a instalação do Python3
if ! command -v python3 &> /dev/null; then
	echo "ERRO: Python3 não encontrado!"
	echo "Instale com: sudo apt install python3"
	exit 1
fi

#Verificando se o arquivo existe
if [ ! -f "calculadora.py" ]; then
	echo "ERRO: arquivo calculadora.py não encontrado!"
	exit 1
fi

#Executa a calculadora
python3 calculadora.py

echo "============================"
echo "   Calculadora encerrada!   "
echo "============================"
