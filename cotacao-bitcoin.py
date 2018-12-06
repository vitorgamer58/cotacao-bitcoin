import requests
import locale
import time

def cotacao():
    #definir locale para Brasil para formato de moeda
    locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')

    #BRAZILIEX
    braziliex = requests.get("https://braziliex.com/api/v1/public/ticker/btc_brl") 
    databrlz = braziliex.json()
    pricebrlz = databrlz['last']
    pricebrlz = float(pricebrlz)
    volumebraziliex = databrlz['baseVolume']
    volumebraziliex = float(volumebraziliex)
    variavelbraziliex = (pricebrlz*volumebraziliex)
    page = requests.get("https://braziliex.com/api/v1/public/ticker/btc_brl")

    #BITCOINTRADE
    bitcointrade = requests.get("https://api.bitcointrade.com.br/v1/public/BTC/ticker")
    databitcointrade = bitcointrade.json()
    pricebitcointrade = databitcointrade['data']['last']
    volumebitcointrade = databitcointrade['data']['volume']
    pricebitcointrade = float(pricebitcointrade)
    volumebitcointrade = float(volumebitcointrade)
    variavelbitcointrade = pricebitcointrade*volumebitcointrade

    #WALLTIME
    walltime = requests.get('https://s3.amazonaws.com/data-production-walltime-info/production/dynamic/walltime-info.json?now=1528962473468.679.0000000000873')
    datawalltime = walltime.json()
    pricewalltime = datawalltime['BRL_XBT']['last_inexact']
    pricewalltime = float(pricewalltime)
    volumewalltime = datawalltime['BRL_XBT']['quote_volume24h_inexact']
    volumewalltime = float(volumewalltime)
    variavelwalltime = pricewalltime*volumewalltime

    #PROFITIFY
    #dataprofitify = profitify.json()
    #priceprofitify = dataprofitify['last']
    #priceprofitify = float(priceprofitify)
    #volumeprofitify = dataprofitify['volume']
    #volumeprofitify = float(volumeprofitify)
    #variavelprofitify = priceprofitify*volumeprofitify

    #NEGOCIECOINS
    negociecoins = requests.get('https://broker.negociecoins.com.br/api/v3/btcbrl/ticker')
    datanegociecoins = negociecoins.json()
    pricenegociecoins = datanegociecoins['last']
    pricenegociecoins = float(pricenegociecoins)
    volumenegociecoins = datanegociecoins['vol']
    volumenegociecoins = float(volumenegociecoins)
    variavelnegociecoins = pricenegociecoins*volumenegociecoins

    #BITCOINTOYOU
    bitcointoyou = requests.get('https://www.bitcointoyou.com/api/ticker.aspx')
    databitcointoyou = bitcointoyou.json()
    pricebitcointoyou = databitcointoyou['ticker']['last']
    pricebitcointoyou = float(pricebitcointoyou)
    volumebitcointoyou = databitcointoyou['ticker']['vol']
    volumebitcointoyou = float(volumebitcointoyou)
    variavelbitcointoyou = pricebitcointoyou*volumebitcointoyou

    #MERCADOBITCOIN
    mercadobitcoin = requests.get('https://www.mercadobitcoin.net/api/btc/ticker/')
    datamercadobitcoin = mercadobitcoin.json()
    pricemercadobitcoin = datamercadobitcoin['ticker']['last']
    pricemercadobitcoin = float(pricemercadobitcoin)
    volumemercadobitcoin = datamercadobitcoin['ticker']['vol']
    volumemercadobitcoin = float(volumemercadobitcoin)
    variavelmercadobitcoin = pricemercadobitcoin*volumemercadobitcoin
    #FLOWBTC
    flowbtc = requests.get('https://publicapi.flowbtc.com.br/v1/ticker/btcbrl')
    dataflowbtc = flowbtc.json()
    priceflowbtc = dataflowbtc['data']['LastTradedPx']
    priceflowbtc = float(priceflowbtc)
    volumeflowbtc = dataflowbtc['data']['Rolling24HrVolume']
    volumeflowbtc = float(volumeflowbtc)
    variavelflowbtc = priceflowbtc*volumeflowbtc


    volumetotal = volumebraziliex+volumebitcointrade+volumewalltime+volumenegociecoins+volumebitcointoyou+volumemercadobitcoin+volumeflowbtc
    precoponderado = ((variavelbraziliex+variavelbitcointrade+variavelwalltime+variavelnegociecoins+variavelbitcointoyou+variavelmercadobitcoin+variavelflowbtc))/volumetotal #Media Ponderada
    
    #calcula o marketshare de cada exchange
    pbraziliex = round(((volumebraziliex/volumetotal)*100), 3)
    pbitcointrade = round(((volumebitcointrade/volumetotal)*100), 3)
    pwalltime = round(((volumewalltime/volumetotal)*100), 3)
    #pprofitify = round(((volumeprofitify/volumetotal)*100), 3)
    pnegociecoins = round(((volumenegociecoins/volumetotal)*100), 3)
    pbitcointoyou = round(((volumebitcointoyou/volumetotal)*100), 3)
    pmercadobitcoin = round(((volumemercadobitcoin/volumetotal)*100), 3)
    pflowbtc = round(((volumeflowbtc/volumetotal)*100), 3)


    #converte os valores para o padrao brasileiro e inclui o simbolo R$
    pricebrlz = locale.currency( pricebrlz, grouping=True )
    pricebitcointrade = locale.currency( pricebitcointrade, grouping=True )
    pricewalltime = locale.currency( pricewalltime, grouping=True )
    #priceprofitify = locale.currency( priceprofitify, grouping=True )
    pricenegociecoins = locale.currency( pricenegociecoins, grouping=True )
    pricebitcointoyou = locale.currency( pricebitcointoyou, grouping=True )
    pricemercadobitcoin = locale.currency( pricemercadobitcoin, grouping=True )
    priceflowbtc = locale.currency( priceflowbtc, grouping=True )
    precoponderado = locale.currency( precoponderado, grouping=True )

    #imprime os dados
    print 'O preco da braziliex e:', pricebrlz, 'detendo', pbraziliex,'% do volume total'
    print 'O preco da bitcointrade e:', pricebitcointrade, 'detendo', pbitcointrade,'% do volume total'
    print 'O preco da walltime e:', pricewalltime, 'detendo', pwalltime,'% do volume total'
    #print 'o preco da profitify e: ', priceprofitify, 'detendo', pprofitify,'% do volume total'
    print 'O preco da negociecoins e:', pricenegociecoins, 'detendo', pnegociecoins,'% do volume total'
    print 'O preco da bitcointoyou e:', pricebitcointoyou, 'detendo', pbitcointoyou,'% do volume total'
    print 'O preco do mercadobitcoin e:', pricemercadobitcoin, 'detendo', pmercadobitcoin,'% do volume total'
    print 'o preco da flowbtc e:', priceflowbtc, 'detendo', pflowbtc,'% do volume total'
    pricefinal = ("O preco medio ponderado e:"), precoponderado, ("com volume de"), volumetotal
    return pricefinal #imprime a media ponderada de preco com relacao ao volume das exchanges
print(cotacao())
time.sleep(10)
print(cotacao())