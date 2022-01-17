import sys
import argparse
import collections
index=0
readIter=0
fileRead = open('task.txt','a+')
fileRead = open('task.txt','r')
fileCompleted = open('completed.txt','a+')
fileCompleted = open('completed.txt','r')
if __name__== "__main__":
    if(len(sys.argv)>1):
        name = sys.argv[1]
        if (name == "help"):
            message1 = "\"Usage :-\n"
            message2 = "$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n"
            message3 = "$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n"
            message4 = "$ ./task del INDEX            # Delete the incomplete item with the given index\n"
            message5 = "$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n"
            message6 = "$ ./task help                 # Show usage\n"
            message7 = "$ ./task report               # Statistics\""
            sys.stdout.buffer.write(message1.encode('utf-8'))
            sys.stdout.buffer.write(message2.encode('utf-8'))
            sys.stdout.buffer.write(message3.encode('utf-8'))
            sys.stdout.buffer.write(message4.encode('utf-8'))
            sys.stdout.buffer.write(message5.encode('utf-8'))
            sys.stdout.buffer.write(message6.encode('utf-8'))
            sys.stdout.buffer.write(message7.encode('utf-8'))
        if (name == "add"):
            try:
                priority = sys.argv[2]
                task = sys.argv[3]
                data = fileRead.readlines()
                for line in data:
                    splitted = line.split()
                    if (int(splitted[0])<=int(priority)):
                        index=index+1
                appendContent = priority+" "+task+"\n"
                with open("task.txt", "w") as f:
                    data.insert(index, appendContent)
                    f.write("".join(data))
                AddMessage = "Added task:"+"\"",task,"\""+"with priority",priority
                print("Added task:"+" \""+task+"\"","with priority",priority)
            except:
                print("Error: Missing tasks string. Nothing added!")
        if (name == "ls"):#There are no pending tasks!
            data = fileRead.readlines()
            if len(data)<1:
                print("There are no pending tasks!")
            for line in data:
                if (line!="\n"):
                    line = line.split()
                    readIter = readIter+1
                    txt=str(readIter)+". "+' '.join(line[1::])+" "+"["+line[0]+"]\n"
                    sys.stdout.buffer.write(txt.encode('utf-8'))
                else:
                    continue
        if (name == "done"):
            readIter=1
            try:
                if int(sys.argv[2]) ==0:
                    print("Error: no incomplete item with index #0 exists.")
                else:
                    data = fileRead.readlines()
                    with open("task.txt", "w") as f:
                        with open("completed.txt", "a+") as fc:
                            for line in data:
                                if (line!="\n"):
                                    line = line.split()
                                    if readIter!= int(sys.argv[2]):
                                        f.write(' '.join(line)+"\n")
                                    else:
                                        fc.write(' '.join(line)+'\n')
                                    readIter = readIter+1
                                    print("Marked item as done.")
            except:
                print("Error: Missing NUMBER for marking tasks as done.")
        if (name == "del"):#"Error: task with index #0 does not exist. Nothing deleted."
            readIter=1
            try:
                if int(sys.argv[2]) ==0:
                    print("Error: task with index #0 does not exist. Nothing deleted.")
                else:
                    data = fileRead.readlines()
                    if (len(data)<int(sys.argv[2])):
                        print("Error: task with index #"+str(sys.argv[2]),"does not exist. Nothing deleted.")
                    else:    
                        with open("task.txt", "w") as f:
                            with open("completed.txt", "a+") as fc:
                                for line in data:
                                    if (line!="\n"):
                                        line = line.split()
                                        if readIter!= int(sys.argv[2]):
                                            success = 1
                                            f.write(' '.join(line)+"\n")          
                                        print("Deleted task #"+str(sys.argv[2]))
                                        readIter = readIter+1    
            except:
                print("Error: Missing NUMBER for deleting tasks.")
                
        if (name == "report"):
            readIter=1
            data1 = fileRead.readlines()
            txt="Pending : "+str(len(data1))+"\n"
            sys.stdout.buffer.write(txt.encode('utf-8'))
            for line in data1:
                if (line!="\n"):
                    line = line.split()
                    txt=str(readIter)+". "+' '.join(line[1::])+" "+"["+line[0]+"]\n"
                    sys.stdout.buffer.write(txt.encode('utf-8'))
                    readIter = readIter+1
                else:
                    continue
            readIter=1
            data2 = fileCompleted.readlines()
            txt="\nCompleted : "+str(len(data2))+"\n"
            sys.stdout.buffer.write(txt.encode('utf-8'))
            for line in data2:
                if (line!="\n"):
                    line = line.split()
                    txt=str(readIter)+". "+' '.join(line[1::])+"\n"
                    sys.stdout.buffer.write(txt.encode('utf-8'))
                    readIter = readIter+1
                else:
                    continue
        
    else:
            message1 = "\"Usage :-\n"
            message2 = "$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n"
            message3 = "$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n"
            message4 = "$ ./task del INDEX            # Delete the incomplete item with the given index\n"
            message5 = "$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n"
            message6 = "$ ./task help                 # Show usage\n"
            message7 = "$ ./task report               # Statistics\""
            sys.stdout.buffer.write(message1.encode('utf-8'))
            sys.stdout.buffer.write(message2.encode('utf-8'))
            sys.stdout.buffer.write(message3.encode('utf-8'))
            sys.stdout.buffer.write(message4.encode('utf-8'))
            sys.stdout.buffer.write(message5.encode('utf-8'))
            sys.stdout.buffer.write(message6.encode('utf-8'))
            sys.stdout.buffer.write(message7.encode('utf-8'))


fileRead.close()
fileCompleted.close()