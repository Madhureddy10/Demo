def name(first_name,last_name):
    full_name=[]
    n=len(first_name)
    if (len(first_name)==len(last_name)):        
        for i in range(n):
                full_name.append(first_name[i]+" "+last_name[i])
    print(full_name)
def append_name():
    length=int(input())
    first_name=list()
    last_name=list()
    for i in range(length):
        first_name.append(input("enter first name:"))
        print("\n")
        last_name.append(input("enter last name:"))
        print("\n")
    name(first_name,last_name)

if __name__ == "__main__":
    append_name()
