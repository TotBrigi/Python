# coding=utf-8
menu_file = open('menu.txt', 'w+')

menu = {}

while True:
    day = raw_input('Milyen nap van?')
    day = day + 'i menu'
    menu_file.write(day)
    menu_file.write('\n')
    leves = raw_input('Napi leves: ')
    menu_file.write(leves)
    menu_file.write(': ')
    leves_ara = raw_input('Mennyibe kerul a leves?')
    menu_file.write(leves_ara)
    menu_file.write('\n')
    foetel = raw_input('Foetel')
    menu_file.write(foetel)
    menu_file.write(': ')
    foetel_ara = raw_input('Mennyibe kerul a foetel?')
    menu_file.write(foetel_ara)
    menu_file.write('\n')
    desszert = raw_input('Desszert')
    menu_file.write(desszert)
    menu_file.write(': ')
    desszert_ar = raw_input('Mennyibe kerül a desszert')
    menu_file.write(desszert_ar)
    menu_file.write('\n')
    menu_file.write('\n')

    new_menu = raw_input('Felvesz ujjabb menut? i/n')

    if new_menu =='n':
        break




menu_file.close()

