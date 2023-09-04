import sys
sys.path.append(path to askcos-core-main here) # need to specify installation path for askcos here
from askcos.prioritization.precursors.scscore import *
import sa_score.sascorer as sascorer
from rdkit import Chem
from tqdm import tqdm
import os
import numpy as np


### SA Score

def get_sa_score(smile_string):
    try:
        mol = Chem.MolFromSmiles(smile_string)
        sa_score = sascorer.calculateScore(mol)
        return sa_score
    except:
        return 'ERROR'

def parallel_apply_sa_score(input):
    df, index = input
    fname = f'sa_score_sublists/sa_score_{index}.txt'

    if not os.path.isfile(fname):
        sa_scores = df.apply(get_sa_score).to_numpy()
        np.savetxt(fname,sa_scores,fmt='%s')



### SC Score

def get_sc_score(smile_string,model_obj):
# try:
    sc_score = model_obj.get_score_from_smiles(smile_string, noprice=True)
    return sc_score
# except:
    return 'ERROR'

def parallel_apply_sc_score(input):
    df, index, model = input
    fname = f'sc_score_sublists/sc_score_{index}.txt'

    if not os.path.isfile(fname):
        sa_scores = df.apply(get_sc_score,model_obj=model).to_numpy()
        np.savetxt(fname,sa_scores,fmt='%s')
        
### Syba Score

def get_syba_score(smile_string,syba):
    try:
        syba_score = syba.predict(smile_string)
        return syba_score
    except:
        return 'ERROR'
    try:
        mol = Chem.MolFromSmiles(smi)
        syba_score = syba.predict(mol=mol)
        return syba_score
    except:
        return 'ERROR'

def parallel_apply_syba_score(input):
    df, index, syba = input
    print(f'calculating index {index}')
    syba_scores = df.apply(get_syba_score,syba=syba).to_numpy()
    print(get_syba_score(df.iloc[0],syba))
    fname = f'syba_score_sublists/syba_score_{index}.txt'

    if not os.path.isfile(fname):
        syba_scores = df.apply(get_syba_score,syba=syba).to_numpy()
        np.savetxt(fname,syba_scores,fmt='%s')