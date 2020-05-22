#!/bin/bash

python transmitter.py

DIR="$( cd "$( dirname "${BASH_SOURCE[channel_input.txt]}" )" >/dev/null 2>&1 && pwd )/files/client.py"

python3 $DIR --input_file files/$1 --output_file files/channel_output.txt --srv hostname=iscsrv72.epfl.ch --srv port=80

/home/guillaume/Desktop/Cours/PDC_project/Repo/PDC_Project>py client.py --input_file=files/channel_input.txt --output_file=files/channel_output.txt --srv_hostname=iscsrv72.epfl.ch –srv_port=80

python receiver.py



