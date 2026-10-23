"""
Computational Modeling of an Abrupt Silicon p-n Junction
Educational project: equilibrium depletion approximation, 300 K.

Model assumptions:
- Abrupt, one-dimensional, uniformly doped junction
- Complete ionization of dopants
- Depletion approximation
- Non-degenerate semiconductor statistics
- No applied external bias
- ni = 1e10 cm^-3 and relative permittivity of silicon = 11.7

Run:
    python pn_junction_model.py
Requires:
    numpy
    matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt

# Physical constants
q = 1.602176634e-19       # elementary charge, C
k_B = 1.380649e-23        # Boltzmann constant, J/K
T = 300.0                 # temperature, K
eps0 = 8.8541878128e-12   # vacuum permittivity, F/m
eps_si = 11.7 * eps0      # silicon permittivity, F/m
ni_cm3 = 1.0e10           # assumed intrinsic carrier concentration, cm^-3
V_T = k_B * T / q         # thermal voltage, V

# Symmetric doping example
NA_cm3 = 1.0e16           # acceptor concentration, cm^-3
ND_cm3 = 1.0e16           # donor concentration, cm^-3

# Convert cm^-3 to m^-3 for SI calculations
NA = NA_cm3 * 1e6
ND = ND_cm3 * 1e6
ni = ni_cm3 * 1e6

# Equilibrium built-in potential (non-degenerate approximation)
V_bi = V_T * np.log((NA * ND) / (ni**2))

# Depletion approximation: total width and charge-neutrality partition
W = np.sqrt((2 * eps_si / q) * (1 / NA + 1 / ND) * V_bi)
x_p = W * ND / (NA + ND)  # depletion extension into p side
x_n = W * NA / (NA + ND)  # depletion extension into n side

print("=== Silicon p-n junction: equilibrium, depletion approximation ===")
print(f"Temperature: {T:.1f} K")
print(f"Acceptor doping NA: {NA_cm3:.2e} cm^-3")
print(f"Donor doping ND:   {ND_cm3:.2e} cm^-3")
print(f"Thermal voltage:   {V_T:.4f} V")
print(f"Built-in potential: {V_bi:.4f} V")
print(f"Total depletion width: {W*1e6:.4f} µm")
print(f"Into p side x_p: {x_p*1e6:.4f} µm")
print(f"Into n side x_n: {x_n*1e6:.4f} µm")
print(f"Charge-neutrality check NA*x_p = ND*x_n: "
      f"{NA*x_p:.4e} vs {ND*x_n:.4e} (m^-2)")

# Plot domain, in micrometers; x=0 is the metallurgical junction
x_um = np.linspace(-1.5, 1.5, 1501)
x = x_um * 1e-6

# Charge density under depletion approximation (C/m^3)
rho = np.zeros_like(x)
p_region = (x >= -x_p) & (x <= 0)
n_region = (x >= 0) & (x <= x_n)
rho[p_region] = -q * NA
rho[n_region] = q * ND

# Electric field from Poisson's equation; E = 0 at depletion edges
E = np.zeros_like(x)  # V/m
E[p_region] = -(q * NA / eps_si) * (x[p_region] + x_p)
E[n_region] = (q * ND / eps_si) * (x[n_region] - x_n)

# Symmetric doping sweep: NA = ND
doping = np.logspace(14, 18, 200)  # cm^-3
doping_m3 = doping * 1e6
V_bi_sweep = V_T * np.log((doping_m3 * doping_m3) / (ni**2))
W_sweep = np.sqrt((2 * eps_si / q) * (2 / doping_m3) * V_bi_sweep)

# Figure 1: electric field
plt.figure(figsize=(7, 4.5))
plt.plot(x_um, E / 1e5)  # V/m -> kV/cm
plt.axhline(0, linewidth=0.7)
plt.xlabel("Position x (µm)")
plt.ylabel("Electric field E (kV/cm)")
plt.title("Electric field across an abrupt Si p-n junction (equilibrium)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("electric_field.png", dpi=180)
plt.close()

# Figure 2: charge density
plt.figure(figsize=(7, 4.5))
plt.plot(x_um, rho / 1e6)  # C/m^3 -> C/cm^3
plt.axhline(0, linewidth=0.7)
plt.xlabel("Position x (µm)")
plt.ylabel("Charge density rho (C/cm^3)")
plt.title("Depletion-region charge density (equilibrium)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("charge_density.png", dpi=180)
plt.close()

# Figure 3 and 4: doping sensitivity
plt.figure(figsize=(7, 4.5))
plt.plot(doping, V_bi_sweep)
plt.xscale("log")
plt.xlabel("Equal acceptor/donor doping NA = ND (cm^-3)")
plt.ylabel("Built-in potential V_bi (V)")
plt.title("Built-in potential vs symmetric doping (300 K)")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.savefig("built_in_potential_vs_doping.png", dpi=180)
plt.close()

plt.figure(figsize=(7, 4.5))
plt.plot(doping, W_sweep * 1e6)
plt.xscale("log")
plt.xlabel("Equal acceptor/donor doping NA = ND (cm^-3)")
plt.ylabel("Total depletion width W (µm)")
plt.title("Depletion width vs symmetric doping (300 K)")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.savefig("depletion_width_vs_doping.png", dpi=180)
plt.close()

print("\\nSaved figures: electric_field.png, charge_density.png, "
      "built_in_potential_vs_doping.png, depletion_width_vs_doping.png")
