#!/bin/bash

PORT=80
SRVR=iscsrv72.epfl.ch

echo "creating file"
base64 -w0 /dev/urandom | head -c 80 > input.txt



echo "runing encoder"
python3 encoder.py
echo "transmitting"
python3 client.py --input_file=encoded.txt --output_file=received.txt --srv_hostname=$SRVR --srv_port=$PORT
echo "running decoder"
python3 decoder.py



echo "comparing files"
cat input.txt; echo ""
cat output.txt; echo ""

SIZE1=$(stat --printf="%s" "input.txt")
SIZE2=$(stat --printf="%s" "output.txt")
DIFF1=$(cmp -l input.txt output.txt 2>/dev/null | wc -l)
DIFF2=$(expr $SIZE1 - $SIZE2 )
RES=$(expr $DIFF1 + ${DIFF2#-})

echo "Character difference(s) = $DIFF1" 
echo "Size difference(s) = $DIFF2"
echo "number of error = $RES"

