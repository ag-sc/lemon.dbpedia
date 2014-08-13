#Checking the RDF

Once you write a .ldp file you would like to check if it is right. Most typical errors are typos.
What we describe here is a procedure to detect errors in the .ldp files.

##Steps

* Generate the RDF
 * Follow the instructions in <a href="http://github.com/jmccrae/lemon.patterns">lemon.patters</a> to generate a file with triples in the RDF/XML format.
* Store it in a SPARQL endpoint
 *For instance, you can use <A HREF="http://jena.apache.org/documentation/serving_data/index.html">Fuseki</A> (part of Jena) due to its simplicity. In this case, take care of the management of 'empty tags' (you can get an error like this: "The attributes on this property element, are not permitted with any content; expecting end element tag"). You can solve it by transforming the RDF/XML file to N3. The command <a href="http://librdf.org/raptor/rapper.html">rapper<a> can do this. 
* Send some SPARQL queries to the SPARQL endpoint and check the results
  *the files in this folder provides SPARQL queries. E.g. the file verbs contains a SPARQL query that retrieves all the verbs (in lemos terminology) stored in the triple store.  
  *This query shows, for each DBpedia Class (lemon:Reference), its gender and its number (singular/plural). 

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


