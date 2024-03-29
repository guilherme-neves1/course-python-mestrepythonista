import logging

logging.basicConfig(level=logging.DEBUG, filename='f081_app.log', filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')

try:
  email = input('Digite seu email: ')
  senha = int(input('Digite sua senha: '))
  if senha == 1234:
    print('Login feito com sucesso!')
    logging.info(f'{email} entrou em sua conta bancária.')
except ValueError as erro:
  print('Digite apenas números.')
  logging.info(erro)
