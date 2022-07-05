#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:08:16 2022

@author: zli
"""
import pandas as pd

table1 = pd.read_csv('table1.csv')

table2 = pd.read_csv('table2.csv')

# https://pandas.pydata.org/docs/user_guide/merging.html
# pd.merge(
#     left,
#     right,
#     how="inner",
#     on=None,
#     left_on=None,
#     right_on=None,
#     left_index=False,
#     right_index=False,
#     sort=True,
#     suffixes=("_x", "_y"),
#     copy=True,
#     indicator=False,
#     validate=None,
# )

# Q1. 求每个 data center，request fail的比例

table_master = pd.merge(table1, table2, on='userid')

table_master['fail'] = table_master.apply(lambda x : 1 if x['success'] == 0 else 0, axis=1)

group1 = table_master[table_master['success'] == 0].groupby('data_center').count()['success']

group2 = table_master.groupby('data_center').count()['success']

print('--Q1--v1--')
print(group1 / group2)

print('--Q1--v2--')
gk = table_master.groupby('data_center')
res1 = gk['fail'].sum() / gk['fail'].size()
print(res1)


# Q2. 求每个国家，request fail的

group1 = table_master[table_master['success'] == 0].groupby('country').count()['success']

group2 = table_master.groupby('country').count()['success']

print('--Q2--v1--')
print(group1 / group2)

print('--Q2--v2--')
gk = table_master.groupby('country')
res1 = gk['fail'].sum() / gk['fail'].size()
print(res1)

# Q3. 求每个国家，有多少个 user 发出的好友请求从来没有 fail 过
print('--Q3--')
user_ids = table_master[table_master['success'] == 0]['userid'].unique()
table = table_master[~table_master['userid'].isin(user_ids)].groupby('country')['userid'].nunique()
print(table)