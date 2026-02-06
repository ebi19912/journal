from bs4 import BeautifulSoup
import pandas as pd

# خواندن محتوای فایل HTML
with open('333.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# تجزیه HTML
soup = BeautifulSoup(html_content, 'html.parser')

# یافتن جدول اصلی (با عرض 90%)
table = soup.find('table', {'width': '90%', 'style': 'border-style: none solid solid solid; border-width: 1px; border-color: #666666; margin-left:auto;margin-right:auto'})

# استخراج داده‌ها
data = []
for row in table.find_all('tr')[1:]:  # رد کردن ردیف هدر
    cols = row.find_all('td')
    if len(cols) >= 5:  # فقط ردیف‌های با ۵ ستون
        row_data = [
            cols[0].get_text(strip=True),  # ردیف
            cols[1].get_text(strip=True),  # عنوان نشریه
            cols[2].get_text(strip=True),  # ISSN
            cols[3].get_text(strip=True),  # E_ISSN
            cols[4].get_text(strip=True)   # H index
        ]
        data.append(row_data)

# ایجاد DataFrame و ذخیره در اکسل
df = pd.DataFrame(data, columns=['ردیف', 'عنوان نشریه', 'ISSN', 'E_ISSN', 'H index'])
df.to_excel('journals_list.xlsx', index=False, engine='openpyxl')

print("فایل اکسل با موفقیت ایجاد شد: journals_list.xlsx")