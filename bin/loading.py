import subprocess
# import shlex
output = ""
result = "Result"
while result not in output:
    cmd = 'sfarkxtc diato.sfArk diato.sf2'
# p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE,
#                      stderr=subprocess.PIPE, shell=True)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
    output = p.stdout
    progress = p.stdout.read(350)  # Don't care about first line of sfarkxtc output
    print progress
    for i in range(0,98):  # Go up to 100%
        progress = p.stdout.read(14)
# Print: Open file '<fdopen>', mode 'rb'
# Not what we want:
        print p.stdout
# Print Progression
        print progress
    output = "Result"
