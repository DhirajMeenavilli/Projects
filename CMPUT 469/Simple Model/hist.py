from collections import Counter
import pandas as pd
def get_histogram(df, topic_column, text_column, topic_value):
    terms_counter = Counter()
    for index, row in df.iterrows():
        if row[topic_column] == topic_value:
            text = row[text_column].lower()  # Convert to lowercase for case-insensitive counting
            terms_counter.update(text.split())  # Split text into terms and count frequencies
    
    return terms_counter


def main():
    # Sample data
    data = pd.read_csv("CMPUT 469\Finetune\Sepearating Questions\Q1LabelerLabels.csv")
    
    topic_column = 'Housing'  # Index of the column containing the topic labels
    text_column = 'a2'  # Index of the column containing the text
    topic_value = 1  # Value indicating the topic of interest
    
    histogram = get_histogram(data, topic_column, text_column, topic_value)

    sorted_histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

    filtered_histogram = [(term, frequency) for term, frequency in sorted_histogram if frequency >= 0]
    
    print("Term\tFrequency")
    for term, frequency in filtered_histogram:
        print(f"{term}\t{frequency}")

if __name__ == "__main__":
    main()