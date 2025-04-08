import os
import shutil

folder_name = ""
last_folder_name = ""


animations = ("Attack", "Dead", "Idle", "Jump", "JumpAttack", "Run", "Walk")
files = os.listdir("knight")
print(files)

for f_n in files:
    file_name = f_n.split(".")[0][:-1]
    if file_name[-1].isdigit():
        file_name = file_name[:-1]

    if file_name in animations:
        if not os.path.exists(f"knight/{file_name}"):
            os.mkdir(f"knight/{file_name}")
         
    shutil.move(f"knight/{f_n}", f"knight/{file_name}/{f_n}")
  