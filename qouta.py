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
import random

driver = webdriver.Firefox()

nums = [["line name","number","password"],
        ["line name","number","password"]
        ]

report = ""
keyboard = Controller()


#logout function
def logoutfun():
    dropdown = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.XPATH, "//*[@id='firstHeader']/div/div/div[2]/div[3]/div/div/div[2]/div/span"))
    )
    dropdown.click()

    logout = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@style='background-color: initial; cursor: pointer; border: 3px solid transparent; height: 2.5rem; display: flex; align-items: center; justify-content: center;']"))
    )
    logout.click()

#send whatsapp function
def sendwhatsapp(phone):
    pywhatkit.sendwhatmsg_instantly(phone,report,tab_close=True,close_time=15)
    sleep(15)
    sleep(round(random.uniform(0.2, 3), 2))
    mouse.click('left')
    sleep(round(random.uniform(0.2, 1.5), 2))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


for num in nums:

    try:
        #login
        driver.get("https://my.te.eg/user/login")
        #Enter phone number
        numbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "login_loginid_input_01"))
        )
        numbox.clear()
        numbox.send_keys(num[1]) 
        sleep(0.5)
        numbox.send_keys(Keys.TAB,Keys.ARROW_DOWN,Keys.RETURN)

        #Enter password
        passbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_password_input_01"))
        )
        passbox.clear()
        passbox.send_keys(num[2],Keys.RETURN)

        try:
            #Check if qouta is empty
            IsEmpty = WebDriverWait(driver, 7.5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ant-modal-body']"))
            )
            #pressing cancel
            #cancel = WebDriverWait(driver, 7.5).until(
            #EC.presence_of_element_located((By.XPATH, "//button[@class='ant-btn ant-btn-link ec_button_ant-btn-link_4Dr4uc']"))
            #)
            #cancel.click()
            #reload page to remove the popup
            driver.get("https://my.te.eg/user/login")
            sleep(2)
            #Logout
            logoutfun()
            print("\n" + num[0] +" "+ num[1] +" : Empty Qouta \n---------------------------------------")
            report = report + "\n" + num[0] +" "+ num[1] +" : Empty Qouta \n---------------------------------------"


        except:
            #Reading Qouta
            qouta = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='_bes_window']/main/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[1]/span[1]"))
            )

            qoutaGB = qouta.text.split()[0]
            print(str(num[0]) +" "+ str(num[1]) +"\n Qouta = " + qoutaGB+ " GB ")
            report = report + "\n" + str(num[0]) +" "+ str(num[1]) +"\n Qouta = " + qoutaGB + " GB "

            #Reading Renewal Date
            driver.get("https://my.te.eg/echannel/#/overview")

            sleep(1)
            days = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='_bes_window']/main/div/div/div[3]/div[2]/div/div/div/div/div[4]/div/span"))
            )
            report = report + days.text + "\n--------------------------------------------"
            print(days.text + "\n--------------------------------------------")

            #Logout
            sleep(1)
            logoutfun()
            
    except:
        #skipping if Error happens
        print("Error in " + num[0] +" "+ num[1] + "\n-----------------------------------------")
        report = report + "\nError in " + num[0] +" "+ num[1] + "\n-----------------------------------------"
        try:
            logoutfun()
        except:
            print("try recover")

driver.quit()

#Save Report as txt File
new_var = date.today()
file = open("Qouta " + str(new_var) + ".txt", 'w') 
file.write(report) 
file.close() 

#send report on whatsapp
sendwhatsapp("+2whatsapp number")

