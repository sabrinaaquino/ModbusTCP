from pyModbusTCP.server import ModbusServer, DataBank
import time
import random
#Create an instance of ModbusServer
server = ModbusServer("127.0.0.1", 502, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    print("Obs: Para sair do server aperte Ctrl+C\n")
    print("Bem vindo à sua planta industrial")
    while True:
        DataBank.set_words(0, [int(random.uniform(0,100))])
        time.sleep(0.5)
        continue
except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")


