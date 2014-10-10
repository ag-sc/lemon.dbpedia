#Checking the RDF

Once you write a .ldp file you would like to check if it is right. Most typical errors are typos.
What we describe here is a procedure to detect errors in the .ldp files.

##Steps

* Generate the RDF
 * Follow the instructions in <a href="http://github.com/jmccrae/lemon.patterns">lemon.patters</a> to generate a file with triples in the RDF/XML format. You will get error messages, for instance, if you typed 'femenine' instead of 'feminine' in the .ldp file.
* Store it in a SPARQL endpoint
 * For instance, you can use <A HREF="http://jena.apache.org/documentation/serving_data/index.html">Fuseki</A> (part of Jena) due to its simplicity. In this case, take care of the management of 'empty tags' (you can get an error like this: "The attributes on this property element, are not permitted with any content; expecting end element tag"). You can solve it by transforming the RDF/XML file to N3. The command <a href="http://librdf.org/raptor/rapper.html">rapper<a> can do this. 
* Send some SPARQL queries to the SPARQL endpoint and check the results
  * the files in this folder provides SPARQL queries. E.g. the file verbs contains a SPARQL query that retrieves all the verbs (in <a href="http://lemon-model.net/">lemon</a> terminology) stored in the triple store.  
  * This query shows, for each DBpedia Class (lemon:Reference) in the triple store, its gender and its number (singular/plural). 

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
ORDER BY ASC(?dbres)
```
  * This query shows the stateVerbs in the dataset. Providing information about the subject and the object of the property

```
prefix lexinfo: <http://www.lexinfo.net/ontology/2.0/lexinfo#>
prefix lemon: <http://lemon-model.net/lemon#>
select distinct ?stateVerbWrittenRep ?subProp_CanonicalFormWrittenVal  ?subProp_PartOfSpeechVal ?objProp_CanonicalFormWrittenVal ?objProp_PartOfSpeechVal where{
{
  ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>  lemon:LexicalEntry .
  ?s lexinfo:partOfSpeech  lexinfo:verb .
  ?s lemon:canonicalForm  ?canonicalFormVerb .
  ?canonicalFormVerb lemon:writtenRep ?stateVerbWrittenRep .
  ?s lemon:sense ?sense .
  ?sense lemon:subjOfProp ?subOfProp .
  ?subOfProp       lemon:marker ?subOfPropValue .
  ?subOfPropValue  lexinfo:partOfSpeech ?subProp_PartOfSpeechVal .
  ?subOfPropValue  lemon:canonicalForm ?subCanForm .
  ?subCanForm       lemon:writtenRep ?subProp_CanonicalFormWrittenVal .
}union
{
  ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>  lemon:LexicalEntry .
  ?s lexinfo:partOfSpeech  lexinfo:verb .
  ?s lemon:canonicalForm  ?canonicalFormVerb .
  ?canonicalFormVerb lemon:writtenRep ?stateVerbWrittenRep .
  ?s lemon:sense ?sense .
  ?sense lemon:reference ?ref .
  ?sense lemon:objOfProp ?objOfProp .
  ?objOfProp       lemon:marker ?objOfPropValue .
  ?objOfPropValue  lexinfo:partOfSpeech ?objProp_PartOfSpeechVal .
  ?objOfPropValue  lemon:canonicalForm ?canForm .
  ?canForm         lemon:writtenRep ?objProp_CanonicalFormWrittenVal 
}
}
ORDER BY ASC (?stateVerbWrittenRep)
```
