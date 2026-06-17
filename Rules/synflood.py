from scapy.layers.inet import *
from scapy.sendrecv import *
from collections import defaultdict
from alerts import alerts

syncounter = defaultdict(int)
def dropOutBound(pack):
    if pack.haslayer(TCP):
            return pack[Ether].src != "00:0c:29:ba:77:5b"

def synFlooder(pack):
      if pack.haslayer(TCP) and pack[TCP].flags == "S":
        src = pack[IP].src
        dport = pack[TCP].dport 
        key = (src, dport)   
        syncounter[key] += 1
        if syncounter[key] > 10:
             alerts(src, "SynFlood", "High") 
