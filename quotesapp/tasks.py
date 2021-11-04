from __future__ import absolute_import, unicode_literals
from celery.task import periodic_task
from celery.schedules import crontab
from . import utils


# Setting the celery task to write exchange details to DB every hour
@periodic_task(run_every=crontab(minute=0, hour='*/1'), name='write_btc_usd_quote')
def write_btc_usd_quote():
    # Get the BTC USD price
    resp = utils.write_btcusd_price()
    return resp.json()
