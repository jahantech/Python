#!/usr/bin/python
import time
from daemon import runner
import psutil
class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/py_daemon_cpustats.pid'
        self.pidfile_timeout = 5
    def run(self):
        while True:
            print("CPU Stats:")
	    print(psutil.cpu_percent(interval=None))
            time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
