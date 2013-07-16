# <a href="http://lemon-model.net/">lemon</a> lexica for <a href="http://dbpedia.org">DBpedia</a> 

The folder `en` contains the development version of an English lexicon for the DBpedia 3.8 ontology. 
It comprises several LDP files with entries using the <a href="https://github.com/jmccrae/lemon.patterns">lemon design patterns</a>
and pooled by domain (persons, organizations, arts and entertainment, animals and plants, etc.), 
together with a file containing all entries that could not be created using those patterns 
but only by writing lemon RDF triples (`extra.ttl`), as well as a file that defines classes and properties 
that are not part of the DBpedia ontology but are used in the lexicalizations (`references.ttl`). 
German and Spanish versions will be added soon.

In order to create a single RDF lexicon file, run the `export` script with the language folder as argument: 

```
$ ./export.sh en
```

This requires:

* <a href="https://github.com/jmccrae/lemon.patterns">lemon.patterns</a>
* Python with <a href="https://github.com/RDFLib/rdflib">rdflib</a>

The file `allURIs` contains a list of all URIs in the DBpedia 3.8 ontology (schema but no instance data). 
Exporting the English lexicon creates the files `en_lexicalizedURIs` (all URIs that occur in the lexicalizations) 
and `en_todoURIs` (all URIs that do not yet occur in any lexicalization).

Further, the `statistics.py` script outputs the number of verbalizations (per classes, properties and total)
as well as the average number of entries and their distribution. 

## Latest release

**Version 1 (July 2013)**

The first release of the English lexicon for DBpedia 3.8 covers 353 classes 
as well as 300 properties (all those that have more than 10,000 occurrences in the DBpedia dataset, 
with only a few exceptions).

* Total lexicalizations: 1,216 (1.8 entries per concept)
* Class lexicalizations: 443 (1.3 entries per class)
* Property lexicalizations: 773 (2.4 entries per property)

Published on: <a href="http://lemon-model.net/lexica/dbpedia_en">lemon-model.net/lexica/dbpedia_en</a> 
(under <a href="https://creativecommons.org/licenses/by/3.0/">Creative Commons BY 3.0</a> license)

## Want to contribute?

If you want to help to improve and extend the lexicon, if you want to port it to others languages,
 or if you are using the lexicon, we'd love to hear from you!
