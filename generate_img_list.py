# coding: utf-8
import os
import csv
img_dir = "/Users/hezheng/Downloads/img/"
with open("img_list.csv", "w", newline="") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    g = os.walk(img_dir)
    for path,d,filelist in g:
        for filename in filelist:
            if filename.endswith('jpg'):
                f = os.path.join(path, filename)
                csvwriter.writerow ([f])

