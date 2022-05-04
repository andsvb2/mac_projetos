import urllib.request, urllib.parse, urllib.error
import json
import ssl
import api_key as ak

api_key = ak.apiKey
serviceurl ="https://api.geoapify.com/v1/geocode/search?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    endereco = input("Digite a localização: ")
    if len(endereco) < 1:
        break

    parms = dict()
    parms['text'] = endereco
    parms['lang'] = 'pt'
    parms['limit'] = 1
    parms['format'] = 'json'
    parms['apiKey'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Requisitando', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Recebidos', len(data), 'caracteres.')

    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, ensure_ascii=False, indent=4))

    if parms['format'] == 'json':
        endereco_formatado = js['results'][0]['formatted']
        id_lugar = js['results'][0]['place_id']
        cep = js['results'][0]['postcode']
    else:
        endereco_formatado = js['features']['results'][0]['formatted']
        id_lugar = js['features'][0]['properties']['place_id']
        cep = js['features'][0]['properties']['postcode']

    if endereco_formatado is not False:
        print(f"\nO endereço é: {endereco_formatado}")

    if id_lugar is not False:
        print(f"ID do lugar: {id_lugar}")

    if cep is not False:
        print(f"O CEP é {cep}.\n")
