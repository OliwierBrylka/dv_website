# pip install APScheduler
from django.conf import settings
import requests
import json
import random
import os
from estan.models import estan


def update_estan():

    url = "https://api.baselinker.com/connector.php"
    token = "1001116-1005478-DDJL1VP93GA367QZFWQ979ZVNKIJGZGCE23NH5LMLIIT6CIY9XSYMDOWHLBIXV3O"

    method = "updateInventoryProductsStock"
    params = {
        "inventory_id": "5284",
        "products": {
            "64368825": {
                "bl_7329": 1245
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
