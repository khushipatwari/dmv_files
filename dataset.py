import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Fix GUI issue
import matplotlib.pyplot as plt
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load dataset
df = pd.read_csv(r"C:\Users\lab.AUKOL\Downloads\Companies_dataset.csv")

# ------------------ Data Cleaning ------------------

df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')

def clean_reviews(x):
    x = str(x)
    x = re.sub(r'[^0-9.]', '', x)
    return float(x) if x else None

df['review_count'] = df['review_count'].apply(clean_reviews)

def extract_employee_count(x):
    if pd.isna(x):
        return None
    x = str(x).lower().replace(',', '')
    
    if 'k' in x:
        return float(re.findall(r'\d+', x)[0]) * 1000
    
    nums = re.findall(r'\d+', x)
    return float(nums[0]) if nums else None

df['employee_count'] = df['employees'].apply(extract_employee_count)

# Drop missing values
df = df.dropna(subset=['ratings', 'review_count', 'employee_count', 'hq'])

# ------------------ Top 10 Companies ------------------

top_10 = df.sort_values(by='review_count', ascending=False).head(10)
print("\n[Top 10 Companies and Their Headquarters:]\n")
print(top_10[['name', 'hq']].to_string(index=False))

# ------------------ 1. Funnel Chart (Review-wise) ------------------

plt.figure()
plt.barh(top_10['name'], top_10['review_count'])
plt.gca().invert_yaxis()
plt.title("Funnel Chart (Top 10 Company Reviews)")
plt.xlabel("Review Count")
plt.ylabel("Company")
plt.tight_layout()
plt.savefig("funnel_top10.png")
plt.close()

# ------------------ 2. Bar Chart (HQ-wise count) ------------------

hq_counts = top_10['hq'].value_counts()

plt.figure()
plt.bar(hq_counts.index, hq_counts.values)
plt.xticks(rotation=45, ha='right')
plt.title("Bar Chart (Headquarters Distribution)")
plt.xlabel("Headquarters")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig("bar_hq.png")
plt.close()

# ------------------ 3. Line Chart (Rating-wise) ------------------

plt.figure()
plt.plot(top_10['name'], top_10['ratings'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title("Line Chart (Top 10 Company Ratings)")
plt.xlabel("Company")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("line_ratings.png")
plt.close()

# ------------------ 4. Pie Chart (Employee-wise) ------------------

plt.figure()
plt.pie(top_10['employee_count'], labels=top_10['name'], autopct='%1.1f%%')
plt.title("Pie Chart (Employee Distribution - Top 10)")
plt.tight_layout()
plt.savefig("pie_employees.png")
plt.close()

print("\n📍 Top 10 Companies and Their Headquarters:\n")

for i, row in enumerate(top_10[['name', 'hq']].itertuples(index=False), start=1):
    print(f"{i}. {row.name}  -->  {row.hq}")