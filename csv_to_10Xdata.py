import sys

ifile = open(sys.argv[1])
line = ifile.readline()
gene_name=line.replace("\n","").split(",")[1:]

ofile = open("gene.tsv","w")
for i in range(len(gene_name)):
    ofile.write(gene_name[i]+"\n")
ofile.close()

ofile = open("matrix.mtx","w")
ofile.write("%%MatrixMarket matrix coordinate integer general\n\n")
barcodes=[];colNum=1;dataNum=0
for line in ifile:
    temp=line.replace("\n","").split(",")
    barcodes.append(temp[0])
    for i in range(len(temp)-1):
        if int(temp[i+1])>0:
            ofile.write(str(i+1)+' '+str(colNum)+' '+temp[i+1]+'\n')
            dataNum=dataNum+1
    colNum=colNum+1
ofile.seek(2)
ofile.write(str(len(gene_name))+" "+str(len(barcodes))+" "+str(dataNum)+'\n')
ifile.close()

ofile = open("barcodes.tsv","w")
for i in range(len(barcodes)):
    ofile.write(barcodes[i]+"\n")
ofile.close()
