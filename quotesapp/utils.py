import requests
import os

from core.settings import env
from quotesapp.models import ExRate

from quotesapp.models import ExRate
from quotesapp.serializers import ExRateSer

def write_btcusd_price():
    """
    This function will write the BTC exchange rate to the postgresql DB
    """
    # Get the BTC USD exchange rate details using Alphavantage API.
    resp = get_btc_usd_details()
    q_data = {}

    var_ex_rate = resp.json()['Realtime Currency Exchange Rate'][r'5. Exchange Rate']
    var_lst = resp.json()['Realtime Currency Exchange Rate'][r'6. Last Refreshed']
    if resp.status_code == 200:
        q_data['ex_rate'] = var_ex_rate
        q_data['lst_refreshed_ts'] = var_lst
        
        ex_ser = ExRateSer(data=q_data)
        if ex_ser.is_valid():
            ex_ser.save()

    return resp


def get_btc_usd_details():
    """
    This function will get the BTC USD exchange rate details using Alphavantage API.
    """
    api_key = env("API_KEY")
    aa_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=api_key"
    resp = requests.get(aa_url)
    return resp
