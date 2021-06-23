import requests
from bs4 import BeautifulSoup

url = 'https://kompas.com'
try:
    response = requests.get(url)
    if response.status_code==200:
        print(f'Success! {response.status_code}')
        #print(f'Success! {response.text}')
        #BS4
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil pemanggilan Url {url}')
        print(f'Title : {soup.title.string}')

    else:
        print(f'Salah request bossskuh {response.status_code}')
except Exception as lah:
    print(f'Error bos {lah}')
    print('End')