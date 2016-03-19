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
* Script to identify key frames in an avi file and save them to disk (idea is to find key frames from a video and use them to compile a gif): video_to_gif.py
