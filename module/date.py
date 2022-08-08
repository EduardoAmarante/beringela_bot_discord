from datetime import datetime


def hour():
    l = []
    atual = datetime.now().strftime('%Y-%m-%dT%H:%M')#%H:%M:%S
    l.append(atual)

    ant = atual.split('T')
    ant = ant[1].split(':')
    ant = int(ant[0])-1

    if ant <0:
        ant = '00'

    ant =  datetime.now().strftime('%Y-%m-%dTx:%M').replace('x',str(ant))
    l.append(ant)

    return l



