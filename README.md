# Projeto de Conversão de Imagem

Este projeto converte uma imagem colorida para escala de cinza e, em seguida, para preto e branco, exibindo as três versões da imagem lado a lado.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

## Instalação

1. Clone este repositório ou baixe os arquivos do projeto.
2. Navegue até o diretório do projeto no terminal ou prompt de comando.
3. Instale as bibliotecas necessárias usando `pip`:

```sh
pip install pillow matplotlib
```

## Como Rodar o Projeto

1. Coloque a imagem que você deseja converter no diretório do projeto e renomeie-a para `image.jpg` ou ajuste o caminho do arquivo no código conforme necessário.
2. Execute o script Python:

```sh
python image.py
```

## Explicação do Código

- O script abre a imagem especificada e converte os pixels para escala de cinza usando a fórmula de luminância.
- Em seguida, aplica um limiar para converter a imagem em preto e branco.
- Por fim, exibe as três versões da imagem (original, escala de cinza e preto e branco) lado a lado usando a biblioteca `matplotlib`.

## Exemplo de Saída

O script exibirá uma janela com as três imagens lado a lado, destacando a transformação de cada etapa.

```
```
