import java.io.FileInputStream
import java.util.zip.GZIPInputStream

if(args.length != 2) {
  System.err.println("Usage: scala link-models.scala from.nt[.gz] to.nt[.gz] > links.nt")
  System.exit(-1);
}

val model1 = args(0) endsWith ".gz" match {
  case true => io.Source.fromInputStream(new GZIPInputStream(new FileInputStream(args(0))))
  case false => io.Source.fromFile(args(0))
}

val model2 = args(1) endsWith ".gz" match {
  case true => io.Source.fromInputStream(new GZIPInputStream(new FileInputStream(args(1))))
  case false => io.Source.fromFile(args(1))
}

case class WordWithPOS(val lemma : String, val pos : String)

def emitWordsWithPOS(model : io.Source) : Set[(String,WordWithPOS)] = {
  val form2rep = collection.mutable.Map[String,String]()
  val lex2form = collection.mutable.Map[String,String]()
  val lex2pos = collection.mutable.Map[String,String]()

  for(line <- model.getLines) {
    val ss = line split "\\s+"

    if(ss(1) == "<http://www.monnet-project.eu/lemon#writtenRep>") {
      val obj = if(ss.length > 4) {
        ss.slice(2,ss.length-1) mkString (" ")
      } else {
        ss(2)
      }
      form2rep put (ss(0),obj.replaceAll("@en$","@eng"))
    } else if (ss(1) == "<http://www.monnet-project.eu/lemon#canonicalForm>") {
      lex2form put (ss(0),ss(2))
    } else if (ss(1) matches ".*#partOfSpeech>") {
      lex2pos put (ss(0),ss(2).substring(ss(2).indexOf("#")+1))
    }
  }

  lex2form flatMap {
    case (lex,form) => {
      if((form2rep contains form) && (lex2pos contains lex)) {
        Some((lex,WordWithPOS(form2rep(form),lex2pos(lex))))
      } else {
        None
      }
    }
  } toSet
}

val m1words = emitWordsWithPOS(model1)
val m2words = emitWordsWithPOS(model2)

val cowords = (m1words ++ m2words) groupBy (_._2)

for(key <- cowords.keys) {
  for(val1 <- cowords(key)) {
    for(val2 <- cowords(key)) {
      if(val1._1 != val2._1) {
        println(val1._1 + " <http://www.w3.org/2000/01/rdf-schema#seeAlso> " + val2._1)
      }
    }
  }
}
