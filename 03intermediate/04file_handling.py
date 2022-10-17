'''
File Handling ->  To store data
text file -> html, txt, doc, py
binary file -> mp3 , mp4, pdf, png

file = open(file_name , mode) 

modes:
rt -> read mode
w -> write mode
a -> append mode

# binary modes:
rb -> read binary
wb -> write mode
'''

# TODO: Read mode file should already exist
file = open("./02scope.py" , "r")
# print(file)
# data = file.read()
# print(data)
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines()[-1])
# file.seek(10)
# print(file.read(10))
file.close()


# TODO: writing in a file
# if file does not exist then it creates a new file
# It overwrites the content
# f1 = open("./ex.txt","w")
# f1.write("hello")
# f1.writelines(["csdnvj\n","sdnjvn\n"])
# f1.close()


# TODO: append mode
# It adds the content at the end of the file

# f2 = open("./ex.txt","a")
# f2.write("Writing with append mode")
# f2.close()

# smarter way of file handling
# with open("./02scope.py" , "r") as f1 , open("./copy.txt" , "w") as f2:
#     for data in f1:
#         f2.write(data)

# print("file is closed automatically")


# TODO: binary file

# with open("./pic.png","rb") as f1:
    # print(f1.read())

with open("./pic.png","rb") as f1 , open("./copy.png","wb") as f2:
    for data in f1:
        f2.write(data)