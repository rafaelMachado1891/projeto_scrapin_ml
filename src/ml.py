import requests
from bs4 import BeautifulSoup
import pandas as pd


keyword = "Abajur"

url = f"https://lista.mercadolivre.com.br/{keyword}"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("não foi possivel conectar ao site")