try:
    filee = open('sample.txt','r+')
    writing1 = filee.write('Line1:This is a sample text file.\n')
    writing2 = filee.write('Line2:It contains multiple lines.')
    print(writing1)
    print(writing2)
    filee.close()

    filee =open('sample.txt','r+')
    reading = filee.read()
    print("Reading file content:")
    print(reading)
    filee.close()

except FileNotFoundError:
    print("Error:The file",'sample.txt'," was not found.")
