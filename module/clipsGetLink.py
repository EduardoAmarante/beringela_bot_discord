import requests
from datetime import date
from dateutil.relativedelta import relativedelta


caminho = "D:/Clips/"
URL = 'https://api.twitch.tv/helix/streams?user_login={}'
authURL = 'https://id.twitch.tv/oauth2/token'
Client_ID = 'luqk87jms2787vmsyobpzrtg4r71xo'
Secret  = '30ajrw2oiedz6b62jcx2rimt86wnir'
listaIdBroad = []
listaNomeStreamer = []
AutParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }

#dataDia = "2021-10-01"
dataFim = date.today()#.strftime('%Y-%m-%d')
periodo = relativedelta(days=+15)
dataDia = dataFim - periodo


def clipsHora(idstreamer,dataI,dataF,qntdVideos,streamer):
    AutCall = requests.post(url=authURL, params=AutParams) 
    access_token = AutCall.json()['access_token']

    head = {
    'Authorization' :  "Bearer " + access_token,
      'Client-ID' : Client_ID,
    }
    

    #abaixo pega o link pra dowload de 1 unico clip
    #r = requests.get('https://api.twitch.tv/helix/clips?id=IcyIronicClintKappaRoss-onGOoFo3xA1Puf2f', headers = head).json()
    r = requests.get('https://api.twitch.tv/helix/clips?broadcaster_id={}&first={}&started_at={}:18Z&ended_at={}:18Z'.format(idstreamer,qntdVideos,dataI,dataF), headers = head).json()

    listaTitulos = []
    listaMp4 = []
    listaUnicoId =[]
    listaDatas = []
    listaUrlClips = []
    
    for i in range(0,qntdVideos):
        try:
            dicionario = r['data'][i]
        except (UnboundLocalError,NameError):
            print("não há clips para este dia")
            continue
        except:        
            #print("erro no dicionario")
            i+=1
            continue
 
        titulo = dicionario['title'] 
        dataPasta = dicionario["created_at"]
        dataPasta = dataPasta.split("T")
        dataPasta = dataPasta[0]
        mp4 = dicionario["thumbnail_url"] #atribui à variável mp4 o valor do link da thumbnail
        unicoId = dicionario["id"]
        linkmp4 = mp4.replace("-preview-480x272.jpg",".mp4") #converte o link jpg para mp4
        
        urlclip = dicionario['url']

        listaUrlClips.append(urlclip)
        listaDatas.append(dataPasta)
        listaTitulos.append(titulo) #adiciona o titulo na lista
        listaMp4.append(linkmp4) #adiciona o link mp4 apos conversao do jpg
        listaUnicoId.append(unicoId)
        #conjunto.append(listaTitulos[i])
        #conjunto.append(listaMp4[i])


    return listaUrlClips