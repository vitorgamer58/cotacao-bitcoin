#python-2.7
#lista de exchanges compativeis: Braziliex, bitcointrade, Walltime, Negocie Coins, Bitcoin To You, Mercado Bitcoin, FlowBTC, Brecoins, TemBTC
import requests
from flask import Flask, jsonify
import locale
import time
import os
import json


#app = flask.Flask(__name__)
#app.config["DEBUG"] = True

def api_all():
    #definir locale para Brasil para formato de moeda
    locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')

    #BRAZILIEX
    braziliex = requests.get("https://braziliex.com/api/v1/public/ticker/btc_brl")
    if(braziliex.status_code==200):
        databrlz = braziliex.json()
        pricebrlz = databrlz['last']
        pricebrlz = float(pricebrlz)
        volumebraziliex = databrlz['baseVolume']
        volumebraziliex = float(volumebraziliex)
        variavelbraziliex = (pricebrlz*volumebraziliex)
    else:
        pricebrlz = 0
        volumebraziliex = 0
        variavelbraziliex = 0
        print 'Braziliex nao disponivel'

    #BITCOINTRADE
    bitcointrade = requests.get("https://api.bitcointrade.com.br/v1/public/BTC/ticker")
    if(bitcointrade.status_code==200):
        databitcointrade = bitcointrade.json()
        pricebitcointrade = databitcointrade['data']['last']
        volumebitcointrade = databitcointrade['data']['volume']
        pricebitcointrade = float(pricebitcointrade)
        volumebitcointrade = float(volumebitcointrade)
        variavelbitcointrade = pricebitcointrade*volumebitcointrade
    else:
        pricebitcointrade = 0
        volumebitcointrade = 0
        variavelbitcointrade = 0
        print 'Bitcointrade nao disponivel'

    #WALLTIME
    walltime = requests.get('https://s3.amazonaws.com/data-production-walltime-info/production/dynamic/walltime-info.json?now=1528962473468.679.0000000000873')
    if(walltime.status_code==200):
        datawalltime = walltime.json()
        pricewalltime = datawalltime['BRL_XBT']['last_inexact']
        pricewalltime = float(pricewalltime)
        volumewalltime = datawalltime['BRL_XBT']['quote_volume24h_inexact']
        volumewalltime = float(volumewalltime)
        variavelwalltime = pricewalltime*volumewalltime
    else:
        pricewalltime = 0
        volumewalltime = 0
        variavelwalltime = 0
        print 'walltime nao disponivel'

    #PROFITIFY
    profitify = requests.get('https://profitfy.trade/apii/v1/public/ticker/btc/brl') #endereco incorreto pois ainda esta em implementacao
    if(profitify.status_code==200):
        dataprofitify = profitify.json()
        priceprofitify = dataprofitify['last']
        priceprofitify = float(priceprofitify)
        volumeprofitify = dataprofitify['volume']
        volumeprofitify = float(volumeprofitify)
        variavelprofitify = priceprofitify*volumeprofitify
    else:
        priceprofitify = 0
        volumeprofitify = 0
        variavelprofitify = 0
        print 'profitify nao disponivel'

    #NEGOCIECOINS
    negociecoins = requests.get('https://broker.negociecoins.com.br/api/v3/btcbrl/ticker')
    if(negociecoins.status_code==200):
        datanegociecoins = negociecoins.json()
        pricenegociecoins = datanegociecoins['last']
        pricenegociecoins = float(pricenegociecoins)
        volumenegociecoins = datanegociecoins['vol']
        volumenegociecoins = float(volumenegociecoins)
        variavelnegociecoins = pricenegociecoins*volumenegociecoins
    else:
        pricenegociecoins = 0
        volumenegociecoins = 0
        variavelnegociecoins = 0

    #BITCOINTOYOU
    bitcointoyou = requests.get('https://www.bitcointoyou.com/api/ticker.aspx')
    if(bitcointoyou.status_code==200):
        databitcointoyou = bitcointoyou.json()
        pricebitcointoyou = databitcointoyou['ticker']['last']
        pricebitcointoyou = float(pricebitcointoyou)
        volumebitcointoyou = databitcointoyou['ticker']['vol']
        volumebitcointoyou = float(volumebitcointoyou)
        variavelbitcointoyou = pricebitcointoyou*volumebitcointoyou
    else:
        pricebitcointoyou = 0
        volumebitcointoyou = 0
        variavelbitcointoyou = 0

    #MERCADOBITCOIN
    mercadobitcoin = requests.get('https://www.mercadobitcoin.net/api/btc/ticker/')
    if(mercadobitcoin.status_code==200):
        datamercadobitcoin = mercadobitcoin.json()
        pricemercadobitcoin = datamercadobitcoin['ticker']['last']
        pricemercadobitcoin = float(pricemercadobitcoin)
        volumemercadobitcoin = datamercadobitcoin['ticker']['vol']
        volumemercadobitcoin = float(volumemercadobitcoin)
        variavelmercadobitcoin = pricemercadobitcoin*volumemercadobitcoin
    else:
        pricemercadobitcoin = 0
        volumemercadobitcoin = 0 
        variavelmercadobitcoin = 0
    
    #FLOWBTC
    flowbtc = requests.get('https://publicapi.flowbtc.com.br/v1/ticker/btcbrl')
    if(flowbtc.status_code==200):
        dataflowbtc = flowbtc.json()
        priceflowbtc = dataflowbtc['data']['LastTradedPx']
        priceflowbtc = float(priceflowbtc)
        volumeflowbtc = dataflowbtc['data']['Rolling24HrVolume']
        volumeflowbtc = float(volumeflowbtc)
        variavelflowbtc = priceflowbtc*volumeflowbtc
    else:
        priceflowbtc = 0
        volumeflowbtc = 0
        variavelflowbtc = 0

    #brecoins
    brecoins = requests.get('https://backend.brecoins.com.br/api/v1/BTC-BRL/ticker')
    if(brecoins.status_code==200):
            databrecoins = brecoins.json()
            pricebrecoins = databrecoins['last']
            volumebrecoins = databrecoins['vol_crypto']
            if type (volumebrecoins)==int:
                pricebrecoins = float(pricebrecoins)
                volumebrecoins = float(volumebrecoins)
                variavelbrecoins = pricebrecoins*volumebrecoins
            else:
                print 'sem volume na brecoins'
                pricebrecoins = 0
                volumebrecoins = 0
                variavelbrecoins = 0
    else:
        print 'brecoins indisponivel'
        pricebrecoins = 0
        volumebrecoins = 0
        variavelbrecoins = 0

    #tembtc
    tembtc = requests.get('https://broker.tembtc.com.br/api/v3/btcbrl/ticker')
    if(tembtc.status_code==200):
        datatembtc = tembtc.json()
        volumetembtc = datatembtc['vol']
        if (volumetembtc>0):
            pricetembtc = datatembtc['last']
            pricetembtc = float(pricetembtc)
            volumetembtc = float(volumetembtc)
            variaveltembtc = pricetembtc*volumetembtc
        else:
            print 'sem volume na tembtc'
            pricetembtc = 0
            volumetembtc = 0
            variaveltembtc = 0
    else:
        print 'tembtc nao disponivel'
        pricetembtc = 0
        volumetembtc = 0
        variaveltembtc = 0

    #coinlib
    coinlib = requests.get('https://coinlib.io/api/v1/coin?key=3602a548384fe25c&pref=BRL&symbol=BTC')
    if(coinlib.status_code==200):
        datacoinlib = coinlib.json()
        pricecoinlib = datacoinlib['price']
        pricecoinlib = float(pricecoinlib)
    else:
        print 'coinlib fora do ar ou excedido limite maximo de requisicoes da API'

    #bitvalor
    bitvalor = requests.get('https://api.bitvalor.com/v1/ticker.json')
    if(bitvalor.status_code==200):
        databitvalor = bitvalor.json()
        pricebitvalor = databitvalor['ticker_24h']['total']['last']
        pricebitvalor = float(pricebitvalor)
    else:
        print 'bitvalor nao disponivel'

    volumetotal = volumebraziliex+volumebitcointrade+volumewalltime+volumenegociecoins+volumebitcointoyou+volumemercadobitcoin+volumeflowbtc+volumebrecoins+volumetembtc
    precoponderado = ((variavelbraziliex+variavelbitcointrade+variavelwalltime+variavelnegociecoins+variavelbitcointoyou+variavelmercadobitcoin+variavelflowbtc+variavelbrecoins+variaveltembtc))/volumetotal #Media Ponderada
    
    #calcula o marketshare de cada exchange
    pbraziliex = round(((volumebraziliex/volumetotal)*100), 3)
    pbitcointrade = round(((volumebitcointrade/volumetotal)*100), 3)
    pwalltime = round(((volumewalltime/volumetotal)*100), 3)
    pprofitify = round(((volumeprofitify/volumetotal)*100), 3)
    pnegociecoins = round(((volumenegociecoins/volumetotal)*100), 3)
    pbitcointoyou = round(((volumebitcointoyou/volumetotal)*100), 3)
    pmercadobitcoin = round(((volumemercadobitcoin/volumetotal)*100), 3)
    pflowbtc = round(((volumeflowbtc/volumetotal)*100), 3)
    pbrecoins = round(((volumebrecoins/volumetotal)*100), 3)
    ptembtc = round(((volumetembtc/volumetotal)*100), 3)
    

    #converte os valores para o padrao brasileiro e inclui o simbolo R$
    pricebrlz = locale.currency( pricebrlz, grouping=True )
    pricebitcointrade = locale.currency( pricebitcointrade, grouping=True )
    pricewalltime = locale.currency( pricewalltime, grouping=True )
    priceprofitify = locale.currency( priceprofitify, grouping=True )
    pricenegociecoins = locale.currency( pricenegociecoins, grouping=True )
    pricebitcointoyou = locale.currency( pricebitcointoyou, grouping=True )
    pricemercadobitcoin = locale.currency( pricemercadobitcoin, grouping=True )
    priceflowbtc = locale.currency( priceflowbtc, grouping=True )
    pricebrecoins = locale.currency( pricebrecoins, grouping=True )
    pricetembtc = locale.currency( pricetembtc, grouping=True )
    pricecoinlib = locale.currency( pricecoinlib, grouping=True )
    pricebitvalor = locale.currency( pricebitvalor, grouping=True )
    precoponderado = locale.currency( precoponderado, grouping=True )

    #imprime os dados
    if(braziliex.status_code==200):
        print 'O preco da braziliex e:', pricebrlz, 'detendo', pbraziliex,'% do volume total'
    if(bitcointrade.status_code==200):
        print 'O preco da bitcointrade e:', pricebitcointrade, 'detendo', pbitcointrade,'% do volume total'
    print 'O preco da walltime e:', pricewalltime, 'detendo', pwalltime,'% do volume total'
    if(profitify.status_code==200):
        print 'o preco da profitify e: ', priceprofitify, 'detendo', pprofitify,'% do volume total'
    print 'O preco da negociecoins e:', pricenegociecoins, 'detendo', pnegociecoins,'% do volume total'
    print 'O preco da bitcointoyou e:', pricebitcointoyou, 'detendo', pbitcointoyou,'% do volume total'
    print 'O preco do mercadobitcoin e:', pricemercadobitcoin, 'detendo', pmercadobitcoin,'% do volume total'
    print 'o preco da flowbtc e:', priceflowbtc, 'detendo', pflowbtc,'% do volume total'
    if(brecoins.status_code==200):
        if (volumebrecoins)==int:
            print 'o preco da brecoins e:', pricebrecoins, 'detendo', pbrecoins,'% do volume total'
    print 'o preco da tembtc e:', pricetembtc, 'detendo', ptembtc,'% do volume total'
    print '' #pula uma linha
    pricefinal = "O preco medio ponderado e:", precoponderado, "com volume de", volumetotal
    print 'o preco do coinlib e:', pricecoinlib, #nao entra no calculo
    print ''
    print 'o preco do bitvalor e:', pricebitvalor #nao entra no calculo
    return pricefinal
print(api_all())
time.sleep(60)
#   bitcoin = {'id': 0,
#   'price': precoponderado,
#   'volume': volumetotal}
    
    #@app.route('/api/v1/btc', methods=['GET'])
    #return jsonify(bitcoin)
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='127.0.0.1', port=port)

