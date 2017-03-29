VALIDATION= validation 
CONFIG_FILES= $(wildcard pipeline_config/*.py)
SIG_FILES= $(patsubst pipeline_config/%.py,%,$(CONFIG_FILES))

.PHONY: all
all:
	echo "specify task"

.PHONY: cleanup
cleanup:
	rm -Rfv tmp/*

.PHONY: clean
clean: cleanup
	rm -Rv results/*

.PHONY: crossvalidation
crossvalidation: $(patsubst %,results/%/signatures.gmt,$(SIG_FILES))

.PHONY: run_bioqc
run_bioqc: $(patsubst %,results/%/signatures_bioqc,$(SIG_FILES)) $(patsubst %,results/%/signatures_fold_intersections_bioqc,$(SIG_FILES))

.PHONY: merge_bioqc
merge_bioqc: $(patsubst %,results/%/signatures_bioqc.uniq.tsv,$(SIG_FILES)) $(patsubst %,results/%/signatures_fold_intersections_bioqc.uniq.tsv,$(SIG_FILES))

results/%/signatures.gmt: pipeline_config/%.py
	$(VALIDATION) crossvalidation $<

results/%/signatures_bioqc: results/%/signatures.gmt results/%/signatures_bioqc/bioqc_todo.txt 
	$(VALIDATION) run_bioqc $< 

results/%/signatures_fold_intersections_bioqc: results/%/signatures_fold_intersections_bioqc.gmt results/%/signatures_fold_intersections_bioqc/bioqc_todo.txt 
	$(VALIDATION) run_bioqc $< 

results/%/signatures_bioqc.uniq.tsv:  results/%/signatures_bioqc
	# signatures_bioqc not made a dependency, as the previous command does not block
	# until finished. 
	$(VALIDATION) merge_bioqc $< 

results/%/signatures_fold_intersections_bioqc.uniq.tsv: results/%/signatures_fold_intersections_bioqc
	# signatures_bioqc not made a dependency, as the previous command does not block
	# until finished. 
	$(VALIDATION) merge_bioqc $< 

results/%/bioqc_todo.txt:
	#empty target, will be created by script. 


