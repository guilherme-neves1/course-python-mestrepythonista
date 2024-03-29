from datetime import datetime

'''
def depositar_dinheiro():
    print("Depositando dinheiro")

    def depositando_dolar():
        print("Depositando dolares")

    def depositando_reais():
        print("Depositando reais")

    depositando_dolar()
    depositando_reais()

depositar_dinheiro()

# Exemplo 1
def pai(numero):
    def filho_1():
        print("Sou o filho 1")
    def filho_2():
        print("Sou o filho 2")
    if numero == 1:
        return filho_1
    
resultado = pai(1)
resultado()

# Decorators
def meu_decorator(funcao):
    def wrapper():
        print("Antes")
        funcao()
        print("Depois")
    return wrapper

@meu_decorator
def parabenizar():
    print("Parabéns!!!!")

parabenizar()

# resultado = meu_decorator(parabenizar)
# resultado() # O @ substitui essas linhas
'''

# DESAFIO 1
## Crie um decorador que irá pegar a função que for passado para ele e imprimir o horário atual antes de executar a função e depois imprimir o horário após ter finalizado a execução da função.
## Dica: Usar o módulo datetime para conseguir o horário atual.

def monitorar_horario(funcao):
  def monitor():
    print(datetime.now())
    funcao()
    print(datetime.now())
  return monitor

@monitorar_horario
def hora_boa():
  print("Hora boa!!!")

hora_boa()
  