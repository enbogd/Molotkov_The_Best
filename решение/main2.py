import time as tm
from collections import OrderedDict

# Получение unix-времени и времени в формате гггг-мм-дд чч:мм:сс
unix_time = int(tm.time())
print(unix_time)
str_date = tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(unix_time))
# print(type(unix_time))
# print(str_date)
# Получение времени в формате гггг-мм-дд чч:мм:сс из unix
t = tm.strptime(str_date, '%Y-%m-%d %H:%M:%S')
# print(int(tm.mktime(t)))
key_list = []
key = "".join(str(unix_time))
key = key *10






# Читаем файл с секретным сообщением
message = open("message.txt")
mes = message.read()
# message.close()
mes = mes.split()
print(mes)
text = open('text.txt')

# Читаем файл с бессмысленным текстом-водой
content = text.read()
water = content.split()
print(water)
water.copy()
res_text = []

print(f'Key: {key}')
sep = ' '
# print(transmit)
ending = f'\n Сообщение отправлено: {str_date}'

'''
1. Проходим по всем элементам сообщения       x
2. Берём элемент сообщения - mes[x]
3. Находим элемент ключа с номером х - key[x] 

5. Находим элемент текста с номером  - water[int(key[x])]  
6. Вставляем элемент сообщения с номером х в текст по номеру     water[int(key[x])] = mes[x] 
7. Прибавляем key[x]   к номеру элемента текста     x =x+key[x]  

номер элемента ключа - x
элемент ключа - key[x]
элемент сообщения - mes[x]
номер элемента сообщения - water[int(key[x])]

'''
def encoding(key, water, mes):
    for z in range (0,1):

        try:
            x = int()
            q = int(0)
            for i in range(0, 100):
                p= int(key[i])
                print("p=", p)
                if i ==0:
                    x = int(key[i])    
                else:
                    if p==q:
                        x=x+1
                        print("Здесь х=0")
                    else:
                        x = x+  int(key[i]) 
                print(x)
                water[x]=mes[i]
                
                  
        except IndexError:
            print('ТЫ ТУПОЙ')

    print(water)
    for i in range(len(water)):
        res_text.append(water[i])
        res_text.append(sep)
    print(f'Итоговое сообщение: {res_text}')

    with open('result.txt', 'w') as file:
        file.writelines(res_text)
        file.writelines(ending)
        #file.writelines(key)

encoding(key, water, mes)
                    
