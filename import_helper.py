import re

imports_file = open(r".\import_statements.txt")
count = 0
items = []
p_alpha_num = re.compile("\w") #Matches any alphanumeric character; [a-zA-Z0-9_].
p_non = re.compile("\W") #Matches any non-alphanumeric character; [^a-zA-Z0-9_].

for line in imports_file:
    s = line.strip()
    for item in (s.split(",")):
        if (item.strip() != ""):
            items.append(item.strip())
    count+=1
    
for it in items:
    print it
    
#print count
    
    
