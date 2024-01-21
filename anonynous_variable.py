coordinate = [5,10]

larger_coordinate = [1,5,10]

list_of_pairs = [['A','B'],['C','D'],['E','F']]

for _ in range(10):
    print("Hello World")

x,_ = coordinate
print(x)

x,_,z = larger_coordinate
print(x,z)

second_elements = [b for _,b in list_of_pairs]
print(second_elements)