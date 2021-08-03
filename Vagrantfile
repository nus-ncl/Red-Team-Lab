Vagrant.configure("2") do |config|
  config.vm.guest = :windows
  config.vm.communicator = "winrm"
  config.vm.boot_timeout = 600
  config.vm.graceful_halt_timeout = 600
  config.winrm.retry_limit = 10
  config.winrm.retry_delay = 20

  config.vm.define "DomainController" do |dc|
    dc.vm.box = "kkolk/w2k12r2-sysprep-ready"
    dc.vm.network "private_network", ip: "192.168.200.10"
    dc.vm.network :forwarded_port, guest: 5985, host: 25985, id: "winrm"
    dc.vm.network :forwarded_port, guest: 3389, host: 23389, id: "msrdp"


  end
  config.vm.define "Server" do |server|
    server.vm.box = "kkolk/w2k12r2-sysprep-ready"
    server.vm.network "private_network", ip: "192.168.200.11"
    server.vm.network :forwarded_port, guest: 5985, host: 35985, id: "winrm"
    server.vm.network :forwarded_port, guest: 3389, host: 33389, id: "msrdp"
  end
  config.vm.define "Workstation" do |workstation|
    workstation.vm.box = "StefanScherer/windows_10"
    workstation.vm.network "private_network", ip: "192.168.200.12"
    workstation.vm.network :forwarded_port, guest: 5985, host: 45985, id: "winrm"
    workstation.vm.network :forwarded_port, guest: 3389, host: 43389, id: "msrdp"
  end
  config.vm.provision "shell", path:"./ConfigureRemotingForAnsible.ps1"
end

