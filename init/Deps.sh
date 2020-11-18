#!/bin/bash

insReq() {
    pip3 install -r $1/requirements.txt &> /dev/null
}

upgradePip() {
    pip3 install -U pip &> /dev/null
}
