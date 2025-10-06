# 1404/ 7 / 
# 2025/ September/ 
"""
version : 1.2.1
Features (English) :
1. Code Refactored into Class Structure:
---All extraction functions (emails, phones, URLs) are now inside a single class (DataExtractor)
---Improved modularity and readability for future updates
#============================================================
2. Automatic Folder Creation:
---If 'outputs' folder doesn’t exist, it is created automatically
#============================================================
3. File Naming by Current Date:
---Output files are named with the current date (e.g., data_20251005.json)
---Helps organize saved data by extraction date
#============================================================
4. User Choice for Output Format:
---User can choose between JSON, CSV, or BOTH for data export
---Invalid input defaults to 'both' automatically
#============================================================
5. Extraction Summary Report:
---After saving, a summary report displays total counts for emails, phones, and URLs
---Shows the full path of the saved folder
#============================================================
6. Improved Regex Accuracy and Case Insensitivity:
---Regex patterns are cleaner and use re.IGNORECASE for better match accuracy
#============================================================
7. Overall Code Optimization:
---Simplified structure, cleaner indentation, and more readable flow
---Prepared for next step (v2.0.0) which will include web scraping
#============================================================
#============================================================
ویژگی‌ها (فارسی) :
1. بازنویسی کد در قالب کلاس:
---تمام توابع استخراج (ایمیل، شماره، آدرس وب) داخل یک کلاس واحد (DataExtractor) قرار گرفتند  
---ساختار کد منظم‌تر و آماده برای توسعه‌های بعدی شد  
#============================================================
2. ایجاد خودکار پوشه خروجی:
---اگر پوشه‌ی outputs وجود نداشته باشد، به‌صورت خودکار ساخته می‌شود  
#============================================================
3. نام‌گذاری فایل‌ها بر اساس تاریخ روز:
---فایل‌های خروجی با تاریخ روز ذخیره می‌شوند (مثلاً data_20251005.json)  
---برای نظم بهتر در فایل‌های ذخیره‌شده  
#============================================================
4. انتخاب نوع خروجی توسط کاربر:
---کاربر می‌تواند بین فرمت JSON، CSV یا هر دو گزینه انتخاب کند  
---در صورت ورود گزینه نامعتبر، به‌طور پیش‌فرض «both» انتخاب می‌شود  
#============================================================
5. نمایش خلاصه عملیات استخراج:
---پس از ذخیره، گزارشی از تعداد ایمیل‌ها، شماره‌ها و آدرس‌ها نمایش داده می‌شود  
---مسیر کامل پوشه خروجی نیز نشان داده می‌شود  
#============================================================
6. بهبود دقت عبارات منظم (Regex):
---عبارات منظم تمیزتر و حساسیت به حروف بزرگ/کوچک حذف شده است  
#============================================================
7. بهینه‌سازی کلی کد:
---کد خواناتر، ساده‌تر و ساختارمندتر شده  
---آماده‌سازی برای نسخه‌ی بعدی (v2.0.0) که شامل web scraping خواهد بود  
"""
############################
import re                                           #
import json                                       #
import csv                                        #
import datetime                              #
import os                                        #
from colorama import Fore, Style  #
##########################

file_path = input(
    Fore.BLACK
    +"enter your text address : "
    +Style.RESET_ALL
    )
try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(
            Fore.RED 
            +"The address is wrong ❌\nCheck your address ❗"
            +Style.RESET_ALL
            ) 
    exit()
#==================================================
class DataExtractor:
    def __init__(self, text):
        self.text = text
        self.emails  =[]
        self.phones  =[]
        self.urls  =[]        
        
    def extract_emails(self):
        self.emails = list(set(re.findall(
            r"[\w\.\-%]+@[\w\.\-]+\.[a-zA-Z]{2,}",
            self.text, flags=re.IGNORECASE)))
#===================================
    def extract_phones(self):
        self.phones = list(set(re.findall(
            r"\+?\d{1,4}[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{3,4}[\s\-]?\d{3,4}",
            self.text, flags=re.IGNORECASE)))
#===================================
    def extract_urls(self):
        self.urls = list(set(re.findall(
            r"https?://[^\s]+",
            self.text, flags=re.IGNORECASE)))
#==================================================
    def save_data(self, output_folder="outputs", format_choice="both", ):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        #===================================
        today = datetime.date.today().strftime("%Y%m%d")
    #===== SAVE JSON =====================================
        if format_choice in ["json", "both"]:
            json_name = os.path.join(output_folder, f"data_{today}.json")
            data = {"Email" : self.emails, "Phone" : self.phones, "URL": self.urls}
            with open(json_name, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
    #===== SAVE CSV ======================================
        if format_choice in ["csv", "both"]:
            csv_name = os.path.join(output_folder, f"data_{today}.csv")
            with open(csv_name, "w", newline="", encoding="utf-8-sig") as c:
                write = csv.writer(c)
                write.writerow(["Type", "Value"])
                for e in self.emails:
                    write.writerow(["Email", e])
                for p in self.phones:
                    write.writerow(["Phone", p])
                for u in self.urls:
                    write.writerow(["URL", u])

        self.report_summary(output_folder)        
    
    def report_summary(self,output_folder):
        print(
                Fore.GREEN
                +"\n✅ Extraction complete!" 
                + Style.RESET_ALL
                )
        print(
                Fore.CYAN
                +"Emails found: "+ Fore.BLUE +f"{len(self.emails)}"
                + Style.RESET_ALL
                )
        print(
                Fore.CYAN
                +"Phones found: "+ Fore.BLUE +f"{len(self.phones)}"
                + Style.RESET_ALL
                )
        print(
                Fore.CYAN
                +"URLs found: "+ Fore.BLUE +f"{len(self.urls)}"
                + Style.RESET_ALL
                )
        print(
                Fore.CYAN
                +"Files saved in folder: "+ Fore.BLUE +f"{os.path.abspath(output_folder)}"
                + Style.RESET_ALL
                )
#==================================================
extractor = DataExtractor(text)
extractor.extract_emails()
extractor.extract_phones()
extractor.extract_urls()
#===================================
choice = input(Fore.BLUE + "Choice output format " + Fore.YELLOW + "(json/csv/both): " + Style.RESET_ALL).lower()
if choice not in ["json", "csv", "both"]:
    print(
        Fore.RED
        + "Invalid choice ❌ default set to 'both'"
        + Style.RESET_ALL
        )
    choice = "both"
extractor.save_data(output_folder="outputs", format_choice=choice)