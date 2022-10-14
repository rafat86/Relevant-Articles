import os

article_num = 1
title = []
article_data = []
folder = os.path.join(os.getcwd(), 'Articles2')
print("Articles Names")
for path, dir, files in os.walk(folder):
    for f in files:
        first_line = os.path.join(path, f)
        with open(first_line, "r") as myfile:
            title.append(myfile.readline())
            article_data.append(myfile.read())

for tit in title:
    print(article_num, ' ', tit)
    article_num += 1

article_num = 1
for article in article_data:
    article_data[article_num - 1] = article_data[article_num - 1].lower()
    irrelevant_word = ["\n", ".", ",", "? ", "! ", " the ", " a ", " for ", "by ", "and ", " to ", " in ",
                       " with ", " is ", " of ", " this ", " very ", " our ", " was ", " all ", " must ", " so ",
                       " no ", " his ", " at ", " on ", " was ", " were ", " his ", " her ", " him ", " its ",
                       " new ", " be ", " had ", " he ", " that ", " it ", " from ", " you ", " as ", " have ",
                       " been ", " would ", " who ", " about ", " has ", " then ", " an ", " i ", " my ", " just ",
                       " not ", " mr ", " up ", " better ", " us ", " she ", " they ", " are ", " could ", " also ",
                       " after", " not ", " will ", " than ", " -- ", " when ", " said ", " want ", " told ",
                       " but ", " - ", " more ", " if ", " which ", " there ", " we ", " or ", " can ", " â€“ ",
                       " u ", " s ", " their ", " most ", " every ", " one ", " didn't ", " such "]
    for irwd in irrelevant_word:
        article_data[article_num - 1] = article_data[article_num - 1].replace(irwd, " ")
        word_list = article_data[article_num - 1].split(" ")
        word_histogram = {}
        for word in word_list:
            if word not in word_histogram.keys():
                word_histogram[word] = 1
            else:
                word_histogram[word] = word_histogram[word] + 1
    word_histogram.pop("")
    sorted_word_histogram = sorted(word_histogram.items(), key=lambda x: x[1], reverse=True)
    final_word_histogram = sorted_word_histogram[0:6]
    print(final_word_histogram)
    article_num += 1

enter_article_no = int(input("Select article nu: "))
print(enter_article_no, title[enter_article_no - 1])
