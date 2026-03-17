import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [29, 33, 55],
    "city": ["NYC", "LA", "Chicago"]
}


df = pd.DataFrame(data)

print(df)