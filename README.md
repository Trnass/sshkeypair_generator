# sshkeypair_generator
Because I am bored of creating ssh keys, configuring aliases etc., I made a script that guide on input and do everything what u need. 
You can look forward to automatic linking to github repository and function for localization. 
## Basic information
The entire project is only tested on a VPS with Debian 11, however it should work on all Debian distributions.
## Requirements
1. Python3
2. Pip3
3. pyyaml (pip3 install pyyaml)
4. Git
## How to use?
1. You have to clone this repository, ofc.
2. Then, you have to cd into that repository
    - You can change language of app in file generate_ssh_keys.py line 6
3. Run that chmod +x create_sshkey.sh (you have to do it to execute that file)
4. Then you can run ./create_sshkey.sh (or if you are lazy as me, you can run ./*.sh)
5. Fill alias - Its like a login name for this sshkey
6. hit enter twice (or fill up passphrase twice)
7. Now you have everything prepared, from the server side, go into settings of repository on github and open "deploy keys"
8. Paste the key from console (in english "Public key for GitHub") into github and give it same name as you gave alias.
9. Now you can use git on repository
## Contributors wanted!
Do you have an idea how to improve the project? Create an issue! Do you want to modify it somehow? You certainly can, but the license under which the project is created clearly defines what you can do with the code.
