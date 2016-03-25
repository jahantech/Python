#!/usr/bin/python

from time import gmtime, strftime



def WriteToLogFile(LogEntry):
    filehandler = open("python_log.txt", 'a')
    filehandler.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) +" : "+ LogEntry+"\n")
    filehandler.close()
    return


WriteToLogFile("User logged in") 
