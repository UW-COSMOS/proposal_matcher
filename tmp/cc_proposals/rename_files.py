import re
import glob 
import shutil
# 56864edacf58f18e60df4c5e.pdf_18 -->56864edacf58f18e60df4c5e_input.pdf-0018
def rename(files, type):
    for file in files:
        split = re.split(".pdf_(\d*)", file)
        num = int(split[1]) - 1
        new_path = f"{split[0]}_input.pdf-{num:0>4}.{type}"
        print(f"{file} --> {new_path}")
        shutil.move(file, new_path)


files = glob.glob("*.png")
rename(files, "png")
files = glob.glob("*.csv")
rename(files, "csv")
