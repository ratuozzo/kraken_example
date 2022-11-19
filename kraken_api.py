import krakenex
from pykrakenapi import KrakenAPI
api = krakenex.API()
k = KrakenAPI(api)
pairs = k.get_tradable_asset_pairs()
#print(pairs['wsname'])

wsname = pairs['wsname'].str.split('/', expand=True)
list1 = wsname[0].tolist() 
list2 = wsname[1].tolist() 


list1 = set(list1)
list2 = set(list2)

in_second = list2 - list1
result = list1  + list(in_second)
print(result)