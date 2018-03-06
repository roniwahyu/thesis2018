import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stemming process
# sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
# output   = stemmer.stem(sentence)


with open('teststem.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    outputs=[]
    for row in readCSV:
        color = row[3]
        # date = row[0]
        output = stemmer.stem(color)
        # dates.append(date)
        colors.append(color)
        outputs.append(output)

    # print(dates)
    print(colors)
    # print(outputs)