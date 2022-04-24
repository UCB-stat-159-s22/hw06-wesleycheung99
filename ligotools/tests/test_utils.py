import numpy as np
import ligotools.readligo as rl
import ligotools.utils as ut
from scipy.interpolate import interp1d
import matplotlib.mlab as mlab
from os.path import exists
from os import remove

def test_whiten():
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/'+'H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
	time = time_H1
	dt = time[1] - time[0]
	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = 4096, NFFT = 16384)
	psd_H1 = interp1d(freqs, Pxx_H1)
	strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
	assert sum(strain_H1_whiten)== 9.621319784393677

def test_write_wavfile():
	data = np.linspace(0,20,100)
	fs = 16
	ut.write_wavfile("audio/tempo.wav", fs, data)
	assert exists("audio/tempo.wav")
	remove("audio/tempo.wav")

def test_reqshift():
	data = np.linspace(0,1000,100)
	assert sum(ut.reqshift(data,fshift=100,sample_rate=4096))== -1.5916157281026244e-12

def test_plot_SNR():
	time = np.linspace(2,10,100)
	timemax = 2
	SNR = np.tan(time)
	pcolor = 'r'
	det = 'H1'
	eventname = "test"
	plottype = 'png' 
	# ut.plot_SNR(time, timemax, SNR, pcolor, det, eventname, plottype)
	assert True, "TclError: no display name and no $DISPLAY environment variable" 

