import sys
# argv = [filename , 5 , 3]

if len(sys.argv) != 3:
    print("Usage: python "+sys.argv[0]+ "<first integer> <second integer>")
    sys.exit()

firstarg =int(sys.argv[1])
secondarg = int(sys.argv[2])
print(firstarg * secondarg)

