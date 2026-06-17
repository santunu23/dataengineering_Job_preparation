import pandas as pd
import numpy as np

# একটি ডামি নোংরা ডেটা ডিকশনারি(যেখানে Null and Duplicate ডাটা আছে)
dirty_data ={
    'employee_id': [101, 102, 103, 101, 104, 105, 105],
    'name': ['Sajib', 'Tanvir', 'Kamal', 'Sajib', 'Rahim', 'Nadia', 'Nadia'],
    'department': ['IT', 'HR', None, 'IT', 'Marketing', 'Sales', 'Sales'],
    'salary': [60000, np.nan, 50000, 60000, 45000, np.nan, np.nan]
}

# df=pd.DataFrame(dirty_data)
# print("--- ১. মূল নোংরা ডেটাসেট ---")
# print(df)
# print("\n" + "="*40 + "\n")

df=pd.DataFrame(dirty_data)
print("--- ১. মূল নোংরা ডেটাসেট ---")
print(df)
print("\n" + "="*40 + "\n")

# নাল ভ্যালু বা মিসিং ডাটা (Null/NaN) হ্যান্ডেল করা

#print("---2.কলামভিত্তিক নাল ভ্যালুর সংখ্যা---")
#print(df.isna().sum())
#print("\n")


# ট্রান্সফরমেশন লজিক: 
# ডিপার্টমেন্ট ফাঁকা থাকলে 'Unknown' বসাবো এবং স্যালারি ফাঁকা থাকলে সবার গড় (Average) স্যালারি বসাবো
df['department']= df['department'].fillna('Unknown')
average_salary=df['salary'].mean()
df['salary']=df['salary'].fillna(average_salary)
# average_salary = df['salary'].mean() # গড় স্যালারি বের করা
# df['salary'] = df['salary'].fillna(average_salary)

print("--- ৩. নাল ভ্যালু ফিক্স করার পর ডেটাসেট ---")
# print(df)
# print("\n" + "="*40 + "\n")

# ডুপ্লিকেট রো খুঁজে বের করা
print("--- ৪. ডুপ্লিকেট রোগুলো (True মানে ডুপ্লিকেট) ---")
print(df.duplicated(subset=['employee_id']))           
print("\n")
print(df)

# ডুপ্লিকেট রিমুভ করা (keep='first' মানে প্রথমটি রেখে পরের ডুপ্লিকেটগুলো মুছে দেবে)
df_clean = df.drop_duplicates(subset=['employee_id'], keep='first').copy()
print("--- ৫. চূড়ান্ত পরিষ্কার ডেটাসেট (Cleaned Data) ---")
print(df_clean)
