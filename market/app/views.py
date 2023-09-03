import pandas as pd
from django.shortcuts import render, HttpResponse
from app.models import Data

# Create your views here.

def index(request):
    df = pd.read_csv("app/stock_market_data.csv")
    for _, row in df.iterrows():
        Data.objects.create(
            date=row['date'],
            trade_code=row['trade_code'],
            high=row['high'],
            low=row['low'],
            open=row['open'],
            volume=row['volume']
        )
    return render(request, "index.html")