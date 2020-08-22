# govtech_section_1

This repository contains the answers to Govtech's section 1: Data Pipelines

## process_dataset.py
This file contains the python code in which when executed, processes the input file `dataset.csv`, and creates the required output file `processed_dataset.csv`. The splitting of name into first and last name logic includes removal of all abbreviations, and then assuming the first name component to be the first name, and the next component to be the last name. If the first name is empty, that means there are no valid name components and the row will be skipped. The logic to handle removal of leading zeros from price and creation of a new field `above_100` to be `true` when the price is greater than 100 is fairly straightforward. Kindly refer to comments in code.

## Approach
For the implementation, I chose a solution that is efficient in memory. During execution, only the current row is loaded into memory as opposed to the entire file contents.
