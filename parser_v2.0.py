# Parser v2.0
# Перевод типовых фрагментов строк вынесен в функцию Translate()
# Удаление ненужных данных из строк с характеристиками вынесен в функцию Delete_from_String()
# Добавлены исключения try/except на случай, если в каком-то товаре из списка отсутствует искомый элемент 
# Добавление новых кусков строк в эти функции делает скрипт ещё более универсальным для сайта по определённой тематике
# Скрипт легко модифицировать для любого другого сайта
# Обращение к элементам в нем реализовано через XPATH. Также можно использовать CSS_SELECTOR.
# Скрипт легко модифицируется для любого другого интересующего сайта
# Интересующий текст заносится в базу данных MYSQL
# Изображения скачиваются в желаемую директорию (смотреть ниже: "Скачивание изображений")
# При хорошей скорости интернета 37 товаров с изображениями обработаны за 2,5 минуты, при более низкой - около 4 минут


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


import pymysql
# from config import host, user, password, db_name

host = "localhost"
user = "your_user_name"
password = "your_password"
db_name = "your_db_name"


import os
import wget





# ссылка на расположение chromedriver.exe
driver = webdriver.Chrome('G:/Programming/chromedriver.exe')



# ссылка на раздел со списком товаров, которые нужно обработать
driver.get('http://www.meclube.com/en/66-air-operated-grease-pumps-sets/brass-connection-fixed-rubber-m1?n=50&selected_filters=brass-connection-fixed-rubber-m1%3F%26selected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1%3Fselected_filters%3Dbrass-connection-fixed-rubber-m1&id_category=66')

# time.sleep(1)



# получаем ссылки на интересующие нас элементы
pages = driver.find_elements_by_tag_name('a.product_img_link')
pages = [page.get_attribute('href') for page in pages]
print('Found ' + str(len(pages)) + ' links')
for page in pages:
  print(page)

print()
print('**************************************************************')
print('**************************************************************')
print()







print('CREATE TABLE `frame_lifter-press_for_grease_kit`')
print()
print()
try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        cursor = connection.cursor()

        # drop table if exists
        with connection.cursor() as cursor:
            create_table_query = "DROP TABLE IF EXISTS `air-operated_grease_pumps_sets`;"
            cursor.execute(create_table_query)

        # create table
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `air-operated_grease_pumps_sets`(id int AUTO_INCREMENT, \
                        header varchar(100), \
                        article varchar(16), \
                        p_1 varchar(80), \
                        p_2 varchar(40), \
                        eq_1 varchar(80), \
                        eq_1_long varchar(150), \
                        eq_2 varchar(80), \
                        eq_2_long varchar(150), \
                        eq_3 varchar(80), \
                        eq_3_long varchar(150), \
                        eq_4 varchar(80), \
                        eq_4_long varchar(150), \
                        eq_5 varchar(80), \
                        eq_5_long varchar(250), \
                        eq_6 varchar(100), \
                        eq_6_long varchar(200), \
                        eq_7 varchar(100), \
                        eq_7_long varchar(200), \
                        wgh varchar(12), \
                        vol varchar(12), \
                        packing varchar(1), \
                        PRIMARY KEY (id));"
            cursor.execute(create_table_query)
            print("Table created successfully")

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)



def Translate(string):
  string = string.replace("Those are suitable for the supply at high pressure of all kinds of grease at short and long distance.", 
                          "Они подходят для подачи под высоким давлением всех видов смазки на короткие и большие расстояния.")
  string = string.replace("Those are suitable for central supply of plants where a major quantity of grease and a major pressure "
    "at long and short distance are required. The operating pressure of the grease pumps hereby may vary between a minimum of 2.5 bar "
    "and a maximum of 8 bar. In order to optimize the efficiency and the life of our pumps we recommend to use filtered and lubricated air.", 
    "Они подходят для централизованного снабжения заводов, где требуется перекачка большого количество смазки под высоким давлением на большие и малые расстояния. "
    "При этом рабочее давление насосов для консистентной смазки может варьироваться от минимального в 2,5 бара до максимального в 8 бар. Чтобы оптимизировать эффективность "
    "и срок службы наших насосов, мы рекомендуем использовать фильтрованный и смазанный воздух.")
  string = string.replace("Those are suitable for central supply of plants where a major pressure at long and short distance is required. The operating pressure of the grease "
    "pumps hereby may vary between a minimum of 2.5 bar and a maximum of 8 bar. In order to optimize the efficiency and the life of our pneumatic pumps we recommend to use filtered and lubricated air.", 
    "Они подходят для централизованного питания заводов, где требуется перекачка под высоким давлением на большие и малые расстояния. При этом рабочее давление насосов для консистентной смазки может варьироваться "
    "от минимального в 2,5 бара до максимального в 8 бар. Чтобы оптимизировать эффективность и срок службы наших пневматических насосов, мы рекомендуем использовать фильтрованный и смазанный воздух.")
  string = string.replace("They are suitable for transferring a lot of types of grease, filling of central distribution plants, dispensers "
    "and manual pumps where a major quantity of grease with slow pressure and short distance is required. The operating pressure of the grease "
    "pumps hereby may vary between a minimum of 3.5 bar and a maximum of 8 bar. In order to optimize the efficiency and the life of our pneumatic "
    "pumps we recommend to use filtered and lubricated air.", 
    "Они подходят для перекачки многих типов смазки, заполнения центральных распределительных станций, дозаторов и ручных насосов. Идеальны там, где требуется перекачивать большое количество смазки "
    "при низком давлении на короткие расстояния. При этом рабочее давление насосов для консистентной смазки может варьироваться от минимального в 3,5 бара до максимального в 8 бар. "
    "Чтобы оптимизировать эффективность и срок службы наших пневматических насосов, мы рекомендуем использовать фильтрованный и смазанный воздух.")
  string = string.replace("The operating pressure of the grease pumps hereby may vary between a minimum of 2.5 bar "
      "and a maximum of 8 bar. In order to optimize the efficiency and the life of our air operated pumps, we recommend "
      "to use filtered and lubricated air.", "При этом рабочее давление насосов для консистентной смазки может варьироваться "
      "от минимального в 2,5 бара до максимального в 8 бар. Чтобы оптимизировать эффективность и срок службы наших пневматических "
      "насосов, мы рекомендуем использовать фильтрованный и смазанный воздух.")
  string = string.replace("Suitable for high pressure transfer of high viscosity grease and fluids over short and long distances and "
    "for central distribution plants with multiple distribution points. The operating pressure of the pumps may vary between a minimum "
    "of 3 bar and a maximum of 8 bar. To optimize the efficiency and the live in time of our air operated pumps Meclube recommend to use filtered and lubricated air.", 
    "Подходит для перекачки под высоким давлением высоковязкой смазки и жидкостей на короткие и большие расстояния, а также для центральных распределительных станций "
    "с несколькими точками распределения. Рабочее давление насосов может варьироваться от минимального в 3 бара до максимального в 8 бар. Для оптимизации эффективности и увеличения срока "
    "службы наших пневматических насосов Meclube рекомендует использовать фильтрованный и смазанный воздух.")
  string = string.replace("Suitable for high pressure transfer of high viscosity grease and fluids over short and long distances and "
    "for central distribution plants with multiple dispensing points.", 
    "Подходит для перекачки под высоким давлением высоковязкой смазки и жидкостей на короткие и большие расстояния, а также для центральных распределительных станций "
    "с несколькими точками распределения.")
  string = string.replace("The operating pressure of the pumps can vary between a minimum of 3 bar and a maximum of 8 bar. To optimize the efficiency and the live time "
      "of our air operated pumps we recommend to use filtered and lubricated air.", 
      "Рабочее давление насосов может варьироваться от минимального в 3 бара до максимального в 8 бар. Для оптимизации эффективности и увеличения срока "
      "службы наших пневматических насосов мы рекомендуем использовать фильтрованный и смазанный воздух.")
  string = string.replace("Equipped with follower plate for grease pumps with shank", 
    "Оборудован подвижной пластиной для насосов консистентной смазки с хвостовиком")
  string = string.replace("equipped with follower plate for pumps with shank", 
    "Оборудован подвижной пластиной для насосов консистентной смазки с хвостовиком")
  string = string.replace("Air operated two columns pumps lifter and press for grease and viscous medias.", 
                          "Пневматический двухколонный подъемник насоса и пресс для смазки и вязких сред.")
  string = string.replace("Air operated two columns pumps lifter and press for lubricants and viscous medias", 
                          "Пневматический двухколонный подъемник насоса и пресс для смазки и вязких сред.")
  string = string.replace("With its particular 3 ways control valve it lifts or pull down the pump and the follower plate, improving the exchanging effort of 180-220kg (400 lbs) barrels.", 
                          "Благодаря особому 3-ходовому регулирующему клапану он поднимает или опускает насос и ведомую пластину, улучшая компенсирующее усилие на бочки 180-220 кг (400 фунтов).")
  string = string.replace("It is particularly advised for the use with high viscosity grease and medias (from 200CPS to 500ASTM).", 
                          "Особенно рекомендуется для использования со смазками и средами с высокой вязкостью (от 200CPS до 500ASTM).")
  string = string.replace("It is particularly advised for the use with high viscosity lubricants and medias (from 200CPS to 500CPS).", 
                          "Особенно рекомендуется для использования со смазками и средами с высокой вязкостью (от 200CPS до 500ASTM).")
  string = string.replace("The follower plate is pushed down by the pressurised pneumatic cylinders, avoiding grease flow interruptions by air pockets in the grease bed.", 
                          "Приводной диск толкается вниз пневматическими цилиндрами, находящимися под давлением, что позволяет избежать прерывания потока смазки из-за воздушных карманов в слое смазки.")
  string = string.replace("Moreover, it allows to collect all the grease from the inner walls down to the bottom of the drum, Pump suction is assisted.", 
                          "Кроме того, он позволяет собирать всю смазку от внутренних стенок до дна бочки. Всасывание насоса поддерживается.")
  string = string.replace("Moreover, it allows to collect all the product from the inner walls down to the bottom of the drum, Pump suction is assisted", 
                          "Кроме того, он позволяет собирать всю смазку от внутренних стенок до дна бочки. Всасывание насоса поддерживается.")
  string = string.replace("Grease control gun with flexible hose and 4-jaws coupling", 
                          "Пистолет для смазки с гибким шлангом и 4-х кулачковой муфтой")
  string = string.replace("Industrial air operated pump for grease ratio", "Пневматический промышленный насос для консистентной смазки")
  string = string.replace("Pneumatic wheeled grease pump for", "Пневматический передвижной насос для смазки на")
  string = string.replace("Grease set suitable for drums", "Набор подачи смазки для бочек")
  string = string.replace("Grease set suitable for barrels", "Набор подачи смазки для бочек")
  string = string.replace("Wheeled grease set suitable for drums", "Передвижной набор подачи смазки для бочек")
  string = string.replace("Wheeled grease set suitable for barrels", "Передвижной набор подачи смазки для бочек")
  string = string.replace("Wall-fixing grease set suitable for drums", "Набор подачи консистентной смазки для бочек для настенного монтажа")
  string = string.replace("Wall- fixing grease set suitable for barrels", "Набор подачи консистентной смазки для бочек для настенного монтажа")
  string = string.replace("Wall-fixing grease set suitable for barrels", "Набор подачи консистентной смазки для бочек для настенного монтажа")
  string = string.replace("Complete installation 1 position for barrels", "Полная установка на 1 место для бочек")
  string = string.replace("Industrial air operated pump for grease ratio", 
                          "Промышленный пневматический насос для консистентной смазки")
  string = string.replace("Kit pump frame lifter and press for grease for barrels", 
                          "Набор с промышленным насосом для рамного подъёмника-пресса. Для консистентной смазки в бочках")
  string = string.replace("Aluminium casted follower plate for grease and viscous medias with rubber double ring", 
                          "Подвижная пластина из литого алюминия для консистентных смазок и вязких сред с двойным кольцом из резины")
  string = string.replace("Aluminium follower plate with rubber double ring", "Алюминиевая подвижная пластина с двойным резиновым кольцом")
  string = string.replace("Frame lifter-press for barrels", "Рамный подъёмный пресс для бочек")
  string = string.replace("Frame lifter and press", "Рамный подъёмный пресс")
  string = string.replace("For high viscosity grease and oils", "Для смазок и масел с высокой вязкостью")
  string = string.replace("Lid for pumps with shank", "Крышка для насосов с хвостовиком")
  string = string.replace("Follower plate for pumps with shank", "Подвижная пластина для насосов с хвостовиком")
  string = string.replace("Air-operated grease pump ratio=", "Пневматический насос для консистентной смазки ")
  string = string.replace("Air-operated transfer grease pump ratio", "Пневматический насос для перекачки смазки")
  string = string.replace("Air-operated grease pump ratio", "Пневматический насос для консистентной смазки ")
  string = string.replace("Air operated industrial pump for grease ratio=", "Пневматический промышленный насос для консистентной смазки ")
  string = string.replace("For pump frame lifter-press and tanks", "Для создания давления внутри рамы подъёмного пресса и резервуаров")
  string = string.replace("For pump frame lift-press and tanks", "Для создания давления внутри рамы подъёмного пресса и резервуаров")
  string = string.replace("For frame lift-press and tanks", "Для создания давления внутри рамы подъёмного пресса и резервуаров") 
  string = string.replace("Synthetic black rubber hose", "Синтетический черный резиновый шланг")
  string = string.replace("Wheeled tank for", "Передвижной бак на")
  string = string.replace("with hose reel", "с катушкой для шланга")
  string = string.replace("For standard drums", "Для стандартных бочек")
  string = string.replace("For standard barrels", "Для стандартных бочек")
  string = string.replace("For barrels", "Для создания давления внутри бочек") 
  string = string.replace("For tanks", "Для создания давления внутри резервуаров") 
  string = string.replace("follower plate", "подвижная пластина")
  string = string.replace("Length flexible hose", "Длина гибкого шланга")
  string = string.replace("flanged double effect", "фланцевый двойной эффект") 
  string = string.replace("Polyurethane seals", "Полиуретановые уплотнения")
  string = string.replace("Grease pump handle", "Ручка насоса для смазки")
  string = string.replace("WORKING PRESSURE", "РАБОЧЕЕ ДАВЛЕНИЕ")
  string = string.replace("BURST", "ДАВЛЕНИЕ \"НА РАЗРЫВ\"")
  string = string.replace("PUMP LIFT - PRESS TANK", "НАСОС ДЛЯ ПРЕССА - НАСОС ДЛЯ БАКА")
  string = string.replace("PUMP LIFT-PRESS TANK", "НАСОС ДЛЯ ПРЕССА - НАСОС ДЛЯ БАКА")
  string = string.replace("TANK", "ДЛЯ БАКА")
  string = string.replace("with adaptor flange for", "с переходным фланцем для")
  string = string.replace("suitable for air operated grease pumps", "подходящих для пневматических насосов для консистентной смазки")
  string = string.replace("Equipped with ball valve, breather valve and adaptor.", 
                          "Оснащен шаровым клапаном, воздушным клапаном и переходником.")
  string = string.replace("Equipped with follower plate for grease pumps with shank", 
                          "Оборудован подвижной пластиной для насосов для консистентной смазки с хвостовиком")
  string = string.replace("Equipped with:", "В комплекте:")
  string = string.replace("2 wheels", "2 колёсами")
  string = string.replace("2 fixed wheels", "2 фиксированными колёсами")
  string = string.replace("1 swivelling wheel", "1 поворотное колесо")
  string = string.replace("2 swivelling wheels", "2 поворотных колеса")
  string = string.replace("2 pneumatic wheels", "2 пневматическими колёсами")
  string = string.replace("Band for fixing drums", "Лентой для фиксации бочек")
  string = string.replace("Band for fixed drums", "Лентой для фиксации бочек")
  string = string.replace("Band for fixed barrels", "Лентой для фиксации бочек")
  string = string.replace("Base dimension", "Размер основания")
  string = string.replace("Adjustable base", "Регулируемая база")
  string = string.replace("Triple-swivel joint", "Тройной поворотный шарнир")
  string = string.replace("Tank of dump and stocking for", "Резервуар сброса и запаса для")
  string = string.replace("Pre-arranged for application of the hose reel", "Подготовлена для использования со шланговым барабаном")
  string = string.replace("equipped with locking device", "оснащена запорным устройством")
  string = string.replace("one is equipped with locking device", "оснащена запорным устройством")
  string = string.replace("Galvanized connection - Swivelling joint 90° galvanized", "Оцинкованное соединение - Поворотный шарнир 90° оцинкованный")
  string = string.replace("Galvanized connection  - Swivelling joint 90° galvanized", "Оцинкованное соединение - Поворотный шарнир 90° оцинкованный")
  string = string.replace("Galvanized connection", "Оцинкованное соединение")
  string = string.replace("Swivelling joint 90° galvanized", "Поворотный шарнир 90° оцинкованный")
  string = string.replace("Synthetic black rubber hose", "Синтетический черный резиновый шланг")
  string = string.replace("Syntethic black rubber hose", "Синтетический черный резиновый шланг")
  string = string.replace("Hose reel swivelling", "Шланговый барабан поворотный")
  string = string.replace("Hose reel fixed", "Шланговый барабан фиксированный")
  string = string.replace("Closed hose reel swivelling", "Барабан для шланга поворотный закрытого типа")
  string = string.replace("FOR GREASE", "ДЛЯ СМАЗКИ")
  string = string.replace("WITH HOSE", "СО ШЛАНГОМ")
  string = string.replace("Support for picking up drops", "Подставка для сбора капель")
  string = string.replace("Rubber hose", "Резиновый шланг")
  string = string.replace("Delivery ", "Производительность: ")
  string = string.replace("Polyurethane", "Полиуретановые")
  string = string.replace("shank length", "длина хвостовика")
  string = string.replace("Dimensions", "Размеры")
  string = string.replace("Inlet-Outlet", "Вход-выход")
  string = string.replace("Inlet-outlet", "Вход-выход")
  string = string.replace("Swivel joint", "Шарнир")
  string = string.replace("For drums", "для бочек")
  string = string.replace("for barrels", "для бочек")
  string = string.replace("barrels", "бочки")
  string = string.replace("barrel", "бочка")
  string = string.replace("barrel of", "бочки")
  string = string.replace("outside", "снаружи")
  string = string.replace("inside", "внутри")
  string = string.replace("lid", "крышка")
  string = string.replace("seals", "уплотнения")
  string = string.replace("shank", "хвостовика") 
  string = string.replace("kg/min", "кг/мин.")
  string = string.replace("Inlet-Outlet", "Вход-выход")
  string = string.replace("hose", "шланг")
  string = string.replace("Trolley for", "Тележка на")
  string = string.replace("drums", "бочки")
  string = string.replace("g/min", "г/мин")
  string = string.replace("l/min", "л/мин")
  string = string.replace("Mod.", "Мод.")
  string = string.replace("Art.", "арт. ") 
  string = string.replace("kg", "кг")
  string = string.replace("Kg", "кг")
  string = string.replace("m³", "м³")
  string = string.replace("m3", "м³")
  string = string.replace("mm", "мм")
  string = string.replace("bar", " бар")
  string = string.replace("length", "длиной")
  string = string.replace("1m", "1 м")
  string = string.replace("1,5m", "1,5 м")
  string = string.replace("2m", "2 м")
  string = string.replace("3m", "3 м")
  string = string.replace("4m", "4 м")
  string = string.replace("5m", "5 м")
  string = string.replace("7,5m", "7,5 м")
  string = string.replace("8m", "8 м")
  string = string.replace("l", "л")
  string = string.replace("dB", "дБ")
  return(string)



def Delete_from_String(string):
  string = string.replace("Weight ", "")
  string = string.replace("Volume ", "")
  string = string.replace("Packing ", "")
  string = string.replace("Compression ratio ", "")
  string = string.replace("Max pressure feeding ", "")
  string = string.replace("Air consumption medium ", "")
  string = string.replace("Air inlet connection ", "")
  string = string.replace("Grease outlet connection ", "")
  string = string.replace("Grease delivery capacity 6 bar ", "")
  string = string.replace("Noise ", "")
  string = string.replace("Shank diameter ", "")
  string = string.replace("Shank lenght ", "")
  string = string.replace("For drums with capacity of ", "")
  string = string.replace("Minimum height ", "")
  string = string.replace("Maximum height ", "")
  string = string.replace("Maximum pressure ", "")
  string = string.replace("Pushing power ", "")
  string = string.replace("Viscosity ", "")
  string = string.replace("Working pressure ", "")
  string = string.replace("Oil outlet connection ", "")
  string = string.replace("Oil delivery capacity 6 bar ", "")
  string = string.replace("Fluid outlet connection ", "")
  string = string.replace("Fluid delivery cap. at 6 bar ", "")
  return(string)


#---------------------------------cycle for all refs--------------------------------------#

# пробегаем по всем ссылкам раздела и собираем все интересующие нас данные
for page in pages:
  #open the webpage
  driver.get(page)

  # time.sleep(1)



  # Обработка элементов с текстом и занесение их в MYSQL БД

  header = driver.find_element_by_xpath('//*[@id="pb-left-column"]/h1').text
  header = Translate(header)
  print(header)

  article = driver.find_element_by_xpath('//*[@id="product_reference"]/span').text
  print(article)

  try:
    p_1 = driver.find_element_by_xpath('//*[@id="short_description_content"]/p[1]/strong').text
    print(p_1)
    p_1 = Translate(p_1)
    print(p_1)
  except Exception as ex:
    print("No p_1")
    print(ex)
    p_1 = ''

  try:
    p_2 = driver.find_element_by_xpath('//*[@id="short_description_content"]/p[2]').text
    print(p_2)
    p_2 = Translate(p_2)
    print(p_2)
  except Exception as ex:
    print("No p_2")
    print(ex)
    p_2 = ''



  try:
    wgh = driver.find_element_by_xpath('//*[@id="idTab2"]/li[1]').text
    print(wgh)
    wgh = Delete_from_String(wgh)
    wgh = Translate(wgh)
    print(wgh)
  except Exception as ex:
    print("No wgh")
    print(ex)
    wgh = ''

  try:
    vol  = driver.find_element_by_xpath('//*[@id="idTab2"]/li[2]').text
    print(vol)
    vol = Delete_from_String(vol)
    vol = Translate(vol)
    print(vol)
  except Exception as ex:
    print("No vol")
    print(ex)
    vol = ''

  try:
    packing = driver.find_element_by_xpath('//*[@id="idTab2"]/li[3]').text
    print(packing)
    packing = Delete_from_String(packing)
    print(packing)
  except Exception as ex:
    print("No packing")
    print(ex)
    packing = ''




  try:
    eq_1 = driver.find_element_by_xpath('//*[@id="product_list"]/li[1]/div[1]/h3/a').text  
    eq_1 = Translate(eq_1)
    print(eq_1)
    eq_1_long = driver.find_element_by_xpath('//*[@id="product_list"]/li[1]/div[1]/p/a').text  
    eq_1_long = Translate(eq_1_long)
    print(eq_1_long)
  except Exception as ex:
    print("No eq_1 and eq_1_long")
    print(ex)
    eq_1 = ''
    eq_1_long = ''


  try:
    eq_2 = driver.find_element_by_xpath('//*[@id="product_list"]/li[2]/div[1]/h3/a').text  
    eq_2 = Translate(eq_2)
    print(eq_2)
    eq_2_long = driver.find_element_by_xpath('//*[@id="product_list"]/li[2]/div[1]/p/a').text  
    eq_2_long = Translate(eq_2_long)
    print(eq_2_long)
  except Exception as ex:
    print("No eq_2 and eq_2_long")
    print(ex)
    eq_2 = ''
    eq_2_long = ''


  try:
    eq_3 = driver.find_element_by_xpath('//*[@id="product_list"]/li[3]/div[1]/h3/a').text  
    eq_3 = Translate(eq_3)
    print(eq_3)
    eq_3_long = driver.find_element_by_xpath('//*[@id="product_list"]/li[3]/div[1]/p/a').text  
    eq_3_long = Translate(eq_3_long)
    print(eq_3_long)
  except Exception as ex:
    print("No eq_3 and eq_3_long")
    print(ex)
    eq_3 = ''
    eq_3_long = ''


  try:
    eq_4 = driver.find_element_by_xpath('//*[@id="product_list"]/li[4]/div[1]/h3/a').text  
    eq_4 = Translate(eq_4)
    print(eq_4)
    eq_4_long = driver.find_element_by_xpath('//*[@id="product_list"]/li[4]/div[1]/p/a').text  
    eq_4_long = Translate(eq_4_long)
    print(eq_4_long)
  except Exception as ex:
    print("No eq_4 and eq_4_long")
    print(ex)
    eq_4 = ''
    eq_4_long = ''


  try:
    eq_5 = driver.find_element_by_xpath('//*[@id="product_list"]/li[5]/div[1]/h3/a').text  
    eq_5 = Translate(eq_5)
    print(eq_5)
    eq_5_long = driver.find_element_by_xpath('//*[@id="product_list"]/li[5]/div[1]/p/a').text  
    eq_5_long = Translate(eq_5_long)
    print(eq_5_long)
  except Exception as ex:
    print("No eq_5 and eq_5_long")
    print(ex)
    eq_5 = ''
    eq_5_long = ''


  try:
    eq_6 = driver.find_element_by_xpath('//*[@id="product_list"]/li[6]/div[1]/h3/a').text  
    eq_6 = Translate(eq_6)
    print(eq_6)
    eq_6_long = driver.find_element_by_xpath('//*[@id="product_list"]/li[6]/div[1]/p/a').text  
    eq_6_long = Translate(eq_6_long)
    print(eq_6_long)
  except Exception as ex:
    print("No eq_6 and eq_6_long")
    print(ex)
    eq_6 = ''
    eq_6_long = ''


  try:
    eq_7 = driver.find_element_by_xpath('//*[@id="product_list"]/li[7]/div[1]/h3/a').text  
    eq_7 = Translate(eq_7)
    print(eq_7)
    eq_7_long = driver.find_element_by_xpath('//*[@id="product_list"]/li[7]/div[1]/p/a').text  
    eq_7_long = Translate(eq_7_long)
    print(eq_7_long)
  except Exception as ex:
    print("No eq_7 and eq_7_long")
    print(ex)
    eq_7 = ''
    eq_7_long = ''





  try:
      connection = pymysql.connect(
          host=host,
          port=3306,
          user=user,
          password=password,
          database=db_name,
          cursorclass=pymysql.cursors.DictCursor
      )
      print("successfully connected...")
      print("#" * 20)

      try:
          cursor = connection.cursor()


          # insert data
          with connection.cursor() as cursor:
              insert_query = "INSERT INTO `air-operated_grease_pumps_sets` (header, article, p_1, p_2, eq_1, eq_1_long, \
              eq_2, eq_2_long, eq_3, eq_3_long, eq_4, eq_4_long, eq_5, eq_5_long, eq_6, eq_6_long, eq_7, eq_7_long, \
              wgh, vol, packing) \
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" 
              val = (header, article, p_1, p_2, eq_1, eq_1_long, eq_2, eq_2_long, eq_3, eq_3_long, eq_4, eq_4_long, 
                eq_5, eq_5_long, eq_6, eq_6_long, eq_7, eq_7_long, wgh, vol, packing);
              cursor.execute(insert_query, val)
              connection.commit()
 
      finally:
          connection.close()

  except Exception as ex:
      print("Connection refused...")
      print(ex)






  # Скачивание изображений
  # ссылка на раздел, в который будут сохраняться изображения
  path = 'G:/Meclube/meclube/grease_distribution/air-operated_grease_pumps_sets/images'

  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigpic"]'))).click()
  time.sleep(1)
  image = driver.find_element_by_xpath('//*[@id="fancybox-img"]').get_attribute('src')
  save_as = os.path.join(path, article + '.jpg')
  wget.download(image, save_as)

  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fancybox-right-ico"]'))).click()
  time.sleep(1)
  image = driver.find_element_by_xpath('//*[@id="fancybox-img"]').get_attribute('src')
  save_as = os.path.join(path, article + '_unit' + '.jpg')
  wget.download(image, save_as)

  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fancybox-right-ico"]'))).click()
  time.sleep(1)
  image = driver.find_element_by_xpath('//*[@id="fancybox-img"]').get_attribute('src')
  save_as = os.path.join(path, article + '_sheme' + '.jpg')
  wget.download(image, save_as)

  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fancybox-close"]'))).click()



  try:
    image = driver.find_element_by_xpath('//*[@id="product_list"]/li[1]/a/img').get_attribute('src')
    save_as = os.path.join(path, article + '_eq_1' + '.jpg')
    wget.download(image, save_as)
  except Exception as ex:
    print("No eq_1 IMG")
    print(ex)

  try:
    image = driver.find_element_by_xpath('//*[@id="product_list"]/li[2]/a/img').get_attribute('src')
    save_as = os.path.join(path, article + '_eq_2' + '.jpg')
    wget.download(image, save_as)
  except Exception as ex:
    print("No eq_2 IMG")
    print(ex)

  try:
    image = driver.find_element_by_xpath('//*[@id="product_list"]/li[3]/a/img').get_attribute('src')
    save_as = os.path.join(path, article + '_eq_3' + '.jpg')
    wget.download(image, save_as)
  except Exception as ex:
    print("No eq_3 IMG")
    print(ex)

  try:
    image = driver.find_element_by_xpath('//*[@id="product_list"]/li[4]/a/img').get_attribute('src')
    save_as = os.path.join(path, article + '_eq_4' + '.jpg')
    wget.download(image, save_as)
  except Exception as ex:
    print("No eq_4 IMG")
    print(ex)

  try:
    image = driver.find_element_by_xpath('//*[@id="product_list"]/li[5]/a/img').get_attribute('src')
    save_as = os.path.join(path, article + '_eq_5' + '.jpg')
    wget.download(image, save_as)
  except Exception as ex:
    print("No eq_5 IMG")
    print(ex)

  try:
    image = driver.find_element_by_xpath('//*[@id="product_list"]/li[6]/a/img').get_attribute('src')
    save_as = os.path.join(path, article + '_eq_6' + '.jpg')
    wget.download(image, save_as)
  except Exception as ex:
    print("No eq_6 IMG")
    print(ex)

  try:
    image = driver.find_element_by_xpath('//*[@id="product_list"]/li[7]/a/img').get_attribute('src')
    save_as = os.path.join(path, article + '_eq_7' + '.jpg')
    wget.download(image, save_as)
  except Exception as ex:
    print("No eq_7 IMG")
    print(ex)

#---------------------------------cycle for all refs--------------------------------------#


input()