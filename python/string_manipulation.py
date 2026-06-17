import pandas as pd

# একটি নোংরা টেক্সট ডেটাসেট (যেখানে স্পেস, ক্যাপিটালাইজেশন এবং ভুল ডেট ফরম্যাট আছে)
raw_data = {
    'emp_id': [101, 102, 103],
    'emp_name': ['  Sajib Chowdhury ', 'tanvir ahmed', 'KAMAL HOSSAIN  '],
    'email': ['SAJIB@bita.org', 'Tanvir@Bita.org', 'kamal@BITA.org'],
    'joining_date': ['2026/01/15', '15-02-2026', '2026.03.01'] # একেকটা একেক ফরম্যাটে
}

df = pd.DataFrame(raw_data)
print("--- ১. মূল আনফরমেটেড ডেটাসেট ---")
print(df)
print("\n" + "="*50 + "\n")



# লজিক ১: নামের আগে-পরের অতিরিক্ত স্পেস কাটা (.strip) 
# এবং নামগুলোর প্রথম অক্ষর বড় হাতের করা (.title)
df['emp_name'] = df['emp_name'].str.strip().str.title()


# ----------------------------------------------------------------------------------

# লজিক ২: ইমেইলের সব লেটার ছোট হাতের করা (.lower) যেন 
# ডাটাবেসে খোঁজার সময় সুবিধা হয়
df['email']=df['email'].str.lower()


# ----------------------------------------------------------------------------------

# লজিক ৩: বিভিন্ন ফরম্যাটের ডেটকে স্ট্যান্ডার্ড 'YYYY-MM-DD' ফরম্যাটে রূপান্তর করা 
# (ইন্টারভিউ স্পেশাল!)
# errors='coerce' দিলে কোনো ডেট ভুল থাকলে ক্র্যাশ না করে 
# সেখানে NaT (Not a Time/Null) বসাবে

df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce').dt.date

df['joining_date']=pd.to_datetime(df['joining_date'],errors-'coerce').dt.date

print("--- ২. চূড়ান্ত ফরম্যাটেড ও ক্লিনড ডেটাসেট ---")
print(df)