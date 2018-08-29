
#import sys
#print sys.path
import railways, railways.railwaysDA as DA,railways.railwaysBL as Bl
#print dir()

DA.loadtrains()
DA.loadusers()
DA.loadusersinroles()

print Bl.get_trains('Ghazipur','Delhi')