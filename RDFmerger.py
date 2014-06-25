
import rdflib as rdf
from   rdflib import URIRef, Literal, Namespace, RDF, XSD

from sys import argv,exit
from os  import listdir
from os.path import isfile
import re


lemon = Namespace("http://lemon-model.net/lemon#")


def frag_uri(uri):
    if not ':/' in unicode(uri): return unicode(uri)
    else: return re.match('.*/([^/]+\#)?([^/]+)$',unicode(uri)).group(2)


def run():

  files = []
  for a in argv[2:-1]:
      if isfile(a):
         files.append(a)
      else: 
         for f in listdir(a):
             if not f.endswith("gitignore") and not f.endswith("~"):
                files.append(a+f)

  graph = rdf.Graph()
  for f in files:
      print 'Loading ' + str(f) + '...'
      if f.endswith('.owl') or f.endswith('.rdf'):
         graph = graph.parse(f)
      elif f.endswith('.ttl') or f.endswith('.n3') or f.endswith('.nt'):
         graph = graph.parse(f,format='n3') 
      else: 
         print 'Unknown format: ' + str(f)
         exit(1)

  lexicon = URIRef("http://github.com/cunger/lemon.dbpedia/target/dbpedia_"+argv[1]+"#")

  print 'Merging lexica into <'+str(lexicon)+'>...'

  for l,_,_ in graph.triples((None,RDF.type,lemon.Lexicon)):
      print l # DEBUG
      for s,p,o in graph.triples((l,RDF.type,lemon.Lexicon)):
          graph.remove((s,p,o))
      for s,p,o in graph.triples((l,lemon.language,None)):
          graph.remove((s,p,o))
      for s,p,o in graph.triples((l,lemon.entry,None)):
          graph.remove((s,p,o))
          graph.add((lexicon,p,o))

  graph.add((lexicon,RDF.type,lemon.Lexicon))
  graph.add((lexicon,lemon.language,Literal(argv[1],datatype=XSD.string)))

  print 'Serializing...'

  result_file = argv[-1:][0]

  out = open(result_file,'w')
  out.write(graph.serialize()+'\n\n')
  out.close()

  print 'Done: ' + str(result_file)

  print 'Generating URI list...' 

  allURIs  = []
  doneURIs = []
  for line in open('allURIs','r').readlines():
      allURIs.append(line.strip())

  for s,p,o in graph:
      if unicode(s).startswith('http://dbpedia.org') and frag_uri(s) in allURIs and not frag_uri(s) in doneURIs:
         doneURIs.append(frag_uri(s))
      if unicode(p).startswith('http://dbpedia.org') and frag_uri(p) in allURIs and not frag_uri(p) in doneURIs:
         doneURIs.append(frag_uri(p))
      if unicode(o).startswith('http://dbpedia.org') and frag_uri(o) in allURIs and not frag_uri(o) in doneURIs:
         doneURIs.append(frag_uri(o))

  out_done = open(argv[1]+'_lexicalizedURIs','w')
  for uri in doneURIs: out_done.write(uri+'\n')
  out_done.close()
  out_todo = open(argv[1]+'_todoURIs','w')
  for uri in list(set(allURIs)-set(doneURIs)): out_todo.write(uri+'\n')
  out_todo.close()

  print 'Done.'


## MAIN #########

if __name__ == "__main__":
   run()

