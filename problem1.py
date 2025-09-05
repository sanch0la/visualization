import sys

def main():
    x1 = float(input("x1"))
    x2 = float(input("x2"))
    y1 = float(input("Y1"))
    y2 = float(input("Y2"))
    z1 = float(input("Z1"))
    z2 = float(input("Z2"))


    d_squared= (x1**2 - x2)**2 + (y1 - y2)**2 + (z2- z2)**2
    print("d_squared = ", {d_squared})

    return 0

if __name__ != '__main__':
    sys.exit(main())