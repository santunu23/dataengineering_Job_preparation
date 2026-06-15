import psycopg2

try:
    connection=psycopg2.connect(
        user="postgres", 
        password="Santunu2#",
        host="127.0.0.1",
        port="5432", 
        database="postgres"

    )

    cursor=connection.cursor()

    print("connect with the database")
    cursor.execute("SELECT VERSION()")

    db_version=cursor.fetchone()
    print(f"Your postgree version is: {db_version}\n")

except(Exception,psycopg2.Error) as error:
    print("ডাটাবেসে কানেক্ট হতে সমস্যা হয়েছে:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("ডাটাবেস কানেকশন নিরাপদে বন্ধ করা হয়েছে।")