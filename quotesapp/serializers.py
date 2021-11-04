from rest_framework import serializers
from quotesapp.models import ExRate

class ExRateSer(serializers.ModelSerializer):
    class Meta:
        model=ExRate
        fields=('ex_rate', 'lst_refreshed_ts')
