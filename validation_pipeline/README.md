# Signature validation pipeline

This pipeline takes a gene expression matrix together with 
sample annotations (e.g. tissue) to generate gene signatures. 

It performs a cross-validation, generates a report that yields
insights into the quality of signatures and generates 
a .gmt file for further use. 

## Usage
All parameters are specified in the config file: 
```
./run_cv.py config_file.py
```

## Config file
A config file is a python file which looks like this: 

```python
from pygenesig.gini import GiniSignatureGenerator
from pygenesig.bioqc import BioQCSignatureTester

config = {
    'expr_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/exprs_processed.npy',
    'target_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/target.csv',
    'fdata_file': '/pstore/home/sturmg/projects/gtex-signatures/data/v3/roche_annotated_fdata.tsv',
    'n_splits': 10,
    'signature_generator': GiniSignatureGenerator,
    'sg_kwargs': {"min_gini": .8, "max_rk": 3, "min_expr": 5},
    'signature_tester': BioQCSignatureTester,
    'st_kwargs': {},
    'out_dir': 'pstore/home/sturmg/projects/gtex-signatures/results/v3/gtex_0.8_3'
}

```
