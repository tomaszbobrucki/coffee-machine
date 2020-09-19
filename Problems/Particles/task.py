spin = input()
el_charge = input()

if spin == '1/2':
    if el_charge == '-1/3':
        print("Strange Quark")
    elif el_charge == '2/3':
        print("Charm Quark")
    elif el_charge == '-1':
        print("Electron Lepton")
    elif el_charge == '0':
        print("Neutrino Lepton")
else:
    print("Photon Boson")
