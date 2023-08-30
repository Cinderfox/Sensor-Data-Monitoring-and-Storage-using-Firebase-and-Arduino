import firebase_admin
from firebase_admin import db

from firebase_admin import firestore
from firebase_admin import credentials
import serial.tools.list_ports

cred = credentials.Certificate("lms-comms-firebase-adminsdk-oknp7-a5dd828112.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://lms-comms-default-rtdb.asia-southeast1.firebasedatabase.app/"})

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM: ")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        qwe = packet.decode('utf')
        print(qwe)  

        one = db.reference('dy/')
        one.push({"Values" : str(qwe)})

        txt = str(qwe)
        w = txt.startswith("D")
        if w:
            ref = db.reference("py/-NGrxOmYZBsqDXzESjoh/-NGrxakR6-31NEFaXp4w")
            ref.set({"Values" : str(qwe)})

            asd = int(qwe[10:12])
            if asd > 12:
                on_off = db.reference('py/-NGrxOmYZBsqDXzESjoh/-NGrxxGteXI7b9-uZtjv')
                on_off.set({"Values" : "Washing Machine OFF"})
                print("Washing Machine OFF")
            else:
                on_off = db.reference('py/-NGrxOmYZBsqDXzESjoh/-NGrxxGteXI7b9-uZtjv')
                on_off.set({"Values" : "Washing Machine in use"})
                print("Washing Machine ON")


        x = txt.startswith("A")
        if x:
            ref = db.reference("py/-NGrxOmYZBsqDXzESjoh/-NGrxaoiSoaQFwxIa4ry")
            # ref = db.reference("py/")
            ref.set({"Values" : str(qwe)})

            if qwe[18] == '-':
                on_off = db.reference('py/-NGrxOmYZBsqDXzESjoh/-NGrycUm-7jL2TU4Xi4c')
                on_off.set({"Values" : "Washing Machine (Vibration OFF)"})
                print("Vibration OFF")
            if qwe[18] != '-':
                if int(qwe[18]) <= 25:
                    on_off = db.reference('py/-NGrxOmYZBsqDXzESjoh/-NGrycUm-7jL2TU4Xi4c')
                    on_off.set({"Values" : "Washing Machine (Vibration OFF)"})
                    print("Washing Machine (Vibration OFF)")
                if int(qwe[18]) >= 1:
                    on_off = db.reference('py/-NGrxOmYZBsqDXzESjoh/-NGrycUm-7jL2TU4Xi4c')
                    on_off.set({"Values" : "Washing Machine (Vibration ON)"})
                    print("Vibration ON")


        y = txt.startswith("R")
        if y:
            ref = db.reference("py/-NGrxOmYZBsqDXzESjoh/-NGrxaqlWUSuxAVOSdME")
            # ref = db.reference("py/")
            ref.set({"Values" : str(qwe)})


        z = txt.startswith("T")
        if z:
            ref = db.reference("py/-NGrxOmYZBsqDXzESjoh/-NGrxasgxR2JZpRGZsSj")
            # ref = db.reference("py/")
            ref.set({"Values" : str(qwe)})