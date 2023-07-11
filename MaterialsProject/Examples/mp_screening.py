#Basic example for ZnO cif files

from pymatgen.ext.matproj import _MPResterLegacy

# api key from Materials Project
api_key = "**************"

# criterias to query the materials
entries = _MPResterLegacy(api_key).query(
    criteria={"elements": ("Zn", "O"), "nelements": {"$gte": 2}},
    properties=["material_id", "pretty_formula", "spacegroup"],
)

# stocking information
mp_ids = [e["material_id"] for e in entries]
pretty_fomula = [e["pretty_formula"] for e in entries]
symbol = [e["spacegroup"]["symbol"] for e in entries]

# pandas DataFrame visualization
df = pd.DataFrame({"material_id":mp_ids,"formula":pretty_fomula,"spacegroup_symbol":symbol})
df

#########################################################################################################################################

#This method can be used for \textbf{High Throughput} calculation by performing screening to collect the CIF file for a certain type of material. 
#The number and type of criteria and properties can be changed and adapted in function of the searched material type. 
#For example, a more advanced type of screening to collect the material id for Ultrawide Bandgap materials is given below. 


# Database search criteria
criteria = {'nelements':{'$in': [3]},            # Only ternary materials
            'band_gap':{'$gte': 4, '$lte': 12},  # Bandgap is between 4 and 12 (gte >= and lte <=)
            'elements':{'$in':elements},         # Allowed elements list 
            '$where':'this.icsd_ids.length>0',   # Has entry in ICSD
            'band_gap.search_gap.is_direct': {'$eq': True}, # Direct bandgap
            'has_bandstructure':{'$eq': True}    # Band structure was calculated
           } 

# Searched properties
properties =['material_id', 'icsd_ids', 'pretty_formula','elements', 'band_gap','formation_energy_per_atom', 'e_above_hull', 'spacegroup']
