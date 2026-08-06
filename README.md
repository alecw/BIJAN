# BIJAN

Utilities for managing BIJAN (Boston Immigration Justice Accompaniment Network) volunteer data: converting
Google Form/Sheet exports and AirTable exports into the CSV formats needed
for Google Group and AirTable uploads, and formatting immigration court
location listings.

## Simplest way to run
1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv).
2. Run one of the commands listed below using `uvx`.  E.g.:
```
uvx --with https://github.com/alecw/BIJAN.git bijan-make-group-upload-csv --help
```
## Installation

Install directly from GitHub:
```
pip install git+https://github.com/alecw/BIJAN.git
```
The commands listed below are then on your path.

## Commands

- `bijan-convert-google-airtable-volunteers`
- `bijan-make-group-upload-csv`
- `bijan-make-letter-writer-community-upload`
- `bijan-format-court-list`

Run any of them with `--help` for usage details.
