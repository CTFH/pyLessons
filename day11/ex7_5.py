file=open('sample.txt', 'r')
for line in file:
    print(line)
file.close()

file_r=open('sample.txt', 'r')
file_w=open('copy.txt', 'w')
for line in file_r:
    file_w.write(line)
file_r.close()
file_w.close()

