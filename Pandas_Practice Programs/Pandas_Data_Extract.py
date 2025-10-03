import pandas as pd

# Sample son data
data = {
    "Father_Name": ["Ravi", "Kumar", "Suresh", "Anil"],
    "Son_Name": ["Arjun", "Rahul", "Varun", "Rohan"],
    "Son_Age": [10, 12, 9, 11],
    "School": ["ABC School", "XYZ Public", "Green Valley", "ABC School"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Show last rows of the DataFrame
#print("Tail of DataFrame:")
#print(df.tail(2))

#print(df.describe())

#print(df.shape)
# If you want to show full DataFrame too
# print("\nFull DataFrame:")
# print(df)
#print(df[0:6:2])
#print(df[["Father_Name","Son_Age","School"]][0:5:2])#Two dimension
#print(df.iloc[0:2,[1,2]])

#print(df.sort_values("Father_Name",ascending =False))

df["Total"]=0

df["Percentage"] =0

print(df)

df.loc[df["Percentage"]<40,["Grade"]] = "Fail"



