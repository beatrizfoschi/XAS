# get info about e_edge, e_fermi, Z from output fdmnes file

from larch.io import read_ascii 

# group = read_ascii("path/to/file")

def read_fdmnes(group):

    with open(group.path) as f:
        line = f.readline()
        header = (line.split())
        e_edge, Z,  e_fermi,  = (float(header[0]),float(header[1]),float(header[6]))
        print(f'Calculated Fermi level: {e_fermi}\nAtomic_number: {Z}\nEnergy_edge: {e_edge}')

        group.e_edge = e_edge
        group.Z = Z
        group.e_fermi = e_fermi
    
    return group
