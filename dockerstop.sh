#!/bin/bash

for i in `seq -f %02g ${1} ${2}`; do
	docker stop digicre${i}
done
