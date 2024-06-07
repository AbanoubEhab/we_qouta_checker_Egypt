# we_qouta_checker_Egypt

a python code to check remaining qouta form your ISP (for we website in egypt) to multiple Lines and send the report to you

## How to use it

1. Download the script  ```git clone https://github.com/AbanoubEhab/we_qouta_checker_Egypt.git```
2. Install required libraries ```pip install -r requirements.txt```
3. open qouta.py 
   - Replace "firefox_profile_Path" in line 12 with the path of your Firefox profile
     - if in Linux it will be inside ~/.mozilla/firefox/your_folder_name
     - if in Windows will be C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\your_folder_name
     
   - fill nums array with your data ```nums = [["line_name","Line_number","Password"],
        ["line_name","Line_number","Password"],
        
        ]```
   - fill the array ```ITTeam = ["number_to_send_whatsapp", "number_to_send_whatsapp", "number_to_send_whatsapp"]```
   with the numbers you want the script to send the report to
1. run the script by python3 ./qouta.py
