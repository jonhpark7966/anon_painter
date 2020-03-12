#!/bin/bash

echo "usage: ./crop.sh IMAGE_NAME CROP_PIXELS OVERLAP_PIXELS "

INPUT_IMAGE=$1
CROP_PIXELS=$2
OVERLAP_PIXELS=$3
WIDTH=`convert $INPUT_IMAGE -print "%w" /dev/null`
HEIGHT=`convert $INPUT_IMAGE -print "%h" /dev/null`
echo "$INPUT_IMAGE : $WIDTH x $HEIGHT"

X_POS=0
Y_POS=0
counter=0
while [ $Y_POS -lt $HEIGHT ]
do
  while [ $X_POS -lt $WIDTH ]
  do
    convert $INPUT_IMAGE -crop $CROP_PIXELS\x$CROP_PIXELS+$X_POS+$Y_POS $counter.jpg
    counter=$(( $counter + 1 ))
    X_POS=$(( $X_POS + $OVERLAP_PIXELS  ))
  done
  X_POS=0
  Y_POS=$(( $Y_POS  +  $OVERLAP_PIXELS  ))
done
