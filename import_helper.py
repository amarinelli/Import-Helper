import re

class Formatter:
    def __init__(self):                
        self.items = []
        self.requires = []
        self.objects = []
        self.p_non = re.compile("\W") #Matches any non-alphanumeric character; [^a-zA-Z0-9_].

    def open_file(self, file_name):
        import_file = open(file_name)
        return import_file

    def find_solo(self, test_requires, test_objects):        
        test_list = test_requires
        dont_exists = []
        exists = bool
        for g in range(len(test_list)-1):
            test_require = test_list[g].rsplit("/", 1)[1][:-1]
            for test_obj in test_objects:
                print "TESTING:  " + test_require + "  against  " + test_obj
                if test_obj.lower() == test_require.lower():
                    print "matched"
                    dont_exists.append(True)
                    break
                else:
                    dont_exists.append(False)
        print dont_exists
        if (exists == False):
            print "trying to remove:  " + test_require 
            del self.requires[g]
        return

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

##for y in formatter.requires:
##    print y
##
##for z in formatter.objects:
##    print z

if ((len(formatter.requires)-1) != len(formatter.objects)):
    #need to handle items like BorderContainer which are not passed into a variable
    formatter.find_solo(formatter.requires, formatter.objects) 



##        if (formatter.requires[g].rsplit("/", 1)[1][:-1] == "BorderContainer"):
##            extra.append(formatter.requires[g])            
##        elif (formatter.requires[g].rsplit("/", 1)[1][:-1] == "ContentPane"):
##            extra.append(formatter.requires[g])
##    
##    formatter.requires.remove("\"dijit/layout/BorderContainer\"")
##    formatter.requires.remove("\"dijit/layout/ContentPane\"")

        

    for f in range(len(formatter.objects)):        
        print "import {0} = require({1});".format(formatter.objects[f], formatter.requires[f])
        
else:
    #requires and objects arrays match except for "dojo/domReady!" in requires
    for f in range(len(formatter.objects)):
        print "import {0} = require({1});".format(formatter.objects[f], formatter.requires[f])

txtFile.close()
    
    
