import os
import random

month = "07"
start_day = 2
end_day = 8

for day in range(start_day, end_day+1):
    if random.randint(0, 1) == 0:
    
        if day < 10:
            day = f"0{day}"
        
        for _ in range(random.randint(3, 10)):
            with open("test.txt", "a") as file:
                file.write("test\n")
            os.system("git add .")
            os.system(f"git commit --date='2023-{month}-{day} -m 'testing'")
    
os.system("git push")
