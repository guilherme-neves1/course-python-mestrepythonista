# String dinâmicos
nome = 'Guilherme'
email = 'guilherme@gmail.com'

# Olá Guilherme, você cadastrou o email guilherme@gmail.com, essa informação está correta?
# ERRADO: print('Olá', nome, ',você cadastrou o email',email,', essa informação está correta?')

print(f'Olá {nome}, você cadastrou o email {email}, essa informação está correta?')

# DESAFIO 1
## Crie os seguintes strings dinâmicos

nome = 'Carol'
hobby = 'ouvir músicas.'
# Olá sou a Carol e gosto de ouvir músicas
print(f'Olá sou a {nome} e gosto de {hobby}')

# DESAFIO 2
## Monte as seguintes palavras, usando as sílabas como base
b = 'ba'
parte2 = 'nica'
a = 'a'
r = 'ri'
parte1 = 'eletrô'
t = 'te'
# Resultado: bateria eletrônica
print(f'{b}{t}{r}{a} {parte1}{parte2}')