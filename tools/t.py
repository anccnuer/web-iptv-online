import csv
import json

# 读取CSV文件并将数据转换为JavaScript中可用的数组格式
js_array = []
with open('t.csv', 'r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        js_array.append({'name': row['name'], 'url': row['url']})

with open('output.js', 'w',encoding='utf-8') as file:
    for item in js_array:
        output_str = "{{name:'{}',url:'{}'}},".format(item['name'], item['url'])
        file.write(output_str + '\n')
