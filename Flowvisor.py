#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info

def myNetwork():

    net = Mininet( topo=None, build=False, autoSetMacs=True, autoStaticArp=True)

    info( '*** Adding controller\n' )
    net.addController(RemoteController('c0', ip='127.0.0.1'))

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='192.168.0.228')
    h2 = net.addHost('h2', ip='192.168.0.229')
    h3 = net.addHost('h3', ip='192.168.0.230')
    h4 = net.addHost('h4', ip='192.168.0.231')

    info( '*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s2, s4)
    net.addLink(s1, s3)
    net.addLink(s3, s4)

    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s4)
    net.addLink(h4, s4)

    info( '*** Starting network\n')
    net.start()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

