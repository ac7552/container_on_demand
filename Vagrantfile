# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"
  
  # config.ssh.username = 'root'
  # config.ssh.password = 'vagrant'
  # config.ssh.insert_key = 'true'
  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network :forwarded_port, guest: 3009, host: 3009
  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.

  # Run the specified shell script when creating the VM. The "provision"
  # line tells Vagrant to use the shell provisioner to setup the machine,
  # with the bootstrap.sh file. The file path is relative to the location
  # of the project root (where the Vagrantfile is).
  config.vm.provision :shell, :path => "setup.sh"
end
