#!/usr/bin/python                                                                                                                 
import sys, os, time, threading, subprocess, fnmatch

class SourceChangeMonitor(threading.Thread):

        # Remember the process ID of the subprocess for when                                                                 
        # we want to restart it                                                                                              
        _process = None

        # How often should we check for changes (in seconds)                                                                 
        POLL_INTERVAL = 1

        # Which files should be monitored for changes?                                                                       
	# Here, we deliberately exclude files beginning with a dot (.)
        FILE_PATTERN = r"[!.]*.py"

        # Which directory is the root of the source files?                                                       
        ROOT_DIRECTORY = r"."

        # Entry point program to run                                                                                         
        PROGRAM = r"hello.py"

        def __init__(self):
                threading.Thread.__init__(self)
                self.this_script_name = os.path.abspath( sys.argv[0] )
                self.files = self.get_files()
                self.start_program()

        def run(self):
                while 1:
                        time.sleep(self.POLL_INTERVAL)
                        if self.poll():
                                print( "-------------------------------------------------")
                                print( "Noticed a change in program source. Restarting...")
                                print( "-------------------------------------------------")
                                self.start_program()

        def get_files(self):
                """                                                                                                          
                Get a list of all files along with their timestamps for last modified                                        
                """
                files = []
                for root, dirnames, filenames in os.walk(self.ROOT_DIRECTORY):
                        for filename in fnmatch.filter(filenames, self.FILE_PATTERN):
                                full_filename = os.path.join(root, filename)
                                files.append(full_filename)

                # Attach the last modified dates                                                                             
                files = [(f, os.stat(f).st_mtime) for f in  files]

                # Don't include this script                                                                                  
                files = [f for f in files if  f[0] != self.this_script_name]
                return list(files)

        def poll(self):
                """                                                                                                                          Check if any source files have changed since last poll. Returns True if                                                      files have changed, False otherwise                                                                                          """
                new_files = self.get_files()
                if self.files != new_files:
                        self.files = new_files
                        return True
                return False

        def start_program(self):
                """                                                                                                                          Start the program. If it was already started, kill it before restarting                                                      """
                if self._process != None and self._process.poll() is None:
                        self._process.kill()
                        self._process.wait()

                self._process = subprocess.Popen( [sys.executable, self.PROGRAM] )



if __name__ == "__main__":
        SourceChangeMonitor().start()
