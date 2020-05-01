import os
import shutil

MAIN_DIR = r'C:\Users\tmizrachi\Data\Alamogordo\books'

os.chdir(MAIN_DIR)

for i in os.listdir():
    try:
        os.mkdir(i.split(" - ")[0])
    except:
        FileExistsError
        pass

for i in os.listdir():
    if not i.endswith("pdf"):
        continue
    cat = i.split(" - ")[0]
    if i.split(" - ")[0] in os.listdir():
        shutil.move(f"{MAIN_DIR}\\{i}", f"{MAIN_DIR}\\{cat}")
