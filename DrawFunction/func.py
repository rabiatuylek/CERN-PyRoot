import ROOT
from ROOT import *
from ROOT import gROOT

c1 = ROOT.TCanvas('c1', 'Example with Formula', 200, 10, 700, 500)

form = ROOT.TFormula('form', 'sqrt(abs(x))')
form.Eval(2)
form.Eval(-45)


funct =ROOT.TF1('funct','abs(sin(x)/x)', 0, 10)

c1.SetGridx()
c1.SetGridy()
funct.Draw()
c1.Update()

gROOT.GetListOfCanvases().Draw()
c1.Print("function.pdf")
