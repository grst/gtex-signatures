from pygenesig.gini import GiniSignatureGenerator
from pygenesig.bioqc import BioQCSignatureTester

config = {
    'expr_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v6/exprs.npy',
    'target_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v6/target.csv',
    'rosetta_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v6/rosetta.csv',
    'n_splits': 10,
    'signature_generator': GiniSignatureGenerator,
    'sg_kwargs': {"min_gini": .8, "max_rk": 3, "min_expr": 5, "max_rel_rk": .33},
    'signature_tester': BioQCSignatureTester,
    'st_kwargs': {},
    'results_dir': '/pstore/home/sturmg/projects/gtex-signatures/results',
    'mem': '240G',
    'n_jobs': 5 # limit number of jobs to reduce memory usage
}
