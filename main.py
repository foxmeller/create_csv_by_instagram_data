import os
import pandas
# import emoji


# Папка с данными из Инстаграма
directory = './data'
# какая будет ссылка у картинки, когда она загрузиться на Вордпрес
WP_DIR = "http://localhost:8888/sabi/wp-content/uploads/2023/02/"

list_txt_files = [] # Список директории файла тхт
list_of_file_nanes = [] # Список имен файлов тхт
for filename in os.listdir(directory):
    print(filename)
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.txt'):
        list_of_file_nanes.append(filename)
        list_txt_files.append(f)
        # print(f)
# print(list_txt_files)
# print(list_txt_files[0])

"""Создание словаря/ имя файла : список по строкам содержания файла"""
text_in_txt_file = {}
i=0
for filename in list_txt_files:

    with open(filename) as file:
        list_strok = file.readlines()
        text_in_txt_file[list_of_file_nanes[i]] = list_strok
        i+=1


print(text_in_txt_file)
"""название, нналичие, полное описание"""
string_with_price = []
nalichie = []
description_toy = []
full_description_toy = []
rem_i = []
for key in text_in_txt_file:
    toy_text = text_in_txt_file[key]
    if "НЕТ В НАЛ" in toy_text[0]:
        nalichie.append(0)
        toy_text.pop(0)
        description_toy.append(toy_text[1])
        toy_text.pop(1)
    else:
        description_toy.append(toy_text[0])
        toy_text.pop(0)
        nalichie.append(1)
    desc = ""

    for string in toy_text:

        if "ОПТОВАЯ ЦЕНА" in string:
            a = string.find(" KZT")
            b = string.find("- ") + 2
            d = string[b:a]
            c = d.replace(" ", "")
            # print(toy_text.index(string))

            i = toy_text.index(string)
            rem_i.append(i)

            if c.isdigit():
                string_with_price.append(c)
            else:
                string_with_price.append(0)
        elif "➖➖" in string:
            pass
        elif "#" in string:
            pass
        elif string == "\n":
            pass
        elif string == "⠀\n":
            pass
        else:
            a = string
            desc += a

    # print(i)
    # toy_text.pop(i)
    full_description_toy.append(desc)

"""Массив и поиск  картинок """
imag_list =[]
count = 0
count_first = 0
for i in list_txt_files:
    str = i
    l=len(str)
    remove_last = str[:l-4]
    remove_first = remove_last[54:]
    # print(remove_first)
    # remove_last = str[:]

    if os.path.isfile(remove_last+f"_1.jpg"):
        count_first += 1
        remove_first = WP_DIR + remove_first + "_1.jpg"
        stroka_kartinok = remove_first
    else:
        stroka_kartinok = WP_DIR+remove_first+".jpg"
        print(i)
        # stroka_kartinok = "КАРТИНКА НЕДОСТУПНА"
    # stroka_kartinok = remove_first

    for i in range(2,9):

        proverka_file = remove_last+f"_{i}.jpg"
        if os.path.isfile(proverka_file):
            # print(f"файл {proverka_file} есть в директории ")
            count += 1
            remove_first = proverka_file[54:]
            remove_first = WP_DIR+remove_first
            stroka_kartinok = stroka_kartinok+","+remove_first



    imag_list.append(stroka_kartinok)

print(count)
print(count_first)

# toy_txt =[]
# for key in text_in_txt_file:
#     toy_text.append(text_in_txt_file[key])
#
""" 
Масив категорий
Сортировка по категориям
"""
categiry =[]
for string in description_toy:
    low_strin = string.lower()
    if "вкладыш" in low_strin or "вложени" in low_strin:
        categiry.append("Вкладыши")
    elif "трансформ" in low_strin or "трансф" in low_strin:
        categiry.append("Лего столы")
    elif "головоломка" in low_strin or "память" in low_strin:
        categiry.append("Головоломки")

    elif "ванн" in low_strin or "пены" in low_strin or "купания" in low_strin or "воде" in low_strin or "аква" in low_strin:
        categiry.append("Игрушки для ванной")

    elif "неваляш" in low_strin or "погремуш" in low_strin or "перчатка" in low_strin or "прорезывател" in low_strin \
            or "малыш" in low_strin:
        categiry.append("Игрушки для малышей")

    elif "конструктор" in low_strin or "вложени" in low_strin:
        categiry.append("Конструкторы")


    elif "магнит" in low_strin :
        categiry.append("Магнитные доски и планшеты")

    elif "математ" in low_strin or "счет" in low_strin or "арифмет" in low_strin or "логарифм" in low_strin \
            or "памят" in low_strin:
        categiry.append("Математическое развитие и обучение")

    elif "мозаик" in low_strin or "мозайк" in low_strin:
        categiry.append("Мозаика")

    elif "шнур" in low_strin or "пальчик" in low_strin or "моторик" in low_strin or "песок" in low_strin \
            or "тактиль" in low_strin:
        categiry.append("Моторика")

    elif "музыкальн" in low_strin or "вложени" in low_strin or "микрофон" in low_strin:
        categiry.append("Музыкальные инструменты")

    elif "планшет" in low_strin or "рисовани" in low_strin or "творчеств" in low_strin or "лепк" in low_strin or "художествен" in low_strin or "маркер" in low_strin:
        categiry.append("Наборы для творчества")

    elif "настольная игра" in low_strin :
        categiry.append("Настольные игры")

    elif "интерактив" in low_strin or "развиваю" in low_strin or "обучаю" in low_strin or "развития" in low_strin:
        categiry.append("Обучение")

    elif "пазл" in low_strin :
        categiry.append("Пазл")
    elif "палатк" in low_strin :
        categiry.append("Палатки")

    elif "рыбалк" in low_strin:
        categiry.append("Рыбалка")


    elif "сортер" in low_strin or "сортиров" in low_strin:
        categiry.append("Сортеры")
    elif "стучалка" in low_strin:
        categiry.append("Стучалки")

    elif "набор" in low_strin or "игровой" in low_strin or "игровая" in low_strin \
            or "кухня" in low_strin or "кук" in low_strin:
        categiry.append("Сюжетно-ролевые наборы")

    elif "поезд" in low_strin or "дорога" in low_strin or "машинок" in low_strin or "трек" in low_strin \
            or "паровоз" in low_strin or "модель" in low_strin or "машинки" in low_strin:
        categiry.append("Транспорт и дороги")
    elif "корзина" in low_strin or "пуф" in low_strin:
        categiry.append("Хранение игрушек")
    else:
        categiry.append("Разное")
hash_in = []
d=0
for string in full_description_toy:
    if "#" in string:
        hash_in.append(1)
        d+=1
    else:
        hash_in.append(0)


dup = [x for i, x in enumerate(description_toy) if i != description_toy.index(x)]
print(dup)

# Замена спец символов, изза юниккода отображались не правильно
alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
def clear_desc(desc):
    alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    pppp = ["'","«",'"']
    while desc[0].lower() not in alphabet:
        desc = desc[1:].lower()
        desc = desc.strip(" ")
        desc = desc.capitalize()
    a =""
    if desc.find('"') >0 :
        i = desc.find('"')
        if desc[i+1].isdigit():
            print(desc[i+1])
            i = desc.find('"',i)

            i = desc.find('"',i)
        # print(i)
        a = desc[i+1].upper()
        b = desc[:i+1]+a+desc[i+2:len(desc)]
        return b
    elif desc.find("'") >0:
        i = desc.find('"')
        # print(i)
        a = desc[i + 1].upper()
        b = desc[:i + 1] + a + desc[i + 2:len(desc)]
        return b
    elif desc.find("«") >0:
        i = desc.find('«')
        # print(i)
        a = desc[i + 1].upper()
        b = desc[:i + 1] + a + desc[i + 2:len(desc)]
        return b
    else:
        a=desc
        return a
    return a
# print(clear_desc(description_toy[0]))
clear_description_toy=[]
for string in description_toy:
    a = clear_desc(string)
    clear_description_toy.append(a)



data_dict ={
    # "name_txt_file":  list_of_file_nanes,
    "short_description": clear_description_toy,
    "category": categiry,
    "availability": nalichie,
    "price": string_with_price,
    "images": imag_list,
    "full_description": full_description_toy,

}

toys_info = pandas.DataFrame(data_dict)
toys_info.to_csv("toy_info.csv")

"""Игрушки у которых нет цен """
no_price = toys_info.loc[(toys_info["price"] == 0)]
no_price.to_csv("no_price.csv")
"""Игрушки у которых категория другое """
noinfo_category = toys_info.loc[(toys_info["category"] == "Лего столы") ]
noinfo_category.to_csv("table_category.csv")


