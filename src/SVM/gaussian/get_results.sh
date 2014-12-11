#!/bin/bash

files=$(ls *.o*)

if [ $# -gt 0 ]
then
    outfile=$1
    echo "Writing results to "$file
    rm $file
    echo -e "C\t\tGamma\t\tTrain\t\tTest\t\tGalaxies\tStars\t\tRatio" > $file
fi

echo -e "C\t\tGamma\t\tTrain\t\tTest\t\tGalaxies\tStars\t\tRatio"
for file in $files
do 
    c=$(echo $file | cut -d 'c' -f 2 | cut -d '-' -f 1)
    gamma=$(echo $file | cut -d 'g' -f 3 | cut -d '.' -f 1,2)
    vals=$(cat $file | grep -B 2 -A 5 "Stars" | grep -v "Stars" | grep -v "Galaxies")
    train=$(echo $vals | awk '{print $1}')
    test=$(echo $vals | awk '{print $2}')
    stars=$(echo $vals | awk '{print $4}')
    gals=$(echo $vals | awk '{print $6}')
    got=$(echo $test | grep -c ".")
    if [ $got -ge 1 ]
    then
	ratio=$(echo "scale=4;$train/$test" | bc)

	echo -e $c"    \t"$gamma"    \t"$train"\t"$test"\t"$gals"\t"$stars"\t"$ratio
	if [ $# -gt 0 ]
	then
	    echo -e $c"    \t"$gamma"    \t"$train"\t"$test"\t"$gals"\t"$stars"\t"$ratio >> $file
	fi
    else
	echo -e $c"    \t"$gamma"    \t0.00\t\t0.00\t\t0.00\t\t0.00\t\t1.00"
	if [ $# -gt 0 ]
        then
	    echo -e $c"    \t"$gamma"    \t0.00\t0.00\t0.00\t0.00\t1.0" >> $file
	fi
    fi
done
