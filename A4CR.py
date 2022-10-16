import os, sys

try:

   __import__("FILE").keycheck()

except Exception as e:

    exit(str(e))
