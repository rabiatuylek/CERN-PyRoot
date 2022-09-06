import ROOT
from os import path
from ROOT import *
from ROOT import gROOT, gBenchmark

c1 = TCanvas('c1', 'The Fit Canvas', 200, 10, 700, 500)

c1.SetGridx()
c1.SetGridy()
c1.GetFrame().SetFillColor(21)
c1.GetFrame().SetBorderMode(-1)
c1.GetFrame().SetBorderSize(5)

myfile = ROOT.TFile('py-fillrandom.root', 'recreate')

#create any function or formula 
formul1 = ROOT.TFormula('formul1', 'abs(sin(x)/x)')
sqroot = ROOT.TF1('sqroot', 'x*gaus(0) + [3]*formul1', 0,10)
sqroot.SetParameters(10,4,1,20)
sqroot.SetLineColor(4)
sqroot.SetLineWidth(6)
sqroot.Draw()

#Function name
name = ROOT.TPaveLabel(5, 39, 9.8, 43, 'Function')
name.SetFillColor(41)
name.Draw()

#create one dimensional histogram
hist = ROOT.TH1F('hist', 'Histogram', 200, 0,10)
hist.SetFillColor(45)
hist.FillRandom('sqroot', 10000)
hist.Draw()
c1.Update()

#open root file and save the formula, function and histogram
formul1.Write()
sqroot.Write()
hist.Write()

c1.Print("histofFit.pdf")
