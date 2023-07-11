import pymatgen.core as mg
from pymatgen.ext.matproj import _MPResterLegacy, MPRester as mpr

def get_info(material_id):
    """
    Get the cif file from a given material using Materials Project Legacy database
    ---------------------------------------------------------
    material(str): material_id from Materials Project
    """
    with _MPResterLegacy("************") as mprl:
        mpid = mprl.get_data(material_id)
        cif = mpid[0]['cif']
        icsd_ids = mpid[0]['icsd_ids']
        space_group = mpid[0]['spacegroup']
        formula = mpid[0]['pretty_formula']
        info = {f'{material_id}':{'formula': f'{formula}', 'icsd_ids':f'{icsd_ids}', 'cif': f'{cif}', 'spacegroup': f'{space_group}'}}
        return info
        


def get_cif(material_id): 
    with _MPResterLegacy("*************") as mprl:
        mpid = mprl.get_data(material_id)
        cif = mpid[0]['cif']
        return cif
