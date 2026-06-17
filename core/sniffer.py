from scapy.layers.inet import *
from scapy.sendrecv import *
from scapy.layers.l2 import ARP, Ether
from collections import defaultdict

from Rules.arpSpoofDetect import spoofDetector
from Rules.portscanner import  portScanDetection
from Rules.icmpDetect import process_packet
from Rules.synflood import synFlooder

def process(pack):
    spoofDetector(pack)
    portScanDetection(pack)
    process_packet(pack)
    synFlooder(pack)

def startSniffer():
    sniff(prn=process)