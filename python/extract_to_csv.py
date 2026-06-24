import psycopg2
import pandas as pd

connection = None

try:
    connection = psycopg2.connect(
        user ="postgres", 
        password ="Santunu2#",
        host ="127.0.0.1",
        port = "5432", 
        database ="dataEng_db" 
    )
    query="SELECT name,department,city,salary FROM practice_db.employee"
    print("Extracting Data from Database.....")
    df=pd.read_sql_query(query,connection)
    csv_file_name="employee_report.csv"
    df.to_csv(csv_file_name, index=False, encoding='utf-8')
    print(f"Successfully Extract DAta.The file is created in your folder '{csv_file_name}' ")
    print("\n Five rows of downloaded file")
    print(df.head())
    
except(Exception, psycopg2.Error) as error:
    print("Error in the pipeline",error)

finally: 
    if connection:
        connection.close()
        print("\n Safly closed Database connection.")