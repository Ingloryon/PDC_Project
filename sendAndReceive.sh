#!/bin/bash

python transmitter.py

DIR="$( cd "$( dirname "${BASH_SOURCE[in.txt]}" )" >/dev/null 2>&1 && pwd )/Code/client.py"

python3 $DIR --input_file Code/IO/$1 --output_file Code/IO/out.txt --srv_hostname iscsrv72.epfl.ch --srv_port 80

python receiver.py
