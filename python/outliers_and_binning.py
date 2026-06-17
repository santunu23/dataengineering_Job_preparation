import pandas as pd
import numpy as np

# আমাদের কোম্পানির কর্মচারীদের ডেটা
emp_data = {
    'emp_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Sajib', 'Tanvir', 'Kamal', 'Rahim', 'Nadia', 'Asif', 'Joy'],
    'age': [28, 35, 42, 150, 31, 24, 38], # লক্ষ্য করো: ১৫০ একটি অস্বাভাবিক বয়স (Outlier)
    'salary': [50000, 75000, 110000, 60000, 85000, 45000, 95000]
}

df = pd.DataFrame(emp_data)
print("--- ১. মূল ডেটাসেট (আউটলায়ারসহ) ---")
print(df)
print("\n" + "="*50 + "\n")

df_clean=df[df['age']<=100].copy()
print("--- ২. আউটলায়ার (১৫০ বছর) ফেলে দেওয়ার পর ক্লিন ডেটাসেট ---")
print(df_clean)
print("\n" + "="*50 + "\n")

# বয়সের বাউন্ডারি (Bins) নির্ধারণ: ২০ থেকে ৩০, ৩০ থেকে ৪০, ৪০ থেকে ৫০
# এখানে আমরা ৩টি গ্রুপ বানাচ্ছি, তাই ৪টি বর্ডার ভ্যালু লাগবে
age_bins = [20, 30, 40, 50] 
age_labels = ['Junior', 'Mid-Level', 'Senior']


# pd.cut() দিয়ে নতুন ক্যাটাগরি কলাম তৈরি করা
df_clean['experience_category'] = pd.cut(df_clean['age'], bins=age_bins, labels=age_labels)

print("--- ৩. বিনিং করার পর চূড়ান্ত রিপোর্ট (Experience Category সহ) ---")
print(df_clean)