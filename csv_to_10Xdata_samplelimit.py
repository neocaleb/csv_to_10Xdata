import sys, os

ifile = open(sys.argv[1])
line = ifile.readline()
gene_name=line.replace("\n","").split(",")[1:]

folder_name=sys.argv[2]

ofile = open(folder_name+"/genes.tsv","w")
for i in range(len(gene_name)):
    ofile.write(gene_name[i]+"\n")
ofile.close()

ofileHead = open(folder_name+"/head.txt","w")
ofile = open(folder_name+"/matrix_temp.mtx","w")
ofileHead.write("%%MatrixMarket matrix coordinate integer general\n")
barcodes=[];rowNum=1;dataNum=0;rowNumFrom=int(sys.argv[3]);rowNumTo=int(sys.argv[4])
for line in ifile:
    if rowNum>rowNumFrom:
        temp=line.replace("\n","").split(",")
        barcodes.append(temp[0])
        for i in range(len(temp)-1):
            if int(temp[i+1])>0:
                ofile.write(str(i+1)+' '+str(rowNum-rowNumFrom)+' '+temp[i+1]+'\n')
                dataNum=dataNum+1
    rowNum=rowNum+1
    if rowNum>rowNumTo:
        break
ofile.close()
ifile.close()

ofileHead.write(str(len(gene_name))+" "+str(len(barcodes))+" "+str(dataNum)+"\n")
ofileHead.close()

os.system("cat "+folder_name+"/head.txt "+folder_name+"/matrix_temp.mtx > "+folder_name+"/matrix.mtx")
os.system("rm "+folder_name+"/matrix_temp.mtx "+folder_name+"/head.txt")

ofile = open(folder_name+"/barcodes.tsv","w")
for i in range(len(barcodes)):
    ofile.write(barcodes[i]+"\n")
ofile.close()
