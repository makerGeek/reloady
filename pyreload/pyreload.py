#!/usr/bin/python                                                                                                                 
from datetime import datetime
import sys, os, time, threading, subprocess, fnmatch

class PyReload(threading.Thread):  # Changed class name from SourceChangeMonitor to PyReload

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

        def __init__(self, program: str = "main.py", args: list = None):
                """
                Initialize the PyReload module.

                :param program: The entry point program to run (default is "main.py").
                :param args: A list of arguments to pass to the program (default is None).
                """
                threading.Thread.__init__(self)
                self.this_script_name = os.path.abspath( sys.argv[0] )
                self.files = self.get_files()
                self.PROGRAM = program  # Set the program to the provided parameter
                self.args = args if args is not None else []  # Set the arguments
                self.start_program()

        def display_help(self) -> None:
                """
                Display usage information for the PyReload script.
                """
                help_text = """
                Usage: PyReload [options]

                Options:
                --help          Show this help message and exit.
                program        Specify the entry point program to run (default is "main.py").
                args           Additional arguments to pass to the program.

                This script monitors specified Python files for changes and restarts the
                specified program when changes are detected.
                """
                print(help_text)

        def run(self) -> None:
                while 1:
                        time.sleep(self.POLL_INTERVAL)
                        if self.poll():
                                print("-------------------------------------------------")
                                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]Noticed a change in program source. Restarting...")
                                print("-------------------------------------------------")
                                self.start_program()

        def get_files(self) -> list:
                """
                Get a list of all files along with their timestamps for last modified.

                :return: A list of tuples containing file paths and their last modified timestamps.
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

        def poll(self) -> bool:
                """
                Check if any source files have changed since the last poll.

                :return: True if files have changed, False otherwise.
                """
                new_files = self.get_files()
                if self.files != new_files:
                        self.files = new_files
                        return True
                return False

        def start_program(self) -> None:
                """
                Start the program. If it was already started, kill it before restarting.
                """
                if self._process != None and self._process.poll() is None:
                        self._process.kill()
                        self._process.wait()

                self._process = subprocess.Popen( [sys.executable, self.PROGRAM] + self.args )  # Pass the arguments



