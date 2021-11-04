from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from quotesapp.models import ExRate
from quotesapp.serializers import ExRateSer
from quotesapp.utils import get_btc_usd_details

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getQuote(request):

    # Before processing the request verify if BTC/USD exchange details
    # are successfully retrieved
    resp = get_btc_usd_details()
    if resp.status_code == 200:
        if request.method == 'GET':
            # GET will return the BTC/USD exchange rate
            resp_data = {}
            resp = get_btc_usd_details()
            var_ex_rate = resp.json()['Realtime Currency Exchange Rate'][r'5. Exchange Rate']
            resp_data['btcusd_exchange_rate'] = var_ex_rate
            return JsonResponse(resp_data, safe=False)

        elif request.method == 'POST':
            # POST will return the BTC/USD ask & bid price details
            resp_data = {}
            resp = get_btc_usd_details()
            var_bid_price = resp.json()['Realtime Currency Exchange Rate'][r'8. Bid Price']
            var_ask_price = resp.json()['Realtime Currency Exchange Rate'][r'9. Ask Price']
            resp_data['btcusd_bid_price'] = var_bid_price
            resp_data['btcusd_ask_price'] = var_ask_price
            return JsonResponse(resp_data, safe=False)
    else:
        # If the details are not fetched, returning the alphavantage API response directly
        # to the client.
        # Possible TODO: Custom response can be sent here
        return resp
