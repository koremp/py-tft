import json, os

script_dir = os.path.dirname(__file__)
champ_rel_path = "set3/champions.json"
trait_rel_path = "set3/traits.json"
item_rel_path = "set3/items.json"

abs_champ_path = os.path.join(script_dir, champ_rel_path)
abs_trait_path = os.path.join(script_dir, trait_rel_path)
abs_item_path = os.path.join(script_dir, item_rel_path)

champ_data = {}
with open(abs_champ_path) as json_file:
    champ_data = json.load(json_file)
'''
    for champ in champ_data:
        print(champ)
'''
'''
        

with open(abs_trait_path) as json_file:
    trait_data = json.load(json_file)
    for trait in trait_data:
        print(trait)

with open(abs_item_path) as json_file:
    item_data = json.load(json_file)
    for item in item_data:
        print(item)
'''

with open('test.txt', 'r') as file:
    for x in file:
        print(champ_data[int(x)])