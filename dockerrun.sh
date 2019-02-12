#!/bin/bash

for i in `seq -f %02g ${1} ${2}`; do
	docker run -d -t --rm --name digicre${i} -p 22${i}:22 -p 80${i}:80 -p 88${i}:8800 digicre:0.1
done
