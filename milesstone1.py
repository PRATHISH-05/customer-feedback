import pandas as pd
import re
import string

STOPWORDS={
    "is","the","and","a","an","to","of","in","on","for","with","this","that","it","was","are","as","at","be","by","from","or","but"
}

def clean_text(text):

    text=str(text).lower()
    text=re.sub(r"https\s+","",text)
    text=re.sub(r"\d+","",text)
    text=text.translate(str.maketrans("","",string.punctuation))
    text=re.sub(r"\s+","",text).strip()
    words=[W for W in text.split() if W not in STOPWORDS]
    return " ".join(words) 

def main():
    file_path="ReviewSense_Customer_Feedback_5000.xlsx - Customer_Feedback.csv"
    file_path_csv="Milestone_cleaned_feedback.csv"

    try:
        df=pd.read_csv(file_path)
        print("Reading from Excel file")
    except FileNotFoundError:
        print("Excel file not found.Attempting to read from Existing csv")
        try:
            df=pd.read_csv(file_path_csv)
            if "clean_feedback" in df.columns:
                print("CSV already has cleaned feedback. Skipping cleaning")
                return 
            elif "feedback" in df.columns:
                print("Re-cleaning feedback from CSV")
            else:
                raise ValueError(" 'feedback' column not found in CSV")
        except FileNotFoundError:
            raise ValueError(" Neither Excel nor CSV file found. Please provide the input file.")

# Ensure feedback column exists

        if "feedback" not in df.columns:
            raise ValueError(" 'feedback' column not found in file")

    df["clean_feedback"] = df["feedback"].apply(clean_text)

    df.to_csv("Milestone1_Cleaned_Feedback.csv", index=False)

    print(" Milestone 1 completed successfully")
    print(df[["feedback", "clean_feedback"]].head())

if __name__ == "__main__":
    main()