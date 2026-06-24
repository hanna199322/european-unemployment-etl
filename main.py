import os

os.system("py extract.py")
os.system("py transform.py")
os.system("py load.py")
os.system("py queries.py")

print("Pipeline completed successfully")