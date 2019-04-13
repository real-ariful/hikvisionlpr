


#This file converts an image of texts into texts and then converts into a csv file 

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import time


##def imgToText:

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def checknames(h_no,h_captureTime,h_plateNo):
    if 'No.' in h_no:
        h_no = 'No.'
    if 'Capture Time' in h_captureTime:
        h_captureTime = 'Capture Time'
    if 'Plate No.' in h_plateNo:
        h_plateNo = 'Plate No.'

    return h_no,h_captureTime,h_plateNo



#while True:
#time.sleep(60)
print("--------Reading image to text--------")
print("-------------------------------------")
# Simple image to string
img2string = pytesseract.image_to_string(Image.open('test1.png'))
print(img2string)
print(type(img2string))
print(len(img2string.split("\n\n")))


h_no = img2string.split("\n\n")[0].split(" ")[0]
h_captureTime = img2string.split("\n\n")[0].split(" ")[1]+" "+ img2string.split("\n\n")[0].split(" ")[2]
h_plateNo = img2string.split("\n\n")[0].split(" ")[3]+ " " + img2string.split("\n\n")[0].split(" ")[4]


h_no,h_captureTime,h_plateNo = checknames(h_no,h_captureTime,h_plateNo)
print(h_no,h_captureTime,h_plateNo)
if h_no =='No.' and h_captureTime == 'Capture Time' and h_plateNo =='Plate No.':

    for row in img2string.split("\n\n"):
        #print(row)
    ##    print(row.split(" "))
        no = row.split(" ")[0]
        capturetime = row.split(" ")[1:3]
        plateno = row.split(" ")[3:]
        #print(no, capturetime, plateno)



        

    fieldnames = [h_no,h_captureTime,h_plateNo]
    print(fieldnames)

    print("--------Converting to a csv file----------")
    print("------------------------------------------")
    import csv
    with open('test1.csv', 'w', newline='') as test_file:
        #fieldnames = ['No.','Capture Time', 'Plate No.']
        
        csv_writer = csv.DictWriter(test_file, fieldnames=fieldnames, delimiter=",")

        csv_writer.writeheader()

        for row in img2string.split("\n\n")[1:]:
            if row[0] != "No.":
                
                no = row.split(" ")[0]
                capturetime = str(row.split(" ")[1]) + " " + str(row.split(" ")[2])
                #MM-DD-YYYY H:M:SS
                plateno = row.split(" ")[3]
                
                #print(no, capturetime, plateno)
                line = str(row.split(" ")[0])+","+str(row.split(" ")[1])+str(row.split(" ")[2])+","+ row.split(" ")[3]
                line={'No.' : no, 'Capture Time':capturetime, 'Plate No.': plateno}
                print(line)
                csv_writer.writerow(line)



        import csv
        print("Reading  a csv file")
        #Reading  a csv file
        with open('test1.csv', 'r') as csv_file:
            #next(csv_reader)
            csv_reader = csv.reader(csv_file)

            #print(csv_reader)# print the object

            for line in csv_reader:
                print(line)

else:
    print("Header does not matvch")

import time
time.sleep(120)










    
