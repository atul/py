#!/usr/bin/python


"""Custom topology script for Mininet

Creates custom tree with parameters depth and fanout (count of childs per parent node) 
Use: mn --custom %PATH to script%/%script_name%.py --topo custom 

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class CustomTopo(Topo):
	
    # fanout - number of child switch per parent switch"
    
    def __init__(self, depth=2, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        #core_switch = self.addSwitch('c1')
        switches = {} #map {depth_level : [list of nodes]}
        hosts = []
        parend_id = 0
        switches[0] = list()
        switches[0].append(self.addSwitch('s1'))

        for s in range(1, depth): #last is host level
            switches[s] = list() #initialize list for dict
            for sw in range(0,fanout**s):
                switch_id = fanout**s+sw
                switches[s].append(self.addSwitch('s%s'%(switch_id)))
                self.addLink(switches[s][-1],switches[s-1][sw//fanout])

        
        for h in range(0, fanout**depth):
            hosts.append(self.addHost('h%s'%(h+1)))
            self.addLink(hosts[-1],switches[depth-1][h//fanout])

                    
topos = { 'custom': ( lambda: CustomTopo(depth=2,fanout=2) ) }  # set params here
