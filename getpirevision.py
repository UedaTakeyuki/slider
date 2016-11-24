import re

def revision():
  revision = "unknown"
  with open('/proc/cpuinfo', 'r') as f:
    for line in f:
#      print line
      m = re.search('Revision.*: ([0123456789abcdef]*)', line)
      if m:
        revision = m.group(1)
        return revision

if __name__ == '__main__':
  print (revision())

