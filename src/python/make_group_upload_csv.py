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
import datetime
import sys
import google_sheet_cols
import pandas


NEGATORY="no"
ALL_EMAIL="bijan@beyondbondboston.org"
ACCOMPANY_EMAIL="accompaniment@beyondbondboston.org"
DRIVE_EMAIL="drivers@beyondbondboston.org"

OUTPUT_COLUMN_NAMES = ["Group Email [Required]",	"Member Email",	"Member Type",	"Member Role"]

def parse_date(s):
    return(pandas.Timestamp(datetime.datetime.strptime(s, '%Y-%m-%d')))

def make_output_df(user_emails, group_email):
    out_dict = {
        "Group Email [Required]": [group_email] * len(user_emails),
        "Member Email": user_emails,
        "Member Type": ["User"] * len(user_emails),
        "Member Role": ["Member"] * len(user_emails)
    }
    return pandas.DataFrame(out_dict)


def main(args=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True, help="Input CSV downloaded from BIJAN Community Sign-Up (Responses).")
    parser.add_argument("--output", "-o", required=True, help="Output CSV to be uploaded to Google Admin console.")
    parser.add_argument("--later-than", type=parse_date, help="Select rows later than this date YYYY-MM-DD.")
    parser.add_argument("--earlier-than", type=parse_date, help="Select rows earlier than this date YYYY-MM-DD.")
    options = parser.parse_args(args)
    df = pandas.read_csv(options.input, parse_dates=[0])
    if options.later_than is not None:
        df = df[df[google_sheet_cols.TIMESTAMP_COL] > options.later_than]
    if options.earlier_than is not None:
        df = df[df[google_sheet_cols.TIMESTAMP_COL] < options.earlier_than]


    accompany_df = df[df.iloc[:, google_sheet_cols.ACCOMPANY_COL] != NEGATORY]
    drive_df = df[df.iloc[:, google_sheet_cols.DRIVER_COL] != NEGATORY]
    out_df = pandas.concat([make_output_df(df[google_sheet_cols.EMAIL_COL], ALL_EMAIL),
                  make_output_df(accompany_df[google_sheet_cols.EMAIL_COL], ACCOMPANY_EMAIL),
                  make_output_df(drive_df[google_sheet_cols.EMAIL_COL], DRIVE_EMAIL)])
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
