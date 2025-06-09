#!/bin/zsh

echo alias mks="python3 '/home/nuvu-pc-n4gx/Personal/University/Lenguajes de programacion/proyecto-final-lenguajes-programacion/main.py'" >>  ~/.zshrc
#!/bin/bash

# Ruta de ANTLR
ANTLR_JAR="$HOME/Downloads/ANTLR-main/antlr-4.13.1-complete.jar"
GRAMMAR_FILE="GramaticaMKS.g4"

echo "Instalando python con antlr..."
sudo apt install python3-pip
sudo pip3 install antlr4-python3-runtime --break-system-packages

# Generar archivos con ANTLR
echo "Generando archivos con ANTLR..."
antlr4 -Dlanguage=Python3 -visitor GramaticaMKS.g4

# Ejecutar la calculadora
echo "Ejecutando la calculadora..."
python3 main.py input_file.mks
