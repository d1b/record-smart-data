#!/usr/bin/python
import os
import subprocess


def main():
      here = os.path.dirname(os.path.abspath(__file__))
      stats_dir = os.path.join(here, 'stats')
      path = '/dev/disk/by-id/'
      if not os.path.exists(stats_dir):
          os.mkdir(stats_dir)
      for i in os.listdir(path):
            full_path = os.path.join(path, i)
            if ('part' not in i.split('-')[-1] and
                  i.startswith('ata-') and not i.lower().endswith('.py')):
                  proc = subprocess.Popen(['smartctl', '-a', full_path],
                        stdout=subprocess.PIPE)
                  output = proc.communicate()[0]
                  with open(os.path.join(stats_dir, i), 'w+') as f:
                        f.write(output)

main()

