from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import os
import json
import requests, copy, time




def index(request):
    return render(request, 'index.html')

def e_stan(request):
    estan_object = estan.objects.all()
    context = { 'estan': estan_object}
    global url, token, method, method2
    url = "https://api.baselinker.com/connector.php"
    token = "1001116-1005478-DDJL1VP93GA367QZFWQ979ZVNKIJGZGCE23NH5LMLIIT6CIY9XSYMDOWHLBIXV3O"
    method = "getInventoryProductsList"
    method2 = "updateInventoryProductsStock"

    if request.POST.get('form_type') == 'eform':
        if request.method == 'POST':
            for bl_id, value in request.POST.items():
                if bl_id.startswith('estan_'):
                    bl_id = bl_id.split('_')[1]
                    obj = estan.objects.get(bl_id=bl_id)
                    obj.Estan = value
                    obj.save()
            return redirect('estan')
    
    if request.POST.get('form_type') == 'sform':
        fsku = request.POST['sku']
        if fsku is None:
            messages.info(request, 'Puste SKU')
            return redirect('estan')
        else:
            if estan.objects.filter(sku=fsku).exists():
                messages.info(request, 'Obiekt już istnieje!')
                return redirect('estan')
            else:
                params = {
                    "inventory_id": "4591",
                    "filter_sku": fsku
                }

                payload = {
                    "token": token,
                    "method": method,
                    "parameters": json.dumps(params)
                    }
                response = requests.post(url, data=payload)
                print(response.json())
                product_data = list(response.json()['products'].values())[0]
                id = product_data['id']
                sku = product_data['sku']
                ean = product_data['ean']
                name = product_data['name']
                print(id, sku, ean, name)
                new_estan = estan(bl_id = id, sku = sku, ean = ean, Estan = 0, name = name)
                new_estan.save()

                messages.info(request, 'Pomyślnie dodano nowy obiekt!')
                return redirect('estan')

    if request.POST.get('form_type') == 'bform':
        obj = estan.objects.values('bl_id', 'Estan')

        url = "https://api.baselinker.com/connector.php"
        token = "1001116-1005478-DDJL1VP93GA367QZFWQ979ZVNKIJGZGCE23NH5LMLIIT6CIY9XSYMDOWHLBIXV3O"
        method = "updateInventoryProductsStock"
        x = []
        y = []
        for item in obj:
            x.append(item['bl_id'])  #przypisujesz po kolei wartości do listy
            y.append(item['Estan'])
        end = len(obj)
        for i in range(0,end,100):
            try:
                params = {
                    "inventory_id": "4591",
                    "products": {
                        x[i]:{
                            "bl_6143": y[i]
                        },
                        x[i+1]:{
                            "bl_6143": y[i+1]
                        },
                        x[i+2]:{
                            "bl_6143": y[i+2]
                        },
                        x[i+3]:{
                            "bl_6143": y[i+3]
                        },
                        x[i+4]:{
                            "bl_6143": y[i+4]
                        },
                        x[i+5]:{
                            "bl_6143": y[i+5]
                        },
                        x[i+6]:{
                            "bl_6143": y[i+6]
                        },
                        x[i+7]:{
                            "bl_6143": y[i+7]
                        },
                        x[i+8]:{
                            "bl_6143": y[i+8]
                        },
                        x[i+9]:{
                            "bl_6143": y[i+9]
                        },
                        x[i+10]:{
                            "bl_6143": y[i+10]
                        },
                        x[i+11]:{
                            "bl_6143": y[i+11]
                        },
                        x[i+12]:{
                            "bl_6143": y[i+12]
                        },
                        x[i+13]:{
                            "bl_6143": y[i+13]
                        },
                        x[i+14]:{
                            "bl_6143": y[i+14]
                        },
                        x[i+15]:{
                            "bl_6143": y[i+15]
                        },
                        x[i+16]:{
                            "bl_6143": y[i+16]
                        },
                        x[i+17]:{
                            "bl_6143": y[i+17]
                        },
                        x[i+18]:{
                            "bl_6143": y[i+18]
                        },
                        x[i+19]:{
                            "bl_6143": y[i+19]
                        },
                        x[i+20]:{
                            "bl_6143": y[i+20]
                        },
                        x[i+21]:{
                            "bl_6143": y[i+21]
                        },
                        x[i+22]:{
                            "bl_6143": y[i+22]
                        },
                        x[i+23]:{
                            "bl_6143": y[i+23]
                        },
                        x[i+24]:{
                            "bl_6143": y[i+24]
                        },
                        x[i+25]:{
                            "bl_6143": y[i+25]
                        },
                        x[i+26]:{
                            "bl_6143": y[i+26]
                        },
                        x[i+27]:{
                            "bl_6143": y[i+27]
                        },
                        x[i+28]:{
                            "bl_6143": y[i+28]
                        },
                        x[i+29]:{
                            "bl_6143": y[i+29]
                        },
                        x[i+30]:{
                            "bl_6143": y[i+30]
                        },
                        x[i+31]:{
                            "bl_6143": y[i+31]
                        },
                        x[i+32]:{
                            "bl_6143": y[i+32]
                        },
                        x[i+33]:{
                            "bl_6143": y[i+33]
                        },
                        x[i+34]:{
                            "bl_6143": y[i+34]
                        },
                        x[i+35]:{
                            "bl_6143": y[i+35]
                        },
                        x[i+36]:{
                            "bl_6143": y[i+36]
                        },
                        x[i+37]:{
                            "bl_6143": y[i+37]
                        },
                        x[i+38]:{
                            "bl_6143": y[i+38]
                        },
                        x[i+39]:{
                            "bl_6143": y[i+39]
                        },
                        x[i+40]:{
                            "bl_6143": y[i+40]
                        },
                        x[i+41]:{
                            "bl_6143": y[i+41]
                        },
                        x[i+42]:{
                            "bl_6143": y[i+42]
                        },
                        x[i+43]:{
                            "bl_6143": y[i+43]
                        },
                        x[i+44]:{
                            "bl_6143": y[i+44]
                        },
                        x[i+45]:{
                            "bl_6143": y[i+45]
                        },
                        x[i+46]:{
                            "bl_6143": y[i+46]
                        },
                        x[i+47]:{
                            "bl_6143": y[i+47]
                        },
                        x[i+48]:{
                            "bl_6143": y[i+48]
                        },
                        x[i+49]:{
                            "bl_6143": y[i+49]
                        },
                        x[i+50]:{
                            "bl_6143": y[i+50]
                        },
                        x[i+51]:{
                            "bl_6143": y[i+51]
                        },
                        x[i+52]:{
                            "bl_6143": y[i+52]
                        },
                        x[i+53]:{
                            "bl_6143": y[i+53]
                        },
                        x[i+54]:{
                            "bl_6143": y[i+54]
                        },
                        x[i+55]:{
                            "bl_6143": y[i+55]
                        },
                        x[i+56]:{
                            "bl_6143": y[i+56]
                        },
                        x[i+57]:{
                            "bl_6143": y[i+57]
                        },
                        x[i+58]:{
                            "bl_6143": y[i+58]
                        },
                        x[i+59]:{
                            "bl_6143": y[i+59]
                        },
                        x[i+60]:{
                            "bl_6143": y[i+60]
                        },
                        x[i+61]:{
                            "bl_6143": y[i+61]
                        },
                        x[i+62]:{
                            "bl_6143": y[i+62]
                        },
                        x[i+63]:{
                            "bl_6143": y[i+63]
                        },
                        x[i+64]:{
                            "bl_6143": y[i+64]
                        },
                        x[i+65]:{
                            "bl_6143": y[i+65]
                        },
                        x[i+66]:{
                            "bl_6143": y[i+66]
                        },
                        x[i+67]:{
                            "bl_6143": y[i+67]
                        },
                        x[i+68]:{
                            "bl_6143": y[i+68]
                        },
                        x[i+69]:{
                            "bl_6143": y[i+69]
                        },
                        x[i+70]:{
                            "bl_6143": y[i+70]
                        },
                        x[i+71]:{
                            "bl_6143": y[i+71]
                        },
                        x[i+72]:{
                            "bl_6143": y[i+72]
                        },
                        x[i+73]:{
                            "bl_6143": y[i+73]
                        },
                        x[i+74]:{
                            "bl_6143": y[i+74]
                        },
                        x[i+75]:{
                            "bl_6143": y[i+75]
                        },
                        x[i+76]:{
                            "bl_6143": y[i+76]
                        },
                        x[i+77]:{
                            "bl_6143": y[i+77]
                        },
                        x[i+78]:{
                            "bl_6143": y[i+78]
                        },
                        x[i+79]:{
                            "bl_6143": y[i+79]
                        },
                        x[i+80]:{
                            "bl_6143": y[i+80]
                        },
                        x[i+81]:{
                            "bl_6143": y[i+81]
                        },
                        x[i+82]:{
                            "bl_6143": y[i+82]
                        },
                        x[i+83]:{
                            "bl_6143": y[i+83]
                        },
                        x[i+84]:{
                            "bl_6143": y[i+84]
                        },
                        x[i+85]:{
                            "bl_6143": y[i+85]
                        },
                        x[i+86]:{
                            "bl_6143": y[i+86]
                        },
                        x[i+87]:{
                            "bl_6143": y[i+87]
                        },
                        x[i+88]:{
                            "bl_6143": y[i+88]
                        },
                        x[i+89]:{
                            "bl_6143": y[i+89]
                        },
                        x[i+90]:{
                            "bl_6143": y[i+90]
                        },
                        x[i+91]:{
                            "bl_6143": y[i+91]
                        },
                        x[i+92]:{
                            "bl_6143": y[i+92]
                        },
                        x[i+93]:{
                            "bl_6143": y[i+93]
                        },
                        x[i+94]:{
                            "bl_6143": y[i+94]
                        },
                        x[i+95]:{
                            "bl_6143": y[i+95]
                        },
                        x[i+96]:{
                            "bl_6143": y[i+96]
                        },
                        x[i+97]:{
                            "bl_6143": y[i+97]
                        },
                        x[i+98]:{
                            "bl_6143": y[i+98]
                        },
                        x[i+99]:{
                            "bl_6143": y[i+99]
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
            except:
                payload = {
                    "token": token,
                    "method": method,
                    "parameters": json.dumps(params)
                }
            
                for i in range(i,end,10):
                    try:
                        params = {
                            "inventory_id": "4591",
                            "products": {
                                x[i]:{
                                    "bl_6143": y[i]
                                },
                                x[i+1]:{
                                    "bl_6143": y[i+1]
                                },
                                x[i+2]:{
                                    "bl_6143": y[i+2]
                                },
                                x[i+3]:{
                                    "bl_6143": y[i+3]
                                },
                                x[i+4]:{
                                    "bl_6143": y[i+4]
                                },
                                x[i+5]:{
                                    "bl_6143": y[i+5]
                                },
                                x[i+6]:{
                                    "bl_6143": y[i+6]
                                },
                                x[i+7]:{
                                    "bl_6143": y[i+7]
                                },
                                x[i+8]:{
                                    "bl_6143": y[i+8]
                                },
                                x[i+9]:{
                                    "bl_6143": y[i+9]
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
                    except:
                        for i in range(i,end,1):
                            params = {
                                "inventory_id": "4591",
                                "products": {
                                    x[i]:{
                                        "bl_6143": y[i]
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
                        
                        print('Koniec listy na: ',i+1)
                        return redirect('estan')
  
    return render(request, 'estan.html', context)



def delete(request, pk):
    
    objestan = estan.objects.get(bl_id = pk)
    mes = str(copy.copy(object))
    if request.method=='POST':
        objestan.delete()
        message = 'Poprawnie usunieto ' + mes
        messages.info(request, message)
        return redirect('estan')
    
    context = {
        'estan':objestan
    }

    return render(request, 'delete.html', context)
