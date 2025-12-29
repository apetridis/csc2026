#!/usr/bin/env python3

import ROOT

def main():
    f = ROOT.TFile("data/sample.root", "RECREATE")
    t = ROOT.TTree("Events", "Sample event tree")

    n = ROOT.std.vector("int")()
    energy = ROOT.std.vector("float")()

    t.Branch("n", n)
    t.Branch("energy", energy)

    for i in range(1000):
        n.clear()
        energy.clear()

        # 100 particles per event
        for p in range(100):
            n.push_back(p)
            energy.push_back(0.1 * p)

        t.Fill()

    t.Write()
    f.Close()
    print("Wrote data/sample.root")

if __name__ == "__main__":
    main()

