import os
path=input("Enter the path  ")
path=path.replace('\\','/')
if not path.endswith('/'):
    path += '/'
print(path)
print(os.listdir(path))
print("enter the name you want to change")
n=input("")
def main():
    i=1
    for filename in os.listdir(path):
        new_name=path+n +str(i)+'.jpg'
        old_name=path+filename
        os.rename(old_name,new_name)
        i=i+1

main()