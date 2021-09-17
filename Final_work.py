#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tqdm import tqdm
import requests
import json
urlp = []
likes= []
size = []
token1 = input('Введите токен: ')
idvk = input('Введите айди вк: ')
api = requests.get('https://api.vk.com/method/photos.get', params ={
        'owner_id': idvk,
        'access_token': '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008',
        'album_id': 'profile',
        'photo_sizes':0,
        'extended':1,
        'v':5.81
    } )
m = json.loads(api.text)
for i in m['response']['items']:
    urlp.append(i['sizes'][-1]['url'])
    size.append(i['sizes'][-1]['type'])
for i in m['response']['items']:
    li = i['likes']['count']
    date = i['date']
    if (f'{li}.jpg') in likes:
        likes.append(f'{li},{date}.jpg')
    else:
        likes.append(f'{li}.jpg')

num = len(urlp)
url = 'https://cloud-api.yandex.net/v1/disk/'
publish = 'resources/upload'
token = token1
headers = {'accept': 'application/json', 'authorization' : f'OAuth {token}'}
requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params={'path': 'Fotos'})
for pics in tqdm(range(num)):
    requests.post(url+publish, headers=headers, params={'path': f'Fotos/{likes[pics]}',
                                                                'url':urlp[pics]})
    try:
        data = json.load(open('jfile'))
    except:
        data = []
    data.append({"file_name": likes[pics],
    "size": size[pics]})
    with open('jfile', 'w') as file:
        json.dump(data, file, indent=2)
with open('jfile', 'r') as file:
    js= json.load(file)
print(js)


# In[ ]:




