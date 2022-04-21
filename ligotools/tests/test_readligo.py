import numpy as np
import ligotools.readligo as rl 

def test_FileList_searchdir():
	hdf5_files = rl.FileList().searchdir('data/')
	assert np.array_equal(hdf5_files, ['data/GW150914_4_template.hdf5','data/H-H1_LOSC_4_V2-1126259446-32.hdf5','data/L-L1_LOSC_4_V2-1126259446-32.hdf5'])

def test_loadfile():
	assert len(rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5','H1')[2]) == 13

def test_dq_channel_to_seglist():
	c = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	assert np.array_equal(rl.dq_channel_to_seglist(c),[slice(0, 131072, None)])

def test_read_hdf5():
	assert rl.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', readstrain=True)[2] == 0.000244140625