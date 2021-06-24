#convenient bash commands
#changing the prompt to just a dollar sign
sh1='$'

#curl
#curl is a tool to transfer data from or to a server, using one of the supported protocols (HTTP, HTTPS, FTP, FTPS, TFTP, DICT, TELNET, LDAP or FILE). The command is designed to work without user interaction.
curl -o memorials-of-old-lincolnshire.txt http://www.het.brown.edu/guide/UNIX-password-security.txt

#wget
#GNU Wget is a free utility for non-interactive download of files from the Web. It supports HTTP, HTTPS, and FTP protocols, as well as retrieval through HTTP proxies.
wget -O memorials-of-old-lincolnshire.txt https://www.gutenberg.org/files/65653/65653-0.txt

#getting a list of process threads
ps aux | grep bash

#to read: http://linuxcommand.org/