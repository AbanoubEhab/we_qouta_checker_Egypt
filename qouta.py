from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import date
import pywhatkit
from pynput.keyboard import Key, Controller
import mouse

driver = webdriver.Firefox()

driver.get("https://my.te.eg/user/login")

nums = [["Line 1","Phone Number","Password"],
        ["Line 2","Phone Number","Password"],
        ]

report = ""

for num in nums:

    try:
        #Enter phone number
        numbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-service-number-et"))
        )
        numbox.clear()
        numbox.send_keys(num[1]) 
        numbox.send_keys(Keys.TAB,Keys.ARROW_DOWN)

        #Enter password
        passbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-password-et"))
        )
        passbox.clear()
        passbox.send_keys(num[2],Keys.RETURN)

        try:
            #Check if qouta is empty
            cancel = WebDriverWait(driver, 7.5).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='bg-transparent border-0 text-color p-button p-component']"))
            )
            cancel.click()

            sleep(2.5)
            #Logout
            dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='p-submenu-icon pi pi-angle-down ng-star-inserted']"))
            )
            dropdown.click()

            logout = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "logout-btn"))
            )
            logout.click()
            report = report + num[0] +" "+ num[1] +" : Empty Qouta \n---------------------------------------"


        except:
            #Reading Qouta
            qouta = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "usage"))
            )

            qoutaGB = qouta.text.split()[0]
            print(str(num[0]) +" "+ str(num[1]) +"\n qouta = " + qoutaGB+ " GB ")
            report = report + "\n" + str(num[0]) +" "+ str(num[1]) +"\n qouta = " + qoutaGB + " GB "

            #Reading Renewal Date
            driver.get("https://my.te.eg/offering/overview")

            days = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "mr-auto"))
            )
            print(days.text+"\n--------------------------------------------")
            report = report + days.text + "\n--------------------------------------------"

            #Logout
            sleep(1)
            dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='p-submenu-icon pi pi-angle-down ng-star-inserted']"))
            )
            dropdown.click()

            logout = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "logout-btn"))
            )
            logout.click()
            
    except:
        #skipping if Error happens
        print("Error in " + num[0] +" "+ num[1] + "\n-----------------------------------------")
        report = report + "\nError in " + num[0] +" "+ num[1] + "\n-----------------------------------------"

driver.quit()

#Save Report as txt File
new_var = date.today()
file = open("Qouta " + str(new_var) + ".txt", 'w') 
file.write(report) 
file.close() 

#send report on whatsapp
keyboard = Controller()
pywhatkit.sendwhatmsg_instantly("Mobile_Number",report,tab_close=True)
sleep(2)
mouse.click('left')
sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
