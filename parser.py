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
db_name = "your_database_name"


import os
import wget





# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('G:/Programming/WebscrapingInstagram-main/chromedriver.exe')



driver.get('http://www.meclube.com/en/24-air-operated-grease-pumps?n=20&id_category=24')

# time.sleep(1)


#target all the link elements on the page
pages = driver.find_elements_by_tag_name('a.product_img_link')
pages = [page.get_attribute('href') for page in pages]
print('Found ' + str(len(pages)) + ' links')
for page in pages:
  print(page)

print()
print('**************************************************************')
print('**************************************************************')
print()



print('CREATE TABLE `air_operated_grease_pumps`')
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


        # create table
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `air_operated_grease_pumps`(id int AUTO_INCREMENT, \
                        header varchar(100), \
                        article varchar(16), \
                        air_operated varchar(80), \
                        drums varchar(25), \
                        kg varchar(10), \
                        shank varchar(30), \
                        polyurethane varchar(15), \
                        seals varchar(10), \
                        more_1 varchar(510), \
                        more_2 varchar(280), \
                        comp_rat varchar(12), \
                        max_pr_feeding varchar(12), \
                        air_cons_medium varchar(12), \
                        air_inlet_conn varchar(12), \
                        grease_outlet_conn varchar(12), \
                        grease_delivery varchar(12), \
                        noise varchar(12), \
                        shank_d varchar(12), \
                        shank_l varchar(12), \
                        for_dr varchar(12), \
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




#---------------------------------cycle for all refs--------------------------------------#

for page in pages:
  #open the webpage
  driver.get(page)

  # time.sleep(1)




  header = driver.find_element_by_xpath('//*[@id="pb-left-column"]/h1').text
  header = header.replace("Air-operated grease pump ratio", "Пневматический насос для консистентной смазки")
  header = header.replace("Air-operated transfer grease pump ratio", "Пневматический насос для перекачки консистентной смазки")
  header = header.replace("Mod.", "Мод.")
  header = header.replace("kg", "кг")  
  print(header)

  article = driver.find_element_by_xpath('//*[@id="product_reference"]/span').text
  print(article)

  air_operated = driver.find_element_by_xpath('//*[@id="short_description_content"]/p[1]/strong').text
  air_operated = air_operated.replace("Air-operated grease pump ratio=", "Пневматический насос для консистентной смазки ")
  air_operated = air_operated.replace("Mod.", "Мод.")
  print(air_operated)

  drums = driver.find_element_by_xpath('//*[@id="short_description_content"]/p[2]').text
  kg = driver.find_element_by_xpath('//*[@id="short_description_content"]/p[2]/strong').text
  drums = drums.replace(" " + kg, "")
  drums = drums.replace("For standard drums", "Для стандартных барабанов")
  drums = drums.replace("For standard barrels", "Для стандартных бочек")
  print(drums)
  kg = kg.replace("kg", "кг")
  print(kg)

  shank = driver.find_element_by_xpath('//*[@id="short_description_content"]/p[3]').text
  shank = shank.replace("shank length", "длина хвостовика")
  shank = shank.replace("mm", "мм")
  print(shank)

  polyurethane = driver.find_element_by_xpath('//*[@id="short_description_content"]/p[4]/strong').text
  seals = driver.find_element_by_xpath('//*[@id="short_description_content"]/p[4]').text
  seals = seals.replace(polyurethane + " ", "") 
  polyurethane = polyurethane.replace("Polyurethane", "Полиуретановые")
  print(polyurethane) 
  seals = seals.replace("seals", "уплотнения")
  print(seals)



  more_1 = driver.find_element_by_xpath('//*[@id="idTab1"]/div/p[1]').text   
  more_1 = more_1.replace("Those are suitable for the supply at high pressure of all kinds of grease at short and long distance.", "Они подходят для подачи под высоким давлением всех видов смазки на короткие и большие расстояния.")
  more_1 = more_1.replace("Those are suitable for central supply of plants where a major quantity of grease and a major pressure "
    "at long and short distance are required. The operating pressure of the grease pumps hereby may vary between a minimum of 2.5 bar "
    "and a maximum of 8 bar. In order to optimize the efficiency and the life of our pumps we recommend to use filtered and lubricated air.", 
    "Они подходят для централизованного снабжения заводов, где требуется перекачка большого количество смазки под высоким давлением на большие и малые расстояния. "
    "При этом рабочее давление насосов для консистентной смазки может варьироваться от минимального в 2,5 бара до максимального в 8 бар. Чтобы оптимизировать эффективность "
    "и срок службы наших насосов, мы рекомендуем использовать фильтрованный и смазанный воздух.")
  more_1 = more_1.replace("Those are suitable for central supply of plants where a major pressure at long and short distance is required. The operating pressure of the grease "
    "pumps hereby may vary between a minimum of 2.5 bar and a maximum of 8 bar. In order to optimize the efficiency and the life of our pneumatic pumps we recommend to use filtered and lubricated air.", 
    "Они подходят для централизованного питания заводов, где требуется перекачка под высоким давлением на большие и малые расстояния. При этом рабочее давление насосов для консистентной смазки может варьироваться "
    "от минимального в 2,5 бара до максимального в 8 бар. Чтобы оптимизировать эффективность и срок службы наших пневматических насосов, мы рекомендуем использовать фильтрованный и смазанный воздух.")
  more_1 = more_1.replace("They are suitable for transferring a lot of types of grease, filling of central distribution plants, dispensers "
    "and manual pumps where a major quantity of grease with slow pressure and short distance is required. The operating pressure of the grease "
    "pumps hereby may vary between a minimum of 3.5 bar and a maximum of 8 bar. In order to optimize the efficiency and the life of our pneumatic "
    "pumps we recommend to use filtered and lubricated air.", 
    "Они подходят для перекачки многих типов смазки, заполнения центральных распределительных станций, дозаторов и ручных насосов. Идеальны там, где требуется перекачивать большое количество смазки "
    "при низком давлении на короткие расстояния. При этом рабочее давление насосов для консистентной смазки может варьироваться от минимального в 3,5 бара до максимального в 8 бар. "
    "Чтобы оптимизировать эффективность и срок службы наших пневматических насосов, мы рекомендуем использовать фильтрованный и смазанный воздух.")
  print(more_1)
  try:
    more_2 = driver.find_element_by_xpath('//*[@id="idTab1"]/div/p[2]').text  
    more_2 = more_2.replace("The operating pressure of the grease pumps hereby may vary between a minimum of 2.5 bar "
      "and a maximum of 8 bar. In order to optimize the efficiency and the life of our air operated pumps, we recommend "
      "to use filtered and lubricated air.", "При этом рабочее давление насосов для консистентной смазки может варьироваться "
      "от минимального в 2,5 бара до максимального в 8 бар. Чтобы оптимизировать эффективность и срок службы наших пневматических "
      "насосов, мы рекомендуем использовать фильтрованный и смазанный воздух.")
    print(more_2)
  except Exception as ex:
    print("No element...")
    print(ex)
    more_2 = ''



  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_info_tab_data_sheet"]'))).click()
  # time.sleep(1)

  comp_rat = driver.find_element_by_xpath('//*[@id="idTab2"]/li[1]').text
  print(comp_rat)
  comp_rat = comp_rat.replace("Compression ratio ", "")
  print(comp_rat)

  max_pr_feeding = driver.find_element_by_xpath('//*[@id="idTab2"]/li[2]').text
  print(max_pr_feeding)
  max_pr_feeding = max_pr_feeding.replace("Max pressure feeding ", "")
  max_pr_feeding = max_pr_feeding.replace("bar", "бар")
  print(max_pr_feeding)

  air_cons_medium = driver.find_element_by_xpath('//*[@id="idTab2"]/li[3]').text
  print(air_cons_medium)
  air_cons_medium = air_cons_medium.replace("Air consumption medium ", "")
  air_cons_medium = air_cons_medium.replace("l/min", "л/мин")
  print(air_cons_medium)

  air_inlet_conn = driver.find_element_by_xpath('//*[@id="idTab2"]/li[4]').text
  print(air_inlet_conn)
  air_inlet_conn = air_inlet_conn.replace("Air inlet connection ", "")
  print(air_inlet_conn)

  grease_outlet_conn = driver.find_element_by_xpath('//*[@id="idTab2"]/li[5]').text
  print(grease_outlet_conn)
  grease_outlet_conn = grease_outlet_conn.replace("Grease outlet connection ", "")
  print(grease_outlet_conn)

  grease_delivery = driver.find_element_by_xpath('//*[@id="idTab2"]/li[6]').text
  print(grease_delivery)
  grease_delivery = grease_delivery.replace("Grease delivery capacity 6 bar ", "")
  grease_delivery = grease_delivery.replace("g/min", "г/мин")
  print(grease_delivery)

  noise = driver.find_element_by_xpath('//*[@id="idTab2"]/li[7]').text
  print(noise)
  noise = noise.replace("Noise ", "")
  noise = noise.replace("dB", "дБ")
  print(noise)

  shank_d = driver.find_element_by_xpath('//*[@id="idTab2"]/li[8]').text
  print(shank_d)
  shank_d = shank_d.replace("Shank diameter ", "")
  shank_d = shank_d.replace("mm", "мм")
  print(shank_d)

  shank_l = driver.find_element_by_xpath('//*[@id="idTab2"]/li[9]').text
  print(shank_l)
  shank_l = shank_l.replace("Shank lenght ", "")
  shank_l = shank_l.replace("mm", "мм")
  print(shank_l)

  for_dr = driver.find_element_by_xpath('//*[@id="idTab2"]/li[10]').text
  print(for_dr)
  for_dr = for_dr.replace("For drums with capacity of ", "")
  for_dr = for_dr.replace("kg", "кг")
  print(for_dr)

  wgh = driver.find_element_by_xpath('//*[@id="idTab2"]/li[11]').text
  print(wgh)
  wgh = wgh.replace("Weight ", "")
  wgh = wgh.replace("kg", "кг")
  print(wgh)

  vol  = driver.find_element_by_xpath('//*[@id="idTab2"]/li[12]').text
  print(vol)
  vol = vol.replace("Volume ", "")
  vol = vol.replace("m³", "м³")
  print(vol)

  packing = driver.find_element_by_xpath('//*[@id="idTab2"]/li[13]').text
  print(packing)
  packing = packing.replace("Packing ", "")
  print(packing)





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
              insert_query = "INSERT INTO `air_operated_grease_pumps` (header, article, \
              air_operated, drums, kg, shank, polyurethane, seals, more_1, more_2, comp_rat, \
              max_pr_feeding, air_cons_medium, air_inlet_conn, grease_outlet_conn, \
              grease_delivery, noise, shank_d, shank_l, for_dr, wgh, vol, packing) \
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" 
              val = (header, article, 
                  air_operated, drums, kg, shank, polyurethane, seals, more_1, more_2, comp_rat, max_pr_feeding, air_cons_medium, 
                  air_inlet_conn, grease_outlet_conn, grease_delivery, noise, shank_d, shank_l, for_dr, wgh, vol, packing);
              cursor.execute(insert_query, val)
              connection.commit()


      finally:
          connection.close()

  except Exception as ex:
      print("Connection refused...")
      print(ex)








  # path to the directory in which we gonna save images
  path = 'G:/Meclube/meclube/grease_distribution/air_operated_grease_pumps/images'

  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigpic"]'))).click()
  time.sleep(1)
  image = driver.find_element_by_xpath('//*[@id="fancybox-img"]').get_attribute('src')
  save_as = os.path.join(path, article + '.jpg')
  wget.download(image, save_as)


  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fancybox-right-ico"]'))).click()
  time.sleep(1)
  image = driver.find_element_by_xpath('//*[@id="fancybox-img"]').get_attribute('src')
  save_as = os.path.join(path, article + '_sheme' + '.jpg')
  wget.download(image, save_as)

#---------------------------------cycle for all refs--------------------------------------#


input()