import jieba
import pandas as pd

corpus = pd.read_csv("../data/corpus.tsv", sep="\t", names = ["doc_id", "title"])
corpus_head = corpus.head()
corpus_head.loc[:, "seg_list"] = corpus_head.apply(lambda x: list(jieba.cut_for_search(x["title"])), axis=1)
print(corpus_head.head())

# print(list(jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")))