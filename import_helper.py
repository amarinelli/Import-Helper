import re

class Formatter:
    def __init__(self):                
        self.count = 0
        self.items = []
        self.requires = []
        self.objects = []
        self.p_alpha_num = re.compile("\w") #Matches any alphanumeric character; [a-zA-Z0-9_].
        self.p_non = re.compile("\W") #Matches any non-alphanumeric character; [^a-zA-Z0-9_].

    def open_file(self, file_name):
        import_file = open(file_name)
        return import_file

#Instantiate
formatter = Formatter()
txtFile = formatter.open_file(r".\import_statements.txt")

for line in txtFile:
    s = line.strip()
    for values in (s.split(",")):
        if (values.strip() != ""):
            formatter.items.append(values.strip())

for item in formatter.items:    
    if (item.startswith("\"") and item.endswith("\"")):        
        formatter.requires.append(item)

for require in formatter.requires:
    formatter.items.remove(require)
    
for obj in formatter.items:    
    if (formatter.p_non.match(obj[0]) or formatter.p_non.match(obj[-1])):
        continue
    else:
        formatter.objects.append(obj)

for y in formatter.requires:
    print y

for z in formatter.objects:
    print z

txtFile.close()
    
    
