# ================================================================
#  UPI Transaction Analysis
#  Digital India Internship Project
#
#  Author  : Pratibha Singh
#  College : Netaji Subhas University of Technology
#
#  What this script does:
#  1. Loads the UPI data from the data/ folder
#  2. Cleans it so both years match
#  3. Prints key numbers in the terminal
#  4. Creates 6 charts and saves them to outputs/
#  5. Saves a summary CSV to outputs/
# ================================================================

# Step 1 — Import the tools we need
# pandas  : reads and works with spreadsheet-like data
# matplotlib : draws charts
import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 2 — Create the outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

print("Loading data...")

# Step 3 — Load both CSV files
df21 = pd.read_csv("data/upi_2021.csv")
df22 = pd.read_csv("data/upi_2022.csv")

# Step 4 — Clean the 2022 file
# The 2022 file has some messy formatting we need to fix:
# (a) Column names have extra spaces — strip them
df22.columns = [col.strip() for col in df22.columns]
# (b) Make column names exactly match 2021
df22.columns = df21.columns
# (c) Numbers are written with commas like "1,234.56" — remove commas so Python can read them
for col in ['Volume (Mn) By Costumers', 'Value (Cr) by Costumers',
            'Volume (Mn)', 'Value (Cr)']:
    df22[col] = df22[col].astype(str).str.replace(',', '').astype(float)

# Step 5 — Combine both years into one big table
df = pd.concat([df21, df22], ignore_index=True)

print(f"  Total rows loaded : {len(df)}")
print(f"  Years in data     : {sorted(df['Year'].unique())}")
print(f"  Unique UPI apps   : {df['UPI Banks'].nunique()}")

# ── Key Numbers ───────────────────────────────────────────────

total_vol_21 = df21['Volume (Mn)'].sum()   # total volume in 2021
total_vol_22 = df22['Volume (Mn)'].sum()   # total volume in 2022 (Jan–Jul only)
total_val_21 = df21['Value (Cr)'].sum()
total_val_22 = df22['Value (Cr)'].sum()

avg_monthly_21 = total_vol_21 / 12         # 2021 had 12 months
avg_monthly_22 = total_vol_22 / 7          # 2022 data has 7 months (Jan–Jul)

# Growth % = how much bigger is 2022 average vs 2021 average
growth = ((avg_monthly_22 - avg_monthly_21) / avg_monthly_21) * 100

print("\n--- Key Metrics ---")
print(f"2021 Total Volume          : {total_vol_21:,.0f} Mn")
print(f"2021 Total Value           : Rs {total_val_21:,.0f} Cr")
print(f"2022 Total Volume (Jan-Jul): {total_vol_22:,.0f} Mn")
print(f"2022 Total Value  (Jan-Jul): Rs {total_val_22:,.0f} Cr")
print(f"Avg Monthly Volume 2021    : {avg_monthly_21:,.0f} Mn")
print(f"Avg Monthly Volume 2022    : {avg_monthly_22:,.0f} Mn")
print(f"Year-over-Year Growth      : {growth:.1f}%")

# ── Top 10 Apps ───────────────────────────────────────────────

# Group all rows by app name, add up their volume, pick top 10
top10 = (df.groupby('UPI Banks')['Volume (Mn)']
           .sum()
           .sort_values(ascending=False)
           .head(10)
           .reset_index())
top10.columns = ['UPI App', 'Total Volume (Mn)']

print("\n--- Top 10 UPI Apps ---")
print(top10.to_string(index=False))

# ── Monthly Totals ────────────────────────────────────────────

# Add up all apps for each month
monthly_21 = df21.groupby('Month')[['Volume (Mn)', 'Value (Cr)']].sum().round(2)
monthly_22 = df22.groupby('Month')[['Volume (Mn)', 'Value (Cr)']].sum().round(2)

# ── Charts ────────────────────────────────────────────────────

# Short month names for x-axis labels
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# Remove the top and right border from all charts (looks cleaner)
plt.rcParams['axes.spines.top']   = False
plt.rcParams['axes.spines.right'] = False

# ----- Chart 1: Monthly Volume 2021 (bar chart) -----
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(monthly_21.index,
       monthly_21['Volume (Mn)'],
       color='#3266ad', width=0.6)
ax.set_xticks(monthly_21.index)
ax.set_xticklabels([months[m-1] for m in monthly_21.index])
ax.set_title('Monthly UPI Transaction Volume in 2021', fontsize=14, pad=12)
ax.set_ylabel('Volume (Millions)')
ax.set_xlabel('Month')
plt.tight_layout()
plt.savefig('outputs/chart1_volume_2021.png', dpi=150)
plt.close()
print("\nSaved chart1_volume_2021.png")

# ----- Chart 2: Monthly Volume 2022 (bar chart) -----
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(monthly_22.index,
       monthly_22['Volume (Mn)'],
       color='#1d9e75', width=0.5)
ax.set_xticks(monthly_22.index)
ax.set_xticklabels([months[m-1] for m in monthly_22.index])
ax.set_title('Monthly UPI Transaction Volume in 2022 (Jan to Jul)', fontsize=14, pad=12)
ax.set_ylabel('Volume (Millions)')
ax.set_xlabel('Month')
plt.tight_layout()
plt.savefig('outputs/chart2_volume_2022.png', dpi=150)
plt.close()
print("Saved chart2_volume_2022.png")

# ----- Chart 3: Side-by-side comparison Jan–Jul 2021 vs 2022 -----
shared = [1, 2, 3, 4, 5, 6, 7]
vol21  = [monthly_21.loc[m, 'Volume (Mn)'] for m in shared]
vol22  = [monthly_22.loc[m, 'Volume (Mn)'] for m in shared]
labels = [months[m-1] for m in shared]
x = range(len(labels))
w = 0.35

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar([i - w/2 for i in x], vol21, w, label='2021', color='#3266ad')
ax.bar([i + w/2 for i in x], vol22, w, label='2022', color='#1d9e75')
ax.set_xticks(list(x))
ax.set_xticklabels(labels)
ax.set_title('2021 vs 2022 — Monthly Volume Comparison (Jan to Jul)', fontsize=13, pad=12)
ax.set_ylabel('Volume (Millions)')
ax.legend()
plt.tight_layout()
plt.savefig('outputs/chart3_comparison.png', dpi=150)
plt.close()
print("Saved chart3_comparison.png")

# ----- Chart 4: Top 10 UPI Apps (horizontal bar) -----
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#3266ad','#1d9e75','#d85a30','#73726c','#ba7517',
          '#993556','#534AB7','#0F6E56','#639922','#E24B4A']
# Reverse so the biggest bar is at the top
ax.barh(top10['UPI App'][::-1],
        top10['Total Volume (Mn)'][::-1],
        color=colors[::-1], height=0.6)
ax.set_title('Top 10 UPI Apps by Total Transaction Volume', fontsize=13, pad=12)
ax.set_xlabel('Total Volume (Millions)')
# Add the number at the end of each bar
for i, val in enumerate(top10['Total Volume (Mn)'][::-1]):
    ax.text(val + 300, i, f'{val:,.0f}', va='center', fontsize=10)
plt.tight_layout()
plt.savefig('outputs/chart4_top10_apps.png', dpi=150)
plt.close()
print("Saved chart4_top10_apps.png")

# ----- Chart 5: Market share pie chart (2021) -----
vol_phonpe = df21[df21['UPI Banks'] == 'PhonePe']['Volume (Mn)'].sum()
vol_gpay   = df21[df21['UPI Banks'] == 'Google Pay']['Volume (Mn)'].sum()
vol_paytm  = df21[df21['UPI Banks'] == 'Paytm Payments Bank App']['Volume (Mn)'].sum()
vol_others = total_vol_21 - vol_phonpe - vol_gpay - vol_paytm

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie([vol_phonpe, vol_gpay, vol_paytm, vol_others],
       labels=['PhonePe', 'Google Pay', 'Paytm', 'Others'],
       autopct='%1.1f%%',
       startangle=140,
       colors=['#3266ad', '#1d9e75', '#d85a30', '#D3D1C7'],
       wedgeprops={'edgecolor': 'white', 'linewidth': 2})
ax.set_title('UPI Market Share by Volume — 2021', fontsize=14, pad=16)
plt.tight_layout()
plt.savefig('outputs/chart5_market_share.png', dpi=150)
plt.close()
print("Saved chart5_market_share.png")

# ----- Chart 6: Monthly value trend line chart -----
fig, ax = plt.subplots(figsize=(11, 5))
# Divide by 1,00,000 to convert Crore to Lakh Crore (easier to read)
ax.plot(monthly_21.index,
        monthly_21['Value (Cr)'] / 100000,
        marker='o', color='#3266ad', label='2021', linewidth=2)
ax.plot(monthly_22.index,
        monthly_22['Value (Cr)'] / 100000,
        marker='s', color='#1d9e75', label='2022', linewidth=2, linestyle='--')
ax.set_xticks(list(range(1, 13)))
ax.set_xticklabels(months)
ax.set_title('Monthly UPI Transaction Value (Rs Lakh Crore)', fontsize=14, pad=12)
ax.set_ylabel('Value (Rs Lakh Cr)')
ax.legend()
plt.tight_layout()
plt.savefig('outputs/chart6_value_trend.png', dpi=150)
plt.close()
print("Saved chart6_value_trend.png")

# ── Save Summary CSV ──────────────────────────────────────────

summary = pd.DataFrame({
    'Metric': [
        'Total Volume 2021 (Mn)',
        'Total Value 2021 (Cr)',
        'Total Volume 2022 Jan-Jul (Mn)',
        'Total Value 2022 Jan-Jul (Cr)',
        'Avg Monthly Volume 2021 (Mn)',
        'Avg Monthly Volume 2022 (Mn)',
        'YoY Growth in Avg Monthly Volume',
        'Number of Unique UPI Apps',
        'Top App by Volume',
    ],
    'Value': [
        f'{total_vol_21:,.2f}',
        f'{total_val_21:,.2f}',
        f'{total_vol_22:,.2f}',
        f'{total_val_22:,.2f}',
        f'{avg_monthly_21:,.2f}',
        f'{avg_monthly_22:,.2f}',
        f'{growth:.1f}%',
        str(df['UPI Banks'].nunique()),
        'PhonePe',
    ]
})
summary.to_csv('outputs/summary.csv', index=False)
print("Saved outputs/summary.csv")

print("\nAll done! Open the outputs/ folder to see your charts.")
