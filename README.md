# FabParticleDA
This is a ParticleDA example plugin for FabSim3. It is meant to provide support for using ParticleDA with FabSim3.

## Installation
Simply type `fabsim localhost install_plugin:FabParticleDA` anywhere inside your FabSim3 install directory.

To install the Julia dependencies for ParticleDA, type:
`fabsim localhost install_particleda_dependencies`

(remote dependency installation support will be added if users need it [just raise a GitHub issue in the repo])

## Testing
1. To test a ParticleDA model, type `fabsim localhost test_community_model`.

By default it will run `llw2d.jl` as model (which produces no output if run correctly). 
It is possible to run other community models using:
`fabsim localhost test_community_model:model=<name of julia script>`
Examples models include:
* llw2d.jl
* lineargaussian.jl
* lorenz63.jl

(a separate command to run user-made models will be added as soon as users need it, but no later than the end of Q2 2023)

## Explanation of files
* FabParticleDA.py - main file containing command implementations.
* config_files/ParticleDA_test - directory containing input data for the community model command.
* templates/test_community_model - template file for running a community model command on the remote machine.


