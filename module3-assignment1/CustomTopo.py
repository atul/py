'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 3 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from mininet.topo import Topo
from mininet.topolib import TreeTopo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel


class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=1, depth=1, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Add your logic here ...
        self.depth = depth         
       # print linkopts1
       # print fanout
       # print depth 
        #lastSwitch = None
        #for i in irange(1,depth):
        # host = self.addHost('h%s' %i)
        #mininet.topolib.TreeTopo.addTree( self, depth, fanout=2) 
        
        #self.TreeTopo( depth=3, fanout=2)
       
        coreswitches = ['s1']
        aggreswitches = []
        edgeswitches = []
        hosts = [] 
 
        self.addSwitch ('s1')

        for i in range(1,1+fanout):
            aggreswitches.append('s%s' %(i+1))
            self.addSwitch ('s%s' %(i+1))

        for i in range(1,1+fanout**2):
            edgeswitches.append('s%s' %(i+1+fanout**2))
            self.addSwitch ('s%s' %(i+1+fanout**2))

        for i in range(1,1+fanout**3):
            hosts.append('h%s' %i)
            self.addHost('h%s' %i)

        print fanout**3
        print fanout
       
        for i in range(0,fanout**3):
           self.addLink(edgeswitches[i/fanout], hosts[i], **linkopts3)

        for i in range(0,len(edgeswitches)):
            self.addLink(aggreswitches[i/fanout], edgeswitches[i], **linkopts2)

        for i in range(0,len(aggreswitches)):
            self.addLink(coreswitches[i/fanout], aggreswitches[i], **linkopts1)

 
#        for i in range(1,9) and for j in ('s3','s3','s4','s4','s6','s6','s7','s7'):
#            print edgeswitch1
#            self.addLink('%s' %j, 'h%s' %i)
  
"Core" 
#linkopts1 = dict(bw=50, delay='5ms', loss=0, max_queue_size=1000)
"Aggregation"
#linkopts2 = dict(bw=30, delay='5ms', loss=0, max_queue_size=1000)
"Edge"
#linkopts3 = dict(bw=10, delay='5ms', loss=0, max_queue_size=1000)
                
topos = { 'custom': ( lambda: CustomTopo() ) }

#print topos
#topos = CustomTopo(linkopts1,linkopts2, linkopts3, fanout=2, depth=3)

#topos.nodes

#net = Mininet(topo=topos, link=TCLink)
#net.start()

#net.pingAll()
#print net.topo.nodes()
#net.stop()

