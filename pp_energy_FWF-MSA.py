# Post-processing code for plotting the energy evolution 
# and water line x_c of the 2D coupled wavetank.

import numpy as np
import matplotlib.pyplot as plt
import os.path

#------ User Input ------#
test_case = "sb0.3_10_10_FWF"

H0 = 1.0
g = 9.81                                             
lamb = 2.0         # Wavelength
k = 2*np.pi/lamb   # Wave number
w = np.sqrt(g*k*np.tanh(k*H0))   # Wave frequency
Tw = 2*np.pi/w     # Wave period
t_stop = 10*Tw     # When to stop the wavemaker

comparison = True 
test_case2 = "sb0.3_10_10_MSA"

save_figure = True
fig1_name = 'energy_variations_MSA.png'
fig2_name = 'waterline_evolution_MSA.png'
fig3_name = 'hc_uc_evolution_MSA.png'
#------------------------#
data_path = 'data/' + test_case
file = os.path.join(data_path,'energy.csv')

with open(file,'r') as f:
    time, E_dw, E_sw, x_w, h_c, u_c = np.loadtxt(f, usecols=(0,1,2,3,4,5), unpack=True)

E_tot = E_dw + E_sw

if save_figure:
    save_path1 = os.path.join(data_path, fig1_name)
    save_path2 = os.path.join(data_path, fig2_name)
    save_path3 = os.path.join(data_path, fig3_name)

if comparison:
    data_path2 = 'data/' + test_case2
    file2 = os.path.join(data_path2,'energy.csv')
    with open(file2,'r') as f2:
        time2, E_dw2, E_sw2, x_w2, h_c2, u_c2 = np.loadtxt(f2, usecols=(0,1,2,3,4,5), unpack=True)
    E_tot2 = E_dw2 + E_sw2


# First figure: Energy variations
fig1, ax1 = plt.subplots()
fig1.set_size_inches(10, 5)
fig1.set_tight_layout(True)

ax1.set_title('Energy variations of the coupled wavetank', fontsize=18)
ax1.set_xlabel('$t$ [s]',fontsize=14)
ax1.set_ylabel('$E(t)-E(t_0)$ [J]',fontsize=14)
ax1.plot(time, E_dw, 'b-', label="Deep water")
ax1.plot(time, E_sw, 'r-', label="Shallow water")
ax1.plot(time, E_tot,'y-', label="Whole domain")
ax1.set_xlim(time[0], time[-1])

# Indicate the time when the wavemaker stops
ax1.axvline(x=t_stop, color='green', linestyle=':', label='Wavemaker switched off')

if comparison:
    ax1.plot(time2, E_dw2, 'bo', label="DW-MSA", markersize=5)
    ax1.plot(time2, E_sw2, 'ro', label="SW-MSA", markersize=5)
    ax1.plot(time2, E_tot2, 'yo', label="TOT-MSA", markersize=5)

ax1.legend(loc='upper right',fontsize=14)  
ax1.grid()

if save_figure:
    fig1.savefig(save_path1, dpi=300)

# Second figure: Waterline evolution
fig2, ax2 = plt.subplots()
fig2.set_size_inches(10, 4)
fig2.set_tight_layout(True)

#ax2.set_title('Evolution of the waterline', fontsize=18)
ax2.set_xlabel('$t$ [s]',fontsize=14)
ax2.set_ylabel('$x_w(t)$ [m]',fontsize=14)
ax2.plot(time, x_w,'b-', label="$x_w$, FWF")
ax2.set_xlim(time[0], time[-1])

if comparison:
    ax2.plot(time2, x_w2, 'c--', label="$x_w$, MSA")

    rel_diff = np.abs(x_w - x_w2) / np.max(np.abs(x_w))
    max_rel_diff = np.max(rel_diff)
    max_idx = np.argmax(rel_diff)
    t_max_diff = time[max_idx]

    print(f"Maximum relative difference in x_w(t): {max_rel_diff:.2%} at t = {t_max_diff:.2f} s")

ax2.legend(loc='upper left',fontsize=14)  
ax2.grid()

if save_figure:
    fig2.savefig(save_path2, dpi=300)

# Third figure: Two subplots for h_c and u_c
fig3, [ax3, ax4] = plt.subplots(2, sharex=True)
fig3.set_size_inches(10, 8)
fig3.set_tight_layout(True)

# Subplot 1: h_c
ax3.plot(time, h_c, 'b-', label='$h_c$, FWF')
ax3.set_ylabel('$h(x_c,t)$ [m]', fontsize=14)
ax3.set_xlim(time[0], time[-1])
ax3.grid()

# Subplot 2: u_c
ax4.plot(time, u_c, 'r-', label='$u_c$, FWF')
ax4.set_xlabel('$t$ [s]', fontsize=14)
ax4.set_ylabel('$u(x_c,t)$ [m/s]', fontsize=14)
ax4.grid()

if comparison:
    ax3.plot(time2, h_c2, color='#FF7F0E', linestyle='--', label="$h_c$, MSA")
    ax4.plot(time2, u_c2, color='#2CA02C', linestyle='--', label="$u_c$, MSA")
    ax3.legend(loc='upper left',fontsize=14)  
    ax4.legend(loc='upper left',fontsize=14)

    rel_diff = np.abs(h_c - h_c2) / np.max(np.abs(h_c))
    max_rel_diff = np.max(rel_diff)
    max_idx = np.argmax(rel_diff)
    t_max_diff = time[max_idx]

    print(f"Maximum relative difference in h_c(t): {max_rel_diff:.2%} at t = {t_max_diff:.2f} s")

    rel_diff = np.abs(u_c - u_c2) / np.max(np.abs(u_c))
    max_rel_diff = np.max(rel_diff)
    max_idx = np.argmax(rel_diff)
    t_max_diff = time[max_idx]

    print(f"Maximum relative difference in u_c(t): {max_rel_diff:.2%} at t = {t_max_diff:.2f} s")

if save_figure:
    fig3.savefig(save_path3, dpi=300)
else:
    plt.show()