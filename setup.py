

def Return_requires(filename) :
    with open(filename , "r") as f :
        requires =  []
        data = f.readlines()
        requires = [i.replace("/n" , "") for i in data ]
    
    return requires


print(Return_requires("requirements.txt"))