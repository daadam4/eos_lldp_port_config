# Arista EOS Simple Scripting

This repo is meant to serve as an introduction to simple scripts that can be ran within the Arista Test Drive (ATD) environment. Initially, the focus will be configuring interfaces but the options are limitless when you get creative.

*Disclaimer: The code contained in this repository is meant to be clear and easily understood to someone new to network automation and therefore is not as condensed or optimized.  There are tons of other great repos that will be linked for more advanced users*

## Summary of Steps

1. [Launch Programmability IDE](#step-1---launch-programmability-ide)
2. [Change Working Directory and Git Clone](#step-2---change-working-directory-and-git-clone)
3. [Update Passwords](#step-3---update-passwords)
4. [Let the fun begin 🚀](#step-4---Let-the-fun-begin-🚀)
5. [Additional Resources](#additional-resources)

## STEP #1 - Launch Programmability IDE

- Launch the Progammability IDE.  If this is the first time starting the IDE you will be prompted for a code-server password.  Your unique password is noted on the Lab Topology page.

<img src="images/code-server.png" alt="folder" width="400"/>

- Click through any pop-ups that may occur.
- Start a new terminal session by clicking on the hamburger and selecting Terminal->New Terminal.

![Topo](images/programmability_ide.png)

## STEP #2 - Change Working Directory and Git Clone

- Change working directory to `labfiles` and clone the repo. Finally, change directory to `./eos_lldp_port_config`. You can either manually type in the commands from the following code block or there is a copy option if you hover to the right.

``` bash
cd ./labfiles
git clone https://github.com/daadam4/eos_lldp_port_config.git
cd ./eos_lldp_port_config/
```

## STEP #3 - Update Passwords

- For each of the files in the image below, update the `password` variable for the line in the code block beneath. *If you left click each file in the explorer, it will open within the editor and you can edit the file directly in the IDE*

<img src="images/password_update.png" alt="folder"/>

`node = pyeapi.client.connect(host=ip_address, username='arista', password='password', transport='https', return_node=True)`

| File Name   | Line # |
| ----------- | ----------- |
| int_conf.py | 8       |
| int_conf_multi.py   | 14        |
| int_conf_detail.py   | 22        |

- For example if my password were `arista1234` the line would read

`node = pyeapi.client.connect(host=ip_address, username='arista', password='arista1234', transport='https', return_node=True)`

- Again, your credentials can be found near the bottom of the Lab Topology page.

![Topo](images/username_passwords.png)

## STEP #4 - Let the fun begin 🚀

- The recommended order of running the scipts is as follows. Each subsequent script builds on the previous one by adding simple features and ends with a practical application of how this could be useful in your network:

```bash
python3 int_conf.py
```
```
python3 int_conf_multi.py
```
```
python3 int_conf_detail.py
```
### What's happening?

**int_conf.py**
---
- Adding a description to Ethernet1 on `node` s1-core1.atd.lab (192.168.0.102) and then validating by showing the running configuration

**int_conf_multi.py**
---
- Building on `int_conf.py` by looping through multiple hosts and multiple interfaces but again configuring a description on interfaces

**int_conf_detail.py**
---
- A real world example where we use the tools from the previous two scripts to now take the `show lldp neighbors` output and use that data to configure the interface descriptions
- After running `int_conf_detail.py` connect to a few of the nodes through the cli and verify the configuration

## Additional Resources
- Now that you have built a base go checkout Arista Networks on github and all of these other awesome resources

[Arista Networks Github](https://github.com/aristanetworks) - A collection of a various resources for EOS, Cloudvision, and other Arista tools

[Arista Networks EOS+](https://github.com/arista-eosplus) - EOS+ extensions, including `pyeapi` which was used in this repo

[PacketAnglers](https://github.com/packetAnglers/) - A few folks who like to fish, network, and automate
