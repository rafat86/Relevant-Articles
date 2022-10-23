import os

article_num = 1
title = []
article_data = []
folder = os.path.join(os.getcwd(), 'Articles2')
print("Articles Names")
for path, dir, files in os.walk(folder):
    for f in files:
        first_line = os.path.join(path, f)
        with open(first_line, "r", errors='ignore') as my_file:
            title.append(my_file.readline())
            article_data.append(my_file.read())

for tit in title:
    print(article_num, ' ', tit)
    article_num += 1

enter_article_no = int(input("Select article nu: "))
Listed_relevant_words = []
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
                       " u ", " s ", " their ", " most ", " le ", " every ", " one ", " didn't ", " such ", " _ ",
                       " iâ€™m ", " it's ", " 000 ", " what ", " 2016 ", " should ", " â€” ", " please "]
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
    list_histogram = list(map(lambda x: x[0], final_word_histogram))
    Listed_relevant_words.append(list_histogram)
    article_num += 1

article_num = 1
print("Relevant Text Number:", " / intersected words")
for relevant in Listed_relevant_words:
    list_1 = Listed_relevant_words[(enter_article_no - 1)]  # the reader choice
    list_2 = Listed_relevant_words[(article_num - 1)]
    intersected_list = list(set(list_1).intersection(set(list_2)))
    if len(intersected_list) >= 3:
        if (enter_article_no - 1) != (article_num - 1):  # to remove the reader choice from relevant articles
            print(article_num, intersected_list)
    article_num += 1
