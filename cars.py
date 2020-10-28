#create a modified version of car_game_v.2.0.py
#try to impliment not to start the car twice
#!/usr/bin/env python3.8
#-*- coding: cp1252 -*-
command = ""
started = False 
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
             started = True
             print("start the car engine")
    elif command == "stop":
        if not started:
            print("car is already stoped")
        else:
            started = False
            print("car is stoped")     
    elif command == "quit":
        print("exiting the program")
        break
    else:
        print("""
To start the car 'start'
To stop the car 'stop'
To quit the program 'quit' 
        """)
