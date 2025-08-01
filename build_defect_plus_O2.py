from ase.io import read, write
from ase import Atoms
import numpy as np

atoms = read("TiO2_clean_supercell.xyz")
print(f"Initial atom count: {len(atoms)}")

cell = atoms.get_cell()
a, b, c = cell.lengths()

target1 = np.array([a / 4, b / 4, c / 4])
target2 = np.array([3 * a / 4, 3 * b / 4, 3 * c / 4])

oxygen_indices = [i for i, atom in enumerate(atoms) if atom.symbol == 'O']
distances = []

for i in oxygen_indices:
    pos = atoms[i].position
    d1 = np.linalg.norm(pos - target1)
    d2 = np.linalg.norm(pos - target2)
    distances.append((d1, d2, i))

idx1 = min(distances, key=lambda x: x[0])[2]
idx2 = min([x for x in distances if x[2] != idx1], key=lambda x: x[1])[2]

del atoms[[idx1, idx2]]
print(f"Removed 2 O atoms. New atom count: {len(atoms)}")

z_max = max([atom.position[2] for atom in atoms])
center_xy = np.mean(atoms.get_positions()[:, :2], axis=0)
bond_length = 1.21  # Approx O–O bond length in Å

o1 = np.array([center_xy[0], center_xy[1], z_max + 2.0])
o2 = np.array([center_xy[0], center_xy[1], z_max + 2.0 + bond_length])
O2 = Atoms('OO', positions=[o1, o2])

atoms += O2.copy()

write("TiO2_defect_plus_O2.xyz", atoms)
print(f"Final atom count: {len(atoms)}")
print("Final structure written to TiO2_defect_plus_O2.xyz")
