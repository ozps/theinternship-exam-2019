import xmltodict
import json

f = open('input.xml')
xml_content = f.read()
x = xmltodict.parse(xml_content, attr_prefix='')
no_root = x.get('current')
j = json.dumps(no_root, indent=2)
print(j)

with open('output.json', 'w') as outfile:
    json.dump(no_root, outfile, indent=2)
