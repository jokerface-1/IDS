import datetime
import os
import psycopg2

connection = psycopg2.connect(
    dbname="IDS",
    port=5432,
    user="postgres",
    password="jokerface",
    host="localhost"
)
cursor = connection.cursor()
cursor.execute(          
    "INSERT INTO alerts (ip, attack, sevierity) VALUES (%s, %s, %s);",
            ("192.16.0.1", "Icmp Flood", "High"))
connection.commit()
cursor.close()
# def alerts(src, type, sevierity):
    
#     print("The attack possible", type, "from", src, "sevierity", sevierity)
    
#     if os.path("/home/ajay/IDS/logs/data.log"):
#         with open("/home/ajay/IDS/logs/data.log", 'w') as f:
#             f.write(f"The source{src}Attack type{type} sevierity{sevierity} time{datetime.datetime.now()}\n")
    
#     else :
#         with open("/home/ajay/IDS/logs/data.log", 'a') as f:
#             f.write(f"The source{src}Attack type{type} sevierity{sevierity} time{datetime.datetime.now()}\n")

