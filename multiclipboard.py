import sys
import clipboard
import json

if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == "save":
        print("save")
    elif command =="load":
        print("load")
    elif command == "list":
        print("load")
    else:
        print("Unknown command")
else:
    print("Please type exactly one command.")
    
    
