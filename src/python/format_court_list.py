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
"""
Read file produced by something like 'curl -o court_locations.html https://www.justice.gov/eoir/eoir-immigration-court-listing'
and convert into compact form for adding to Hearing Locations in AirTable Hearings table
"""
import argparse
import re
import sys
from bs4 import BeautifulSoup

address_sep_re = re.compile("\n+\s*")
non_breaking_space=" "

def clean_string(s):
    return s.strip().rstrip().replace(non_breaking_space, " ")

def main(args=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', '-i', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--output', '-o', type=argparse.FileType('w'), default=sys.stdout)
    options = parser.parse_args(args)
    tree = BeautifulSoup(options.input, 'html.parser')
    courtHeaders = tree.find_all("strong", text="Court")
    for courtHeader in courtHeaders:
        tr = courtHeader.parent.parent
        for court_row in tr.next_siblings:
            tds = court_row.find_all("td")
            court_name = clean_string(tds[0].get_text().strip())
            court_name = re.sub(address_sep_re, " ", court_name)
            court_address = clean_string(tds[1].get_text())
            court_address_str = re.sub(address_sep_re, ", ", court_address)
            print(f"{court_name} Court, {court_address_str}", file=options.output)

if __name__ == "__main__":
    sys.exit(main())
