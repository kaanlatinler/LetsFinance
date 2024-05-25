import json 
import http.client
import uuid
from finance.Database.database import Database

api_key = "apikey 3upvqIzhkfd35PPwJpGeOm:12lRp8PyY5h8W3wWnz3XDo"
def get_card_currency_data():
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': api_key,
    }

    conn.request("GET", "/economy/allCurrency", headers=headers)
    res = conn.getresponse()
    data = res.read()

    json_data = json.loads(data.decode("utf-8"))

    filtered_data = [
        {
            "Name": entry["name"],
            "SellingStr": entry["sellingstr"],
            "BuyingStr": entry["buyingstr"],
            "ico": "dollar" if entry["name"] == "Amerikan Doları" else "euro" if entry["name"] == "Euro" else None
        }
        for entry in json_data["result"]
        if entry["name"] in ["Amerikan Doları", "Euro"]
    ]

    db = Database()
    db.SaveCardData(filtered_data)

def get_gold_price():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': api_key
    }

    conn.request("GET", "/economy/goldPrice", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_data = json.loads(data.decode("utf-8"))

    filtered_data = [
        {
            "id": str(uuid.uuid4()),
            "Name": entry["name"],
            "Price": entry["sellingstr"],
            "Buy": entry["buyingstr"]
        }
        for entry in json_data["result"]
        if entry["name"] == "Gram Altın"
    ]

    db = Database()
    db.SaveGoldData(filtered_data)

def get_borsa_istanbul_data():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': api_key
    }

    conn.request("GET", "/economy/borsaIstanbul", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_data = json.loads(data.decode("utf-8"))

    data = [
        {
            "id": str(uuid.uuid4()),
            "name": "BIST100",
            "Price": entry["currentstr"],
            "Open": entry["openingstr"],
            "Close": entry["closingstr"],
        }
        for entry in json_data.get("result")
    ]

    db= Database()
    db.SaveBISTData(data)

def hisseArray():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': api_key
    }

    conn.request("GET", "/economy/hisseSenedi", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_data = json.loads(data.decode("utf-8"))

    data_array = [
        {
            "ID": str(uuid.uuid4()),
            "NAME": entry["code"],
            "PRICE": entry["lastpricestr"],
            "RATE": str(entry["rate"]),
            "TIME": entry["time"],
        }
        for entry in json_data.get("result", [])
    ]

    db = Database()
    db.SaveHisseData(data_array)

def dovizArray():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': api_key
        }

    conn.request("GET", "/economy/allCurrency", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_data = json.loads(data.decode("utf-8"))

    data_array=[
        {
            "id": str(uuid.uuid4()),
            "Name": entry["name"],
            "SellingStr": entry["sellingstr"],
            "BuyingStr": entry["buyingstr"],
            "Code": entry["code"]
        }
        for entry in json_data["result"]
    ]

    db = Database()
    db.SaveDovizData(data_array)