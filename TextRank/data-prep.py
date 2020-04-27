import csv
import os
import sys

f = open('data.csv', 'w')
writer = csv.writer(f)

dir="news/"
news_articles="news_articles/"
summaries="summaries/"

# Read BBC News Data from text files
subfolders = os.listdir(dir+news_articles)

# for each folder in news
for folder in subfolders:

        article_directory = dir+news_articles+folder+"/"
        summary_directory = dir+summaries+folder+"/"

        for i in range(len(os.listdir(article_directory))):

            ID=""
            if i<9:
                    ID="00"+str(i+1)+".txt"
            elif i>=9 and i<99:
                ID="0"+str(i+1)+".txt"
            else:
                ID=str(i+1)+".txt"
            try:
                # text file
                text=""
                with open(article_directory+ID, encoding="utf-8") as tf:
                    next(tf)
                    text=tf.read()
                    tf.close()

                summary=""
                with open(summary_directory+ID, encoding="utf-8") as sf:
                    summary=sf.read()
                    sf.close()

                writer.writerow([text,summary])
            except:
                continue

f.close()