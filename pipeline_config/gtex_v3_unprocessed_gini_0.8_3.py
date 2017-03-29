from pygenesig.gini import GiniSignatureGenerator
from pygenesig.bioqc import BioQCSignatureTester

config = {
    'expr_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/exprs_unprocessed.npy',
    'target_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/target.csv',
    'rosetta_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/rosetta_unprocessed.csv',
    'n_splits': 10,
    'signature_generator': GiniSignatureGenerator,
    'sg_kwargs': {"min_gini": .8, "max_rk": 3, "min_expr": 5, "max_rel_rk": None},
    'signature_tester': BioQCSignatureTester,
    'st_kwargs': {},
    'out_dir': '/pstore/home/sturmg/projects/gtex-signatures/results/v3/gtex_unprocessed_gini_0.8_3'
}
