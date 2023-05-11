import pymatgen.core as mg
from pymatgen.ext.matproj import _MPResterLegacy, MPRester as mpr


def get_cif(material_id): 
    with _MPResterLegacy("iZVT66G5iKswixmF") as mprl:
        mpid = mprl.get_data(material_id)
        cif = mpid[0]['cif']
        return cif
