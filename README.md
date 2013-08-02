sudo dhclient eth1
sudo mn --test pingall --topo single,3
sudo mn --test pingall --topo linear,3
sudo mn --test pingall --topo minimal
sudo mn --test pingall --topo linear,5
sudo mn --test pingall --topo linear,4
xterm -fg green -bg black  &
xterm -fg tan -bg black &
xterm -fg yellow -bg black &

# sudo apt-get install cgroup-bin

