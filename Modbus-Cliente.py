from pyModbusTCP.client import ModbusClient
import time

#Create an instance of ModbusSClient
client = ModbusClient(host="localhost", port=502, auto_open=True)

client = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=True)

client = ModbusClient()
client.host("localhost")
client.port(502)

# The function write_single_register is used to write a single
# holding register in a remote device.

led = client.write_single_register(1,0)
controler = client.write_single_register(2,0)
valvula = client.write_single_register(3,0)
alarm = client.write_single_register(4,0)

while True:
    client.open()
    # The function read_holding_registers() is used to 
    # read the binary contents of holding registers in the slave.
    led = client.read_holding_registers(1)
    controler = client.read_holding_registers(2)
    valvula = client.read_holding_registers(3)
    alarm = client.read_holding_registers(4)
    print("Para verificação digite 1")
    print("Para alteração do estado dos dispositivos digite 2")
    t=int(input("Digite o número equivalente: "))
    if t == 1:
        print("\nQual o dispositivo que você quer verificar?")
        print("LED: 1")
        print("Controlador de nível de fluidos: 2")
        print("Válvula:  3")
        print("Alarme: 4")
        ans = int(input("Digite o número equivalente: "))
        if ans == 1:
            print("\nVocê escolheu LED:")
            if led[0] == 1:
                print("\nLED Ligado")
            elif led[0] == 0:
                print("\nLED Desligado")
        elif ans == 2:
            print("\nVocê escolheu Controlador de nível de fluidos \n")
            if controler[0] == 0:
                print("\nNível mínimo")
            elif controler[0] < 5:
                print("\nMenos de 50% da capacidade")
            elif controler[0] >= 5 and controler[0] < 8:
                print("\nEntre 50% e 80% da capacidade")
            elif controler[0] >=8 and controler[0] < 10:
                print("\nQuase 100% da capacidade")
            elif controler[0] == 10:
                print("\nNivel máximo")
        elif ans == 3:
            print("\nVocê escolheu Válvula \n")
            if valvula[0] == 1:
                print("\nVálvula aberta")
            elif valvula[0] == 0:
                print("\nVálvula fechada")
        elif ans == 4:
            print("\nVocê escolheu Alarme \n")
            if alarm[0] == 1:
                print("\nALARME LIGADO")
            elif alarm[0] == 0:
                print("\nAlarme desligado")
                
    elif t == 2:
        print("\nQual o dispositivo que você quer alterar?")
        print("LED: 1")
        print("Controlador de nível de fluidos: 2")
        print("Válvula:  3")
        print("Alarme: 4")
        ans = int(input("Digite o número equivalente: "))
        if ans == 1:
            print("\nVocê escolheu LED:")
            l = int(input("Para Ligar: 1, Para Desligar: 0: "))
            if l == 1:
                client.write_single_register(1,1)
                print("LED ligado")
            elif l == 0:
                client.write_single_register(1,0)
                print("LED Desligado")
        elif ans == 2:
            print("\nVocê escolheu Controlador de nível de fluidos \n")
            c = int(input("Escolha o nível para o tanque de 0 a 10: "))
            client.write_single_register(2,c)
            print("Nível do tanque: ", c)
        elif ans == 3:
            print("\nVocê escolheu Válvula \n")
            v = int(input("Para Ligar: 1, Para Desligar: 0: "))
            if v == 1:
                client.write_single_register(3,1)
                print("Válvula ligada")
            elif v == 0:
                client.write_single_register(3,0)
                print("Válvula Desligada")
        elif ans == 4:
            print("\nVocê escolheu Alarme \n")
            a = int(input("Para Ligar: 1, Para Desligar: 0: "))
            if a == 1:
                client.write_single_register(4,1)
                print("Alarme ligado")
            elif a == 0:
                client.write_single_register(4,0)
                print("Alarme Desligado")
    
    if controler[0] >= 8:
        # Setting alarm to One
        client.write_single_register(4,1)
    else:
        # Setting alarm to Zero
        client.write_single_register(4,0)
    if controler[0]==10:
        # CONTROLER FULL
        # Setting LED to Zero
        client.write_single_register(1,0)
        # Setting Valvula to One
        client.write_single_register(3,1)
	
    if controler[0]==0:
        # Setting Valvula to Zero
        client.write_single_register(3,0) 
    time.sleep(2)
