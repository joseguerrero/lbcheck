
#  :point_right: How to use ? :wink:

Configure the following parameters to get the offers you are looking for:

- treshold: Minimum amount accepted for an offer. 
- bank_name: Name of the bank.
- currency: Name of currency.
	- [Currencies](https://localbitcoins.com/api/currencies/) Url that show List of valid and recognized fiat currencies for LocalBitcoins.com. Also contains human readable name for every currency and boolean that tells if currency is an altcoin.
- country = Name of the country.
- countrycode: Country code.
	- [Countrycodes](https://localbitcoins.com/api/currencies/) Url that show the List of valid and recognized countrycodes for LocalBitcoins.com.
- url: Route to obtain offers.
	- If you want to sell: 'https://localbitcoins.com/sell-bitcoins-online/%(cc)s/%(country)s/transfers-with-specific-bank/.json?' % {'cc' : countrycode, 'country': country}.
	- If you want to buy: 'https://localbitcoins.com/buy-bitcoins-online/%(cc)s/%(country)s/transfers-with-specific-bank/.json?' % {'cc' : countrycode, 'country': country}.

## Now a real example: 

```
treshold = 1400000000

bank_name = 'mercantil'

currency = 'VEF'

country = 'venezuela'

countrycode = 'VE'

url = 'https://localbitcoins.com/sell-bitcoins-online/%(cc)s/%(country)s/transfers-with-specific-bank/.json?' % {'cc' : countrycode, 'country': country}
```

## Execute in a terminal

```
$ python lbcheck.py
```


## License

The APP is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).