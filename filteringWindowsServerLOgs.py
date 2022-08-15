import re
import os
pattern =  re.compile(r'^(Image|User|ProcessId|CommandLine):([^\n]*)$')
#os.chdir('C:\\Users\\KM\\Documents\\AI')
#loop over report and find the pattern save 
#matched result in freport file
for i, line in enumerate(open('report.csv')):
    for match in re.finditer(pattern, line):
        with open('freport.txt', 'a') as f:
            f.write(line + '\n')
