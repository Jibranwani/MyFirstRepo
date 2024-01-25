from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import TreeTopo
from mininet.cli import CLI

def create_topology():
    # Create a Mininet instance
    net = Mininet()

    # Create a remote controller
    controller = RemoteController('c0', ip='127.0.0.1', port=6633)

    # Add the controller to the network
    net.addController(controller)

    # Create the tree topology with depth=2 and fanout=8
    topo = TreeTopo(depth=2, fanout=8)

    # Build the network based on the specified topology
    net.buildFromTopo(topo)

    # Start the network
    net.start()

    # Open the Mininet command-line interface for testing
    CLI(net)

    # Stop the network when done
    net.stop()

if __name__ == '__main__':
    create_topology()
