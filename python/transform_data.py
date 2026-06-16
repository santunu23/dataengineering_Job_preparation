import pandas as pd
from sqlalchemy import create_engine

try:
    print("1. Extracting data from database....")
    engine=create_engine('postgresql://postgres:Santunu2#@127.0.0.1:5432/postgres') 
    query="SELECT name,department,city,salary FROM practice_db.employee;"


    df=pd.read_sql_query(query,con=engine)
    print("2.Starting data transformation....")
    #transformation step 1: Only filter which City is Chittagong
    df_chittagong=df[df['city']=='Chittagong'].copy()
    #transformation step =2: change the type and add 10% bonus
    # If the salary is in the text change it into integer and add 10% Bonus with it

    df_chittagong['salary'] = df_chittagong['salary'].astype(int)
    df_chittagong['bonus_salary']=df_chittagong['salary']*1.10
    #3. Save transformed data into new CSV file
    final_csv="chittagong_bonus_report.csv"
    df_chittagong.to_csv(final_csv,index=False,encoding='utf-8')

    print(f"\n✅ The pipeline run successfully and created the file '{final_csv}'")
    print("\nChittagong First 3 rows with team bonus: ")
    print(df_chittagong.head(3))




except Exception as error:
    print("\n Problem in the pipeline",error)