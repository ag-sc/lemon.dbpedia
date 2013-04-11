@prefix dbpedia: <http://dbpedia.org/ontology/> .
@prefix lex: <http://github.com/cunger/lemon.dbpedia/target/dbpedia_en#> .

Lexicon(<http://github.com/cunger/lemon.dbpedia/target/dbpedia_en#>,"en",

  // Classes

  ClassNoun("protein",dbpedia:Protein),
  ClassNoun(["chemical"/adjective "compound"/noun],dbpedia:ChemicalCompound),
  ClassNoun("disease",dbpedia:Disease),
  ClassNoun("illness",dbpedia:Disease),
  ClassNoun("sickness",dbpedia:Disease),
  ClassNoun("drug",dbpedia:Drug),
  ClassNoun("medicine",dbpedia:Drug),
  ClassNoun("medicament",dbpedia:Drug),
  ClassNoun("pharmaceutical",dbpedia:Drug),
  ClassNoun("bacteria",dbpedia:Bacteria),
  ClassNoun("bacillus",dbpedia:Bacteria),
  ClassNoun("germs",dbpedia:Bacteria),
  ClassNoun(["anatomical"/adjective "structure"/noun],dbpedia:AnatomicalStructure),
  ClassNoun("brain",dbpedia:Brain),
  ClassNoun("bone",dbpedia:Bone),
  ClassNoun("artery",dbpedia:Artery),
  ClassNoun("vein",dbpedia:Vein),
  ClassNoun(["blood"/noun "vessel"/noun],lex:BloodVessel),
  ClassNoun("muscle",dbpedia:Muscle),
  ClassNoun("nerve",dbpedia:Nerve),
  ClassNoun("lymph",dbpedia:Lymph)

)
