
import pandas as pd
# import seaborn as sns
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split

penguin_df = pd.read_csv("penguins.csv")
penguin_df.dropna(inplace=True)
output = penguin_df["species"]
features = penguin_df[
    [
        "island",
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
        "sex",
    ]
]
features = pd.get_dummies(features)
print('Here are our output variables')
print(output.head(10))
print('Here are our feature variables')
print(features.head(10))
