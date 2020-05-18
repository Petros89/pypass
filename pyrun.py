import sys
import os
import subprocess

def main_default():
    list = ["test0", "test1"]

    for file in list:
            print("Execute: %s" % file)
            process = subprocess.Popen("./" + file, shell=False)
            process.wait()


def main():

    if os.getcwd() != " ":
        print("\n")
        print("---------------------------------------------")
        print(" *** Execution of list <testlist> begins *** ")
        print("---------------------------------------------")
        print("     Work Dir: %s" % os.getcwd())
        print("---------------------------------------------")
        print("\n")
    else:
        return False

    listfile = "testlist"

    with open(listfile, "r") as list:
        for line in list:
            line = line.strip()
            print("Execute: %s" % line)
            process = subprocess.Popen("./" + line, shell=False)
            process.wait()


if __name__ == '__main__':

    main()
    print("\n")
    print("---------------------------------------------")
    print("Execution of list finished")


    #main_default()
