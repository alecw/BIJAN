#!/usr/bin/env python3
# MIT License
# 
# Copyright 2022 Broad Institute
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Convert from CSV exported from google sheet "BIJAN Community Sign-Up (Responses)"
https://docs.google.com/spreadsheets/d/18vBBgLRoKzQmrP01PmnWeKiOyk_Wv4gCcUT_K1heU38/edit#gid=1774967150
populated from google form https://www.beyondbondboston.org/join

to CSV format suitable for upload into AirTable BIJAN Volunteer Database
"""
import argparse
import sys
import pandas
import google_sheet_cols

# Some enumerations are different in old and new forms
weekdays_value_conv = {
    'only during the summer / solamente durante el verano': "summertime only / solamente durante el verano"
}

english_value_conv = {
    'proficient / proficiente' : 'proficient'
}

portuguese_value_conv = {
    'fluente / fluent' : 'fluente',
    'un poco / some' : ' um pouco'
}

values_conversion_dict = {
    google_sheet_cols.WEEKDAYS_COL: weekdays_value_conv,
    google_sheet_cols.ENGLISH_COL: english_value_conv,
    google_sheet_cols.PORTUGUESE_COL: portuguese_value_conv
}

def convert_values(df):
    for row_index in range(len(df)):
        for col_index, dct in values_conversion_dict.items():
            if df.iloc[row_index, col_index] in dct:
                df.iloc[row_index, col_index] = dct[df.iloc[row_index, col_index]]
    return(df)

def main(args=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True, help="Input CSV downloaded from Google Sheet 'BIJAN Community Sign-Up (Responses)'.")
    parser.add_argument("--output", "-o", required=True, help="Output CSV to be uploaded to AirTable BIJAN Volunteer Database.")
    options = parser.parse_args(args)
    df = pandas.read_csv(options.input, parse_dates=[0])
    if False:
        # experimenting
        interesting_cols = frozenset(['Daytime during the week / durante el día, los días de semana',
                                      'English / ingles', 'Portuguese / portugués'
                                      ])
        for col in df.columns:
            if col in interesting_cols:
                print(f"{col}: {df[col].unique()}")
    df = convert_values(df)
    if False:
        # experimenting
        print("after")
        for col in df.columns:
            if col in interesting_cols:
                print(f"{col}: {df[col].unique()}")
    out_dict = {
        "First Name": df.iloc[:, google_sheet_cols.FIRSTNAME_COL],
        "Last Name": df.iloc[:, google_sheet_cols.LASTNAME_COL],
        "Email": df[google_sheet_cols.EMAIL_COL],
        "Phone": df.iloc[:, google_sheet_cols.PHONE_COL],
        "Affiliation - Congregation/Organization": df.iloc[:, google_sheet_cols.AFFILIATION_COL],
        "City/Town/Neighborhood": df.iloc[:, google_sheet_cols.CITY_COL],
        "Willing To Drive": df.iloc[:, google_sheet_cols.DRIVER_COL],
        "Special Skills": df.iloc[:, google_sheet_cols.SKILLS_COL],
        "Evenings and Weekends": df.iloc[:, google_sheet_cols.EVENINGS_WEEKENDS_COL],
        "During the Week": df.iloc[:, google_sheet_cols.WEEKDAYS_COL],
        "Email/Writing/Phone Independent Tasks": df.iloc[:, google_sheet_cols.INDEPENDENT_TASKS_COL],
        "Filler 1": "" * len(df.index),
        "English": df.iloc[:, google_sheet_cols.ENGLISH_COL],
        "Español": df.iloc[:, google_sheet_cols.SPANISH_COL],
        "Portugués": df.iloc[:, google_sheet_cols.PORTUGUESE_COL],
        "Other Languages": df.iloc[:, google_sheet_cols.OTHER_LANG_COL]
    }
    out_df = pandas.DataFrame(out_dict)
    out_df.to_csv(options.output, index=False)
    print(f"Wrote {len(out_df)} rows to {options.output}")

if __name__ == "__main__":
    sys.exit(main())
