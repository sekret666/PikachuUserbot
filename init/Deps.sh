#!/bin/bash

insReq() {
    echo '••• Installing Requirements •••'
    pip3 install -r $1/requirements.txt &> /dev/null
    echo 'Installed Requirements 🚶'
}

upgradePip() {
    echo '••• Updating Pip •••' 
    pip3 install -U pip &> /dev/null
    echo 'Updated Pip 🚶'
}
