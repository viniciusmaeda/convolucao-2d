# Programa desenvolvido para a disciplina de Visão Computacional.
# Professor: Dr. Hemerson Pistori
# Atividade: Convolução em 2D
#
# Autor: Vinícius Maeda (viniciusmaeda@gmail.com)
#
# Exemplo de uso:
# 
# Executar o seguinte comando no terminal
# $ python atividadeConvolucao2D.py
#
# 
# Bibliotecas
#
# OpenCV: 4.9.0
# Numpy: 1.26.4
# Pytorch: 2.3.0+cpu


# Bibliotecas utilizadas
import cv2 as cv
import numpy as np
import os.path
import torch
import matplotlib.pyplot as plt


# nome dos núcleos utilizados e nomes dos arquivos com os núcleos
nucleos = [
  {'nome': 'Média', 'arquivo': 'nucleoMean.txt'},
  {'nome': 'Scharr Horizontal', 'arquivo': 'nucleoScharrHorizontal.txt'},
  {'nome': 'Scharr Vertical', 'arquivo': 'nucleoScharrVertical.txt'},
  {'nome': 'Sobel Horizontal', 'arquivo': 'nucleoSobelHorizontal.txt'},
  {'nome': 'Sobel Vertical', 'arquivo': 'nucleoSobelVertical.txt'},
  {'nome': 'Núcleo Personalizado', 'arquivo': 'nucleoPersonalizado.txt'}
]


# função para verificar existência dos arquivos
def verificarExistenciaArquivoImagem(arquivoImagem):
  # verfica se o arquivo do núcleo está na pasta
  if (not os.path.isfile(arquivoImagem)):
    print("\nO arquivo 'nucleo.txt' não foi encontrado na pasta do projeto.\n")
    exit()


def verificarExisteniaArquivosNucleos():

  # verifica se todos os arquivos estão na pasta
  for n in nucleos:
    # nome do arquivo que será verificado
    nomeDoArquivo = n['arquivo']
    # verfica se o arquivo do núcleo está na pasta
    if (not os.path.isfile('./nucleos/' + nomeDoArquivo)):
      print('\nO arquivo ' + nomeDoArquivo + ' não foi encontrado na pasta do projeto.\n')
      print('Verifique se o arquivo está na pasta. Programa finalizado.')
      exit()


# mosta mensagens iniciais e o núcleo que será utilizado
def inicioPrograma():
  print("\n<><><><><><><><><><><><><><><><><><>")
  print("Programa para aplicar a convolução numa imagem a partir de um núcleo (kernel) fornecido pelo usuário.")
  print("<><><><><><><><><><><><><><><><><><>\n")


def abrirArquivoNucleo(arquivo):
    # Lista para armazenar o núcleo
    nucleoLista = []

    # Abre o arquivo com o kernel
    with open(arquivo, "r") as f:
        for linha in f:
            # Remove o caractere de nova linha
            listaString = linha.strip()
            # Converte a linha em uma lista (array)
            lista = eval(listaString)
            # Adiciona a lista ao núcleo
            nucleoLista.append(lista)

    # Retorna o núcleo como um tensor
    return torch.tensor(nucleoLista)


# função para identificar o núcleo utilizado na convolução
def identificarNucleoConvolucao():
  # verifica se todos os arquivos estão na pasta
  verificarExisteniaArquivosNucleos()

  # menu para apresentar as opções
  print('Escolha o núcleo desejado para a convolução.')
  print('1 - Média')
  print('2 - Scharr (horizontal)')
  print('3 - Scharr (vertical)')
  print('4 - Sobel (horizontal)')
  print('5 - Sobel (vertical)')
  print('6 - Personalizado (editar o arquivo nucleoPersonalizado.txt)')
  opcao = input('Escolha sua opcão: ')

  # lista com as opções válidas
  opcoes_validas = ['1', '2', '3', '4', '5', '6']

  # verifica se a opção escolhida está disponível
  if opcao in opcoes_validas:
    nome_arquivo = nucleos[int(opcao) - 1]['arquivo']
    nucleo = abrirArquivoNucleo(f'./nucleos/{nome_arquivo}')
    return nucleo, int(opcao)
  else:
    print('Opção inválida. Programa finalizado.')
    exit()


if (__name__ == "__main__"):

  # constante com o nome do arquivo da imagem
  ARQUIVO_IMAGEM = "./assets/lenna-gray-50x50.png"

  # função para verificar existência dos arquivos
  verificarExistenciaArquivoImagem(ARQUIVO_IMAGEM)

  # imprime mensagens de início do programa
  inicioPrograma()

  # obtém o filtro desejado pelo usuário
  nucleo, opcao = identificarNucleoConvolucao()

  # mostra no terminal o núcleo escolhido pelo usuário
  print("\nNúcleo utilizado para o processamento:")
  print(nucleo)

  # abre a imagem
  imagem = cv.imread(ARQUIVO_IMAGEM, cv.IMREAD_GRAYSCALE)

  # converte a imagem (numpy) para tensor (torch)
  imagemTensor = torch.tensor(imagem)

  # Criação da matriz zerada com o resultado 
  matrizResultado = torch.zeros((imagemTensor.size(0) - 2, imagemTensor.size(1) - 2))

  # Criar a janela de plotagem
  fig, (ax_esquerdo, ax_direito) = plt.subplots(1, 2)

  # define a primeira imagem mostrada na janeal (imagem original)
  ax_esquerdo.imshow(imagemTensor.numpy(), cmap='gray')
  ax_esquerdo.set_title('Imagem Original')
  ax_esquerdo.set_xticks([])
  ax_esquerdo.set_yticks([])

  # define a imagem que será mostrada no lado direito
  ax_direito.imshow(np.zeros_like(imagemTensor.numpy()), cmap='gray')
  ax_direito.imshow(imagemTensor.numpy(), cmap='gray')
  ax_direito.set_title('Imagem Variável')
  ax_direito.set_xticks([])
  ax_direito.set_yticks([])

  plt.tight_layout()

  plt.show(block=False)

  # Inicia na posição 1 e vai até a penúltima posição, pois na convolução
  # as bordas da matriz são descartadas
  for i in range(1, imagemTensor.size(0) - 1):
    for j in range(1, imagemTensor.size(1) - 1):

      # Calcula a convolução entre o recorte da matriz e o nucleo, ao final soma os valores
      valorCalculadoConvolucao = (imagemTensor[i - 1 : i + 2, j - 1 : j + 2] * nucleo).sum()

      # salva o resultado na posição da matriz resultado
      matrizResultado[i - 1][j - 1] = valorCalculadoConvolucao

      # mostra a imagem com o resultado parcial
      ax_direito.imshow(matrizResultado.numpy(), cmap='gray')
      ax_direito.set_title(f'Pixel: ({i}, {j})')
      plt.draw()
      # Aguarda alguns instantes antes de trocar a imagem
      plt.pause(0.00005)
  
  # mostra no terminal a imagem original e o resultado
  print('Imagem entrada:\n', imagemTensor)
  print('Resultado:\n', matrizResultado)

  # salva a imagem na pasta resultados
  cv.imwrite('./resultados/resultado_' + nucleos[opcao - 1]['arquivo'].split('.')[0] + '.png', matrizResultado.numpy())
