#!/bin/bash

python transmitter.py

python3 /home/guillaume/Desktop/Cours/PDC_project/Repo/PDC_Project/client.py --input_file files/channel_input.txt --output_file files/channel_output.txt --srv_hostname iscsrv72.epfl.ch --srv_port 80

python receiver.py



