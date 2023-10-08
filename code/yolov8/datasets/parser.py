import os

path  = "C:\\Users\\saisi\\source\\datasets\\bleeding\\labels"
ext = ".txt"
name="img"
sent = "1"
for i in range(1310, 2619):
    file_name = path+"//"+name+str(i)+ext
    with open(file_name, mode="w") as f:
        f.write(sent)