from django.shortcuts import render
from finance.models import *
from finance.utils import *
import json

def index(request):
    get_card_currency_data()
    get_gold_price()
    get_borsa_istanbul_data()
    hisseArray()
    dovizArray()
    
    cardData = CardDataModel.cardData
    goldData = GoldDataModel.goldData
    bistData = BISTDataModel.BISTData
    hisseData = HisseDataModel.hisseData
    dovizData = DovizDataModel.dovizData

    cardDataJSON = json.loads(cardData)
    goldDataJSON = json.loads(goldData)
    bistDataJSON = json.loads(bistData)
    hisseDataJSON = json.loads(hisseData)
    dovizDataJSON = json.loads(dovizData)

    context = {
        'cardData': cardDataJSON,
        'goldData': goldDataJSON,
        'bistData': bistDataJSON,
        'hisseData': hisseDataJSON,
        'dovizData': dovizDataJSON
    }

    return render(request, 'finance/index.html', context)

def hisse(request, id):
    get_card_currency_data()
    get_gold_price()
    get_borsa_istanbul_data()
    hisseArray()
    dovizArray()
    
    cardData = CardDataModel.cardData
    goldData = GoldDataModel.goldData
    bistData = BISTDataModel.BISTData
    hisseData = HisseDataModel.hisseData
    dovizData = DovizDataModel.dovizData

    cardDataJSON = json.loads(cardData)
    goldDataJSON = json.loads(goldData)
    bistDataJSON = json.loads(bistData)
    hisseDataJSON = json.loads(hisseData)
    dovizDataJSON = json.loads(dovizData)

    selectedData = None
    for data in hisseDataJSON:
        if data["HisseName"] == id:
            selectedData = data
            break

    context = {
        'id': id,
        'cardData': cardDataJSON,
        'goldData': goldDataJSON,
        'bistData': bistDataJSON,
        'hisseData': hisseDataJSON,
        'dovizData': dovizDataJSON,
        'selectedData':selectedData
    }
    
    return render(request, "finance/hisse.html", context)

def doviz(request, id):
    get_card_currency_data()
    get_gold_price()
    get_borsa_istanbul_data()
    hisseArray()
    dovizArray()
    
    cardData = CardDataModel.cardData
    goldData = GoldDataModel.goldData
    bistData = BISTDataModel.BISTData
    hisseData = HisseDataModel.hisseData
    dovizData = DovizDataModel.dovizData

    cardDataJSON = json.loads(cardData)
    goldDataJSON = json.loads(goldData)
    bistDataJSON = json.loads(bistData)
    hisseDataJSON = json.loads(hisseData)
    dovizDataJSON = json.loads(dovizData)

    selectedData = None
    for data in dovizDataJSON:
        if data["DovizName"] == id:
            selectedData = data
            break

    context = {
        'id': id,
        'cardData': cardDataJSON,
        'goldData': goldDataJSON,
        'bistData': bistDataJSON,
        'hisseData': hisseDataJSON,
        'dovizData': dovizDataJSON,
        'selectedData':selectedData
    }
    
    return render(request, "finance/doviz.html", context)

def altin(request, id):
    get_card_currency_data()
    get_gold_price()
    get_borsa_istanbul_data()
    hisseArray()
    dovizArray()
    
    cardData = CardDataModel.cardData
    goldData = GoldDataModel.goldData
    bistData = BISTDataModel.BISTData
    hisseData = HisseDataModel.hisseData
    dovizData = DovizDataModel.dovizData

    cardDataJSON = json.loads(cardData)
    goldDataJSON = json.loads(goldData)
    bistDataJSON = json.loads(bistData)
    hisseDataJSON = json.loads(hisseData)
    dovizDataJSON = json.loads(dovizData)

    selectedData = None
    for data in goldDataJSON:
        if data["GoldName"] == id:
            selectedData = data
            break

    context = {
        'id': id,
        'cardData': cardDataJSON,
        'goldData': goldDataJSON,
        'bistData': bistDataJSON,
        'hisseData': hisseDataJSON,
        'dovizData': dovizDataJSON,
        'selectedData':selectedData
    }
    
    return render(request, "finance/altin.html", context)

def bist(request, id):
    get_card_currency_data()
    get_gold_price()
    get_borsa_istanbul_data()
    hisseArray()
    dovizArray()
    
    cardData = CardDataModel.cardData
    goldData = GoldDataModel.goldData
    bistData = BISTDataModel.BISTData
    hisseData = HisseDataModel.hisseData
    dovizData = DovizDataModel.dovizData

    cardDataJSON = json.loads(cardData)
    goldDataJSON = json.loads(goldData)
    bistDataJSON = json.loads(bistData)
    hisseDataJSON = json.loads(hisseData)
    dovizDataJSON = json.loads(dovizData)

    selectedData = None
    for data in bistDataJSON:
        if data["BISTName"] == id:
            selectedData = data
            break

    context = {
        'id': id,
        'cardData': cardDataJSON,
        'goldData': goldDataJSON,
        'bistData': bistDataJSON,
        'hisseData': hisseDataJSON,
        'dovizData': dovizDataJSON,
        'selectedData':selectedData
    }
    
    return render(request, "finance/bist.html", context)