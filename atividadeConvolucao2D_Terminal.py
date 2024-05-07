# Esta atividade tem por objetivo mostrar a convolução passo a passo através do terminal

# Importação das bibliotecas
import torch

# Código para limpar o terminal
print("\033[H\033[J", end="")

# Função para mostrar a matriz de entrada
def mostrarMatrizEntradaKernel(m, k):
  # Mostra a matriz de entrada
  print('Matriz de entrada:\n', matrizEntrada)

  # Mostra a matriz que representa o kernel
  print('\nKernel para a convolução:\n', kernel)


# Criação de uma matriz aleatória 5x5 com valores de 1 a 9
matrizEntrada = torch.randint(1, 10, (5, 5))

# Criação de uma matriz que representa o kernel da convolução
# kernel = torch.tensor([
#   [-1., -2., -1.],
#   [0., 0., 0.],
#   [1., 2., 1.]]
# )
kernel = torch.tensor([
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1]
])


# Criação da matriz zerada com o resultado 
matrizResultado = torch.zeros((matrizEntrada.size(0) - 2, matrizEntrada.size(1) - 2))

# Inicia na posição 1 e vai até a penúltima posição, pois na convolução
# as bordas da matriz são descartadas
for i in range(1, matrizEntrada.size(0) - 1):
  for j in range(1, matrizEntrada.size(1) - 1):
    # Mostra a matriz de entrada
    mostrarMatrizEntradaKernel(matrizEntrada, kernel)

    # Mostra o elemento analizado
    print('\nElemento analisado: ', matrizEntrada[i][j].item())

    # Calcula a convolução entre o recorte da matriz e o nucleo, ao final soma os valores
    valorCalculadoConvolucao = (matrizEntrada[i-1:i+2, j-1:j+2] * kernel).sum()

    # Mostra o resultado do cálculo da convolução
    print('Valor calculado da convolução:', valorCalculadoConvolucao.item())

    # salva o resultado na posição da matriz resultado
    matrizResultado[i - 1][j - 1] = valorCalculadoConvolucao

    # Mostra os resultados parciais  
    print('\n--------- RESULTADO --------\n')
    print('Matriz com o resultado:\n', matrizResultado)

    # Pausa para veririficar os resultados parciais
    input('\nPressione qualquer tecla para continuar...')

    # Código para limpar o terminal
    print("\033[H\033[J", end="")

# Mostra o resultado final
print('\n----- RESULTADO FINAL ------\n')
mostrarMatrizEntradaKernel(matrizEntrada, kernel)
print('\nMatriz com o resultado final:\n', matrizResultado)
