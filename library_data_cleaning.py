import argparse
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

def file_loader(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    return pd.read_csv(path)

def dropna(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(how='all')
    return df

def duplicates_check(df: pd.DataFrame, subset: list = None, keep: str = "first") -> pd.DataFrame:
    if not isinstance(df, (pd.DataFrame, pd.Series)):
        df = pd.DataFrame()

    initial_rows = df.shape[0]

    df = df.drop_duplicates(subset=subset, keep=keep)

    deleted = initial_rows - df.shape[0]
    print(f"Removed {deleted} duplicate rows.")  # Optional: helpful log message
    
    return df

def date_cleaner(df: pd.DataFrame, columns: list, date_format: str = "%d/%m/%Y", replacements: dict = None) -> pd.DataFrame:
    for col in columns:
        if col not in df.columns:
            continue

        df[col] = df[col].astype(str).str.replace('"','')

        if replacements:
            for old_str, new_str in replacements.items():
                df[col] = df[col].str.replace(old_str,new_str)
    return df

def convert_to_int(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
    return df

def calculate_dates_difference(df: pd.DataFrame, start_date: str, end_date: str, new_col: str, date_format: str = "%d/%m/%Y") -> pd.DataFrame:
    if start_date in df.columns and end_date in df.columns:
        df[start_date] = pd.to_datetime(df[start_date], format=date_format, errors="coerce")
        df[end_date] = pd.to_datetime(df[end_date], format=date_format, errors="coerce")
        df[new_col] = (df[end_date] - df[start_date]).dt.days.astype("Int64")
    return df

def export_to_sql(df: pd.DataFrame, db_name: str, table_name: str ):

    engine = create_engine(f"sqlite:///{db_name}")    
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)


def library_cleaning_data(input_path: str, output_path: str=None) -> str:
    input_file = Path(input_path)
    output_path = input_file.parent / f"{input_file.stem}_Cleaned.csv"
    df = file_loader(input_path)
    df = dropna(df)
    df = duplicates_check(df)
    date_columns = ["Book checkout","Book Returned"]
    date_fixes = {"32/05/2023":"31/05/2023"}
    df = date_cleaner( df, columns=date_columns,date_format="%d/%m/%Y", replacements=date_fixes)
    df = calculate_dates_difference(df, start_date="Book checkout", end_date="Book Returned", new_col="days_diff", date_format="%d/%m/%Y")

    df = convert_to_int(df, columns=["Customer ID","Id"])
    df.to_csv(output_path, index=False)
    export_to_sql(df, db_name="library_clean_data_2.db", table_name="cleaned_books")

    engine = create_engine("sqlite:///library_clean_data.db")

    query = "SELECT * FROM cleaned_books"
    df_result = pd.read_sql(query, con=engine)
    print(df_result)



if __name__ == "__main__":
    library_cleaning_data("Data/03_Library Systembook.csv")



