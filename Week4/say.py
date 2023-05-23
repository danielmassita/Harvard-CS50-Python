import sys
from sayings import hello, goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])

#hello, world
#goodbye, world
#hello, Daniel

# The problem is that the import from hello.py, main() was called and we saw the basic main hello world and goodbye.
# That's why we use from the importer file ('sayings.py')

# if __name__ == "__main__":
#    main()