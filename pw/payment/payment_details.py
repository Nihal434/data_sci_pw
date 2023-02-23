import os,sys
from os.path import dirname, join , abspath
sys.path.insert(0,abspath(join(dirname(__file__), '..')))
from course import course_details # if we are writhing import at a same time in both the files then it will give a circular error
#so write import in any one file 
def payment():
    print("payment file")

course_details.course()