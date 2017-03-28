from pygenesig.gini import GiniSignatureGenerator
from pygenesig.bioqc import BioQCSignatureTester

config = {
    'expr_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/exprs_unprocessed.npy',
    'target_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/target.csv',
    'fdata_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/roche_annotated_fdata.tsv',
    'n_splits': 10,
    'signature_generator': GiniSignatureGenerator,
    'sg_kwargs': {"min_gini": .8, "max_rk": 3, "min_expr": 5},
    'signature_tester': BioQCSignatureTester,
    'st_kwargs': {},
    'out_dir': '/pstore/home/sturmg/projects/gtex-signatures/results/v3/gtex_unprocessed_0.8_3'
}
