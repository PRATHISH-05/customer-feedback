# from textblob import TextBlob
# text=input("Say something: ")
# score=TextBlob(text).sentiment.polarity

# print("positive" if score>0 else "negative" if score<0 else "neutral")
# print(f"({score:.2f})")






from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
def get_sentiment(text):
    polarity=TextBlob(str(text)).sentiment.polarity
    
    if polarity>0:
        return "positive",polarity
    elif polarity<0:
        return "negative",polarity

    else:
        return "neutral",polarity

if __name__ == "__main__":
    df=pd.read_csv("Milestone1_Cleaned_Feedback.csv")
    df[["sentiment","confidence_score"]]=df["clean_feedback"].apply(lambda x: pd.Series(get_sentiment(x)))
    df.to_csv("Milestone2_Sentiment_Results_new.csv",index=False)
    print("Milestone 2 completed successfully") 
    sentiment_counts=df["sentiment"].value_counts()
    plt.figure(figsize=(8,5))
    colors=["green","red","blue"]
    sentiment_counts.plot(kind="bar",color=colors)

    plt.title('How customer feel _Sentiment summary',fontsize=14)
    plt.xlabel('Sentiment',fontsize=12)
    plt.ylabel('Number of Reviews',fontsize=12)
    plt.xticks(rotation=0)
    
    for i, count in enumerate(sentiment_counts):
        plt.text(i, count + 20, str(count), ha='center', fontsize=12)

    # Save/show once to avoid oversized tight-bbox output.
    plt.tight_layout()
    plt.savefig('sentiment-bar-chart.png', dpi=100)
    plt.show()
    print('Bar chart saved as sentiment-bar-chart.png')

    print(df[["clean_feedback", "sentiment", "confidence_score"]].head())
    