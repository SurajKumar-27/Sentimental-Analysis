import csv
import re
from emoji import demojize
from string import punctuation
data=open("data.csv",'r')
file=csv.DictReader(data)
text=[]
sentiment=[]

for col in file:
    text.append(col['review'])
    sentiment.append(col['sentiment'])
print(len(text))
for i in text:
        i=demojize(i)
        i=i.lower()
        i=i.casefold()
        i=" ".join([w for w in i.split() if w.isalnum()])
        i= " ".join([w for w in i.split() if w.isalpha()])
        i= re.sub(r"[^A-Za-z0-9\s]+", "",i)
        i= " ".join([w for w in i.split() if not w.isdigit()])
        #i= re.sub(f"[{re.escape(punctuation)}]", "",i)
        #i= re.sub(r"\b[0-9]+\b\s*", "",i)
        #i= " ".join(i.split())
        #i= re.sub(r"<a[^>]*>(.*?)</a>", r"\1",i)
print(text)
print(sentiment)