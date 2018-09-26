import os
import filecmp


def check():
    flag = filecmp.cmp("dev", "cur")

    if flag:
        work_func()
    else:
        print("PIRATE!!1")


def work_func():
    print("Working function.")


os.system("sysctl -a hw > /Users/dima/University/07_sem/defence/lab_01/cur")
check()
