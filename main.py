import pandas as pd
import numpy as np
import sqlite3

# خواندن فایل اکسل
data = pd.read_excel("data.xls")
# برای اینکه فایل اصلی دستنخورده باشه ازش کپی میگیریم تا تغییرات روش اعمال کنیم
dt=data.copy()
# ۵ ردیف اول رو چاپ میکنه
# print(data.head(5))

# حذف سطرهای دارای مقدار خالی
dt.dropna(axis=0, how='all', inplace=True)

# حذف سطرهای تکراری
dt.drop_duplicates(inplace=True)

# print(data.isna()

# اضافه کردن ستون جدید که نسبت profit به sales هست
dt['Profit/Sales'] = dt['Profit'] / dt['Sales']

# گروه بندی بر اساس کتگوری
dt.groupby('Sub-Category')
# print("done")

dt.to_excel('dt.xlsx', index=False)
