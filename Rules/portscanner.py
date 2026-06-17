from scapy.layers.inet import *
from scapy.sendrecv import *
from collections import defaultdict
from alerts import alerts

portScan = defaultdict(list)

def filterTheIncomming(pack):
      if pack.haslayer(TCP):
            return pack[Ether].src != "00:0c:29:ba:77:5b"

def portScanDetection(pack):
    if pack.haslayer(TCP) and pack[TCP].flags == "S":
            dports = pack[TCP].dport
            portScan[dports] = dports
            if(len(portScan) > 10):
                alerts(pack[IP].src, 
                       "PortScan", "High")
print(len(portScan))
