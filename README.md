# 2D Wavetank Coupled With a Sloping Beach
This repository contains the source code for a **coupled numerical wavetank** that links a potential-flow solver for deep water with a nonlinear shallow-water solver for the nearshore region. The two models are coupled through an interface, enabling efficient simulations of the full life cycle of waves—from generation by a wavemaker, to shoaling, breaking, and dissipation on a sloping beach.
## Simulation instructions
- Set the simulation parameters in `settings.py`.
- Adjust the length of the dry beach through the coefficient `margin` in the main file `coupled_tank`.
- Run the main code in serial `python3 coupled_tank.py`.
