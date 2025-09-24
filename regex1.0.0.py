# 1404/ 7/ 1
# 2025/ september/ 23 
import re
import csv

def extract_data(text):
    emails=re.findall(r"[\w%\-+.]+@[\w\-.]+\.[a-zA-Z]{2,}", text)
    phones=re.findall(r"\+?\d[\d\s\-]{8,}\d", text)
    urls=re.findall(r"httpt?://[^\s]", text)

    return emails, phones, urls

def save_to_csv(emails, phones, urls, filename="output.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Value"])

        for e in emails:
            writer.writerow(["Email", e])
        for p in phones:
            writer.writerow(["Phone", p])
        for u in urls:
            writer.writerow(["URL", u])

if __name__=="__main__":
    text =  """
    سلام، ایمیل من test.user123@example.com هست.
    شماره تماس: +98 912-345-6789
    وبسایت: https://persianghost.dev و http://example.org
                """
    emails, phones, urls = extract_data(text)
    save_to_csv(emails, phones, urls)

    print("✅ داده‌ها استخراج و در output.csv ذخیره شدند.")
