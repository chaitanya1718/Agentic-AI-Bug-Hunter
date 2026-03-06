import pandas as pd

def write_csv(results):

    df = pd.DataFrame(results)

    df.to_csv("output.csv", index=False)