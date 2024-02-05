import csv
import functions

nameFile = "ejemplo.csv"
nameFileCorrect = "FileOutput.csv"
nameFileIncorrect = "FileOutputIncorrect.csv"
with open(nameFile,  newline='', encoding='ascii') as archivo, \
     open(nameFileCorrect, 'w', newline='', encoding='utf-8', ) as nameFileCorrect, \
     open(nameFileIncorrect, 'w', newline='', encoding='utf-8', ) as nameFileIncorrect:
    lector_csv = csv.reader(archivo, delimiter=',')
    isFirst = True
    errorData = 0
    for fila in lector_csv:
        if isFirst:
            writerCsvCorrect = csv.writer(nameFileCorrect, delimiter=',')
            writerCsvCorrect.writerow(fila)
            writerCsvInCorrect = csv.writer(nameFileIncorrect, delimiter=',')
            writerCsvInCorrect.writerow(fila)
            isFirst = False
            continue
        id = fila[0]
        dateData = fila[1]
        page = fila[2]
        time = fila[3]

        if id.strip().isnumeric():
            idValid = id
        else:
            errorData = -1

        if functions.tryToConvertData(dateData):
            dateDataValid = dateData
        else:
            errorData = -1

        if page:
            pageValid = page
        else:
            errorData = -1

        if time.strip().isnumeric():
            timeValid=time
        else:
            errorData = -1

        if errorData == 0:
            writerCsvCorrect = csv.writer(nameFileCorrect, delimiter=',')
            writerCsvCorrect.writerow(fila)

        else:
            writerCsvInCorrect = csv.writer(nameFileIncorrect, delimiter=',')
            writerCsvInCorrect.writerow(fila)

        print(f"Id: {id}, Date: {dateData}, Page: {page}, Time: {time}, Register Data Error: {errorData}")
        errorData = 0
