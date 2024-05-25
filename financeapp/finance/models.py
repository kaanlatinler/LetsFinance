from finance.Database.database import Database
from django.db import models


class CardDataModel(models.Model):
    cardData = Database().GetCardData()

class GoldDataModel(models.Model):
    goldData = Database().GetGoldData()

class BISTDataModel(models.Model):
    BISTData = Database().GetBISTData()

class HisseDataModel(models.Model):
    hisseData = Database().GetHisseData()

class DovizDataModel(models.Model):
    dovizData = Database().GetDovizData()

