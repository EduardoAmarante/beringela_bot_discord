caminho = "D:/Clips/"
URL = 'https://api.twitch.tv/helix/streams?user_login={}'
authURL = 'https://id.twitch.tv/oauth2/token'

listaIdBroad = []
listaNomeStreamer = []
AutParams = {'client_id': CLIENT_ID_TWITCH,
             'client_secret': TWITCH_SECRET,
             'grant_type': 'client_credentials'
             }

dataFim = datetime.today()#.strftime('%Y-%m-%d')
periodo = relativedelta(days=+15)
dataDia = dataFim - periodo

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

def clipsHora(idstreamer,dataI,dataF,qntdVideos,streamer):
    AutCall = requests.post(url=authURL, params=AutParams) 
    access_token = AutCall.json()['access_token']

    head = {
    'Authorization' :  "Bearer " + access_token,
      'Client-ID' : CLIENT_ID_TWITCH,
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

streamers = { "cidcidoso":"138375255",
    "alanzoka":"38244180",
    "anaclara":"463843332",
    "faye_tan":479479605,
    "ratoborrachudo":51891532}