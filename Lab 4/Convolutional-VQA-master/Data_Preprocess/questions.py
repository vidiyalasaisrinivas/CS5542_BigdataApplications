

import json

input_file = open ('v2_OpenEnded_mscoco_train2014_questions.json')
json_array = json.load(input_file)
store_list = []

ids = []
filepath = 'path.txt'
with open(filepath, "r") as ins:
    array = []
    for line in ins:
        ids.append(line.rstrip('\n'))

cnt = 0
for item in json_array['questions']:
    store_details = {"image_id":None, "question":None, "question_id":None}
    store_details['image_id'] = str(item['image_id'])
    store_details['question'] = item['question']
    store_details['question_id'] = item['question_id']
    if store_details['image_id'] in ids:
        store_list.append(store_details)
        cnt = cnt + 1

#print(store_list)
with open('Name of output file', 'w') as outfile:
    json.dump(store_list, outfile)

print(cnt)
