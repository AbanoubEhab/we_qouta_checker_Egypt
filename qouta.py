from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import date
from pynput.keyboard import Key, Controller
from urllib.parse import quote
from dotenv import load_dotenv, dotenv_values
import random, os, csv
 
load_dotenv('.env')

profile_path: str = os.getenv('profile_path')
savetxt = os.getenv('savetxt')

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('-profile')
firefox_options.add_argument(profile_path)

driver = webdriver.Firefox(options=firefox_options)

report = ""
actreport = ""
keyboard = Controller()
#Creating Arrays to hold the data from CSVs
nums = []
ITTeam = []

def read_csv(csv_file,data_Array):
    
    # Open the CSV file and read its contents
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header row (optional)
        next(csv_reader)
        
        # Iterate over each row and append it to the list
        for row in csv_reader:
            data_Array.append(row)

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
def sendwhatsapp(phone,message):
    driver.get("https://web.whatsapp.com/send?phone=" + phone + "&text="+ message )
    sleep(14 + round(random.uniform(0.2, 3), 2))
    send = WebDriverWait(driver, 7.5).until(
       EC.presence_of_element_located((By.XPATH, "/html/body"))
    )
    send.send_keys(Keys.RETURN)
    sleep( 2 + round(random.uniform(0.2, 3), 2))

read_csv("Numbers.csv",nums)
read_csv("Whatsapp.csv",ITTeam)
random.shuffle(ITTeam)

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
        sleep(1)
        numbox.send_keys(Keys.TAB,Keys.ARROW_DOWN,Keys.RETURN)
        #Enter password
        passbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_password_input_01"))
        )
        passbox.clear()
        passbox.send_keys(num[2],Keys.RETURN)

        try:
            #Check if qouta is empty
            sleep(2)
            IsEmpty = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ant-modal-confirm-content"))
            )
            sleep(2)
            if IsEmpty.text == "Please renew your package to resume the service or you can use Salefny service for 10 EGP to get 5 GB at your original speed valid for 48 hours till you renew your package":
                driver.get("https://my.te.eg/user/login")
                sleep(2)
                #Logout
                logoutfun()
                print("\n🚨 " + num[0] +" : "+ num[1] +" : Empty Qouta \n--------------------------------------------")
                report = report + "\n🚨 " + num[0] +" : "+ num[1] +" : Empty Qouta \n--------------------------------------------"

                if num[3] == "0":
                    actreport = actreport + "\n🚨 " + num[0] +" : "+ num[1] +" : Empty Qouta \n--------------------------------------------"

            else:
                # Just Promo popup
                driver.get("https://my.te.eg/user/login")
                sleep(2)
                raise Exception("Intentional crash to continue read data")


        except:
            #Reading Qouta
            qouta = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='_bes_window']/main/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[1]/span[1]"))
            )
            qoutaGB = qouta.text.split()[0]
            qoutanum = float(qoutaGB)
            
            #if the number is mobile qouta shows in MB instaed of GB
            if num[1][:3] == "015":
                unit = " MB "
            else:
                unit = " GB "

            if qoutanum < 30:
                print(str(num[0]) +" : "+ str(num[1]) +"\n⚠️ Qouta = " + qoutaGB + unit )
                report = report + "\n" + str(num[0]) +" : "+ str(num[1]) +"\n⚠️ Qouta = " + qoutaGB + unit

                if num[3] =="0":
                    actreport = actreport + "\n" + str(num[0]) +" : "+ str(num[1]) +"\n⚠️ Qouta = " + qoutaGB + unit
            else:
                print(str(num[0]) +" : "+ str(num[1]) +"\nQouta = " + qoutaGB + unit )
                report = report + "\n" + str(num[0]) +" : "+ str(num[1]) +"\nQouta = " + qoutaGB + unit

            #Reading Renewal Date
            driver.get("https://my.te.eg/echannel/#/overview")

            sleep(2)
            days = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='_bes_window']/main/div/div/div[3]/div[2]/div/div/div/div/div[4]/div/span"))
            )

            daynum = int(days.text.split()[3])

            if daynum < 4:
                report = report + "\n⚠️ " + days.text + "\n--------------------------------------------"
                print("\n⚠️ " + days.text + "\n--------------------------------------------")

                if num[3] =="0":
                    actreport = actreport + "\n" + str(num[0]) +" : "+ str(num[1]) +"\n Qouta = " + qoutaGB + unit + "\n⚠️ " + days.text + "\n--------------------------------------------"

            else:
                report = report + days.text + "\n--------------------------------------------"
                print(days.text + "\n--------------------------------------------")

            #Logout
            sleep(1)
            logoutfun()
            
    except:
        try:

            IsEmptyMob = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@style='font-size: var(--ec-title-h6); color: rgb(49, 49, 49); font-weight: 700; margin-left: 20px; height: 8rem; margin-top: 20px;']"))
                )
            if IsEmptyMob.text == "No usage data available":
                logoutfun()
                print("\n🚨 " + num[0] +" : "+ num[1] +" : Empty Qouta \n--------------------------------------------")
                report = report + "\n🚨 " + num[0] +" : "+ num[1] +" : Empty Qouta \n--------------------------------------------"

                if num[3] =="0":
                    actreport = actreport + "\n🚨 " + num[0] +" : "+ num[1] +" : Empty Qouta \n--------------------------------------------"
            else:
                raise Exception("Intentional crash to continue read data")


        except:
            #skipping if Error happens
            print("Error in " + num[0] +" "+ num[1] + "\n--------------------------------------------")
            report = report + "\nError in " + num[0] +" "+ num[1] + "\n--------------------------------------------"
            try:
                driver.get("https://my.te.eg/echannel/#/overview")
                sleep(3)
                logoutfun()
            except:
                print("try recover")

#Save Report as txt File
if savetxt == "True":
    new_var = date.today()
    file = open(str(new_var)+ " Qouta" + ".txt", 'w') 
    file.write(report) 
    file.close() 

#reformat the report to be added to whatsapp link
creport = quote(report)
cactreport = quote(actreport)

#send report on whatsapp
driver.get("https://web.whatsapp.com")
sleep(20)

for mem in ITTeam:
    if mem[1]=="0":
        sendwhatsapp(mem[0],creport)
    elif cactreport != "":
        sendwhatsapp(mem[0],cactreport)

driver.quit()
