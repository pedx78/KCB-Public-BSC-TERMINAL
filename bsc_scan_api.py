
from urllib.request import Request, urlopen
import json
import timeit
import random

def get_BSC_API_KEY():
    users = ["92MM9Q3NG1AHGE21YEHMX6F56VWM6GM3PW", "EVC2IFRX4NJ2IAMTK592SI8YX9YWPQCZWJ", "A5NDCHK6QBHRCXVSD2JHG9VMDQKPVZYHCE"]
    magic_number = random.randint(0, 2)
    return (users[magic_number])

def honey(contract):
    #start = timeit.default_timer()

    #api_key = "92MM9Q3NG1AHGE21YEHMX6F56VWM6GM3PW"
    api_key = get_BSC_API_KEY()

    ABI = "https://api.bscscan.com/api?module=contract&action=getabi&address="+ contract +"&apikey=" + api_key + ".json"

    headers = {'User-Agent': 'XYZ/3.0'}
    req = Request(ABI , headers=headers) 
    response_all = urlopen(req).read()
    response = json.loads(response_all)

    print(response['message'])
    #stop = timeit.default_timer()
    #print('\nRunTime: ', stop - start)

honey("0xda84f181ec6fc0dd14e5950ec5bada9421325283")