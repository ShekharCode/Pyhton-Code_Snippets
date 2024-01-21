items = ['a','b','c','d','e','f']

i = 0
found = False

while i<len(items):
    item = items[i]
    if(item == 'b'):
        print("Found it")
        found = True
        break;
    i+=1
if not found:
    print("do something")

# same code with while-else

i = 0
while i<len(items):
    item = items[i]
    if(item == 'z'):
        print("Found it")
        break
    i+=1
else:
    print("do something")