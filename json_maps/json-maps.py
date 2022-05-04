import urllib.request, urllib.parse, urllib.error
import json
import ssl
# from turtledemo.minimal_hanoi import play

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    endereco = input("Digite a localização: ")
    if len(endereco) < 1:
        break

    parms = dict()
    parms['address'] = endereco
    parms['language'] = 'pt-BR'
    print(parms)
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print(url)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    # print(data)
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, ensure_ascii=False, indent=4))# Imprime todo o conteúdo do arquivo, já com indentação

    id_lugar = js['results'][0]['place_id']
    print(f"\nID do lugar: {id_lugar}")

    # plus_code = js['results'][0]['plus_code']['global_code']
    # print(f"Global code: {plus_code}\n")
