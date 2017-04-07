from pygenesig.gini import GiniSignatureGenerator
from pygenesig.bioqc import BioQCSignatureTester

config = {
    'expr_file': '/pstore/home/sturmg/projects/pygenesig-example/data_processed/v3/exprs_processed.npy',
    'target_file': '/pstore/home/sturmg/projects/pygenesig-example/data_processed/v3/target.csv',
    'rosetta_file': '/pstore/home/sturmg/projects/pygenesig-example/data_processed/v3/rosetta_processed.csv',
    'n_splits': 10,
    'signature_generator': GiniSignatureGenerator,
    'sg_kwargs': {"min_gini": .8, "max_rk": 3, "min_expr": 5, "max_rel_rk": .33},
    'signature_tester': BioQCSignatureTester,
    'st_kwargs': {},
    'mem': '100G',
    'results_dir': '/pstore/home/sturmg/projects/pygenesig-example/results'
}
