def greeting_decore(fu):
    def wrapper(name):
        fu(name)
        if wrapper.count % 5 == 0:
            print("Вы получаете бесплатную плюшку!", end='')
            
        print("\n", end='')
        wrapper.count += 1
    
    wrapper.count = 1
    return wrapper


@greeting_decore
def greeting(name):
    print('Привет, ' + name.strip() + '! ', end = '')


with open('bakery.txt', 'r') as file:
    counter = 0
    limit = 3
    for name in file:
        if counter < limit:
            greeting(name)
            counter += 1
        else:
            break


while(1):
    name = input()
    greeting(name)