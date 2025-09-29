# 1404/ 7 / 7
# 2025/ September/ 29 
"""
version : 1.1.1
Features :
- Removed duplicate function calls
- Added dynamic filenames (with date)
- Improved CSV encoding (utf-8-sig)
"""
################
import re                 #
import csv               #
import json             #
import datetime     #
###############

file_path = input("enter your text address : ")
try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("The address is wrong ❌\nCheck your address ❗")
    exit()
#==================================================
def extract_emails(text):
    return re.findall(r"[\w\.\-%]+@[\w\.\-]+\.[a-zA-Z]{2,}",text, flags=re.IGNORECASE)
emails = list(set(extract_emails(text)))
#===================================
def extract_phones(text):
    return re.findall(r"\+?\d[\d\s\-]{7,}\d",text, flags=re.IGNORECASE)
Phones = list(set(extract_phones(text)))
#===================================
def extract_urls(text):
    return re.findall(r"https?://[^\s]+", text, flags=re.IGNORECASE)
urls = list(set(extract_urls(text)))
#==================================================
today = datetime.date.today().strftime("%Y%m%d")
#===== SAVE JSON =====================================
json_name = f"data_{today}.json"
data = {"Email" : emails, "Phone" : Phones, "URL": urls}
with open(json_name, "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
#===== SAVE CSV ======================================
csv_name = f"data_{today}.csv"
with open(csv_name, "w", newline="", encoding="utf-8-sig") as c:
    write = csv.writer(c)
    write.writerow(["Type", "Value"])
    for e in emails:
        write.writerow(["Email", e])
    for p in Phones:
        write.writerow(["Phone", p])
    for u in urls:
        write.writerow(["URL", u])
    if not (emails or Phones or urls):
        print("Not found data in your file ❗")
    else:
        print(f"your output data saved in {csv_name} and {json_name} files ✔")
