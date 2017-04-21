#-*- coding: utf8 -*-
# Filename: Query data from MySQL to python program
# Author : Chen Guang
# Date: 2017/4/19

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/amz_commercial_db')

start_date = '2017-03-03'
end_date = '2017-03-18'

expr1 = "SELECT * " \
       "FROM ads_sxde " \
       "WHERE Start_Date " \
       "BETWEEN STR_TO_DATE('" + start_date + "', '%%Y-%%m-%%d')" \
                                              "AND STR_TO_DATE('" + end_date + "', '%%Y-%%m-%%d');"

df = pd.read_sql_query(expr1, engine)

print df.info()
