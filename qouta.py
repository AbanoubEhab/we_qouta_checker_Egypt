from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import date
from pynput.keyboard import Key, Controller
import random
from urllib.parse import quote
import csv

profile_path = r'Firefox_Profile_Path'

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('-profile')
firefox_options.add_argument(profile_path)

driver = webdriver.Firefox(options=firefox_options)

report = ""
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
def sendwhatsapp(phone):
    driver.get("https://web.whatsapp.com/send?phone=" + phone + "&text="+ creport )
    sleep(14 + round(random.uniform(0.2, 3), 2))
    send = WebDriverWait(driver, 7.5).until(
       EC.presence_of_element_located((By.XPATH, "/html/body"))
    )
    send.send_keys(Keys.RETURN)
    sleep( 2 + round(random.uniform(0.2, 3), 2))

read_csv("Numbers.csv",nums)
read_csv("Whatsapp.csv",ITTeam)

# Print the filled arrays
print(nums)
print(ITTeam)

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
            sleep(2)
            IsEmpty = WebDriverWait(driver, 7.5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ant-modal-body']"))
            )

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
            
            #if the number is mobile qouta shows in MB instaed of GB
            if num[1][:3] == "015":
                unit = " MB "
            else:
                unit = " GB "

            print(str(num[0]) +" "+ str(num[1]) +"\n Qouta = " + qoutaGB+ unit )
            report = report + "\n" + str(num[0]) +" "+ str(num[1]) +"\n Qouta = " + qoutaGB + unit

            #Reading Renewal Date
            driver.get("https://my.te.eg/echannel/#/overview")

            sleep(2)
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

#Save Report as txt File
new_var = date.today()
file = open(str(new_var)+ " Qouta" + ".txt", 'w') 
file.write(report) 
file.close() 

#reformat the report to be added to whatsapp link
creport = quote(report)

#send report on whatsapp
driver.get("https://web.whatsapp.com")
sleep(20)

for mem in ITTeam:
    sendwhatsapp(mem[0])

driver.quit()
