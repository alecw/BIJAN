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
    'only during the summer / solamente durante el verano': "summertime only / solamente durante el verano",
    'yes': 'yes / sí'
}

evenings_weekends_value_conv = {
    'yes /sí': 'yes / sí'
}

independent_task_conv = {
    'yes': 'yes / sí'
}

english_value_conv = {
    'proficient / proficiente' : 'proficient'
}

portuguese_value_conv = {
    'fluente / fluent' : 'fluente',
    'un poco / some' : ' um pouco'
}

spanish_value_conv = {
    'hablante nativa' : 'hablante nativa / native speaker'
}

english_value_conv = {
    'Yes': 'fluent'
}

values_conversion_dict = {
    google_sheet_cols.WeekdaysKey: weekdays_value_conv,
    google_sheet_cols.EveningsWeekendsKey: evenings_weekends_value_conv,
    google_sheet_cols.IndependentTasksKey: independent_task_conv,
    google_sheet_cols.EnglishKey: english_value_conv,
    google_sheet_cols.PortugueseKey: portuguese_value_conv,
    google_sheet_cols.SpanishKey: spanish_value_conv
}

def convert_values(colNameDct, df):
    for row_index in range(len(df)):
        for colKey, dct in values_conversion_dict.items():
            colName = colNameDct[colKey]
            col_index = df.columns.get_loc(colName)
            if df.iloc[row_index, col_index] in dct:
                df.iloc[row_index, col_index] = dct[df.iloc[row_index, col_index]]
    return(df)

def fixTeamsForGSuiteAffiliation(df):
    """
    Affiliation field is choice from a drop-down menu.  Affiliation2 is free text.  So, if Affiliation is not
    interesting and Affiliation2 is interesting, replace Affiliation with Affiliation2
    """
    affiliationColIndex = df.columns.get_loc(google_sheet_cols.TeamsForGSuiteColNames[google_sheet_cols.AffiliationKey])
    affiliation2ColIndex = df.columns.get_loc(google_sheet_cols.TeamsForGSuiteColNames[google_sheet_cols.Affiliation2Key])
    for row_index in range(len(df)):
        affiliation = df.iloc[row_index, affiliationColIndex]
        affiliation2 = df.iloc[row_index, affiliation2ColIndex]
        if affiliation2 != "" and (affiliation == "Other" or affiliation == ""):
            df.iloc[row_index, affiliationColIndex] = affiliation2
    return(df)

InputTypeBijanSignUpGoogleForm = "form"
InputTypeTeamsForGSuite = "gsuite"

ColNameDct = {
InputTypeBijanSignUpGoogleForm: google_sheet_cols.BijanSignUpColNames,
InputTypeTeamsForGSuite: google_sheet_cols.TeamsForGSuiteColNames

}

def printEnumCols(colNameDct, df):
    for colKey in google_sheet_cols.EnumColumnKeys:
        if colKey in colNameDct:
            print(f"{colKey}: {df[colNameDct[colKey]].unique()}")

AirTableEmailColName = "Email"
AirTableTimestampColName = "Timestamp"

def loadAndConvertDf(input, fileType, sep):
    df = pandas.read_csv(input, parse_dates=["Timestamp"], sep=sep, header=0)
    # This was only necessary when there was some junk in the input (a header line in the middle of the file)
    #    df.loc[df["Timestamp"] == "", "Timestamp"] = "1/1/1970 01:00:00"
    #    df["Timestamp"] = pandas.to_datetime(df['Timestamp'])
    print(f"Loaded {len(df)} rows from {input} type {fileType}")
    if fileType == InputTypeTeamsForGSuite:
        df = fixTeamsForGSuiteAffiliation(df)
    for col in df.columns:
        print(f'"{col}",')
    colNameDct = ColNameDct[fileType]
    print("Before enum conversion")
    printEnumCols(colNameDct, df)
    df = convert_values(colNameDct, df)
    print("After enum conversion")
    printEnumCols(colNameDct, df)
    blank_values = "" * len(df.index)
    out_dict = {
        "First Name": df[colNameDct[google_sheet_cols.FirstNameKey]],
        "Last Name": df[colNameDct[google_sheet_cols.LastNameKey]],
        AirTableEmailColName: df[colNameDct[google_sheet_cols.EmailKey]],
        "Phone": df[colNameDct[google_sheet_cols.PhoneKey]],
        "Affiliation - Congregation/Organization": df[colNameDct[google_sheet_cols.AffiliationKey]],
        "City/Town/Neighborhood": df[colNameDct[google_sheet_cols.LocationKey]],
        "Willing To Drive": df[colNameDct[google_sheet_cols.DriverKey]],
        "Willing To Accompany": df[colNameDct[google_sheet_cols.AccompanyKey]] if google_sheet_cols.AccompanyKey in colNameDct else blank_values,
        "Special Skills": df[colNameDct[google_sheet_cols.SkillsKey]],
        "Evenings and Weekends": df[colNameDct[google_sheet_cols.EveningsWeekendsKey]],
        "During the Week": df[colNameDct[google_sheet_cols.WeekdaysKey]],
        "Email/Writing/Phone Independent Tasks": df[colNameDct[google_sheet_cols.IndependentTasksKey]],
        "Filler 1": blank_values,
        "English": df[colNameDct[google_sheet_cols.EnglishKey]],
        "Español": df[colNameDct[google_sheet_cols.SpanishKey]],
        "Portugués": df[colNameDct[google_sheet_cols.PortugueseKey]],
        "Other Languages": df[colNameDct[google_sheet_cols.OtherLanguageKey]],
        "Timestamp": df[colNameDct[google_sheet_cols.TimestampKey]]
    }
    return(pandas.DataFrame(out_dict))



def main(args=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True, nargs=2, action="append", metavar=("INPUT_FILE", "TYPE"),
                        help="Input CSV or TSV downloaded from Google Sheet 'BIJAN Community Sign-Up (Responses)'. "
                             f"Type is one of '{InputTypeBijanSignUpGoogleForm}' for 'BIJAN Community Sign-Up', "
                             f"or '{InputTypeTeamsForGSuite}' for 'Teams for GSuite'")
    parser.add_argument("--output", "-o", required=True,
                        help="Output CSV to be uploaded to AirTable BIJAN Volunteer Database.")

    parser.add_argument("--sep", default='\t',
                        help="Separator for input fields.  Use ',' for csv.  Default: tab.")
    parser.add_argument("--outsep", default=',',
                        help="Separator for output fields.  Use ',' for csv.  Default: comma.")
    options = parser.parse_args(args)
    dfs = [loadAndConvertDf(input, fileType, options.sep) for input, fileType in options.input]
    all_dfs = pandas.concat(dfs)
    #all_dfs.set_index(["Email", "Timestamp"], inplace=True)
    newest_emails = all_dfs.groupby(AirTableEmailColName, as_index=False).agg(Timestamp=pandas.NamedAgg(column=AirTableTimestampColName, aggfunc=max))
    print(f"{len(all_dfs)} rows loaded, and {len(newest_emails)} unique email addresses")
    # Select most recent entry for each email address.
    # I'm sure there is a better way of doing this
    join_columns = [AirTableEmailColName, AirTableTimestampColName]
    all_dfs.set_index(join_columns, drop=False, inplace=True)
    newest_emails.set_index(join_columns, drop=False, inplace=True)
    to_drop_suffix = "_xxx"
    best_df = all_dfs.join(newest_emails, how="inner", rsuffix=to_drop_suffix)
    for colname in join_columns:
        best_df.drop(colname + to_drop_suffix, axis='columns', inplace=True)
    best_df.to_csv(options.output, index=False, sep=options.outsep)
    print(f"Wrote {len(best_df)} rows to {options.output}")

if __name__ == "__main__":
    sys.exit(main())
