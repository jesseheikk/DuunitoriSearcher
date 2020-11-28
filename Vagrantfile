VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "bento/ubuntu-18.04"
  
  config.vm.provision "shell", path: "script.sh"
  config.vm.synced_folder "src/", "/srv/mount_folder"

end