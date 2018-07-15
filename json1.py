import json
 
#data = []
with open('text.json') as f:
    #for line in f:
    	
        #data.append(json.loads(line))

 	data=json.loads(f.readline())
#print json.dumps(data, ensure_ascii=False)
#print(data)
str = "\r\n"
for item in data:
    #print json.dumps(item)
    print(item)
    str = str + "insert into rules (Id,Rule_Type,Rule_Item) values "
    str = str + r'({},"{}","{}");'.format(item['Id'],item['RuleType'],item['RuleItem'])+'\r\n'
 
import codecs
file_object = codecs.open('json.sql', 'w' ,"utf-8")
file_object.write(str)
file_object.close()
print ("success")