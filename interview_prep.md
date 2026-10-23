# Interview Preparation: Silicon p–n Junction Model

Use these as study prompts. Answer in your own words; do not memorize phrases you do not understand.

## 1. What is a p–n junction?
A junction between p-type material (acceptors, holes are majority carriers) and n-type material (donors, electrons are majority carriers). Diffusion after contact leaves fixed ionized dopants near the junction, creating a depletion region and built-in electric field.

## 2. What is the depletion approximation?
It treats the depletion region as containing fixed ionized dopants but negligible mobile carriers. Outside it, the semiconductor is approximated as quasi-neutral. This is an idealization.

## 3. What is built-in potential?
The equilibrium electrostatic potential difference across the junction that arises from carrier diffusion and the resulting electric field. For a non-degenerate abrupt junction, V_bi = (kT/q) ln(NA ND / ni²).

## 4. Why does doping increase built-in potential?
For symmetric doping N_A=N_D=N, V_bi=(kT/q) ln(N²/ni²). Increasing N increases the logarithm, so V_bi rises slowly (logarithmically), within the model's validity.

## 5. Why does depletion width decrease with doping?
W = sqrt[(2 ε/q)(1/NA + 1/ND)V_bi]. Higher doping makes (1/NA+1/ND) smaller. Although V_bi increases, the inverse-doping factor dominates, so W decreases.

## 6. Why is the p-side depletion charge negative and the n-side positive?
The p-side depletion region contains fixed ionized acceptors (negative); the n-side contains fixed ionized donors (positive).

## 7. Why is the electric field linear in each depletion region?
Poisson's equation says dE/dx = ρ/ε. Under uniform doping, ρ is constant on each side, so the field slope is constant and E varies linearly.

## 8. Why are x_p and x_n equal in this example?
The example uses equal doping (NA=ND). Charge neutrality requires NA*x_p=ND*x_n, so equal doping gives equal depletion extensions.

## 9. What does the code validate?
It checks charge neutrality and computes the depletion partition. The field is set to zero at depletion edges by the analytical formula. A good next validation step is to compare results with an independent textbook example or trusted semiconductor reference.

## 10. What are the limitations?
One-dimensional, abrupt, uniformly doped, equilibrium-only, no external bias; complete ionization; non-degenerate statistics; fixed intrinsic concentration. No I–V curve, carrier transport, recombination, quantum effects, or experimental comparison.

## 11. Is this TCAD?
No. It is a small Python implementation of standard analytical depletion-approximation equations. TCAD solves more complete device equations numerically and requires validated models and boundary conditions.

## 12. What would you do next?
Possible extensions: asymmetric doping; reverse-bias depletion width; temperature dependence; compare against a textbook numerical example; or use a validated simulator if access and training are available.
