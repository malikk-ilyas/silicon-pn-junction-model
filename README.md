# Computational Modeling of an Abrupt Silicon p–n Junction

**Project type:** Small, reproducible computational physics study  
**Language/tools:** Python, NumPy, Matplotlib  
**Model:** One-dimensional abrupt silicon p–n junction at thermal equilibrium using the depletion approximation

## Project question

How do acceptor and donor doping concentrations affect the built-in potential, depletion width, charge density, and electric field of a silicon p–n junction?

## Scope and assumptions

This is an educational analytical/numerical model, not a commercial device simulation. It assumes:

- An abrupt junction with uniform acceptor concentration on the p side and uniform donor concentration on the n side.
- Thermal equilibrium and no applied external bias.
- Complete dopant ionization.
- The depletion approximation: mobile carriers are neglected inside the depletion region, and the charge there is due to fixed ionized dopants.
- Non-degenerate semiconductor statistics.
- A fixed intrinsic carrier concentration \(n_i = 10^{10}\,\mathrm{cm^{-3}}\), silicon relative permittivity \(\epsilon_r=11.7\), and temperature \(T=300\,\mathrm K\).
- The doping sweep sets \(N_A=N_D\) and varies both from \(10^{14}\) to \(10^{18}\,\mathrm{cm^{-3}}\). The simple model becomes less reliable at very high doping where degeneracy and band-gap narrowing can matter.

## Governing equations

Thermal voltage:

\[
V_T = \frac{k_B T}{q}
\]

Built-in potential at equilibrium:

\[
V_{bi} = V_T \ln\left(\frac{N_A N_D}{n_i^2}\right)
\]

Total depletion width for an abrupt junction at zero applied bias:

\[
W = \sqrt{\frac{2\epsilon_{Si}}{q}\left(\frac{1}{N_A}+\frac{1}{N_D}\right)V_{bi}}
\]

Charge-neutrality condition:

\[
N_A x_p = N_D x_n,\qquad W=x_p+x_n
\]

Thus:

\[
x_p=W\frac{N_D}{N_A+N_D},\qquad
x_n=W\frac{N_A}{N_A+N_D}
\]

Within the depletion approximation, with the metallurgical junction at \(x=0\):

\[
\rho(x)=
\begin{cases}
-qN_A, & -x_p \le x \le 0\\
+qN_D, & 0 < x \le x_n\\
0, & \text{outside the depletion region}
\end{cases}
\]

The electric field follows Poisson's equation \(dE/dx=\rho/\epsilon_{Si}\), with \(E=0\) at the depletion edges. For this sign convention, the field points from the positively charged n-side depletion region toward the negatively charged p-side depletion region.

## Baseline parameters and computed results

- Temperature: 300 K
- \(N_A=N_D=10^{16}\,\mathrm{cm^{-3}}\)
- \(n_i=10^{10}\,\mathrm{cm^{-3}}\)
- \(\epsilon_r=11.7\)

The included Python script computes the built-in potential, total depletion width, the width on each side, and the spatial charge and field distributions. Re-run the script to obtain the exact numerical output for the local Python/NumPy environment.

## Results to interpret

1. **Built-in potential versus doping:** The model predicts an increase with doping because \(V_{bi}\) depends logarithmically on \(N_A N_D/n_i^2\).
2. **Depletion width versus doping:** For symmetric doping, the total depletion width decreases as doping rises. The reduction in width is much stronger than the increase in built-in potential.
3. **Charge density:** It is negative on the p side and positive on the n side of the depletion region, with zero charge density outside the idealized depletion region.
4. **Electric field:** It is zero at the depletion edges and varies linearly within each side of an abrupt, uniformly doped depletion region. Its magnitude is largest at the junction.

## Validation checks

- Check charge neutrality: \(N_Ax_p \approx N_Dx_n\).
- Check the depletion partition: \(x_p+x_n=W\).
- Check that the electric field is zero at both depletion edges.
- Check that the field is continuous at the junction for a standard abrupt junction without a sheet charge.
- Check units carefully: doping is supplied in cm\(^{-3}\) but converted to m\(^{-3}\) for SI calculations.
- Compare the calculated baseline values with a semiconductor-device textbook or a trusted educational reference before using numerical values in a presentation.

## Limitations

This model does **not** simulate a full current–voltage curve, carrier transport, recombination, quantum confinement, tunneling, or a real fabricated device. It is not TCAD and does not predict measured device performance. The assumed intrinsic concentration and simplified non-degenerate model limit interpretation at high doping. More advanced work could include applied bias, asymmetric doping, temperature dependence, or comparison with a validated device simulator.

## Suggested 60-second explanation

“I implemented a one-dimensional equilibrium model of an abrupt silicon p–n junction using Python. I used the built-in-potential relation and the depletion approximation to calculate the total depletion width and how it divides between the p and n sides. I then plotted the fixed charge density and electric field, and swept equal p- and n-side doping concentrations to study trends. I checked charge neutrality and the depletion-edge boundary conditions. The main result is that increasing doping raises the built-in potential logarithmically but reduces the depletion width. This is an idealized model; it does not replace TCAD or include carrier transport.”

## Before presenting this as your own project

- Run the script yourself and inspect all plots.
- Read the equations and be able to explain every variable and unit.
- Verify the baseline numerical values independently.
- Record any changes you make to the code and report.
- Cite any textbook, paper, or web resource used to verify the model.
