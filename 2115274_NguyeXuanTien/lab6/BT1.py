import pandas as pd
df=pd.read_csv("D:\A_ Tài liệu môn học\lap trinh python\Automobile_data.csv")
# print(df)
# print(df.head(6))
# print(df.tail(7))

# df=df[['company','price']][df.price==df['price'].max()]
# print(df)

# car_Manufactures=df.groupby('company')
# toyotadf=car_Manufactures.get_group("toyota")
# print(toyotadf)

# print(df['company'].value_counts())       

# car_Manufactures=df.groupby('company')
# pricedf=car_Manufactures[['company', 'price']].max('price')
# print(pricedf)

car_Manufactures=df.groupby('company')
pricedf=car_Manufactures[['company', 'price']].mean('price')
print(pricedf)