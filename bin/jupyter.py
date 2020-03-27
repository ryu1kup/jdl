import sys
import subprocess
import re

args = sys.argv
std = subprocess.check_output(['ssh', args[1], args[2], '{}@dali-login1.rcc.uchicago.edu'.format(args[3]), args[4]]).decode('utf8')
print(std)

std = std.split('\n')
if args[5] == 'Linux':
    cmd1, cmd2 = std[std.index('All done! If you have linux, execute this command on your laptop:') + 2].split(' && ')
    subprocess.run(cmd1.split(' '))
    subprocess.run(cmd2.split(' '))
elif args[5] == 'Mac':
    cmd1, cmd2 = std[std.index('If you have a mac, instead do:') + 2].split(' && ')
    subprocess.run(cmd1.split(' '))
    subprocess.run(cmd2.split(' '))
elif args[5] == 'Cygwin':
    cmd1, cmd2 = std[std.index('If you have a mac, instead do:') + 2].split(' && ')
    subprocess.run(cmd1.split(' '))
    subprocess.run(cmd2.replace('open', 'cygstart').split(' '))
