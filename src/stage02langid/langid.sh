# table of unique n-grams; input noisy corpus; prefix of output files: for generating filenames for cleaned corpus and removed output
python langid.py uniq-ru_ngramsEd.txt news.lemmatized.shuffled.10k.txt langid-news.lemmatized.shuffled.10k
python langid.py uniq-ru_ngramsEd.txt news.tokenized.shuffled.10k.txt langid-news.tokenized.shuffled.10k

# python langid.py uniq-ru_ngramsEd.txt '/Volumes/G-RAID with Thunderbolt/elisp/gdata/ukcorpus/news.lemmatized.shuffled.1m.txt' '/Volumes/G-RAID with Thunderbolt/elisp/gdata/ukcorpus/langid-news.lemmatized.shuffled.100k'
# python langid.py uniq-ru_ngramsEd.txt '/Volumes/G-RAID with Thunderbolt/elisp/gdata/ukcorpus/news.tokenized.shuffled.1m.txt' '/Volumes/G-RAID with Thunderbolt/elisp/gdata/ukcorpus/langid-news.tokenized.shuffled.100k'
# 
# python langid.py uniq-ru_ngramsEd.txt '/Volumes/G-RAID with Thunderbolt/elisp/gdata/ukcorpus/news.lemmatized.shuffled.txt' '/Volumes/G-RAID with Thunderbolt/elisp/gdata/ukcorpus/langid-news.lemmatized.shuffled'
# python langid.py uniq-ru_ngramsEd.txt '/Volumes/G-RAID with Thunderbolt/elisp/gdata/ukcorpus/news.tokenized.shuffled.txt' '/Volumes/G-RAID with Thunderbolt/elisp/gdata/ukcorpus/langid-news.tokenized.shuffled'

