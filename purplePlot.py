#!/usr/bin/env python
from ROOT import *
from purplePlot_tools import *
from collections import OrderedDict


### List samples here.
samples = OrderedDict()
samples["10 TeV"] = {"name":"10 TeV Z'", "filename":"pp_Zprime_10TeV_ttbar"}
samples["15 TeV"] = {"name":"15 TeV Z'", "filename":"pp_Zprime_15TeV_ttbar"}

samples["jj 10000_15000"]  = {"name":"10-15 TeV QCD dijet",  	"filename":"pp_jj_M_10000_15000"}
samples["tt 10000_15000"]  = {"name":"10-15 TeV ttbar",  	"filename":"pp_tt_M_10000_15000"}
samples["vv 10000_15000"]  = {"name":"10-15 TeV VV",  		"filename":"pp_vv_M_10000_15000"}


### List any variables you want to use or manipulate here.
variables = [
			'Jet1_eta',
			'Jet2_eta',
			'Jet1_pt',
                        'Jet2_pt',
			'zPrimeReconstructedMass',
]


### List plots here. Make sure the variables used are the same as the ones listed above. For example: Jet1_eta ==> v['Jet1_eta']
### This is so you can manipulate the variables instead of having to rerun heppy to do something. :/
plots = OrderedDict()
plots["eta difference"] = {	"title":"\Delta eta", 
                           	"output":"eta.png", 
                           	"xlabel":"", 
                           	"ylabel":"count", 
                           	"bin":50, 
                           	"xmin":0, 
                           	"xmax":10, 
                           	"content":"abs( v['Jet1_eta'] - v['Jet2_eta'] )"
			  } 
plots["z prime mass"]   = {	"title":"Z\' Reconstructed Mass",
				"output":"mass.png",
				"xlabel":"TeV",
				"ylabel":"count",
				"bin":50,
				"xmin":10,
				"xmax":15,
				"content":"v['zPrimeReconstructedMass']/1000."
			  }	
			
				
### Are we saving these plots? True == yes, saving
save_bool = True
### Where are we saving the plots?
save_location = "plots"
### Where do the heppy files come from?
heppy_location = "/eos/user/r/rasmith/fcc_v01/Zprime_tt/hadronic_bdtQCD"
### What is the analysis name?
analysis_name = "FCChhAnalyses.Zprime_tt"
### Number of events to run over per sample? Give "all" or a number:
num_events = 10000
### Define any cuts you want.
cuts = "v['Jet1_pt'] > 2800. and v['Jet2_pt'] > 2800. and abs(v['Jet1_eta']) < 3. and abs(v['Jet2_eta']) < 3."


### Now make the plots!
Draw(samples, variables, plots, heppy_location, analysis_name, save_location, save_bool, num_events, cuts)



