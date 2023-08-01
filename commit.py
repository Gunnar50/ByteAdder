import os
import random

for i in range(1, 5):
    for _ in range(random.randint(0, 10)):
        with open("test.txt", "a") as file:
            file.write("test")
        os.system("git add .")
        os.system(f"git commit --date='2023-08-0{i} -m 'testing'")
    
os.system("git push")
