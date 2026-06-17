import pandas as pd

# টেবিল ১: কর্মচারীদের বেসিক তথ্য
df_emp = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'name': ['Sajib', 'Tanvir', 'Kamal', 'Rahim'],
    'city': ['Chittagong', 'Dhaka', 'Chittagong', 'Sylhet']
})

# টেবিল ২: কর্মচারীদের ডিপার্টমেন্ট ও স্যালারি (এখানে ১০৪ নম্বর আইডির ডাটা নেই, বদলে ১০৫ আছে)
df_salary = pd.DataFrame({
    'emp_id': [101, 102, 103, 105],
    'department': ['IT', 'HR', 'IT', 'Marketing'],
    'salary': [60000, 55000, 50000, 45000]
})

print("--- টেবিল ১ (Employees) ---")
print(df_emp)
print("\n--- টেবিল ২ (Salaries) ---")
print(df_salary)
print("\n" + "="*40 + "\n")

df_inner= pd.merge(df_emp,df_salary,on='emp_id',how='inner')

print("--- ৩. INNER JOIN এর আউটপুট (Common Rows) ---")
print(df_inner)
print("\n" + "="*40 + "\n")

df_left= pd.merge(df_emp,df_salary,on='emp_id',how='left')
print("--- ৪. LEFT JOIN এর আউটপুট (All from Left Table) ---")
print(df_left)

df_left=pd.merge(df_emp,df_salary,on='emp_id',how='left')
print(df_left)