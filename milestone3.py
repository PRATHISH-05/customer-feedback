import pandas as pd
from collections import Counter
import re

def extract_keywords(text):
    text=str(text).lower()
    text=re.sub(r"[^a-z\s]","",text)
    words=text.split()
    return words

#---- Main Execution ----
if __name__ == "__main__":
   
   #input from Milestone 2
   df=pd.read_csv("Milestone2_Sentiment_Results_new.csv")

   #--Extract Keywords from clean feedback
   all_words=[]
   df["clean_feedback"].apply(lambda x:all_words.extend(extract_keywords(x)))

   #--Count Keyword frequency
   keyword_freq=Counter(all_words)

   #--Convert to Dataframe
   keywords_df=pd.DataFrame(keyword_freq.items(), columns=["keyword", "frequency"]).sort_values(by="frequency", ascending=False)
   #Save results
   keywords_df.to_csv("Milestone3_keyword_Insights.csv",index=False)

   print("Milestone 3 completed successfully")
   print(keywords_df.head(10))