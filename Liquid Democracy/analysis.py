import pandas as pd
# Load the DataFrame from the CSV file
df = pd.read_csv('Liquid Democracy/data.csv')

columns_to_drop = [0,2,3]
df = df.drop(columns=df.columns[columns_to_drop])

columns_to_drop = ["ConsideredDuringPreviousSitting", "IsInSenatePreStudy", "ParliamentNumber", "LatestCompletedMajorStageName","DidReinstateInNextSession", "LatestCompletedMajorStageId", "IsProForma", "BillFormId", "BillFormName", "Notes", "ShortLegislativeSummary", "IsFullLegislativeSummaryAvailable", "StatuteYear", "StatuteChapter", "BillStages", "Publications", "HouseVoteDetails", "SenateVoteDetails", "HouseRulingAndStatements", "SenateRulingAndStatements", "WebReferences", "BibliographicNotices", "SenatePreStudyCommitteeDetails", "SimilarBills", "IsDroppedFromSenateOrderPaper", "ShortTitle"]  # List of column names to drop
df = df.drop(columns=columns_to_drop)

df = df.dropna(axis=1, thresh=20)

columns_to_drop = [col for col in df.columns if 'Sponsor Person' in col and col != 'Sponsor Person Name']
df = df.drop(columns=columns_to_drop)

columns_to_drop = [col for col in df.columns if 'En' in col or 'Fr' in col or 'Id' in col or 'Time' in col]
df = df.drop(columns=columns_to_drop)

# Print the resulting DataFrame

print(df)
df.to_csv('modifiedData.csv', index=False)