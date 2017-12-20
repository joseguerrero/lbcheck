import requests

"""
Referential LBC AD API SPEC
{
    "data": {
        "require_feedback_score": 0,
        "hidden_by_opening_hours": False, 
        "trusted_required": False, 
        "currency": "", 
        "require_identification": True, 
        "age_days_coefficient_limit": "0.00", 
        "is_local_office": False, 
        "first_time_limit_btc": None, 
        "city": "", 
        "location_string": "", 
        "countrycode": "", 
        "max_amount": "10", 
        "lon": 0.0, 
        "sms_verification_required": True, 
        "require_trade_volume": 0.0, 
        "online_provider": "SPECIFIC_BANK", 
        "max_amount_available": "0", 
        "msg": "I buy your cryptos!", 
        "email": None, 
        "volume_coefficient_btc": "1", 
        "profile": {
            "username": "xxxx", 
            "feedback_score": 100, 
            "trade_count": "500+", 
            "name": "xxxx (500+; 100%)", 
            "last_online": ""}, 
            "bank_name": "", 
            "trade_type": "", 
            "ad_id": 1, 
            "temp_price": "", 
            "payment_window_minutes": 90, 
            "min_amount": "1", 
            "limit_to_fiat_amounts": "", 
            "require_trusted_by_advertiser": False, 
            "temp_price_usd": "", 
            "lat": 0.0, "visible": True, 
            "created_at": "", 
            "atm_model": None, 
            "is_low_risk": False
    }, 
    "actions": {
        "public_view": ""
    }
}

"""

def is_last(url, payload, pages):

    r = requests.get(url, params=payload)

    pages.append(r.json()['data']['ad_list'])

    next_pag = r.json().get('pagination').get('next', None)

    if next_pag:
        print next_pag
        return is_last(next_pag, payload, pages)
    else:
        return pages

treshold = 0

bank_name = ''

currency = ''

country = ''

countrycode = ''

url = 'https://localbitcoins.com/sell-bitcoins-online/%(cc)s/%(country)s/transfers-with-specific-bank/.json?' % {'cc' : countrycode, 'country': country}

payload = {'fields': 'public_view,min_amount,max_amount,temp_price,bank_name,currency'}

pages = []

results = is_last(url, payload, pages)

merged_results = [item for sublist in results for item in sublist]

for ad in merged_results:
    if bank_name in ad['data']['bank_name'].lower() \
     and ad['data']['currency'] == currency \
     and float(ad['data']['temp_price']) >= float(treshold):
        print "#########################################################################"
        #print ad_data.get('msg')
        print ad['actions']['public_view']
        print ad['data']['min_amount']
        print ad['data']['max_amount']
        print ad['data']['temp_price'], ad['data']['currency'], "/ BTC"
        print "#########################################################################\n"
