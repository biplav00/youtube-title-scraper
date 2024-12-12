import pandas as pd
import os

def save_to_csv(data, output_path):
    if not data:
        print("No data to save.")
        return
    

    file_exists = os.path.isfile(output_path)

    df = pd.DataFrame([data])
    df.to_csv(output_path, mode='a', header=not file_exists, index=False)