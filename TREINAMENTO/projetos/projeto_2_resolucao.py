from turtle import Turtle

t = Turtle()
t.speed(1)

while True:
  direcao = input('Para qual direção devemos ir? "f:frente" ou "t:tras" ')
  if direcao == 'f':
    distancia = int(
      input("Quantos pixels devemos movimentar para frente? "))
    movimentar_para_lado = input(
      "Rotacionar para d:direita, e:esquerda ou n:não rotaconar? ")

    if movimentar_para_lado == "d":
      angulo = int(
        input("Quanto para a direita devemos rotacionar? "))
      t.right(angulo)

    elif movimentar_para_lado == "e":
      angulo = int(
        input("Quanto para a esquerda devemos rotacionar?"))
      t.left(angulo)
    t.forward(distancia)

  if direcao == 't':
    distancia = int(input("Quantos pixels devemos movimentar para trás? "))
    movimentar_para_lado = input(
      "Rotacionar para d:direita, e:esquerda ou n:não rotacionar? ")

    if movimentar_para_lado == "d":
      angulo = int(input("Quaanto para a direita devemos rotacionar? "))
      t.right(angulo)

    elif movimentar_para_lado == "e":
      angulo = int(input("Quanto para a esquerda devemos rotacionar? "))
      t.left(angulo)
    t.backward(distancia)

  resposta = input("Continuar andando? ")
  if resposta not in ('sim', 's'):
    break