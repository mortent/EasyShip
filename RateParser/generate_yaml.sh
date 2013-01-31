#!/bin/bash

rm -f Rates.yaml

touch Rates.yaml

python RateParser.py -s 1 -p 1 Datafiles/UPS_Ground.txt >> Rates.yaml
python RateParser.py -s 2 -p 1000 Datafiles/UPS_3_Day_Select.txt >> Rates.yaml
python RateParser.py -s 3 -p 2000 Datafiles/UPS_2nd_Day_Air.txt >> Rates.yaml
python RateParser.py -s 4 -p 3000 Datafiles/UPS_2nd_Day_Air_AM.txt >> Rates.yaml
python RateParser.py -s 5 -p 4000 Datafiles/UPS_Next_Day_Air_Saver.txt >> Rates.yaml
python RateParser.py -s 6 -p 5000 Datafiles/UPS_Next_Day_Air.txt >> Rates.yaml