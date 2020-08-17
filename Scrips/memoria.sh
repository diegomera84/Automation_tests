#!/bin/bash


mkdir Memoria/
for i in {1..130000}
do 
	echo "CICLO $i"	
	ls -lh |grep "Memoria"
	echo "Hora $i">> Memoria.txt
	date >> Memoria.txt
	free -h >> Memoria.txt
	echo "------------------------------------------------" >> Memoria.txt
	cp Memoria.txt Memoria/Memoria$i.txt	
	sleep 3
	
done

