import pandas as pd
df=pd.read_csv("D:\A_ Tài liệu môn học\lap trinh python\sales_data.csv")


#Hiện thị toàn bộ nội dung
#print(df)

#3 Xuất dữ liệu của tháng có nhiều lợi nhuận nhất
# df=df[df.total_profit==df['total_profit'].max()]
# print(df)

#4 Xuất hàng dữ liệu của tháng bán nhiều mặt hàng nhất
# df=df[df.total_units==df['total_units'].max()]
# print(df)

# print('5. Xuất hàng dữ liệu của tháng bán nhiều kem đánh răng nhất')
# df=df[df.toothpaste==df['toothpaste'].max()]
# print(df)

print('6) Cho biết tổng lợi nhuận của cả năm')

sum=df['total_profit'].sum()
print(sum)
# print(df)

df=df[df.total_units==df['total_units'].max()]
print(df)