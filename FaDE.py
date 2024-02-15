# FaDE (file and dictionary eradicator)
import os
import time
import shutil
import stat
from alive_progress import alive_bar
from git import Repo
try:
    with alive_bar(total=1,bar="filling",title="updating program",calibrate=1) as bar:
        os.remove("C:\\Users\\manji\\Downloads\\FaDE")
        Repo.clone_from("https://github.com/err0404/python-krish.git","C:\\Users\\manji\\Downloads\\FaDE")
        bar.text("this should take 1 sec")
        bar()
except Exception as e:
    print(f"error{e}")
    input("press any key to continue")


try:
    dic = input("enter dictionary name:")
    files = os.listdir(dic)
    print("\nfiles found:", len(files))
    print(f"files={files}\n")
    count = 0
    fail_count = 0

    tim = float(input("time (in seconds):"))
    tim = tim / len(files)


    print("DANGER: ALL files will NOT be put in the RECYCLING BIN")

    input("press enter to start")
    with alive_bar(total=len(files),bar="filling",title="eradicator",calibrate=1) as bar:
        for file in range(len(files)):
            sel_file = files[file]
            file_path = os.path.join(dic, sel_file)
            time.sleep(tim)
            try:
                if os.path.isdir(file_path):
                    os.chmod(file_path, stat.S_IWRITE)
                    if os.path.exists(file_path):
                        shutil.rmtree(file_path,)
                        if not os.path.exists(file_path):
                            count += 1

                elif os.path.isfile(file_path):
                    os.chmod(file_path,stat.S_IWRITE)
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        if not os.path.exists(file_path):
                            count += 1
                bar()

            except Exception as e:
                fail_count += 1


    print(f"\nfailed to delete: {fail_count}\nsuccessfully eradicated: {count}")

    input("press any key to close")

except Exception as e:
    print(f"error{e}")
    input()