from __future__ import division
import rdflib as rdf
from   rdflib import URIRef
import re


def frag_uri(uri):
    if not ':/' in str(uri): return str(uri)
    else: return re.match('.*/([^/]+\#)?([^/]+)$',str(uri)).group(2)


def run():

  lexicon = 'target/dbpedia_en.rdf'

  graph = rdf.Graph()
  graph = graph.parse(lexicon)


  dontcount = ['propertyDomain','propertyRange','someValuesFrom','first']

  number_cs = dict()
  number_ps = dict()

  number_entries = 0

  uris = []
  for line in open('en_lexicalizedURIs','r').readlines():
      uris.append(line.strip())
      if line.strip()[0].isupper():
         number_cs[line.strip()] = 0
      else:
         number_ps[line.strip()] = 0

  for s,p,o in graph:
      if str(o).startswith('http://dbpedia.org'):
         uri = frag_uri(o) 
         skip = False
         for dont in dontcount:
             if dont in str(p): 
                skip = True
                break
         if uri in uris and not skip:
            if number_cs.has_key(uri):
               number_cs[uri] = number_cs[uri] + 1
            if number_ps.has_key(uri):
               number_ps[uri] = number_ps[uri] + 1

  print 'COUNTS \n' 
  print '==== Classes ===================\n'
  for k in number_cs.keys():
      print k + ': ' + str(number_cs[k])
  print '==== Properties ================\n'
  for k in number_ps.keys():
      print k + ': ' + str(number_ps[k])

  distribution_cs = dict()
  distribution_ps = dict()
  
  for k in number_cs.keys():
      v = number_cs[k]
      if distribution_cs.has_key(v):
         distribution_cs[v] = distribution_cs[v] + 1
      else:
         distribution_cs[v] = 1
  for k in number_ps.keys():
      v = number_ps[k]
      if distribution_ps.has_key(v):
         distribution_ps[v] = distribution_ps[v] + 1
      else:
         distribution_ps[v] = 1

  c_lex = 0
  p_lex = 0
  for k,v in distribution_cs.items():
      c_lex += k*v
  for k,v in distribution_ps.items():
      p_lex += k*v

  print '\n\n---------------------------------------------'
  print 'Total    lexicalizations: ' + str(c_lex+p_lex) + ' (' + str((c_lex+p_lex)/(len(number_cs)+len(number_ps))) + ' per concept)'
  print 'Class    lexicalizations: ' + str(c_lex) + ' (' + str(c_lex/len(number_cs)) + ' per class)'
  print 'Property lexicalizations: ' + str(p_lex) + ' (' + str(p_lex/len(number_ps)) + ' per property)'
  print '---------------------------------------------'

  # CHECK
  for _,_,o in graph.triples((None,URIRef("http://www.monnet-project.eu/lemon#entry"),None)):
      number_entries += 1

  print 'Actually counted ' + str(number_entries) + ' entries...'

  print '\n'
  print 'DISTRIBUTION \n' 
  print '==== Classes ===================\n'
  for k in distribution_cs.keys():
      print str(k) + ': ' + str(distribution_cs[k])
  print '==== Properties ================\n'
  for k in distribution_ps.keys():
      print str(k) + ': ' + str(distribution_ps[k])


## MAIN #########

if __name__ == "__main__":
   run()

