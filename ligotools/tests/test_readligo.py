import numpy as np
from ligotools.readligo import FileList, loaddata

def test_FileList_searchdir():
	hdf5_files = FileList().searchdir('data/')
	assert np.array_equal(hdf5_files, ['data/GW150914_4_template.hdf5','data/H-H1_LOSC_4_V2-1126259446-32.hdf5','data/L-L1_LOSC_4_V2-1126259446-32.hdf5'])

