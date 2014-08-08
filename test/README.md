#Checking the RDF

Once you write a .ldp file you would like to check if it is right. Most typical errors are typos.
What we describe here is a procedure to detect errors in the .ldp files.

##Steps

* Generate the RDF
* Store it in a SPARQL endpoint
* Send some SPARQL queries to the SPARQL endpoint and check the results

## Learn by example
This is an example for the Spanish lexicalization of DBpedia.

### Generation of RDF

### Storing the RDF in a SPARQL endpoint (by using Jena Fuseki)

### Make some queries to find out errors

This query shows the DBpedia Classes, its gender and its form (singular/plural). 

```
prefix lexinfo: <http://www.lexinfo.net/ontology/2.0/lexinfo#>
prefix lemon: <http://lemon-model.net/lemon#>
select ?dbres ?singular ?genero ?plural where {
  ?s lemon:reference  ?dbres .
   filter (strstarts(str(?dbres), "http://dbpedia.org/ontology")) .
  ?s lemon:reference  ?dbres .
  ?noun lemon:sense ?s .
  ?noun lemon:canonicalForm ?canonical .
  ?canonical lemon:writtenRep ?singular .
  ?noun lexinfo:gender ?genero .
  ?noun lemon:otherForm ?other .
  ?other lemon:writtenRep ?plural .
}
```


