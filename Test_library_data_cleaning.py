import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from library_data_cleaning import (
    dropna,
    duplicates_check,
    convert_to_int,
    calculate_dates_difference,
)

def test_dropna():
    data = {
        "col a": [1.0, None, 3.0],
        "col b": [4.0, None, 6.0]
    }
    df = pd.DataFrame(data)
    
    result_df = dropna(df)
    
    expected_data = {
        "col a": [1.0, 3.0],
        "col b": [4.0, 6.0]
    }
    expected_df = pd.DataFrame(expected_data)
    assert_frame_equal(result_df.reset_index(drop=True), expected_df)

def test_duplicates_check():
    data = {
        "col a": [1, 2, 1],
        "col b": ["A", "B", "A"]
    }
    df = pd.DataFrame(data)
    
    result_df = duplicates_check(df)
    
    assert len(result_df) == 2

def test_convert_to_int():
    data = {
        "Customer ID": ["1.0", "2.0", "invalid"]
    }
    df = pd.DataFrame(data)
    
    result_df = convert_to_int(df, columns=["Customer ID"])
    
    assert result_df["Customer ID"].dtype == "Int64"
    assert result_df["Customer ID"].iloc[0] == 1
    assert result_df["Customer ID"].iloc[1] == 2
    assert pd.isna(result_df["Customer ID"].iloc[2])

def test_calculate_dates_difference():
    data = {
        "Book checkout": ["01/05/2023", "10/05/2023"],
        "Book Returned": ["05/05/2023", "12/05/2023"]
    }
    df = pd.DataFrame(data)
    
    result_df = calculate_dates_difference(
        df, 
        start_date="Book checkout", 
        end_date="Book Returned", 
        new_col="days_diff", 
        date_format="%d/%m/%Y"
    )
    
    assert result_df["days_diff"].iloc[0] == 4
    assert result_df["days_diff"].iloc[1] == 2