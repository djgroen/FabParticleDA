# Load ParticleDA
using ParticleDA

# Save some variables for later use
test_dir = joinpath(dirname(pathof(ParticleDA)), "..", "test")
llw2d_src = joinpath(test_dir, "models", "llw2d.jl")
input_file = joinpath(test_dir, "integration_test_1.yaml")
observation_file = tempname()

# Instantiate the test environment
using Pkg
Pkg.activate(test_dir)
Pkg.instantiate()

# Include the sample model source code and load it
include(llw2d_src)
using .LLW2d

# Simulate observations from the model to use 
simulate_observations_from_model(LLW2d.init, input_file, observation_file)

# Run the (optimal proposal) particle filter with simulated observations computing the
# mean and variance of the particle ensemble. On non-Intel architectures you may need
# to use NaiveMeanAndVarSummaryStat instead
final_states, final_statistics = run_particle_filter(
  LLW2d.init, input_file, observation_file, OptimalFilter, MeanAndVarSummaryStat
)
