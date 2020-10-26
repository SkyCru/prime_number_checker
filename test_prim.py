def es_prim(number):
    if number == 1:
        return False
    else:
        count = 0
    
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

def run():
    number = int(input('INGRESA UN NÚMERO: '))
    if es_prim(number):
        print('ES PRIMO')
    else:
        print('NO ES PRIMO')

if __name__ == '__main__':
    run()