import pandas as pd

df = pd.read_csv(r'/tmp/blocks.csv')
print(df)
mean1 = df['GAS_USED'].mean()
sum1 = df['GAS_USED'].sum()
max1 = df['GAS_USED'].max()
min1 = df['GAS_USED'].min()
median1 = df['GAS_USED'].median()
std1 = df['GAS_USED'].std()
var1 = df['GAS_USED'].var()

print('Mean gas used: ' + str(mean1))
print('Sum of gas used: ' + str(sum1))
print('Max gas used: ' + str(max1))
print('Min gas used: ' + str(min1))
print('Median gas used: ' + str(median1))
print('Standard Deviation of gas used: ' + str(std1))
print('Variance of gas used: ' + str(var1))
