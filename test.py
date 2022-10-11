import os
a = 1
title=[]
article_data=[]
folder = os.path.join(os.getcwd(),'Articles2')
print("Articles Names")
for path,dir, files in os.walk(folder):
    for f in files:
        firstline =os.path.join(path,f)
        with open(firstline,"r") as myfile:
            title.append(myfile.readline())
            article_data.append(myfile.read())
#            print(a,":", myfile.readline())
#            a = a + 1

for tit in title:
    print (a, ' ', tit)
    a+=1

enter_article_no=int(input("Select article nu"))
print(enter_article_no , title[enter_article_no -1])
print(article_data[enter_article_no - 1])



