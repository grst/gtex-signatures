from pygenesig.gini import GiniSignatureGenerator
from pygenesig.bioqc import BioQCSignatureTester

config = {
    'expr_file': '/pstore/home/sturmg/projects/pygenesig-example/data_processed/v6/expr_solid.npy',
    'target_file': '/pstore/home/sturmg/projects/pygenesig-example/data_processed/v6/target_solid.csv',
    'rosetta_file': '/pstore/home/sturmg/projects/pygenesig-example/data_processed/v6/rosetta.csv',
    'n_splits': 10,
    'signature_generator': GiniSignatureGenerator,
    'sg_kwargs': {"min_gini": .8, "max_rk": 3, "min_expr": 5, "max_rel_rk": .33},
    'signature_tester': BioQCSignatureTester,
    'st_kwargs': {},
    'results_dir': '/pstore/home/sturmg/projects/pygenesig-example/results',
    'mem': '200G',
    'n_jobs': 10
}
