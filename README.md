# cotacao-bitcoin
Cotação do Bitcoin via MercadoBitcoin

Python script que imprime a cotação do bitcoin. Pode ser facilmente adaptado para sua aplicação, bastando para isso copiar a função cotacao().

Utiliza as bibliotecas requests e locale. 

Fonte da cotação: *API do Bitvalor.com*

Maiores informações nos comentários do código.

# Troubleshooting

Em caso de erro: locale.Error: unsupported locale setting

Em Debian e derivados abra um terminal e digite: 

**$ sudo dpkg-reconfigure locales **

Marque o locale desejado, neste caso pt_BR.UTF-8 e confirme. 

Aos usuários de outras distros, pesquisem sobre como gerar locales no sistema. 
