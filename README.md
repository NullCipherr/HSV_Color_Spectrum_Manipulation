# 🌈 HSV_Color_Spectrum_Manipulation
  Este repositório contém um programa que realiza a alteração de uma faixa de valores de matizes (Hue) em uma imagem colorida, representada no sistema de cor HSV.

## 🎯 Objetivo
  O objetivo deste projeto é implementar e testar um programa que recebe uma imagem colorida e realiza uma alteração em uma faixa de valores de matizes na imagem representada no sistema de cor HSV.

## 📝 Parâmetros
  O programa recebe os seguintes parâmetros:

  - Uma imagem de entrada colorida.
  - Um valor inteiro de matiz m (0 <= m < 360).
  - Um valor inteiro x.

## ⚙️ Funcionamento
  Inicialmente, após ser carregada, a imagem de entrada estará representada no sistema RGB, onde a imagem é então convertida para o sistema HSV. Em seguida, a banda H, de matiz, é manipulada e todas as matizes no intervalo [m - x, m + x] são substituídas por suas matizes inversas, isto é, se a matiz q está no intervalo, ela é substituída pela matiz q + 180. Após as alterações serem realizadas, a imagem é retornada para o sistema RGB.

  

