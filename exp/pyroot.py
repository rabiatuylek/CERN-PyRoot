from ROOT import *

#create histogram with Pyroot
h1 = TH1F("h1", "Random Numbers",200, -5,5)
h1.FillRandom("gaus") #randomly

c1 = TCanvas()
h1.Draw()

#input()    #to show histogram on screen

c1.Print("c1.pdf")  # evince c1.pdf (open pdf on terminal)
