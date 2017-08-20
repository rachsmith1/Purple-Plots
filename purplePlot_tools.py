#!/usr/bin/env python
from ROOT import *
from collections import OrderedDict

def Draw(samples, variables, plots, heppy_location, analysis_name, save_location, save_bool, num_events, cuts):

	### Write the opening monologue.
	print ""
	print "######## START ########"
        print "Heppy trees come from: " + heppy_location
	print ""

        print "Running over the following samples: "
	for sample in samples:
		print "... " + samples[sample]["name"]
	print ""

	if save_bool:
		print "YES, we are saving!"
		print "Save location: " + save_location
	else:
		print "NO, we are NOT saving!"	
	print ""

	### Make plots.
	print "######## START MAKING PLOTS ########"
	print ""
	for plot in plots:
		print "Plot: " + plots[plot]["title"]
		print "######## START FILLING HISTOGRAMS ########"

		### Define histograms.
		histogram = OrderedDict()
		for sample in samples:
			histogram[sample] = TH1D(sample+"_"+plot, sample+"_"+plot, plots[plot]["bin"], plots[plot]["xmin"], plots[plot]["xmax"]) 		
			histogram[sample].SetDirectory(0)

		### Fill histograms.
		for sample in samples:
			rootFile = TFile(heppy_location+"/"+samples[sample]["filename"]+"/heppy."+analysis_name+".TreeProducer.TreeProducer_1/tree.root","read")
			tree = rootFile.Get("events")
			num = 0
			if num_events=="all":
				num = tree.GetEntries()
			else:
				num = num_events
			
			print samples[sample]["name"]
			for entry in xrange(num):
                        	tree.GetEntry(entry)
				if entry%1000==0: print "... {}/{}".format(entry, num)	

				v = {}
				for variable in variables:
					v[variable] = getattr(tree, variable)	
				
				if eval(cuts): histogram[sample].Fill(eval(plots[plot]["content"]))
			
		print ""

		### Draw (and save) canvases.
		canvas = TCanvas(plot, plot, 900, 600)
	        canvas.SetLeftMargin(0.12)
        	canvas.SetRightMargin(0.25)

		inputColorStart = 0
		gStyle.SetOptStat(0000000)
		gStyle.SetPalette(kCandy) #IT DOESN'T HAVE TO BE PURPLE!!!!!!!!!!!!!
		inputColorIter = int(gStyle.GetNumberOfColors()/len(samples))

		leg = TLegend(0.78,0.5,0.97,0.88)
		leg.SetLineColor(0)
		leg.SetFillColor(0)

		ths = THStack("ths",plots[plot]["title"])

		for sample in samples:
			NBins = histogram[sample].GetSize() - 2 #minus underflow and overflow bins
			leg.AddEntry(histogram[sample],samples[sample]["name"])
			histogram[sample].SetLineColor(gStyle.GetColorPalette(inputColorStart))
			histogram[sample].SetLineWidth(4)
			ths.Add(histogram[sample])
			inputColorStart+=inputColorIter

		ths.Draw("nostack")
		ths.GetYaxis().SetTitle(plots[plot]["ylabel"])
		ths.GetXaxis().SetTitle(plots[plot]["xlabel"])
		ths.GetYaxis().SetTitleOffset(1.4)
		ths.Draw("nostack")
		leg.Draw("same")

		if (save_bool):
			canvas.SaveAs(save_location + "/" + plots[plot]["output"])

	print "######## FINISH ########"

	


