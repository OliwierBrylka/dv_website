import time
import pandas as pd
import requests
import json

unix = []
first_day = 1677840051
last_day = 1677840034

while first_day <= last_day:
    unix.append(first_day)
    first_day = first_day + 7200 #(2h)

container = []

for i in unix:
    counter = 10
    while counter != 0:
        counter = counter - 1
        time.sleep(1)
    print(f'Add: {i}')
    data = {
        'token': '3012734-3027312-U1B2BTFXU1YL6L4B756ZC93OBOIIMLAZJLEJ5GSOANM5ZS4YVS7EKA029M17G5GL',
        'method': 'getInvoices',
        'parameters': f'{{"date_from": {i}}}'
    }
    response = requests.post('https://api.baselinker.com/connector.php', data=data)
    baza = json.loads(response.text)
    container.append(baza)

df = pd.DataFrame(container)
df.to_json(r'./data.json')