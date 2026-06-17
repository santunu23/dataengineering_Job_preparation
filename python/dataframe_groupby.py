import pandas as pd

# আমাদের কোম্পানির সেলস ডেটাসেট
sales_data = {
    'store_id': [1, 2, 1, 2, 1, 2, 1],
    'product_category': ['Electronics', 'Furniture', 'Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics'],
    'revenue': [25000, 18000, 30000, 15000, 22000, 40000, 12000],
    'items_sold': [10, 5, 12, 4, 8, 15, 3]
}

df_sales=pd.DataFrame(sales_data)
print("--- ১. মূল সেলস ডেটাসেট ---")
print(df_sales)
print("\n" + "="*40 + "\n")


# লজিক ১: প্রতিটা ক্যাটাগরির (Product Category) মোট রেভিনিউ (Total Revenue) কত?
# df_category_revenue=df_sales.groupby('product_category')['revenue'].sum().reset_index
# print("--- ২. ক্যাটাগরিভিত্তিক মোট রেভিনিউ (Total Revenue) ---")
# print(df_category_revenue)
# print("\n" + "="*40 + "\n")

df_category_revenue=df_sales.groupby('product_category')['revenue'].sum().reset_index
print("--- ২. ক্যাটাগরিভিত্তিক মোট রেভিনিউ (Total Revenue) ---")
print(df_category_revenue)
print("\n" + "="*40 + "\n")

# ----------------------------------------------------------------------

# লজিক ২: একই সাথে মোট রেভিনিউ এবং গড় আইটেম সোল্ড হিসাব করা (Advanced .agg method)
# df_advanced_summary=df_sales.groupby('product_category').agg(
#     total_revenue=('revenue','sum'),
#     average_items_sold=('items_sold','mean')
# ).reset_index()

# print("--- ৩. প্রফেশনাল মাল্টি-এগ্রিগেশন সামারি রিপোর্ট ---")
# print(df_advanced_summary)

df_advanced_summary=df_sales.groupby('product_category').agg(
    total_revenue=('revenue','sum'),
    average_items_sold=('items_sold','mean')
).reset_index()

print("--- ৩. প্রফেশনাল মাল্টি-এগ্রিগেশন সামারি রিপোর্ট ---")
print(df_advanced_summary)
