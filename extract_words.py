import csv

# get words
with open("five_letter_words.txt", "r") as words_file:

    words_list = [word.strip() for word in words_file]
    words_file.close()
    print("words file read")

# split words
with open('split_words.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    # header row
    csvwriter.writerow([x for x in range(1, 6)])

    # split words so each letter is in a column
    for word in words_list:
        csvwriter.writerow([*word])
    
    print("split words written to csv")