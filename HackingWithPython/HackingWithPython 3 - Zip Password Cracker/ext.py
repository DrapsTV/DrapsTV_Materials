import zipfile, threading, time, os, platform
Clear_Screen = "cls" if (platform.system() == "Windows") else "clear"
 
def Main():
    os.system(Clear_Screen)
    Archive = str(input("What is the file name and extension of the ZIP archive? "))
    if (os.path.isfile(Archive) == False):
        NotExist(Item = "Archive")
    Dictionary = str(input("What is the file name and extension of the password dictionary? "))
    if (os.path.isfile(Dictionary) == False):
        NotExist(Item = "Dictionary")
    List = open(Dictionary)
    Archive_Zip = zipfile.ZipFile(Archive)
    Start = time.time()
    for line in List.readlines():
        Password = line.strip('\n\r')
        t = threading.Thread(target=Attempt, args=(Archive_Zip, Password))
        t.start()
 
def Attempt(Archive_Zip, Password):
    try:
        Archive_Zip.extractall(pwd=bytes(Password, "UTF-8"))
        Cracked(Password)
    except:
        print("The password is not " + Password + ".\n")
        pass
 
def NotExist(Item):
    os.system(Clear_Screen)
    print("ERROR: " + Item  + " File Does Not Exist!")
    time.sleep(3)
    Main()
 
def Cracked(Password):
    os.system(Clear_Screen)
    print("Password Cracked: " + Password)
    End = time.time()
    Time_Taken = End - Start
    Stats = open("Cracking_V2_Stats.txt", "w+")
    Stats.write("Cracked Password: " + Password +"\n")
    Stats.write("Calculated Generations: N/A\n")
    Stats.write("Counted Generations: N/A\n")
    Stats.write("Time Taken: " + str(format(Time_Taken, '.20f')) + "'s")
    #Stats.write("\n" + "Time Per Generation: " + str(format(Time_Taken/Num, '.20f')) + "'s")
    Stats.close()
 
if __name__ == '__main__':
    Main()