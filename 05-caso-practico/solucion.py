
import glob
import os
##
## Parte 1
##

file_in = open('tabla1.csv', 'r')

isfirstline = True

n = 0
for line in file_in:

    if isfirstline:
        isfirstline = False
        continue

    text = line.split(',')
    filename = text[0] + '-' + text[1] + '-' + text[6] + '.txt'

    f = open(filename, 'a')
    f.write(text[-1])
    f.close()

    n += 1

    if n == 5000:
        break

file_in.close()

##
## Parte 1
##
n = 0

file_out = open('tabla2.csv', 'w')
file_out.write('ESTACION,ANO,MES,DIA,HORA,VEL\n')


for filename in glob.glob("*.txt"):

    file_in = open(filename, 'r')

    lines = file_in.readlines()
    text = [float(x) for x in lines]
    filename = filename.replace('-', ',')
    prom = sum(text) / len(text)
    prom = '%.2f' % prom
    file_out.write(filename[:-4] + ',' + str(prom) + '\n')
    file_in.close()

    n += 1
    if n == 10:
        break

file_out.close()
os.remove('*.txt')
