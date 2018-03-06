import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

with file("afterfilter.csv", "r") as rfh, file("afterstemming.csv", "w") as wfh:
    baca = csv.reader(rfh,delimiter=',')
    tulis = csv.writer(wfh,delimiter=',', quoting=csv.QUOTE_MINIMAL)
    tulis.writerow(['After Filter', 'After Stemming'])
    keluaran=[]
    for row in baca:
        kategori=row[3]
        katid=row[4]
        disposisi=row[5]
        dispid=row[6]
        origdoc=row[8]
        stemdoc=stemmer.stem(origdoc)
        tulis.writerow([katid, kategori,dispid, disposisi,origdoc, stemdoc])
        keluaran.append(stemdoc)
    print(keluaran)
