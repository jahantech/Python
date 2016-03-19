# Python
This repo contains useful python scripts that can prove to be very useful for general DevOPS/Automation tasks

List of scripts:
* Script to connect to MySQL database and get result for select query: db_access.py
```
Usage: 
./db_access.py 
Output:
TestUser1 First test user
```
* Script to list files in a given directory: list_files.py
```
Usage:
./list_files.py
Output:
Directory: scripts
File: tempfile.txt
```
* Script to read json from testdata.json file and print data from it: read_json.py
```
Usage:
./read_json.py
Output:
test1 24
test2 26
```
* Script to read xml from testdata.xml file and print data from it: read_xml.py
```
Usage:
./read_xml.py
Output:
Name  :  TV
Model :  TVx86
Price :  300.00
******************
Name  :  Fridge
Model :  FRIDGEx64
Price :  200.0
******************
```
* Daemon written in python that prints CPU usage after 10 seconds. Ofcourse you can modify the script to send these stats to elasticsearch or influxdb and use the data to graph it. (Note you will need psutil and daemon module for this)
```
Usage:
./py_daemon_cpustats.py start (To start the daemon)
./py_daemon_cpustats.py stop (To stop the daemon)
Output:
[root@testserver Python]# ./py_daemon_cpustats.py start
[root@testserver Python]# started with pid 10546
CPU Stats:
71.4
[root@testserver Python]# ./py_daemon_cpustats.py stop
Terminating on signal 15
```
* Script to identify key frames in an avi file and save them to disk (idea is to find key frames from a video and use them to compile a gif): video_to_gif.py
