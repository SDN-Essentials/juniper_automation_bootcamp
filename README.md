# Juniper Automation Bootcamp Overview
Public Repository for the SDN Essentials Juniper Automation Bootcamp Content

This repository contains all the necessary scripts for the Juniper Automation Bootcamp. It uses Vagrant to automate the provisioning of the Ansible workstation called ndo on this lab, two vSRXs and two private linux vms. There are multiple steps to this lab where you will be creating and applying scripts to the different devices deployed. This document will also walk through the steps to get your local environment up and running for the Junos Automation Bootcamp.


# Lab Topology built by VagrantFile

![topology](https://user-images.githubusercontent.com/19932683/35638353-e4e1520e-0684-11e8-9edb-c760cbd8d503.png)

# Creating the Lab Topology (Vagrant)

This portion of the lab setup document walks through the steps to get your local environment up and running for the Junos Automation Bootcamp using Vagrant to setup the necessary lab virtual-machines.

<p><strong> Step 1. Install Vagrant </strong></p>

This lab shall use Vagrant 2.0.1. Download the installer from the link below for your platform Use .dmg for a Mac and .msi for Windows. Run through the installer which handles any relevant dependencies. You may skip this step if you already have Vagrant installed.

<p><strong> Step 2. Install VirtualBox </strong></p>

This lab requires using VirtualBox 5.0 (not the newest 5.1). Vagrant does not recognize VirtualBox 5.1 as a provider, so your environment will not build on VirtualBox 5.1 or later. You may skip this step if you already have VirtualBox installed

https://www.virtualbox.org/wiki/Download_Old_Builds_5_0

<p><strong> Step 3. Install Git</strong></p>
 
 Once you have installed Vagrant, we need to install the Git version control tool. Navigate to the
 appropriate link to install the tool for your appropriate platform. Use the latest versions available.
 You may skip this step if you already have Git installed.
 
 * &nbsp;&nbsp; For a Mac: <br />
  http://git-scm.com/download/mac
 *  Note: For Mac users, you may be prompted to install XCode command line tools to install git. <br />
  https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
  
  * For Windows: <br />
  https://git-scm.com/download/win
  * Note: <br />
  For Windows users, the installation of Git (if you haven't completed this prior to the class) also installs a bash-list shell. Be sure to use this for the lab and launching Vagrant.
 
 <p><strong>Step 4.  Verify Vagrant and Utilities</strong></p>
 
Next, verify that you have the tools required.

$ git --version <br />
git version 2.15.0 <br />
$ vagrant --version <br />
Vagrant 2.0.1

<p><strong>Step 5. Clone the Appropriate VagrantFile and Code Examples </strong></p>
 
 Navigate to a directory where you want to stage your sample code. Create the directory if needed. Clone the Vagrant file and required installers to build the topology. Change to the repository directory.
 
*  Optional Step Below <br />
$ mkdir ~/git <br />
* Optional Step Above <br />
$ cd ~/git <br />
$ git clone https://github.com/darien-hirotsu/JNPRAutomationBootcamp  <br />
$ cd JNPRAutomationBootcamp/ <br />
 
<p><strong>Step 6. Install the required plugins to load the topology </strong></p>
 
$ vagrant plugin install vagrant-host-shell <br />
$ vagrant plugin install vagrant-junos <br />

<p><strong>Step 7. Launch the required topology  </strong></p>
 
Launch the network topology using the Vagrant tool. This may take several minutes to complete. If this is the first time launching the appropriate VMs your host must download the required files and install each of the components. <br />
 
 $ vagrant up

<p><strong>Step 8. Verify Access </strong></p>

Once Vagrant launches all components, try connecting to one of the VMs to ensure the topology has launched correctly.

$ vagrant ssh ndo

<p><strong>Step 9. Check the Python and Ansible Version </strong></p>

$ ansible --version <br />
ansible 2.3.2.0 <br />
  config file = <br />
  configured module search path = [u'/etc/ansible/roles/'] <br />
  python version = 2.7.6 (default, Nov 23 2017, 15:49:48) [GCC 4.8.4] <br />
  
  $ python --version <br />
  Python 2.7.6



# Accessing Virtual Machines

Using Vagrant within host machine
No IP addresses or passwords are required!

<p>
vagrant ssh ndo               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Used to access the host where you run scripts and Ansible <br />
vagrant ssh srx_r1            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Used to access srx_r1 <br />
vagrant ssh srx_r2            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Used to access srx_r2 <br />
vagrant ssh private_server_1  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Used to access private_server_1 to generate ping traffic <br />
vagrant ssh private_server_2  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Used to access private_server_2 to generate ping traffic <br />
 <p>


## Who to contact if you need help ?
