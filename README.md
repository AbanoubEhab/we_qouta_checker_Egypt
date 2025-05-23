# we_qouta_checker_Egypt

a python code to check remaining qouta form your ISP (for we website in egypt) to multiple Lines and send the report to you

## How to use it

### prerequisites

- Python 3
- pip
- git
- firefox browser (you can use any browser if you install it's selenium web driver but firefox just works [webdriver](https://www.selenium.dev/documentation/webdriver/))
  
### Installtion
1. Make new folder and open git terminal inside it

2. Download the script  ```git clone https://github.com/AbanoubEhab/we_qouta_checker_Egypt.git```

3. open the repo folder by ```cd we_qouta_checker_Egypt```

4. Install required libraries ```pip install -r requirements.txt```

5. open qouta.py 
   
   - Create '.env' file using .env.Example and add "profile_Path" with the path of your Firefox profile
     
     - if in Linux it will be inside ~/.mozilla/firefox/your_folder_name
     - if in Windows will be C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\your_folder_name
   
   - Copy Numbers.Example.csv to Numbers.csv and replace the data with your data Using excel or any program that can edit CSV
     
     | line_name | Line_number | Password |
     | --------- | ----------- | -------- |
     | line 1    | 2123456     | Password |
     | line 2    | 1234567     | password |
   
   - Copy Whatsapp.Example.csv to Whatsapp.csv and fill the numbers you want the report to be sent to,
   **MUST INCLUDE COUNTRY CODE**
      | Numbers       |
      | ------------- |
      | +201234567890 |
      | +201198765432 |
      | +201512345678 |

*Note : Make sure you logged in with whatsapp web before running the script

6. run the script by ```python3 ./qouta.py```
