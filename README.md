# csv_to_10Xdata

csv_to_10Xdata is a tool for transforming a gene expression matrix csv file into 10X style files.

## Usage

python csv_to_10Xdata.py [expression_file]

python csv_to_10Xdata_samplelimit.py [expression_file] [output_folder] [From i] [To j]

## Input

#### (1) expression_file - a csv file with N cells in the rows and M genes in the columns.

		GENE_1	GENE_2	GENE_3	...	GENE_M

	CELL_1	

	CELL_2

	CELL_3

	.
	.
	.

	CELL_N

#### (2) [From i] [To j] - From the next cell of ith cell to jth cell you want to choose.

###### If you want to choose first cell to 100th cell, you can type 0 for [From i] and 100 for [To j]

## Output

(1) matrix.mtx - expression file with MatrixMarket File Format

(2) genes.tsv

(3) barcodes.tsv

