import yaml

def load_data():
    with open('produtos.yaml') as f:
        
        data = yaml.load(f, Loader=yaml.FullLoader)
        #print(data)
        return data

def add_item(data,item = []):
    print(item)

    data['produtos'][item[0]] = [item[1]]
    salve_data(data)

def add_img(data,item,img_url):
    lista = data['produtos'][item]
    lista.append(img_url) 
    salve_data(data)

def salve_data(data):
    with open('produtos.yaml', 'wt') as f:
        yaml.dump(data, f, encoding='utf-8')
        print("salvo: ",data)
