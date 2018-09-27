#  Animesh Patel      Keysight Coding Exercise

#!/usr/bin/env python
import os.path# added
import json
from pathlib import Path
import sys
import copy

""" algorithm: take the transaction values and check for it's availability, enough quantity, and enough funds
    then update the balance, and once found all the possible purchases, shows remaining balance in terms of coin values
"""

inventory_json = open(sys.argv[1]).read()
#os.path.abspath("C:/example/cwd/mydir/myfile.txt")

'''
if os.path.exists(inventory_json):
    print os.path.basename(inventory_json)
'''

transactions_json = open(sys.argv[2]).read()
"""
if os.path.exists(transactions_json):
    print os.path.basename(transactions_json)
"""

#lines = inventory_json.readlines()

# reading a transactions file
with open('transactions.json') as transactions_json:
    tra_data = json.load(transactions_json)

# reading a inventory file
with open('inventory.json') as inventory_json:
    inv_data = json.load(inventory_json)

#list of dictionaries for both
result = []
balance = sum(tra_data[0]['funds']) # to keep track of the funds

for i in range(0, len(tra_data)):  # to iterate through the list finding total number of transaction items
# take care of quantity in the inventory after matching with the data in transaction list
    tra_item = tra_data[i]['name']
    price = 100* inv_data.get(tra_item)['price'] # dollar to cents for inventory
    
    if ((tra_data[i]['name'] in inv_data) and (inv_data.get(tra_item)['quantity'] > 0) and (balance >= price)): # check for item existance, enough quantity, and sufficient funds
        dict_value = {'product_delivered': True}
        result.append(dict(dict_value))
        balance -= price
        coin_value = balance
        
       # to keep track of printing coin amount
        if (coin_value == 0):
            result[i]['change']= []
        
        if (coin_value >= 100):
            while(coin_value >= 100):
                coin_value-=100
                result[i].setdefault('change',[]).append(100)
    
        if (coin_value >= 25):
            while(coin_value >= 25):
                coin_value -= 25
                result[i].setdefault('change',[]).append(25)

        if (coin_value >= 10):
            while(coin_value >= 10):
                coin_value -= 10
                result[i].setdefault('change',[]).append(10)

        if (coin_value >= 5):
            while(coin_value >= 5):
                coin_value-= 5
                result[i].setdefault('change',[]).append(5)

        if (coin_value > 0):
            while(coin_value >= 1):
                coin_value-=1
                result[i].setdefault('change',[]).append(1)
                
    # else produce is not delivered
    else:
        dict_value = {'product_delivered': False}
        result.append(dict(dict_value))
        result[i]['change'] = tra_data[i]['funds']

# function to write the results to json file
def json_write(path, file, result):
    file_ext = './'+ path + '/' + file
    with open(file_ext, 'w') as fp:
        json.dump(result,fp)
path = './'
file = 'expected.json'
json_write(path, file, result)
