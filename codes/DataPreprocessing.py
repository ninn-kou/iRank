import pandas as pd
from tqdm import tqdm


# Read data from original AMiner-Paper file.
data = [
    line.strip() for line in open("AMiner-Paper.txt", "r", encoding="utf-8").readlines()
]
# data1 = data[:1000]

save_edge = []
# Show a smart progress meter.
for i in tqdm(range(len(data))):
    if "#index" == data[i][:6]:
        id1 = data[i].replace("#index", "").strip()
        for j in range(i + 1, len(data)):
            # Index
            if "#%" == data[j][:2]:
                id2 = data[j].replace("#%", "").strip()
                save_edge.append([id1, 2, id2, 2, 1])
            elif data[j].strip() == "":
                break

df = pd.DataFrame(save_edge)
df.to_csv("paper.csv", index=None)


# Read data from original AMiner-Coauthor file.
data = [
    line.strip()
    for line in open("AMiner-Coauthor.txt", "r", encoding="utf-8").readlines()
]

save_edge = []
for i in tqdm(range(len(data))):
    dd = data[i].split("\t")
    save_edge.append([dd[0].replace("#", ""), 1, dd[1], 1, dd[2]])
df = pd.DataFrame(save_edge)
df.to_csv("author_author.csv", index=None)


# Read data from original AMiner-Author2Paper file for mapping from authors to papers.
data = [
    line.strip()
    for line in open("AMiner-Author2Paper.txt", "r", encoding="utf-8").readlines()
]

save_edge = []
for i in tqdm(range(len(data))):
    dd = data[i].split("\t")
    save_edge.append([dd[1], 1, dd[2], 2, 1])

df = pd.DataFrame(save_edge)
df.to_csv("Author2Paper.csv", index=None)

# Merge these data into a single file to represent the multilayered network.
df1 = pd.read_csv("paper.csv")
df2 = pd.read_csv("author_author.csv")
df3 = pd.read_csv("Author2Paper.csv")
df_1 = df1.append(df2)
df_1 = df_1.append(df3)
df_1.dtypes
df_1.columns
df_1["0"] = df_1["0"].astype(int)
df_1["2"] = df_1["2"].astype(int)
df_1["4"] = df_1["4"].astype(float)
df_1.to_csv("all.csv", index=None, header=None)
df_1.dtypes

# Obtain the list of authors and their H-index, which could be used as a ground truth.

data = [
    line.strip()
    for line in open("AMiner-Author.txt", "r", encoding="utf-8").readlines()
]
data1 = data[:1000]

save_edge = []
for i in tqdm(range(len(data))):
    if "#index" == data[i][:6]:
        id1 = data[i].replace("#index", "").strip()
        for j in range(i + 1, len(data)):
            if "#hi" == data[j][:3]:
                id2 = data[j].replace("#hi", "").strip()
                save_edge.append([id1, id2])
            elif data[j].strip() == "":
                break

df = pd.DataFrame(save_edge)
df.dtypes
# df[0] = df[0].astype(float)
df.to_csv("hidex.csv", index=None, header=None)
