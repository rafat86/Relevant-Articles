import os

article_num = 1
title=[]
article_data=[]
folder = os.path.join(os.getcwd(),'Articles2')
print("Articles Names")
for path,dir, files in os.walk(folder):
  for f in files:
    first_line =os.path.join(path,f)
    with open(first_line,"r") as myfile:
      title.append(myfile.readline())
      article_data.append(myfile.read())

for tit in title:
  print (article_num, ' ', tit)
  article_num+=1

enter_article_no=int(input("Select article nu: "))
print(enter_article_no , title[enter_article_no -1])
print(article_data[enter_article_no - 1])




