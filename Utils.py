from typing import List
import pandas as pd
import re



def docs_to_sentences(csvpath:str   ):
    """Limpia texto y separa el verso en oraciones"""
    df_docs = pd.read_csv(csvpath)
    df_sentences = pd.DataFrame(columns=['sentence']) 
    for poem in df_docs['nombre']:
        clean=cleanTitles(str(poem))
        clean=clean.split('\n')
        clean=cleanList(clean)
        print(clean)
        for s in clean:
            if len(s)>0:
                df_sentences=df_sentences.append({"sentence": s}, ignore_index=True)
    print(df_sentences)
    df_sentences.to_csv('sentences.csv',index=False)


def cleanTitles(poem:str)->str:
    return ''.join(re.split(r",",poem)[1:])
    
def cleanList(listVerso:List[str])->List[str]:
    return [cleanGarbage(verso) for verso in listVerso]

def cleanGarbage(verso:str)->str:
    cleanverso=verso.lower()
    cleanverso=re.sub('[^a-zA-Z\u00C0-\u00FF]', ' ', cleanverso)
    cleanverso=cleanverso.strip()
    return cleanverso
