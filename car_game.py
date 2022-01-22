#code with a lot of repetation of .lower()
#command=""
#while command.lower() !="quit":
#    command = input(">")
#    if command.lower()=="start":
#       print("Car =False...")
#    elif command.lower()=="stop":
#      print("Car stopped")
#    elif command =="help":
 #        print("""
  #           start - to start the car
   #          stop - to stop the car
  #           quit - to quit
   #      """")
  #  else:print("I don't understand this")
#

#dry dont repeat yourself

#code without a lot of repetation of .lower()
command=""
started=False
while  True: #command !="quit":
     command = input(">").lower()
     if command=="start":
         if started:
             print("Car already started!")
         else:
             started=True
             print("Car Started...")
     elif command=="stop":
         if not started:
            print("Car is already stopped")
         else:
             started=False
             print("Car stopped")

     elif command =="help":
         print("""
start - to start the car
stop - to stop the car
quit - to quit
                """)
     elif command =="quit":
         break
     
     else:
        print("I don't understand this")


