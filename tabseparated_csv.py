#to make subject,predicate) ,(object), (language_tag)
#into separate "\t" separated .csv file


import csv
with open('short_abstracts_copy.csv','r')as f:
    reader= csv.reader(f,delimiter='\"')
    for i in range(5):
        next(reader)
    with open("short_abstracts_copy_tab.csv", 'w')as new_file:
        writer = csv.writer(new_file, delimiter="\t")
        for r in reader:
            writer.writerow(r)



