import subprocess

if __name__ == '__main__':

    #This is the place where distribution is save
    outfd = open('Sl', 'w+')

    #Getting the distributions
    subprocess.call(['uname', '-a'], stdout=outfd)
    outfd.close()

    #read the file with distribution
    fd = open('Sl', 'r')
    output = fd.read()

    #Apps on the host
    apps = open('Apps.txt', 'w+')

    #getting the apps of the system
    if(output.find("Debian")!= -1):
        subprocess.call(['dpkg', '--get-selections'], stdout=apps)
    else:
        if(output.find("fedora")!= -1 ):
            subprocess.call(['rmp', '-qa'])

    #Delete de file with the distribution
    subprocess.call(['rm', 'Sl'])
