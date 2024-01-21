def numbers(a,b,c,d):
    print(a,b,c,d)

lst = [1,2,3,4]
numbers(*lst)

values = {
    'key' : 5,
    'target' : 123
}

def parse_values(target,key):
    print(key,target)

parse_values(**values)

