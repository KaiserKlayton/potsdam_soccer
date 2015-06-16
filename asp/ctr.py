#script (python)

from gringo import *
from pprint import pprint

def onModel(model):
    atoms = model.atoms(Model.ATOMS)
    events = getFluents(atoms, "ticker")
    states = getFluents(atoms, "holds" )
    for time in range(len(states)):
        print "{}".format(time)
        if time in events:
            for e in events[time]:
                print "[e]  {}".format(e)
        print "[s] "
        for s in states[time]:
            print "     {}".format(s)

def getFluents(atoms, name):
    fluents = {}
    for (lit,time) in [atom.args() for atom in atoms if atom.name() == name]:
        if time not in fluents:
            fluents[time] = [lit]
        else:
            fluents[time].append(lit)
    return fluents

def main(ctr):
    ctr.ground([("base", [])])
    ret = ctr.solve([], onModel)

#end.
