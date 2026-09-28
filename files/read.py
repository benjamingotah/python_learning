import pandas as pd
import matplotlib.pyplot as plt

data_src = "Lending-company.csv"
df = pd.read_csv(data_src, index_col="LoanID")
print(df)

total_amount = df["AmtPaid60"].sum()
print("the total amount is: ", total_amount)

plt.hist(df["AmtPaid60"])
plt.show()