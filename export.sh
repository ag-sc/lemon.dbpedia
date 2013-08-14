#!/bin/bash

if [[ -z "$1" ]] 
then
  echo >&2 "Required argument: language folder (e.g. en)" 
  exit 1
fi

mkdir target/tmp

for file in $1/*.ldp
do 
    echo 'Converting patterns in '$file'...' 
    name=${file#*\/}
    lemonpatterns $file target/tmp/${name/.ldp/.rdf}
done

LINKS=linking/dbpedia_$1_wn.nt
if [[ -f $LINKS ]];
then
   python RDFmerger.py $1 $1/extra.ttl references.ttl $LINKS target/tmp/ 'target/dbpedia_'$1'.rdf'
else
   python RDFmerger.py $1 $1/extra.ttl references.ttl target/tmp/ 'target/dbpedia_'$1'.rdf'
fi

rm target/tmp/*
rmdir target/tmp
