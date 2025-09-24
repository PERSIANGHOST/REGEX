# 1404/ 7/ 2
# 2025/ september/ 24
"""
version : 1.1.0
Features :
- extract emails, phones, urls from text file
- save results to JSON and CSV
- handle wrong file path
- remove duplicates
"""
import re 
import csv
import json

file_path = input("enter your text address : ")
try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("The address is wrong ❌\nCheck your address ❗")
    exit()

def extract_emails(text):
    return re.findall(r"[\w\.\-%]+@[\w\.\-]+\.[a-zA-Z]{2,}",text, flags=re.IGNORECASE)
emails = extract_emails(text)
emails = list(set(extract_emails(text)))
#==================================================
def extract_phones(text):
    return re.findall(r"\+?\d[\d\s\-]{7,}\d",text, flags=re.IGNORECASE)
Phones = extract_phones(text)
Phones = list(set(extract_phones(text)))
#==================================================
def extract_urls(text):
    return re.findall(r"https?://[^\s]+", text, flags=re.IGNORECASE)
urls = extract_urls(text)
urls = list(set(extract_urls(text)))
#==================================================
data = {"Email" : emails, "Phone" : Phones, "URL": urls}
with open("data_v1_1_0.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
#==================================================
with open("data_v1_1_0.csv", "w", newline="", encoding="utf-8") as c:
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
        print("your output data seved in data_v1_1_0.json and data_v1_1_0.csv files ✔")