import pandas as pd

df = pd.read_csv ("animals.csv")

# df.head()
# print (df)

print("Welcome to Julia's Animal Analysis Program")
# part 1
sum_of_weight = df.sum()
print(sum_of_weight)

count_of_animals = df.shape[0]
print ("Analyzing" , count_of_animals , " animals")


# part 2
sum_of_weight2 = df['bodywt'].sum()
print ("Total Body Weights:", sum_of_weight2)
# print("The program ran part 2")


# part 3
sum_of_weight3 = df['brainwt'].sum()
print ("Total BRAIN Weights: ", sum_of_weight3)
# print("The program ran part 3")
