#!/usr/bin/env python3

# Author:      Alexander Koc <alexander.koc@slu.se>
# Date:        2017-10-11
# Description: This script takes a fastq-file as input and outputs a fasta file to STDOUT.

from Bio import SeqIO
import sys

input_fq = sys.argv[1]

with open(input_fq) as fastq_in:
    records = SeqIO.parse(fastq_in, "fastq")
    for record in records:
        print(">{}\n{}".format(record.id, record.seq))
