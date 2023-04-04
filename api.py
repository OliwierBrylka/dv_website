import requests
import json
import pandas as pd



global url, token
url = "https://api.baselinker.com/connector.php"
token = "1001116-1005478-DDJL1VP93GA367QZFWQ979ZVNKIJGZGCE23NH5LMLIIT6CIY9XSYMDOWHLBIXV3O"


def update_estan():
    


    method = "updateInventoryProductsStock"
    params = {
        "inventory_id": "5284",
        "products": {
            "64368825": {
                "bl_7329": 10000
            }
        }
    }

    payload = {
        "token": token,
        "method": method,
        "parameters": json.dumps(params)
    }
    response = requests.post(url, data=payload)
    print(response.json())



def get_estan():
    data = pd.read_excel(r'Zeszyt1.xlsx', sheet_name='Arkusz1')
    df = pd.DataFrame(data, columns=['Indeks'])
    return df


def match():

    params = {
        'inventory_id':'5284',
        'filter_sku': 'DV-TEST-TW',
    }
    payload = {
        'token': token,
        'method': 'getInventoryProductsList',
        'parameters': json.dumps(params)
    }
    response = requests.post(url, data=payload)
    baza = json.loads(response.text)
    print(baza)

match()
