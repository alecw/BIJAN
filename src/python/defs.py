#!/usr/bin/env python3
# MIT License
# 
# Copyright 2023 Broad Institute
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
import datetime

import pandas

NEGATORY = "no"
ALL_EMAIL = "bijan@beyondbondboston.org"
ACCOMPANY_EMAIL = "accompaniment@beyondbondboston.org"
DRIVE_EMAIL = "drivers@beyondbondboston.org"
OUTPUT_COLUMN_NAMES = ["Group Email [Required]", "Member Email", "Member Type", "Member Role"]


def parse_date(s):
    return (pandas.Timestamp(datetime.datetime.strptime(s, '%Y-%m-%d')))


def make_output_df(user_emails, group_email):
    out_dict = {
        "Group Email [Required]": [group_email] * len(user_emails),
        "Member Email": user_emails,
        "Member Type": ["User"] * len(user_emails),
        "Member Role": ["Member"] * len(user_emails)
    }
    return pandas.DataFrame(out_dict)
