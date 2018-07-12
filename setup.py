from distutils.core import setup
import py2exe
import sys
sys.argv.append("py2exe")
sys.argv.append("-q")
# insert your own source code filename below ...
code_file = 'convert.pyw'
# replace windows with console for a console program
setup(windows = [{"script": code_file}])
