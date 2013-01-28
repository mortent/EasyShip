#!/bin/bash

rm Ground.yaml
rm 3_Day_Select.yaml

python RateParser.py -s 1 -p 1 Datafiles/UPS_Ground.txt > Ground.yaml
python RateParser.py -s 2 -p 500 Datafiles/UPS_3_Day_Select.txt > 3_Day_Select.yaml
