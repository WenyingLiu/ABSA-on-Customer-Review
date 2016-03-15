import pandas as pd

def cleanFile(inputPath):

    with open(inputPath) as f:
        data = f.read()

    review_list = data.split('[t]') # Each review starts with a title tagged as [t]
    review_list = filter(None, review_list)

    cleaned_sents = []
    cleaned_labels = []
    for reivew in review_list:
        review_sents = reivew.split('\r\n')
        #print 'Title is: ', review_sents[0]
        for s in review_sents[1:]:
            label = re.findall(r"(?:^|,)(.*?)\[\+?(\-?\d+)\]", s) # Split review text, aspect and corresponding polarity score.
            if label != []: # Igonore neural sentence or sentence without referencing to specific aspect.
                cleaned_sents.append(s.split('##')[-1])
                cleaned_labels.append(label)

    return cleaned_sents, cleaned_labels

def main():

    cleaned_sents, cleaned_labels = cleanFile(inputPath)

    pd_canon = pd.DataFrame(columns=['cleaned_sent', 'cleaned_label'])
    pd_canon['cleaned_sent'] = cleaned_sents
    pd_canon['cleaned_label'] = cleaned_labels
    pd_canon.to_csv(outputPath)

if __name__ == '__main__':
    main()

