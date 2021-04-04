# from django.test import TestCase
# import pandas as pd
# from policy.models import Customer, Policy_feature, Policy_tbl

# tmp_data=pd.read_csv('C:/Users/Aditya/Downloads/Telegram Desktop/customer.csv',sep='\\t')

# customers=[
#     Customer(
#         Customer_id=tmp_data.ix[row]['Customer_id'],
#         Customer_Gender=tmp_data.ix[row]['Customer_Gender'],
#         Customer_Income_group=tmp_data.ix[row]['Customer_Income group'],
#         Customer_Region=tmp_data.ix[row]['Customer_Region'],
#         Customer_Marital_status=tmp_data.ix[row]['Customer_Marital_status']
#     )

#     for row in temp_data['ID']
# ]
# print(customers)

def fun(n):
    if n==0 or n==1 or n==2:
        return 0
    if n==3:
        return 1
    else:
        return fun(n-1)+fun(n-2)+fun(n-3)

def voo(n):
    for x in range(1,n):
        print(fun(x))

voo(6)