import ROOT
import math

ROOT.gStyle.SetPadGridX(True)
ROOT.gStyle.SetPadGridY(True)
ROOT.gStyle.SetOptStat("e")
ROOT.gStyle.SetStatX(0.9)
ROOT.gStyle.SetStatY(0.9)


#part1
#  create a histogram and fill it with random number.
#  then write out to a root file.


#Functions for Fitting

class myGaus_with_bg:
    def __call__(self, t, par):
        a = par[0]  #amplitude
        c = par[1]  #center
        s = par[2]  #sigma
        b = par[3]  #bg
        x = t[0]
        tmp = -1.*(x-c)*(x-c)/2. /(s*s)
        return a * math.exp( tmp ) + b
        

class myGaus:
    def __call__(self,t,par):
        a = par[0] #amplitude
        c = par[1]
        s = par[2]
        x = t[0]
        tmp = tmp = -1.*(x-c)*(x-c)/2. /(s*s)
        return a * math.exp( tmp )
        
        
c1 = ROOT.TCanvas('c1', 'canvas title')
# name: c1, title: canvas title

f = ROOT.TFile('my.root', 'recreate')

h1 = ROOT.TH1F('h1','histogram; x axis; y axis', 100, 0, 100)
h2 = ROOT.TH1F('h2','histogram; x axis; yaxis',100,0,100)

#Fill the Random Numbers
center = 0.1
sigma = 0.5

for i in range(10000):
    g = ROOT.gRandom.Gaus(center, sigma)
    k = ROOT.gRandom.Uniform(-3,3)
    h1.Fill(g)
    h2.Fill(g); h2.Fill(k)
    
    
# Draw the histogram into the canvas.
h2.Draw()
h1.Draw("same")
c1.Update()
c1.Print("basic2.pdf")

h1.Write()
