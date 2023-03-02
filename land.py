import requests

def info_alt():
    url = "https://restcountries.com/v3.1/all"
    svar = requests.get(url)
    return svar.json()

def info_land(land):
    url = f"https://restcountries.com/v3.1/name/{land}"
    svar = requests.get(url)
    return svar.json()