import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": [2010, 2014, 2018, 2022],
    "Votes": [45, 55, 60, 70]
}

df = pd.DataFrame(data)

plt.plot(df["Year"], df["Votes"], marker="o")
plt.title("Election Voting Trend")
plt.xlabel("Year")
plt.ylabel("Votes Percentage")

plt.show()
