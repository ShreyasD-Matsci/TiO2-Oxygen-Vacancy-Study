from ase.build import bulk, make_supercell
from ase.io import write
import numpy as np
from ase.lattice.tetragonal import Rutile

#lattice constants (Source: https://next-gen.materialsproject.org/materials/mp-2657)
a = 4.594
c = 2.958
unit = Rutile('TiO2', latticeconstant=(a, c))

P = np.diag([2, 3, 3])
supercell_54 = make_supercell(unit, P)

P_clone = np.diag([2, 1, 1])  #repeating along x
supercell_108 = make_supercell(supercell_54, P_clone)

z_max = max([atom.position[2] for atom in supercell_108])
center_xy = np.mean(supercell_108.get_positions()[:, :2], axis=0)

print(f"Supercell shape after duplication: {supercell_108.get_cell().lengths()}")
print(f"Final atom count: {len(supercell_108)}")
print(f"z_max: {z_max:.3f}, center_xy: ({center_xy[0]:.3f}, {center_xy[1]:.3f})")

write("TiO2_clean_supercell.xyz", supercell_108)
print("Saved to TiO2_clean_supercell.xyz")
