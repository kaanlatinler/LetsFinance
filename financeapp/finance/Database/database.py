import pypyodbc
import uuid
import json

class Database:
    connStr = 'DRIVER={SQL Server};SERVER=KAAN\\SQLEXPRESS;DATABASE=LetsFinance'

    def DeleteDataFrom(self, table):
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM {}".format(table))
        connection.commit()
        connection.close()
        
    def SaveCardData(self, data):
        Database().DeleteDataFrom("CardData")
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        for item in data:
            cursor.execute("INSERT INTO CardData (CardID, CardName, CardSellPrice, CardBuyPrice, CardIco) VALUES (?, ?, ?, ?, ?)",
                           (str(uuid.uuid4()), item['Name'], item['SellingStr'], item['BuyingStr'], item['ico']))
        connection.commit()
        connection.close()
    
    def GetCardData(self):
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CardData")
        CardDatas = cursor.fetchall()
        connection.close()

        card_data_json = []
        for row in CardDatas:
            card_data_json.append({
                'CardDataID': row[0],
                'CardID': row[1],
                'CardName': row[2],
                'CardSellPrice': row[3],
                'CardBuyPrice': row[4],
                'CardIco': row[5]
            })

        return json.dumps(card_data_json)

    def SaveGoldData(self, data):
        Database().DeleteDataFrom("GoldData")
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        for item in data:
            cursor.execute("INSERT INTO GoldData (GoldID, GoldName, GoldSellPrice, GoldBuyPrice) VALUES (?, ?, ?, ?)",
                           (str(uuid.uuid4()), item['Name'], item['Price'], item['Buy']))
        connection.commit()
        connection.close()

    def GetGoldData(self):
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM GoldData")
        GoldDatas = cursor.fetchall()
        connection.close()

        gold_data_json = []
        for row in GoldDatas:
            gold_data_json.append({
                'GoldDataID': row[0],
                'GoldID': row[1],
                'GoldName': row[2],
                'GoldSellPrice': row[3],
                "GoldBuyPrice": row[4],
            })

        return json.dumps(gold_data_json)

    def SaveBISTData(self, data):
        Database().DeleteDataFrom("BISTData")
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        for item in data:
            cursor.execute("INSERT INTO BISTData (BISTID, BISTName, BISTSellPrice, BISTOpen, BISTClose) VALUES (?, ?, ?, ?, ?)",
                           (str(uuid.uuid4()), item['name'], item['Price'], item['Open'], item['Close']))
        connection.commit()
        connection.close()

    def GetBISTData(self):
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM BISTData")
        BISTDatas = cursor.fetchall()
        connection.close()

        bist_data_json = []
        for row in BISTDatas:
            bist_data_json.append({
                'BISTDataID': row[0],
                'BISTID': row[1],
                'BISTName': row[2],
                'BISTSellPrice': row[3],
                "BISTOpen": row[4],
                "BISTClose": row[5]
            })

        return json.dumps(bist_data_json)

    def SaveHisseData(self, data):
        Database().DeleteDataFrom("HisseData")
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        for item in data:
            cursor.execute("INSERT INTO HisseData (HisseID, HisseName, HisseRate, HisseTime, HissePrice) VALUES (?, ?, ?, ?, ?)",
                           (str(uuid.uuid4()), item['NAME'], item['RATE'], item['TIME'], item['PRICE']))
        connection.commit()
        connection.close()

    def GetHisseData(self):
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM HisseData")
        HisseDatas = cursor.fetchall()
        connection.close()

        hisse_data_json = []
        for row in HisseDatas:
            hisse_data_json.append({
                'HisseDataID': row[0],
                'HisseID': row[1],
                'HisseName': row[2],
                'HisseRate': row[3],
                'HisseTime': row[4],
                'HissePrice': row[5]
            })

        return json.dumps(hisse_data_json)

    def SaveDovizData(self, data):
        Database().DeleteDataFrom("DovizData")
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        for item in data:
            cursor.execute("INSERT INTO DovizData (DovizID, DovizName, DovizSellPrice, DovizBuyPrice, DovizCode) VALUES (?, ?, ?, ?, ?)",
                           (str(uuid.uuid4()), item['Name'], item['SellingStr'], item['BuyingStr'], item['Code']))
        connection.commit()
        connection.close()

    def GetDovizData(self):
        connection = pypyodbc.connect(Database.connStr)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM DovizData")
        DovizDatas = cursor.fetchall()
        connection.close()

        doviz_data_json = []
        for row in DovizDatas:
            doviz_data_json.append({
                'DovizDataID': row[0],
                'DovizID': row[1],
                'DovizName': row[2],
                'DovizSellPrice': row[3],
                'DovizBuyPrice': row[4],
                'DovizCode': row[5]
            })

        return json.dumps(doviz_data_json)