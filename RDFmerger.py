import rdflib as rdf
from sys import argv,exit
from os  import listdir
from os.path import isfile



files = []
for a in argv[1:-1]:
     if isfile(a):
        files.append(a)
     else: 
        for f in listdir(a):
            files.append(a+f)

graph = rdf.Graph()
for f in files:
    print 'Loading ' + str(f) + '...'
    if f.endswith('.owl') or f.endswith('.rdf'):
       graph.parse(f)
    elif f.endswith('.ttl') or f[:-3] in ('.n3','.nt'):
       graph.parse(f,format='n3') 
    else: 
       print 'Unknown format: '+f
       exit(1)
 
# TODO compile list of lexicalized DBpedia URIs

print 'Serializing...'

result_file = argv[-1:][0]

out = open(result_file,'w')
out.write(graph.serialize()+'\n\n')
out.close()

print 'Done: ' + result_file
