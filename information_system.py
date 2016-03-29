#!/usr/bin/python
import webbrowser
import os
import datetime

def stringchecker (orig,v1):
 ret = True
 x = len(v1)
 j=0
 for j in range(0,x,1):
    if(len(v1)<=len(orig)):
      if orig[j].capitalize() == v1[j] or orig[j]==v1[j]:
          ret = ret and True
      elif orig[j] != v1[j]:
          ret = ret and False
    else:
      ret = ret and False

 return ret


username = raw_input("Login Name:")

while 1:
 print "\n**************************************************************"
 print "1:Customer\n2:Suppliers\n3:Useful Calls\n4:Useful Data\n5:Contacts and emails\n6:Clear Screen"
 print  "7:End the Program\n8:Internet\n9:Edit Data\n10:Printers"
 sel = raw_input("Please Select an Option:")
 print "**************************************************************\n"

 if sel=="1":

	  phonenum = raw_input("Enter the telephone Number OR Account Code:")
          v = phonenum
	  status1 = raw_input("Log a new call? (Y or N):")

	  NUMBERFILE = open("numfile.txt","r+")
 
       	  NUMLINES  = NUMBERFILE.readlines()
          i=0

	  if status1 == "Y":
   
	     comm1 = raw_input("Enter the comments:")
             now = datetime.datetime.now()      
             NUMBERFILE.write("=========================\n"+phonenum+"\n" +comm1+"\n"+str(now)+" By:"+username+"\n=========================")
    
             print "New call logged"
             NUMBERFILE.close()

	  elif status1 == "N":
            
            print "\n*********************\n"
	    for phonenum in NUMLINES:

             if(stringchecker(phonenum,v) or (i>0)):
	        print phonenum
                i = i+ 1
                if (i==4):
                          i=0
                 
             else:
                i = 0

          NUMBERFILE.close() 

 elif sel=="2":
    
	  phonenum = raw_input("Enter the Supplier Name:")
          v = phonenum

	  status1 = raw_input("New call? (Y or N):")

	  NUMBERFILE = open("suppfile.txt","r+")
 
       	  NUMLINES  = NUMBERFILE.readlines()


	  if status1 == "Y":
    
	     comm1 = raw_input("Enter the comments:")
             now = datetime.datetime.now()      
             NUMBERFILE.write("=========================\n"+phonenum+"\n" +comm1+"\n"+str(now)+" By:"+username+"\n=========================")
    
             print "NEW CALL LOGGED SUCCESSFULLY"
             NUMBERFILE.close()

	  elif status1 == "N":
	  
            print "\n*********************\n"
	    for phonenum in NUMLINES:

             if(stringchecker(phonenum,v) or (i>0)):
	        print phonenum
                i = i+ 1
                if (i==4):
                          i=0
                 
             else:
                i = 0

          NUMBERFILE.close() 
 
 elif sel=="3":
          
	  phonenum = raw_input("Name:")
          v = phonenum

	  status1 = raw_input("Enter contact (Y/N):")

	  NUMBERFILE = open("confile.txt","r+")
 
       	  NUMLINES  = NUMBERFILE.readlines()

	  if status1 == "Y":
    
	     comm1 = raw_input("Enter the comments:")
             now = datetime.datetime.now()      
             NUMBERFILE.write("=========================\n"+phonenum+"\n" +comm1+"\n"+str(now)+" By:"+username+"\n=========================")
    
             print "NEW CONTACT ADDED SUCCESSFULLY"
             NUMBERFILE.close()

	  elif status1 == "N":
 
            print "\n*********************\n"
	    for phonenum in NUMLINES:

             if(stringchecker(phonenum,v) or (i>0)):
	        print phonenum
                i = i+ 1
                if (i==4):
                          i=0
                 
             else:
                i = 0



          NUMBERFILE.close() 

 elif sel=="4":
          
	  phonenum = raw_input("Data to Search:")

	  status1 = raw_input("New Data(Y/N):")

	  NUMBERFILE = open("datafile.txt","r+")
 
       	  NUMLINES  = NUMBERFILE.readlines()

          v = phonenum
          i=0
	  if status1 == "Y":
    
	     comm1 = raw_input("Enter the comments:")
             now = datetime.datetime.now()      
             NUMBERFILE.write("=========================\n"+phonenum+"\n" +comm1+"\n"+str(now)+" By:"+username+"\n=========================")
    
             print "NEW DATA ENTERED SUCCESSFULLY"
             NUMBERFILE.close()

	  elif status1 == "N":

            print "\n*********************\n"
	    for phonenum in NUMLINES:

             if(stringchecker(phonenum,v) or (i>0)):
	        print phonenum
                i = i+ 1
                if (i==4):
                          i=0
                 
             else:
                i = 0

          NUMBERFILE.close()

 elif sel=="5":
          
	  phonenum = raw_input("Contact or Number to Search:")

	  status1 = raw_input("New Contact(Y/N):")

	  NUMBERFILE = open("incon.txt","r+")
 
       	  NUMLINES  = NUMBERFILE.readlines()

          v = phonenum
          i=0
	  if status1 == "Y":
    
	     comm1 = raw_input("Enter the details:")
             now = datetime.datetime.now()      
             NUMBERFILE.write("=========================\n"+phonenum+"  " +comm1+"\n=========================")
    
             print "NEW Contact ENTERED SUCCESSFULLY"
             NUMBERFILE.close()

	  elif status1 == "N":

            print "\n*********************\n"
	    for phonenum in NUMLINES:

             if(stringchecker(phonenum,v) or (i>0)):
	        print phonenum
                i = i+ 1
                if (i==1):
                          i=0
                 
             else:
                i = 0

          NUMBERFILE.close()

 elif sel=="6":
          os.system('CLS')

 elif sel=="7":
          print "Thanks for using this software"
          exit()

 elif sel=="8":
          url = raw_input("Enter the URL:")
          webbrowser.open("http://"+url,new=2)

 elif sel=="9":

	  phonenum = raw_input("Data to Search:")

	  status1 = "N"

	  NUMBERFILE = open("datafile.txt","r+")
          TEMPFILE = open("tempfile.txt","r+")
       	  NUMLINES  = NUMBERFILE.readlines()
          linecount =0
          v = phonenum
          i=0
	  if status1 == "Y":
 
	   NUMBERFILE.close()  

	  elif status1 == "N":

            print "\n*********************\n"
	    for phonenum in NUMLINES:
             linecount = linecount + 1
             if(stringchecker(phonenum,v) or (i>0)):
	        phonenum = phonenum.replace("\n"," ")
                print phonenum+" at line:"+str(linecount)
	        
                i = i+ 1
                if (i==4):
                          i=0
                 
             else:
                i = 0

          linecount=0
          editline = input("Enter the Line Number to edit:")
          print "\n*********************\n"
          phonenum =""
	  for phonenum in NUMLINES:
             linecount = linecount + 1
             
             if(linecount==editline):
	        print "ORIGINAL DATA:"+phonenum
	        CHANGED = raw_input("Enter new Data:") 
                TEMPFILE.write(CHANGED+"\n")                 
             else:
                TEMPFILE.write(phonenum)
                i = 0
          TEMPFILE.close()
          NUMBERFILE.close()
          os.remove("datafile.txt")
          os.rename("tempfile.txt","datafile.txt")
          TEMPNEW = open("tempfile.txt","w+")
 elif sel=="10":
     	  phonenum = raw_input("Enter Printer Serial Number or Press Enter:")

	  status1 = "N"

	  NUMBERFILE = open("printers.txt","r+")
 
       	  NUMLINES  = NUMBERFILE.readlines()

          v = phonenum
          i=0
	  if status1 == "Y":
    
	     comm1 = raw_input("Enter the details:")
             now = datetime.datetime.now()      
             NUMBERFILE.write("=========================\n"+phonenum+"  " +comm1+"\n=========================")
    
             print "NEW Contact ENTERED SUCCESSFULLY"
             NUMBERFILE.close()

	  elif status1 == "N":

            print "\n*********************\n"
	    for phonenum in NUMLINES:

             if(stringchecker(phonenum,v) or (i>0)):
	        print phonenum

                i = i+ 1
                if (i==1):
                          i=0
                 
             else:
                i = 0

          NUMBERFILE.close()
 
 if sel=="1":

	  phonenum = raw_input("Enter the telephone Number OR Account Code:")
          v = phonenum
	  status1 = raw_input("Log a new call? (Y or N):")

	  NUMBERFILE = open("numfile.txt","r+")
 
       	  NUMLINES  = NUMBERFILE.readlines()
          i=0

	  if status1 == "Y":
   
	     comm1 = raw_input("Enter the comments:")
             now = datetime.datetime.now()      
             NUMBERFILE.write("=========================\n"+phonenum+"\n" +comm1+"\n"+str(now)+" By:"+username+"\n=========================")
    
             print "New call logged"
             NUMBERFILE.close()

	  elif status1 == "N":
            
            print "\n*********************\n"
	    for phonenum in NUMLINES:

             if(stringchecker(phonenum,v) or (i>0)):
	        print phonenum
                i = i+ 1
                if (i==4):
                          i=0
                 
             else:
                i = 0

          NUMBERFILE.close() 

 elif sel=="11":
    
	  phonenum = raw_input("Enter the WORD:")
          v = phonenum

	  status1 = "N"

	  NUMBERFILE = open("datafile.txt","r+")
 
       	  NUMLINES  = NUMBERFILE.read()


	  if status1 == "Y":
    
	     comm1 = raw_input("Enter the comments:")
             now = datetime.datetime.now()      
             NUMBERFILE.write("=========================\n"+phonenum+"\n" +comm1+"\n"+str(now)+" By:"+username+"\n=========================")
    
             print "NEW CALL LOGGED SUCCESSFULLY"
             NUMBERFILE.close()

	  elif status1 == "N":
	  
            print "\n*********************\n"
	    for phonenum in NUMLINES:

             if stringchecker(phonenum,v):
	        print "MATCHED"
          NUMBERFILE.close() 
           
