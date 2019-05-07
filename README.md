# cotacao-bitcoin
Cotação média do Bitcoin

Python script que imprime a cotação média do bitcoin. 

Utiliza as bibliotecas requests e locale. 

Fonte das cotações: *API das exchanges*

Exchanges utilizadas
```
Braziliex

Bitcointrade

Walltime

NegocieCoins

BitcoinToYou

MercadoBitcoin

FlowBTC
```
![](https://raw.githubusercontent.com/vitorgamer58/cotacao-bitcoin/master/running.png)

Maiores informações nos comentários do código.

# Troubleshooting

Em caso de erro: locale.Error: unsupported locale setting

Em Debian e derivados abra um terminal e digite: 

**$ sudo dpkg-reconfigure locales **

Marque o locale desejado, neste caso pt_BR.UTF-8 e confirme. 

Aos usuários de outras distros, pesquisem sobre como gerar locales no sistema. 
