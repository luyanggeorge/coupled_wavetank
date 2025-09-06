# 2D Wavetank Coupled With a Sloping Beach
This repository contains the source code for a **coupled numerical wavetank (NWT)** that links a potential-flow solver for deep water with a nonlinear shallow-water solver for the nearshore region. The two models are coupled through an interface, enabling efficient simulations of the full life cycle of waves—from generation by a wavemaker, to shoaling, breaking, and dissipation on a sloping beach.

## Simulation instructions
- Set the simulation parameters in `settings.py`.
- Adjust the length of the dry beach through the coefficient `margin` in the main file `coupled_tank`.
- Run the main code in serial with `python3 coupled_tank.py`.

### Notes 
- The solution may fail to converge depending on the choice of the coupling point $x_c$.
  - If this happens, move the coupling interface further into the dry beach by reducing `Hc` in the function `domain()` in `settings.py`. This reduces the $z$-dependence of the deep-water velocity potential $\phi(x,z,t)$ at $x=x_c$.
- Simulations can also fail when waves begin to overturn in the shallow-water domain.
  - In this case, try reducing the wavemaker amplitude or stopping the wavemaker motion earlier.

## Visualisation of the waves with *ParaView*  

### Output files  
The solver saves several `.pvd` files for visualising wave motion in the coupled numerical wavetank:  
- **Wave fields**:  
  - `dw_waves.pvd`: velocity potential field in the deep-water domain.  
  - `sw_waves.pvd`: horizontal velocity field in the shallow-water domain.  
- **Free-surface profiles**:  
  - `dw_h_t.pvd`: wave profile $h(x,t)$ in the deep-water region.  
  - `sw_h_t.pvd`: wave profile $h(x,t)$ in the shallow-water region.  
- **Seabed geometry**:  
  - `dw_beach.pvd`: time-independent seabed $b(x)$ in the deep-water region.  
  - `sw_beach.pvd`: time-independent seabed $b(x)$ in the shallow-water region.

These outputs can be combined in *ParaView* to reconstruct the full wave dynamics in the wavetank (example: [YouTube demo](https://www.youtube.com/watch?v=HFw2ayh2oXk)).  

### Visualisation instructions  
1. Open `dw_waves.pvd` in *ParaView*.  
   - Apply the **Transform** filter, rotate by 90° around the x-axis to display the field in the x-z plane.  
   - Apply the **Gradient** filter (with respect to x) to compute the horizontal velocity $u = \phi_x$.  
   - In the *Properties* panel, under the *Coloring* section, choose `Gradient` and `X` to visualise $u$.  
2. Open `sw_waves.pvd` and apply the **Transform** filter again to display the field in the x-z plane.  
3. Open `dw_beach.pvd`.  
   - Apply the **Warp By Scalar** filter to render the seabed profile.  
   - In the *Properties* panel, under the *Coloring* section, choose `Solid Color` for a uniform seabed appearance.  
4. Repeat step 3 for `sw_beach.pvd` to display the shallow-water beach.  
5. *(Optional)* Apply the **Warp By Scalar** filter to `dw_h_t.pvd` and `sw_h_t.pvd` to highlight the free-surface wave profiles.  



