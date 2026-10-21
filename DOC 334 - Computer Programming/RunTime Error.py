
try :
    print(value)
except NameError:
    print("name error was captured")
except:
    print("General Captured")
