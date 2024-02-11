import pandas as pd
import sys
import pickle
import argparse

def main(input1, input2, output):
    contact_df = pd.read_csv(input1)
    other_df = pd.read_csv(input2)

    contact_df.rename(columns={'respondent_id': 'ID'}, inplace=True)
    other_df.rename(columns={'id': 'ID'}, inplace=True)
    merged_df = pd.merge(contact_df, other_df, on='ID')

    merged_df.dropna(inplace=True)

    no_insurance_jobs = ~merged_df['job'].str.contains('insurance', case=False, na=False)
    cleaned_df = merged_df[no_insurance_jobs]

    cleaned_df.to_csv(output, index=False)
    print(f"Data cleaned and saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clean data by merging and filtering.')
    parser.add_argument('input1', help='Path to the respondent_contact.csv file')
    parser.add_argument('input2', help='Path to the respondent_other.csv file')
    parser.add_argument('output', help='Path to the output file where the cleaned data will be saved')
    args = parser.parse_args()

    main(args.input1, args.input2, args.output)