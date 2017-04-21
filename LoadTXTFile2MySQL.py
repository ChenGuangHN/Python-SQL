#-*- coding: utf8 -*-
'''
# Filename: Load TXT File to MySQL
# Author : Chen Guang
# Date: 2017/4/19
# Comment: This is a test version.
'''


import pandas as pd
from sqlalchemy import create_engine

data = pd.read_table('D:/pycharmFile/amazonAdDataAnalysis/data1/SX/EU/ads/DE/ads report/2017.04/ADs_SXDE_2017-4-11.txt',
                     sep='\t', encoding='utf-8')

data.columns = ['Campaign_Name',
                'Ad Group_Name',
                'Advertised_SKU',
                'Keyword',
                'Match_Type',
                'Start_Date',
                'End_Date',
                'Clicks',
                'Impressions',
                'CTR',
                'Total_Spend',
                'Average_CPC',
                'Currency',
                '1-day_Orders_Placed_(#)',
                '1-day_Ordered_Product_Sales',
                '1-day_Conversion_Rate',
                '1-day_Same_SKU_Units_Ordered',
                '1-day_Other_SKU_Units_Ordered',
                '1-day_Same_SKU_Units_Ordered_Product_Sales',
                '1-day_Other_SKU_Units_Ordered_Product_Sales',
                '1-week_Orders_Placed_(#)',
                '1-week_Ordered_Product_Sales',
                '1-week_Conversion_Rate',
                '1-week_Same_SKU_Units_Ordered',
                '1-week_Other_SKU_Units_Ordered',
                '1-week_Same_SKU_Units_Ordered_Product_Sales',
                '1-week_Other_SKU_Units_Ordered_Product_Sales',
                '1-month_Orders_Placed_(#)',
                '1-month_Ordered_Product_Sales',
                '1-month_Conversion_Rate',
                '1-month_Same_SKU_Units_Ordered',
                '1-month_Other_SKU_Units_Ordered',
                '1-month_Same_SKU_Units_Ordered_Product_Sales',
                '1-month_Other_SKU_Units_Ordered_Product_Sales']

data['Start_Date'] = pd.to_datetime(data['Start_Date'], dayfirst=True)
data['End_Date'] = pd.to_datetime(data['End_Date'], dayfirst=True)

data['Total_Spend'] = data['Total_Spend'].apply(str)
data['1-day_Ordered_Product_Sales'] = data['1-day_Ordered_Product_Sales'].apply(str)

def rep(string):
    return string.replace(',', '.')

data['Total_Spend'] = data['Total_Spend'].apply(rep).apply(float)
data['1-day_Ordered_Product_Sales'] = data['1-day_Ordered_Product_Sales'].apply(rep).apply(float)

print data.head()

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/amz_commercial_db?charset=utf8')
data.to_sql('ads_sxde', engine, schema='amz_commercial_db', if_exists='replace')

