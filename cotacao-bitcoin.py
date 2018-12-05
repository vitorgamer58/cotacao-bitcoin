import requests
import locale
#definir locale para Brasil para formato de moeda
locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')
#baixando os dados da pagina
braziliex = requests.get("https://braziliex.com/api/v1/public/ticker/btc_brl") 
#parseando os valores JSON para o objeto "data"
databrlz = braziliex.json()
pricebrlz = databrlz['last']
pricebrlz = float(pricebrlz)
volumebraziliex = databrlz['baseVolume']
volumebraziliex = float(volumebraziliex)
variavelbraziliex = (pricebrlz*volumebraziliex)
page = requests.get("https://braziliex.com/api/v1/public/ticker/btc_brl")

bitcointrade = requests.get("https://api.bitcointrade.com.br/v1/public/BTC/ticker")
databitcointrade = bitcointrade.json()
pricebitcointrade = databitcointrade['data']['last']
volumebitcointrade = databitcointrade['data']['volume']
pricebitcointrade = float(pricebitcointrade)
volumebitcointrade = float(volumebitcointrade)
variavelbitcointrade = pricebitcointrade*volumebitcointrade

pesos = volumebraziliex+volumebitcointrade
precoponderado = (variavelbraziliex+variavelbitcointrade)/pesos #Media Ponderada

print pricebrlz
print pricebitcointrade
print precoponderado
