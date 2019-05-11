from os import listdir

ROOT = "/code/src/deep-puppets/data/"

def main():
    dirs = [f for f in listdir(ROOT)]
    txt = open("input.txt", "w")
    for d in dirs:
        txt.write(ROOT + d + "/frame.jpg\n")
    txt.close()


if __name__ == "__main__":
    main()

