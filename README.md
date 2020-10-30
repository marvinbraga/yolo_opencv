# Marvin Yolo OpenCV
By Marcus Vinicius Braga, 2020.

## Project Description 
Este projeto tem como finalidade criar uma coleção de classes que facilitem a 
detecção de imagens utilizando as tecnologias YOLO V4 e OpenCv.
Um outro objetivo deste projeto é a difusão da programação orientada a objetos,
padrões de projetos e código limpo.

## Considerações Sobre o Projeto
Para utilizar-se da programação orientada a objetos deve-se pensar, em primeiro
lugar: 
- quais serão as **entidades** (classes) que irão interagir entre si, 
- seus **comportamentos** (métodos e propriedades) e, por fim, 
- seus **construtores** (onde são passados objetos e informações para a execução 
do processamento).

Enquanto no _paradigma de programação procedural_ pensa-se em **métodos** para 
resolver um determinado problema, no _paradigma orientado a objetos_, em vez
de procedimentos e funções utiliza-se **abstrações** (interfaces e classes) e 
projeta-se como suas interações permitem chegar a uma determinada solução em
excelência.  

Neste processo de análise torna-se fundamental a identificação das **interfaces**, 
ou **classes abstratas**, pois, estes tipos é que poderão ser distribuídos pelo 
sistema. Todo acoplamento deverá estar relacionado apenas a estes tipos abstratos.

Este projeto foi iniciado em laboratório e incrementado, pouco a pouco, como
experimento de POO. Seu produto final deverá ser uma implementação completamente
orientada a objetos.

## Requisitos

### Requisitos Funcionais

#### Inputs
- Preciso ler nomes de arquivos de imagens de um diretório e disponibiliza-los
para o processamento de detecção de objetos.
- O processamento, inicialmente, deve ser feito **uma imagem por vez** e 
posteriormente passar a ser multiprocessamento por threads.
- Preciso carregar um arquivo que contem a **configuração** da YOLO V4.
- Preciso carregar um arquivo que contem os **peso**s do treinamento da RN YOLO V4.
- Preciso carregar um arquivo que contem os **labels** do treinamento da RN YOLO V4.
- Preciso passar informação sobre o **threshold** e **threshold nns**.
- Preciso passar a informação sobre **quais labels serão procurados** e 
respectivamente contabilizados, por imagem.

#### Outputs
- Preciso receber a informação sobre os **labels encontrados** e esta **respectiva 
quantidade** ou não.
- Preciso **exibir a imagem processada, ou não**.
- Preciso exibir o **relatório detalhado e consolidado de labels encontrados**. 
- Preciso salvar a imagem de resultado.

### Requisitos Não Funcionais


## Project Analysis

### Image Manager
Objetivo de:
- carregar imagens de arquivos através de caminhos de diretórios.
- carregar imagens diretamente de Bytes (stream).
- carregar imagens de strings em base64.
- devolver resultado para salvar em arquivo (diretório de saída).
- devolver resultado em bytes (stream).
- devolver resultado em string de base64.

#### Abstração - Métodos e Propriedades
##### AbstractImageManager
Interface para gerenciadores de imagem que tem como objetivo recuperar
imagens em um determinado formato, prepará-las para serem utilizadas 
pelo YOLO4 com OpenCV e fornecer o resultado de seu processamento.

###### Properties:

####### output:
Esta propriedade retorna uma **lista que contém itens de dicionário** formado pelo _nome do arquivo_ de 
imagem e a _própria imagem_ já como _dado do OpenCV_. 
Ex.: [{'file_name': Nome da imagem, 'data': dado do OpenCV}]

####### output_in_base64:
Esta propriedade retorna uma **lista que contém itens de dicionário** formado pelo _nome do arquivo_ de 
imagem e a _própria imagem_ já no formato de _string base64_. 
Ex.: [{'file_name': Nome da imagem, 'data': Imagem em string base64}]

####### output_in_bytes:
Esta propriedade retorna uma **lista que contém itens de dicionário** formado pelo _nome do arquivo_ de 
imagem e a _própria imagem_ já no formato de _bytes_. 
Ex.: [{'file_name': Nome da imagem, 'data': Imagem em bytes}]

###### Methods:
####### save_in_files:
Este método salva em arquivo as imagens constantes na propriedade **output**.

### Gerador de Relatório

##### AbstractImageReport

###### Properties:
####### report:
Esta propriedade retorna uma **lista que contém itens de dicionário** formado pelo _nome do arquivo_ de 
imagem e a _lista_ com informações coletadas no processamento. 
Ex.: [{'file_name': Nome da imagem, 'report': [{'label': Nome do Label, 'count': Quantidade de vezes que 
apareceu na imagem.}]}]

###### Methods:

 
- ComputerVisionManager
- **kwargs**: 
#### Classe e Construtores
