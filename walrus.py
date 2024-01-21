# def get_data():
#     for i in range(10):
#         yield i 
#     yield -1


# def process(data):
#     print(data)

# gen = get_data()

# data = next(gen)

# while(data != -1):
#     process(data)
#     data = next(gen)
# Example - 1 
def get_data():
    for i in range(5):
        yield i 
    yield -1


def process(data):
    print(data)

gen = get_data()

while(data :=next(gen)) != -1:
    process(data)

#Example - 2

def f(x):
    return x-1

results= [f(x) for x in range(10) if f(x) > 3]
results_with_walrus = [ans for x in range(10) if (ans :=f(x))>3]
print(results)
print(results_with_walrus)
