import time
start= time.process_time()
words = []
fileOB = open("findtext.txt","r")
lines= fileOB.read().splitlines()
for lines in lines:
    words.extend(lines.splitlines())
    
words1=[]
fileOB1= open("replace.txt","r")
lines1 =fileOB1.read().splitlines()
for line in lines1:
    words1.extend(line.splitlines())

with open("t8.shakespeare.txt","r") as file:
    filedata= file.read()

for i in range(len(words)):
    filedata=filedata.replace(words[i],words1[i])

with open ("t8.shakespeare.txt","w") as file:
    file.write(filedata)

print(time.process_time()-start)