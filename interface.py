import PySimpleGUIWeb as sg
from cripto import *
import time

# Layout
sg.change_look_and_feel('DarkBlue13')
layout = [
    [sg.Image('simbolo.png', size=(50, 50))],
    [sg.Text('  ')],
    [sg.Text('Usuário 1:')],
    [sg.Input(key='user1', size=(360, 50))],
    [sg.Text('  ')],
    [sg.Text('Usuário 2:')],
    [sg.Input(key='user2', size=(360, 50))],
    [sg.Text('  ')],
    [sg.Button('Validar', size=(60, 30)), sg.Button('Hack', size=(60, 30)), sg.Button('Sair', size=(60, 30))],
    [sg.Text('  ')],
    [sg.Text('Log:')],
    [sg.Output(size=(360, 250))]
]

# Janela
janela = sg.Window('MetaZap').layout(layout)

while True:
    # Coleta dos dados
    botao, dados = janela.Read()

    # Finalização da janela
    if botao == sg.WINDOW_CLOSED or botao == 'Sair':
        print('Programa encerrado com êxito!')
        janela.close()
        break

    # Execução correta
    if botao == 'Validar':
        msgs_cripto = {'msg1': criptografa('user1', dados['user1']), 'msg2': criptografa('user2', dados['user2'])}

        # Validação das mensagens
        print(valida(msgs_cripto['msg1'], criptografa('user1', dados['user1'])))
        print(valida(msgs_cripto['msg2'], criptografa('user2', dados['user2'])), '\n')

    # Simulação ataque Man-in-the-Middle
    if botao == 'Hack':
        msgs_cripto = {'msg1': criptografa('user1', dados['user1']), 'msg2': criptografa('user2', dados['user2'])}

        # Arquivo com mensagens interceptadas
        with open('dados_hack.txt', 'a', encoding='utf-8') as arq_hack:
            for key in dados.keys():
                arq_hack.write(f'[{time.ctime()}] {key}: {dados[key]}\n')

        # Alteração das mensagens interceptadas
        dados.update({'user1': hacker(dados['user1'])})
        dados.update({'user2': hacker(dados['user2'])})

        # Validação das mensagens
        print(valida(msgs_cripto['msg1'], criptografa('user1', dados['user1'])))
        print(valida(msgs_cripto['msg2'], criptografa('user2', dados['user2'])), '\n')
