import os
from modeller import *
from modeller.automodel import *
from modeller.parallel import *

N_CPU = 30
ALI = "alignment.pir"
TEMPLATE = "5JQH"
TARGET = "hT2R16"
SCORES = (assess.DOPE,
          assess.DOPEHR,
          assess.GA341)

# create a new MODELLER environment to build this model in
j = job()
for i in range(N_CPU):
    j.append(local_slave())
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = automodel(
    env,
    alnfile  = ALI,
    knowns   = TEMPLATE,
    sequence = TARGET,
    assess_methods = SCORES,
)

# index of the first model
a.starting_model= 1
# index of the last model
a.ending_model  = 1000

# Variable Target Function method: VTFM optimization with conjugate gradient
a.library_schedule = autosched.normal     # default: autosched.normal
a.max_var_iterations = 300    # default: 200

# MD optimization with simulated annealing
a.md_level = refine.slow # default: refine.very_fast

# Repeat the whole cycle n times and do not stop unless obj.func. > 1e7
a.repeat_optimization = 1    # default: 1
a.max_molpdf = 1e7   # default: 1e7

# Build
a.use_parallel_job(j)
a.make()

# Write modeller scores for each model
ok_models = [x for x in a.outputs if x['failure'] is None]
with open(os.path.join(TARGET, TEMPLATE, "modeller_scores.out"),
          'w') as f:
    # Rank the models by score
    keys = ["%s score" % x.__name__ if x.__name__ != 'DOPEHR' else 'DOPE-HR score'
            for x in SCORES ] + ['molpdf']
    sorter = keys[0]
    ok_models.sort(key=lambda model: model[sorter])
    # write CSV
    formatter = '{}' + '\t{}'*len(keys) + '\n'
    f.write(formatter.format('Filename', *keys))
    formatter = '{}' + '\t{:.3f}'*len(keys) + '\n'
    for model in ok_models:
        results = [model[key] if key != 'GA341 score' else model[key][0]
                   for key in keys]
        f.write(formatter.format(model['name'], *results))