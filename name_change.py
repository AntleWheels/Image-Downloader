import os
os.chdir("Directory path")
i=1
for file in os.listdir():
    src =file 
    dst = "new_name"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1