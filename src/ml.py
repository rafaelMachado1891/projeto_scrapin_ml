import requests
import pandas as pd
from bs4 import BeautifulSoup

keyword = "Abajur"

url = "https://lista.mercadolivre.com.br/{keyword}"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print("não foi possivel conectar ao site")