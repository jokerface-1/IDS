from scapy.layers.inet import *
from scapy.sendrecv import *
from collections import defaultdict
from alerts import alerts
floodCount = defaultdict(int)
ips = defaultdict(set)
seconds = time.time()
secpass = time.localtime(seconds)


def process_packet(pack):
    if pack.haslayer(ICMP):
        if pack[ICMP].type == 8:
            src = pack[IP].src
            floodCount[src] += 1
            if floodCount[src] > 10 :
                alerts(
                    src, "ICMP Ping", "High"
                )

