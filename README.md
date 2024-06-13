# ContadorVagasEstacionamento

# Contador de Vagas de Estacionamento com OpenCV e Python

Este projeto implementa um sistema de contagem de vagas de estacionamento utilizando técnicas de visão computacional com OpenCV e Python. Ele identifica vagas disponíveis em um estacionamento através da análise de imagens/vídeos capturados por uma câmera.

## Objetivo

O objetivo deste projeto é desenvolver um sistema capaz de identificar vagas de estacionamento disponíveis utilizando OpenCV, Python e uma câmera.

## Tecnologias Utilizadas

- Python
- OpenCV
- Numpy
- Pickle
- Hardware: Raspberry Pi Zero W (ou outro hardware utilizado)

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos e diretórios:

- `contadorvagas.py`: Script principal que processa o vídeo para identificar vagas de estacionamento.
- `vagas.pkl`: Arquivo que contém os dados das coordenadas das vagas de estacionamento.
- `arquivos/video.mp4`: Vídeo de exemplo utilizado para demonstração.
- `README.md`: Documentação do projeto.

## Configuração e Execução

### Pré-requisitos

Certifique-se de ter o Python e o Git instalados em seu sistema.

### Passos para Configuração

1. Clone este repositório para o seu sistema local:
   ```sh
   git clone https://github.com/loliveirads/ContadorVagasEstacionamento.git
   cd ContadorVagasEstacionamento
