# import json
#
# country_capital_dict = {}
#
# def add_country(country, capital):
#     country_capital_dict[country] = capital
#     print(f"Добавлена информация: {country} - {capital}")
#
# def remove_country(country):
#     if country in country_capital_dict:
#         del country_capital_dict[country]
#         print(f"Информация о стране {country} удалена")
#     else:
#         print(f"Страна {country} не найдена")
#
# def search_country(country):
#     if country in country_capital_dict:
#         print(f"Столица страны {country}: {country_capital_dict[country]}")
#     else:
#         print(f"Информация о стране {country} не найдена")
#
# def update_country(country, new_capital):
#     if country in country_capital_dict:
#         country_capital_dict[country] = new_capital
#         print(f"Информация о стране {country} обновлена: Новая столица - {new_capital}")
#     else:
#         print(f"Страна {country} не найдена")
#
# def save_data(filename):
#     with open(filename, "w") as file:
#         json.dump(country_capital_dict, file)
#         print("Данные сохранены в файл")
#
# def load_data(filename):
#     global country_capital_dict
#     with open(filename, 'r') as file:
#         country_capital_dict = json.load(file)
#     print("Данные загружены из файла")
#
# add_country("Russia", "Moscow")
# add_country("Germany", "Berlin")
#
# search_country("Russia")
# search_country("France")
#
# update_country("Germany", "Hamburg")
#
# remove_country("Japan")
#
# save_data("country_capital_data.json")
# load_data("country_capital_data.json")


# 2


# import json
#
# group_album_dict = {}
#
# def add_group(group, albums):
#     group_album_dict[group] = albums
#     print(f"Добавлена информация: {group} - {albums}")
#
# def remove_group(group):
#     if group in group_album_dict:
#         del group_album_dict[group]
#         print(f"Информация о группе {group} удалена")
#     else:
#         print(f"Группа {group} не найдена")
#
# def search_group(group):
#     if group in group_album_dict:
#         print(f"Альбомы группы {group}: {group_album_dict[group]}")
#     else:
#         print(f"Информация о группе {group} не найдена")
#
# def update_group(group, new_albums):
#     if group in group_album_dict:
#         group_album_dict[group] = new_albums
#         print(f"Информация о группе {group} обновлена: Новые альбомы - {new_albums}")
#     else:
#         print(f"Группа {group} не найдена")
#
# def save_data(filename):
#     with open(filename, 'w') as file:
#         json.dump(group_album_dict, file)
#         print("Данные сохранены в файл")
#
# def load_data(filename):
#     global group_album_dict
#     with open(filename, 'r') as file:
#         group_album_dict = json.load(file)
#     print("Данные загружены из файла")
#
# add_group("The Beatles", ["Abbey Road", "Sgt. Pepper's Lonely Hearts Club Band"])
# add_group("Queen", ["A Night at the Opera", "The Game"])
#
# search_group("The Beatles")
# search_group("Led Zeppelin")
#
# update_group("Queen", ["Bohemian Rhapsody", "A Kind of Magic"])
#
# remove_group("AC/DC")
#
# save_data("group.album_data.json")
# load_data("group.album_data.json")