#!/bin/bash

rm -f Zones.yaml

python ZoneParser.py ZoneParser.txt > Zones.yaml
