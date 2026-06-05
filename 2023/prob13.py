while True:
    data = input().split('-')
    if (data != ['0']):
        if (len(data) == 4):
            print(f'xxxx-xxxx-xxxx-{data[-1]}')
        else:
            print(f'xxx-xx-{data[-1]}')
    else:
        break