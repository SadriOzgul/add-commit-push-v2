import os
import sys

print("testing")
numOfArgs = len(sys.argv)
print("Total Arguements Passed: ", numOfArgs)
message = "Update files"
if numOfArgs == 3:
  if sys.argv[1] == "-m":
    print("Number of args = 3 and p2 = -m")
    message = sys.argv[2]

print(message)



print("Add Commit Push")
print("\ngit status")
os.system("git status")

force = False
for x in range(len(sys.argv)):  
   if sys.argv[x] == 'f':
      force = True


#w3c schools code lines4-6.
if force == False:
    print("Do you want to continue with add commit push? (y):")
    confirm = input()
    if confirm != "y":
        print("Canceling ", confirm)
        quit()

print("\ngit add -A")
os.system("git add -A")

commitStatement = '\ngit commit -m "' + message + '"'
print(commitStatement)
os.system(commitStatement)

print("\ngit push")
os.system("git push")
