#!/bin/bash


for sourcefile in ./sources/*.jpg; do
  for stylefile in ./styles_test/*; do
    tmp=${sourcefile##*/}
    sourceprefix=${tmp%.*} 
    stylepostfix=${stylefile##*/}
    echo $sourceprefix$stylepostfix
    python ./style_transfer/style_transfer.py $sourcefile $stylefile ./results/$sourceprefix$stylepostfix
  done
done
