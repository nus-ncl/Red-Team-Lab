import commands

vagrant_download = "https://releases.hashicorp.com/vagrant/2.2.10/vagrant_2.2.10_linux_amd64.zip"
virtualbox_download = "https://download.virtualbox.org/virtualbox/6.1.14/virtualbox-6.1_6.1.14-140239~Ubuntu~xenial_amd64.deb"


def check_vagrant(software):
    stats, info = commands.getstatusoutput("vagrant -v")  
    tmp_file = software + ".zip"
    bin_file = "vagrant"
    if "not found" in info:
        print "[!] Downloading " + software + ""
        stats,info = commands.getstatusoutput("wget " + vagrant_download + " -O " + tmp_file)
        print "[!] Installing " + software + ""
        stats, info = commands.getstatusoutput("unzip "+tmp_file)
        stats, info = commands.getstatusoutput("sudo mv  vagrant /usr/local/bin/")
        stats, info = commands.getstatusoutput("vagrant -v")
        stats, info = commands.getstatusoutput("rm " + tmp_file)

    else: 
        print "[+] " + info + " installed"


def check_virtualbox(software):
    dwnld_bin = "virtualbox.deb"
    stats, info = commands.getstatusoutput("vboxmanage --version")  
    if "not found" in info:
        print "[!] Downloading " + software + ""
        stats, info = commands.getstatusoutput("wget " + virtualbox_download + " -O " + dwnld_bin) 
        print "[!] Installing " + software + ""
        stats, info = commands.getstatusoutput("sudo dpkg -i ./" + dwnld_bin )
        stats, info = commands.getstatusoutput("vboxmanage --version")
        print "[+]" + info + " Installed"
        stats, info = commands.getstatusoutput("rm " + dwnld_bin)

    else: 
        print "[+] VirtualBox " + info + " installed"

commands.getstatusoutput("mkdir tmp")
check_vagrant('vagrant')
check_virtualbox('virtualbox')
commands.getstatusoutput("rm -r tmp")
