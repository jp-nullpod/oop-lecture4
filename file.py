f = open('secrets.txt','a+')

try: 
    f.write("\nLife is really good\n")
finally:
    f.close()