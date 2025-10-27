animal = input()
temperature = float(input())
if animal == 'ЧАЙКА':
    counter = 0.634 * temperature + 10.6
    print(round(counter))
elif animal == 'ГОЛОМЯНКА':
    counter = -5.147 * temperature + 262.6
    print(round(counter))
else:
    print('ОШИБКА')