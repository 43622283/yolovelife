#!/bin/bash
# Author Yo
# Time 2018-12-12
openssl rand -base64 12 > ~root/.openssl
PASSWORD=`cat ~root/.openssl`
SSHPASSWORD=`echo ${PASSWORD:0:13}`
echo "root:${SSHPASSWORD}" | chpasswd
cat ~root/.openssl
rm -f ~root/.openssl