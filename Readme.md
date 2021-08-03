# Red Team Lab

## Red Team Lab Documentation
## Introduction
Welcome to the Red team lab wiki!

This lab is a practice space, rather than text book, mainly focusing on practices tools and procedures of Red Team Lab.


## Pre-Requisites
The following software  is required for setting up the Red Team Lab environment 
* Access to experiment nodes (technical specifications can be accessed [here](https://ncl.sg/testbedInformation))
    * One node can accomodate 4 participants 
* The following softwares, can be installed using the setup.py file
    * Vagrant
    * Virtual-Box
    * Ansible (for Automation - Work in progress)
    * VNCServer

> Any issues in the pre-requisite software, please contact support@ncl.sg

## Creating an experiment (for NCL staff)
* Login to the web portal of NCL

* Create an experiment with the below configuration
  ```
  set ns [new Simulator]
  source tb_compat.tcl

  # Set node.
  set n1 [$ns node]
  tb-set-node-os $n1 Ubuntu16.04.3-amd64

  # Go!
  $ns run
  ```

## Procedure to setup Red-Team lab (for NCL staff)
* Login to the experiment node in NCL using your credentials via terminal
  ```
  ssh <ncl_username>@ncl.sg
  ssh <ncl_username>@<experiment_name>.<team_name>.ncl.sg
  ```
### Create new partition (for 250GB)
* Enter disk partition using the below command 
  ```
  sudo fdisk /dev/sda
  ```
* Create new partition using the option `n` and then with option `e`  
* Hit `Enter` 2 times to create “Extended” partition. 
* Retype `n` and partition size (250G) to get the new logical partition.
* Using option `p` check if new partition is created. 
* Using option `w` save the created partition  
* Reboot the experiment node after adding the new partition
  ```
  sudo reboot now 
  ```
* After reboot login to the experiment node and format the new disk partition (sda5 in my example)
  ```
  sudo mkfs.ext3 /dev/sda5
  ```
* Mount the new partition using the below command 
  ```
  sudo mount /dev/sda5 Red-Team/
  ```
* Navigate into the new folder to access the new partition of 250GB
  ```
  cd Red-Team
  ```
### Installing ansible 
* Check if Python 3 is installed in the Experiment node using the below command
    ```
    python3 --version
    ```
* Install pip for python3 using the below commands 
    ```
    wget https://bootstrap.pypa.io/pip/3.5/get-pip.py
    python3 get-pip.py
    ```
* Install ansible and pywinrm packages using pip
    ```
    python3 -m pip install ansible
    python3 -m pip install pywinrm
    ``` 
### Lab Setup
* Clone the repository into the experiment node assigned to you for your experiment 
  ```
  git clone https://github.com/nus-ncl/Red-Team-Lab.git
  ```
* Run the following command, to install the pre-requisite software 
  ```
  python setup.py
  ```
* 
  

### Pending tasks for automation
- [x] Configure and add Domain controller using ansible
- [ ] Configure the servers and services using ansible
- [ ] Configure tools in workstation using ansible