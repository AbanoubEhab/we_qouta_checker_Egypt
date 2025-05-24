# we_qouta_checker_Egypt

a python code to check remaining qouta form your ISP (for we website in egypt) to multiple Lines and send the report to you

## How to use it

### prerequisites

- Python 3
- pip (usually comes with Python by default)
- git (Optional)
- firefox browser (you can use any browser if you install it's selenium web driver but firefox just works [webdriver](https://www.selenium.dev/documentation/webdriver/))
  
### Installtion
1. Make new folder 

2. Open git terminal inside it and download the script  ```git clone https://github.com/AbanoubEhab/we_qouta_checker_Egypt.git``` or just download the repo as zip file and extract it.

3. open the repo folder by ```cd we_qouta_checker_Egypt```

4. Install required libraries ```pip install -r requirements.txt```

5. Adding Your Data and configs
   
   - Create '.env' file using .env.Example and add "profile_Path" with the path of your Firefox profile
     
     - If in Linux it will be inside ~/.mozilla/firefox/your_folder_name
     - If in Windows will be C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\your_folder_name
     - If You want to save the report as txt after finishing set savetxt to True
   
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
