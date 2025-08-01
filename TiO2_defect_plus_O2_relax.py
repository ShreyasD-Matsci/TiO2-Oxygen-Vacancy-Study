from ase.io import read

atoms = read("TiO2_defect_plus_O2.xyz")

with open("TiO2_defect_plus_O2_relax.in", "w") as f:
    f.write("&control\n")
    f.write("  calculation = 'relax',\n")
    f.write("  prefix = 'TiO2_defect_O2',\n")
    f.write("  outdir = './tmp',\n")
    f.write("  pseudo_dir = './',\n")
    f.write("  verbosity = 'high',\n")
    f.write("/\n\n")

    f.write("&system\n")
    f.write(f"  ibrav = 0,\n")
    f.write(f"  nat = {len(atoms)},\n")
    f.write("  ntyp = 2,\n")
    f.write("  ecutwfc = 30,\n")
    f.write("  ecutrho = 240,\n")
    f.write("  occupations = 'smearing',\n")
    f.write("  smearing = 'mv',\n")
    f.write("  degauss = 0.01,\n")
    f.write("/\n\n")

    f.write("&electrons\n")
    f.write("  conv_thr = 1.0d-6,\n")
    f.write("  mixing_beta = 0.7,\n")
    f.write("/\n\n")

    f.write("&ions\n")
    f.write("  ion_dynamics = 'bfgs',\n")
    f.write("/\n\n")

    f.write("ATOMIC_SPECIES\n")
    f.write("Ti  47.867  Ti.upf\n")
    f.write("O   15.999  O.upf\n\n")

    f.write("CELL_PARAMETERS angstrom\n")
    for v in atoms.get_cell():
        f.write(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
    f.write("\n")

    f.write("ATOMIC_POSITIONS angstrom\n")
    for atom in atoms:
        f.write(f"{atom.symbol} {atom.position[0]:.6f} {atom.position[1]:.6f} {atom.position[2]:.6f}\n")
    
    f.write("\nK_POINTS automatic\n")
    f.write("2 2 2 0 0 0\n")
