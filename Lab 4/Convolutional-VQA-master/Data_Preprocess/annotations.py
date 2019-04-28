

import json

input_file = open ('v2_mscoco_train2014_annotations.json')
json_array = json.load(input_file)
store_list = []

ids = []
filepath = 'Path.txt'
with open(filepath, "r") as ins:
    array = []
    for line in ins:
        ids.append(line.rstrip('\n'))

cnt = 0
for item in json_array['annotations']:
    if str(item['image_id']) in ids:
        store_list.append(item)
        cnt = cnt + 1

#print(store_list)
with open('Outfile Name', 'w') as outfile:
    json.dump(store_list, outfile)

print(cnt)
