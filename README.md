# Juniper Automation Bootcamp Overview
Public Repository for the SDN Essentials Juniper Automation Bootcamp Content

This repository contains all the necessary scripts for the Juniper Automation Bootcamp. It uses Vagrant to automate the provisioning of the Ansible workstation called ndo on this lab, two vSRXs and two private linux vms. There are multiple steps to this lab where you will be creating and applying scripts to the different devices deployed. This document will also walk through the steps to get your local environment up and running for the Junos Automation Bootcamp.


# Lab Topology built by VagrantFile

![topology](https://user-images.githubusercontent.com/19932683/35638353-e4e1520e-0684-11e8-9edb-c760cbd8d503.png)

# Creating the Lab Topology (Vagrant)

This portion of the lab setup document walks through the steps to get your local environment up and running for the Junos Automation Bootcamp using Vagrant to setup the necessary lab virtual-machines.

Step 1. Install Vagrant

This lab shall use Vagrant 2.0.1. Download the installer from the link below for your platform Use .dmg for a Mac and .msi for Windows. Run through the installer which handles any relevant dependencies. You may skip this step if you already have Vagrant installed.


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



iii.      How do I make this work?
iv.      Who to contact if you need help?
