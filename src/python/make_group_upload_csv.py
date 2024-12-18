#!/usr/bin/env python3
# MIT License
# 
# Copyright 2022 Alec Wysoker
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
import argparse
import sys

import numpy as np

import google_sheet_cols
import pandas
from functools import reduce

from defs import NEGATORY, ALL_EMAIL, ACCOMPANY_EMAIL, DRIVE_EMAIL, parse_date, make_output_df


def main(args=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True,
                        help="Input CSV downloaded from BIJAN Community Sign-Up (Responses) "
                             "or BIJAN AirTable Volunteers")
    parser.add_argument("--format", "-f", required=True, choices=[google_sheet_cols.InputTypeBijanSignUpGoogleForm,
                                                                  google_sheet_cols.InputTypeAirTableVolunteers])
    parser.add_argument("--output", "-o", required=True, help="Output CSV to be uploaded to Google Admin console.")
    parser.add_argument("--later-than", type=parse_date, help="Select rows later than this date YYYY-MM-DD.")
    parser.add_argument("--earlier-than", type=parse_date, help="Select rows earlier than this date YYYY-MM-DD.")
    options = parser.parse_args(args)
    if options.format == google_sheet_cols.InputTypeBijanSignUpGoogleForm:
        dctColNames = google_sheet_cols.BijanSignUpColNames
    else:
        dctColNames = google_sheet_cols.AirTableVolunteersColNames

    timestampColName = dctColNames[google_sheet_cols.TimestampKey]
    # this is now a list of column names
    accompanyColNames = dctColNames[google_sheet_cols.AccompanyKey]
    driveColName = dctColNames[google_sheet_cols.DriverKey]
    emailColName = dctColNames[google_sheet_cols.EmailKey]
    df = pandas.read_csv(options.input, parse_dates=[timestampColName])
    if options.later_than is not None:
        df = df[df[timestampColName] > options.later_than]
    if options.earlier_than is not None:
        df = df[df[timestampColName] < options.earlier_than]

    accompanyMasks = [df[accompanyColName] != NEGATORY for accompanyColName in accompanyColNames]
    accompanyMask = reduce(np.logical_or, accompanyMasks)
    accompany_df = df[accompanyMask]
    drive_df = df[df[driveColName] != NEGATORY]
    out_df = pandas.concat([make_output_df(df[emailColName], ALL_EMAIL),
                            make_output_df(accompany_df[emailColName], ACCOMPANY_EMAIL),
                            make_output_df(drive_df[emailColName], DRIVE_EMAIL)])
    if False:
        pandas.set_option('display.max_colwidth', None)
        pandas.set_option('display.max_columns', None)
        # Do not wrap
        pandas.set_option('display.width', None)
        print(out_df)
    out_df.to_csv(options.output, index=False)
    print(f"Wrote {len(out_df)} rows to {options.output}")


if __name__ == "__main__":
    sys.exit(main())
