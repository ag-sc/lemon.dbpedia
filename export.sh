#!/bin/bash

if [[ -z "$1" ]] 
then
  echo >&2 "Required argument: language folder (e.g. en)" 
  exit 1
fi

for file in $1/*.ldp
do 
    echo 'Converting patterns in '$file'...' 
    name=${file#*\/}
    lemonpatterns $file target/tmp/${name/.ldp/.rdf}
done

python RDFmerger.py $1 $1/extra.ttl $1/references.ttl target/tmp/ 'target/dbpedia_'$1'.rdf'

rm target/tmp/*
