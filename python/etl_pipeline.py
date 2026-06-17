import pandas as pd
from sqlalchemy import create_engine


try:
    # ১। ডাটাবেস ইঞ্জিন তৈরি(এখানে তোমার সঠিক পাসওয়ার্ড ও ডাটাবেস নাম দেবে)
    engine=create_engine('postgresql://postgres:Santunu2#@127.0.0.1:5432/dataEng_db')
    # ─── STEP 1: EXTRACT(ডেটা তুলে আনা) ───
    print("১. [EXTRACT] ডাটাবেস থেকে মূল এমপ্লয়ী ডেটা তোলা হচ্ছে... ⏳")
    query = "SELECT name, department, city, salary FROM practice_db.employee;"
    df = pd.read_sql_query(query, con=engine)

    # ─── STEP 2: TRANSFORM(ডেটা সাইজ করা) ───
    print("২. [TRANSFORM] চট্টগ্রামের ডেটা ফিল্টার ও ১০% বোনাস হিসাব করা হচ্ছে... ⚙️")
    df_chittagong=df[df['city']=='Chittagong'].copy()
    df_chittagong['salary'] = df_chittagong['salary'].astype(int)
    df_chittagong['bonus_salary']=df_chittagong['salary']*1.10

    # ─── STEP 3: LOAD (ডাটাবেসে ফেরত পাঠানো) ───
    print("৩. [LOAD] ট্রান্সফর্মড ডেটা আবার ডাটাবেসে নতুন টেবিল আকারে পাঠানো হচ্ছে... 🚀")

    # name= 'chittagong_bonus_employees' -> নতুন টেবিলের নাম
    # schema =  'practice_db' -> আমাদের নির্দ্দিষ্ট স্কিমা
    # if_exists= 'replace' -> টেবিল আগে থাকলে তা মুছে নতুন করে ডেটা রাইট করবে

    df_chittagong.to_sql(
        name='chittagong_bonus_employees',
        con= engine,
        schema = 'practice_db',
        if_exists= 'replace',
        index=False 
    )  

    print("\n✅ [SUCCESS] পুরো ETL পাইপলাইন সফলভাবে সম্পন্ন হয়েছে!")
    print("এখন pgAdmin-এ গিয়ে 'chittagong_bonus_employees' টেবিলটি চেক করো।")



except Exception as error:
    print("\n পাইপলাইনে সমস্যা হয়েছেঃ",error)