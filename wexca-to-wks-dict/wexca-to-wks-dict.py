#!/usr/bin/python
# Copyright IBM Corporation 2016,
# LICENSE Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)

import argparse
import csv
import re
import sys

parser = argparse.ArgumentParser(description='Convert the DATA.csv file from an LW dictionary to a WKS-compatible CSV format')
parser.add_argument('inputFile', type=file, help='Location of the LW-formatted DATA.csv file')
parser.add_argument('outputFile', type=argparse.FileType('w'), help='Filename of the output WKS-compatible CSV file that will be created')
args = parser.parse_args()

acronym = re.compile("^[A-Z0-9\-]{1,8}$")

reader = csv.reader(args.inputFile);
writer = csv.writer(args.outputFile);
writer.writerow( [ 'lemma', 'poscode', 'surface'] )

count=0
for row in reader:
  if count > 0 :
    output = []

    parts = row[0].split('\f');
    terms = map( lambda x: x.split('\t')[0].strip(),  parts );
    normalized = map( lambda y: y if acronym.match(y) else y.lower(), terms )

    lemma = normalized[0];
    surfaceforms = set(normalized);

    output.append( lemma );
    output.append( 3 ); # pos code, noun

    for surfaceform in surfaceforms:
      if len( surfaceform ) > 0 :
        output.append( surfaceform );

    writer.writerow( output );

  count = count + 1
