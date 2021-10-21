# gass-ppi

## TM-Align

Build using below command in Mac:

```
g++ -O3 -ffast-math -lm -o TMalign TMalign.cpp
```

Example command:

```
./TMalign 1pme.pdb 4n4s.pdb
```

Note:

1. Cannot use `#include <malloc.h>` since it's deprecated, use `#include <stdlib.h>` instead.

## PDB Preprocessing

Example command:

```
python pdb-preprocessing.py /Users/albertdarmawan/Documents/gass-ppi/core/ 3nos.pdb
```
