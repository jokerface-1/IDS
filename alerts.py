import datetime
import os

def alerts(src, type, sevierity):
    
    print("The attack possible", type, "from", src, "sevierity", sevierity)
    
    if os.path("/home/ajay/IDS/logs/data.log"):
        with open("/home/ajay/IDS/logs/data.log", 'w') as f:
            f.write(f"The source{src}Attack type{type} sevierity{sevierity} time{datetime.datetime.now()}\n")
    
    else :
        with open("/home/ajay/IDS/logs/data.log", 'a') as f:
            f.write(f"The source{src}Attack type{type} sevierity{sevierity} time{datetime.datetime.now()}\n")