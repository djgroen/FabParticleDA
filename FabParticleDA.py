# -*- coding: utf-8 -*-
#
# This source file is part of the FabSim software toolkit, which is distributed under the BSD 3-Clause license.
# Please refer to LICENSE for detailed information regarding the licensing.
#
# This file contains FabSim definitions specific to FabDummy.

try:
    from fabsim.base.fab import *
    from fabsim.VVP import vvp
except ImportError:
    from base.fab import *

# Add local script, blackbox and template path.
add_local_paths("FabDummy")


@task
def particleda(config, **args):
    """Submit a Dummy job to the remote queue.
    The job results will be stored with a name pattern as defined in the environment,
    e.g. cylinder-abcd1234-legion-256
    config : config directory to use to define input files, e.g. config=cylinder
    Keyword arguments:
            cores : number of compute cores to request
            images : number of images to take
            steering : steering session i.d.
            wall_time : wall-time job limit
            memory : memory per node
    """
    update_environment(args)
    with_config(config)
    execute(put_configs, config)
    job(dict(script='dummy', wall_time='0:15:0', memory='2G'), args)


@task
def particleda_ensemble(config="dummy_test", **args):
    """
    Submits an ensemble of dummy jobs.
    One job is run for each file in <config_file_directory>/dummy_test/SWEEP.
    """

    path_to_config = find_config_file_path(config)
    print("local config file path at: %s" % path_to_config)
    sweep_dir = path_to_config + "/SWEEP"
    env.script = 'dummy'
    env.input_name_in_config = 'dummy.txt'
    with_config(config)
    run_ensemble(config, sweep_dir, **args)


@task
def install_particleda_dependencies():
    for p in ["Distributions","GaussianRandomFields","HDF5","PDMats"]:
        cmdstr = f'import Pkg; Pkg.add("{p}")'
        local(f"julia -e '{cmdstr}'")

