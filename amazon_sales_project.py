# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:33:34 2025

@author: Rehma

Case Questions:
    
    - How many sales have been made with amounts greater than 1000?
    - How many sales have they made that belong to the category 'Tops' and 
    have a quantity of 3?
    - The total sales by category
    - Average amount by category and status
    - Total Sales by Fulfilment and Shipment type



"""

import pandas as pd

sales_data = pd.read_excel("C:/Users/Rehma/OneDrive/Desktop/Python Projects/Amazon+Sales+Project/Amazon Sales Project/sales_data.xlsx")

#data summary

# =============================================================================
# exploring the data
# =============================================================================

sales_data.info()
sales_data.describe()


#looking at coulmns

print(sales_data.columns)

#having a look at data rows

print(sales_data.head)

#check data types

print(sales_data.dtypes)

# =============================================================================
# cleaning the data
# =============================================================================

#checking missing data

sales_data.isnull()
sales_data.isnull().sum()

#removing all null values

sales_data_dropped = sales_data.dropna() #not a good drop rule

#dropping rows with missing amounts

sales_data_cleaned = sales_data.dropna(subset = ['Amount'])


# 1. How many sales have been made with amounts greater than 1000?
sales_above_1000 = sales_data[sales_data['Amount'] > 1000].shape[0]

# 2. How many sales belong to the category 'Tops' and have a quantity of 3?
tops_qty_3 = sales_data[(sales_data['Category'] == 'Top') & (sales_data['Qty'] == 3)].shape[0]

# 3. Total sales by category
total_sales_by_category = sales_data.groupby('Category')['Amount'].sum()

# 4. Average amount by category and status
avg_amount_by_category_status = sales_data.groupby(['Category', 'Status'], as_index=False)['Amount'].mean()

# 5. Total Sales by Fulfilment and Shipment type
total_sales_by_fulfilment_shipment = sales_data.groupby(['Fulfilment', 'ship-service-level'])['Amount'].sum()

# 6. Average amount by Category and Fulfilment

fulfilment_averages = sales_data.groupby(['Category', 'Fulfilment'], as_index = False)['Amount'].mean()
fulfilment_averages = fulfilment_averages.sort_values('Amount', ascending =False)

total_sales_shipandfulfil = sales_data.groupby(['Courier Status', 'Fulfilment'], as_index = False)['Amount'].sum()

# Display results
print("Sales above 1000:", sales_above_1000)
print("Sales of 'Tops' with quantity 3:", tops_qty_3)
print("Total Sales by Category:\n", total_sales_by_category)
print("Average Amount by Category and Status:\n", avg_amount_by_category_status)
print("Total Sales by Fulfilment and Shipment Type:\n", total_sales_by_fulfilment_shipment)


#renaming data frame

total_sales_shipandfulfil.rename(columns={'Courier Status': 'Shipment'}, inplace = True)


# =============================================================================
# Exporting Data 
# =============================================================================

avg_amount_by_category_status.to_excel('Average_Sales_by_category_and_status.xlsx', index = False)
total_sales_shipandfulfil.to_excel('Total_sales_by_ship_and_fulfil.xlsx', index = False)







