import sys, os

ifile = open(sys.argv[1])
line = ifile.readline()
gene_name=line.replace("\n","").split(",")[1:]

ofile = open("genes.tsv","w")
for i in range(len(gene_name)):
    ofile.write(gene_name[i]+"\n")
ofile.close()

ofileHead = open("head.txt","w")
ofile = open("matrix_temp.mtx","w")
ofileHead.write("%%MatrixMarket matrix coordinate integer general\n")
barcodes=[];rowNum=1;dataNum=0
for line in ifile:
    temp=line.replace("\n","").split(",")
    barcodes.append(temp[0])
    for i in range(len(temp)-1):
        if int(temp[i+1])>0:
            ofile.write(str(i+1)+' '+str(rowNum)+' '+temp[i+1]+'\n')
            dataNum=dataNum+1
    rowNum=rowNum+1
ofile.close()
ifile.close()

ofileHead.write(str(len(gene_name))+" "+str(len(barcodes))+" "+str(dataNum)+"\n")
ofileHead.close()

os.system("cat head.txt matrix_temp.mtx > matrix.mtx")
os.system("rm matrix_temp.mtx head.txt")

ofile = open("barcodes.tsv","w")
for i in range(len(barcodes)):
    ofile.write(barcodes[i]+"\n")
ofile.close()
