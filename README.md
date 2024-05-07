# Programa para realizar a convolução (2D) em uma imagem a partir de um núcleo definido pelo usuário
## Autor: Vinícius de Araújo Maeda

## Resumo
Programa desenvolvido para uma atividade da disciplina de Visão Computacional (turma 2024-1) ofertada pelo professor Dr. Hemerson Pistori. A disciplina é oferecida para os estudantes de graduação e pós-graduação da Universidade Católica Dom Bosco.

Dado uma imagem em tons de cinza (2D) o programa irá realizar a convolução a partir de um núcleo (kernel) definido pelo usuário. De forma didática, o programa mostra as etapas de processamento da imagem, calculando pixel a pixel.

## Versões das bibliotecas
- OpenCV: 4.9.0
- Numpy: 1.26.4
- Pytorch: 2.3.0+cpu

## Execução do programa
Foram criadas 3 versões para esta atividade.
1) *atividadeConvolucao2D_Terminal.py* - versão de programa que irá mostrar o processo de convolução no Terminal.

```
$ python atividadeConvolucao2D_Terminal.py
```

2) *atividadeConvolucao2D_UmaImagem.py* - versão de programa que irá abrir uma imagem e, dependendo do kernel (núcleo) escolhido pelo usuário, mostrará o resultado da imagem numa janela.

```
$ python atividadeConvolucao2D_UmaImagem.py
```

3) *atividadeConvolucao2D_DuasImagens.py* - versão do programa que irá abrir uma imagem e, dependendo do kernel (núcleo) escolhido pelo usuário, mostrará uma janela com duas imagens, a imagem original e outra imagem com os resultados sendro processados dinamicamente.

```
$ python atividadeConvolucao2D_DuasImagens.py
```

## Resultado esperado
Ao executar cada uma das versões espera-se os seguintes resultados.

1) *atividadeConvolucao2D_Terminal.py* - o programa irá mostrar no Terminal o cálculo da convolução pixel a pixel, de forma dinâmica.

2) *atividadeConvolucao2D_UmaImagem.py* - o programa irá mostrar o resultado da convolução de uma imagem, baseado no núcleo escolhido pelo usuário no Terminal. A imagem resultante será mostrada dinâmicamente numa janela, onde os pixels serão calculados um a um.

3) *atividadeConvolucao2D_DuasImagens.py* - o programa irá mostrar o resultado da convolução de uma imagem, baseado no núcleo escolhido pelo usuário no Terminal. Nesta versão de código, a janela mostrará duas imagens, a imagem original e a imagem com os resultados parciais sendo calculados pixel a pixel.