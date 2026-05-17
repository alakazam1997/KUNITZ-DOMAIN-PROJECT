#!/usr/bin/env python 

import sys 

 

# Reading command line arguments 

# pdbfile should be the path to your .pdb file 

# chain should be the specific ID (e.g., 'I' for BPTI in the 3TGI complex) [cite: 77] 

pdbfile = sys.argv[1] 

chain = sys.argv[2] 

 

# Opening the file using the handle 'fh' as seen in your image 

fh = open(pdbfile) 

 

# Looping through every line in the PDB file 

for line in fh: 

    # 1. We only want 'ATOM' lines which contain 3D coordinates [cite: 358] 

    # 2. line[21] is the standard PDB position for the Chain ID [cite: 358] 

    if line.startswith('ATOM') and line[21] == chain: 

        # rstrip() removes the newline character so we don't get double spacing 

        print(line.rstrip()) 

 

# It's good practice to close the file handle 

fh.close() 
