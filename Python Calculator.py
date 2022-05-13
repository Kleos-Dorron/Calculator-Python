while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  
   # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(choice==""):
      print("Something Went Wrong")
  elif(choice=="#"):
    print("Done. Terminating")
    exit()
  else:
    fn=float(0.0)
    sn=float(0.0)
    result=float(0)
    fn = input("Enter first number: ")
    print(fn)
    fn=float(fn)
    sn = input("Enter second number: ")
    print(sn)
    sn=float(sn)
  if(choice=="+"):
    result = float(fn)  + float(sn)
    print('{0} + {1} = {2}'.format(fn, sn, result,))
  elif(choice=="-"):
    result = fn - n
    print('{0} - {1} = {2}'.format(fn, sn, result))
  elif(choice=="*"):
    result = float(fn) * float(sn)
    print('{0} * {1} = {2}'.format(fn, sn, result))
  elif(choice=="/"):
    if(sn==0):
      print("float division by zero")
      result="None"
      print('{0} / {1} = {2}'.format(fn, sn,result))
    elif(sn!=0):
     result = float(fn) / float(sn)
     print('{0} / {1} = {2}'.format(fn, sn, result))
    else:
      print("Reset. Terminating")
  elif(choice=="^"):
    result = float(fn) ** float(sn)
    print('{0} ** {1} = {2}'.format(fn, sn, result))
  elif(choice=="%"):
    result = float(fn) % float(sn)
    print('{0} % {1} = {2}'.format(fn, sn, result))
  else:
    print("Unrecognized operation")
  
