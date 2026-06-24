import pandas as pd

# একটি কোম্পানির মাসিক সেলস ডেটা (Long Format)
raw_sales = {
    'Year': [2025, 2025, 2025, 2026, 2026, 2026],
    'Month': ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
    'Sales': [15000, 18000, 20000, 22000, 25000, 28000]
}

df=pd.DataFrame(raw_sales)
print("--- ১. মূল লং ডেটাসেট (Long Format) ---")
print(df)
print("\n" + "="*50 + "\n")

df_pivot = df.pivot_table(index='Year', columns='Month', values='Sales').reset_index()

print("--- ২. পিভট করার পর চওড়া ডেটাসেট (Wide Format) ---")
print(df_pivot)
print("\n" + "="*50 + "\n")
#### ৩. `melt()` দিয়ে ডেটাকে আবার আগের লম্বালম্বি ফরম্যাটে ফেরত আনা
## ডাটা ইঞ্জিনিয়ার হিসেবে ডেটা ডাটাবেসে লোড করার জন্য চওড়া টেবিল খুব একটা সুবিধাজনক নয়। 
# তাই আমরা আবার এটিকে ভেঙে নিচে নিচে রো আকারে নিয়ে আসবো।
# ```python
# melt ব্যবহার করে চওড়া টেবিলকে আবার লম্বা টেবিলে রূপান্তর

df_melt = pd.melt(df_pivot, id_vars=['Year'], value_vars=['Jan', 'Feb', 'Mar'], 
                  var_name='Month', value_name='Sales')

print("--- ৩. মেল্ট করার পর আবার লম্বালম্বি ডেটাসেট (Back to Long Format) ---")
print(df_melt)