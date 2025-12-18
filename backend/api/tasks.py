import requests
from .models import EuronextData, FtseData, Snp500Data, Nikkei225Data, SseData
from datetime import date

datefrom = "2015-01-01"

today = date.today()
dateto = today.isoformat()

api_key = "xjDy6auzJiNBaXQjmERBIGb84lN93EsR"


def create_url(symbol, datefrom, dateto, apikey):
    return (
        "https://financialmodelingprep.com/stable/historical-price-eod/full?"
        + f"apikey={apikey}"
        + f"&from={datefrom}"
        + f"&to={dateto}"
        + f"&symbol={symbol}"
    )


def fetch_daily_data():
    ftse_api_url = create_url("^FTSE", datefrom, dateto, api_key)
    ftse_response = requests.get(ftse_api_url, timeout=30)

    if ftse_response.status_code == 200:
        data = ftse_response.json()

        if isinstance(data, list):
            for item in data:
                FtseData.objects.update_or_create(
                    date=item["date"],
                    defaults={
                        "open": item["open"],
                        "high": item["high"],
                        "low": item["low"],
                        "close": item["close"],
                        "volume": item["volume"],
                        "change": item["change"],
                        "changePercent": item.get("changePercent"),
                    },
                )

    snp500_api_url = create_url("^GSPC", datefrom, dateto, api_key)
    snp500_response = requests.get(snp500_api_url, timeout=30)

    if snp500_response.status_code == 200:
        data = snp500_response.json()

        if isinstance(data, list):
            for item in data:
                Snp500Data.objects.update_or_create(
                    date=item["date"],
                    defaults={
                        "open": item["open"],
                        "high": item["high"],
                        "low": item["low"],
                        "close": item["close"],
                        "volume": item["volume"],
                        "change": item["change"],
                        "changePercent": item.get("changePercent"),
                    },
                )
    nikkei225_api_url = create_url("^N225", datefrom, dateto, api_key)
    nikkei225_response = requests.get(nikkei225_api_url, timeout=30)

    if nikkei225_response.status_code == 200:
        data = nikkei225_response.json()

        if isinstance(data, list):
            for item in data:
                Nikkei225Data.objects.update_or_create(
                    date=item["date"],
                    defaults={
                        "open": item["open"],
                        "high": item["high"],
                        "low": item["low"],
                        "close": item["close"],
                        "volume": item["volume"],
                        "change": item["change"],
                        "changePercent": item.get("changePercent"),
                    },
                )

    Euronext_api_url = create_url("^n100", datefrom, dateto, api_key)
    Euronext_response = requests.get(Euronext_api_url, timeout=30)

    if Euronext_response.status_code == 200:
        data = Euronext_response.json()

        if isinstance(data, list):
            for item in data:
                EuronextData.objects.update_or_create(
                    date=item["date"],
                    defaults={
                        "open": item["open"],
                        "high": item["high"],
                        "low": item["low"],
                        "close": item["close"],
                        "volume": item["volume"],
                        "change": item["change"],
                        "changePercent": item.get("changePercent"),
                    },
                )

    Sse_api_url = create_url("000001.SS", datefrom, dateto, api_key)
    Sse_response = requests.get(Sse_api_url, timeout=30)

    if Sse_response.status_code == 200:
        data = Sse_response.json()

        if isinstance(data, list):
            for item in data:
                SseData.objects.update_or_create(
                    date=item["date"],
                    defaults={
                        "open": item["open"],
                        "high": item["high"],
                        "low": item["low"],
                        "close": item["close"],
                        "volume": item["volume"],
                        "change": item["change"],
                        "changePercent": item.get("changePercent"),
                    },
                )
