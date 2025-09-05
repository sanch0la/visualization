import sys

def main():
      name = input("Enter your name: ")
      if name != str.capitalize():
          print ("ungrammatical")
      else:
          print("Hello " + name)

          return 0

      if __name__ == "__main__":
         sys.exit(main())