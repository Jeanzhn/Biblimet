import PySimpleGUI as psg

psg.theme('DarkGreen7')

layout = [
    [psg.Text('Projetinho?')],
    [psg.Button('Sim'), psg.Button('Sair')]
]

window = psg.Window('', layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Sim':
        psg.popup('BYEBYE')
window.close()
