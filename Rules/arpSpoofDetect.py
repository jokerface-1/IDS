from scapy.layers.inet import *
from scapy.sendrecv import *
from scapy.layers.l2 import ARP, Ether
from collections import defaultdict
from alerts import alerts

arp_tabe = defaultdict(set)

def spoofDetector(pack):
    if pack.haslayer(ARP):
            src = pack[ARP].psrc
            mac = pack[ARP].hwsrc
            arp_tabe[src] = mac
            if src not in arp_tabe:
                arp_tabe[src] = mac
            elif arp_tabe[src] != mac:
                alerts(src, "ARP Spoof", "High")
