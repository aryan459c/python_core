"""read mode(r)"""
file=open("demo.txt","r")
print(file.read())
print(file.read(5))

"""Write Mode"""
var=open(r"file_path","w")
var.write("Aryan")
var.writelines(["alo","rader","Ali lelo","Kanda lelo"])

"""Append mode()"""

var=open(r"file_path","a")
var.write("Water")


"""With (open or close handling)"""
with open("file path","mode") as var,open("fil_path") as var2:
    var.read()
    print(var.closed) #Check File closed or not