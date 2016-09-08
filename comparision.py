import json
import random

quality = '''{
  "standardSequence": {
    "coding": [
      {
        "system": "https://precision.fda.gov/files/",
        "code": "Bk50V4Q0qVb65P0v2VPbfYPZ"
      }
    ]
  },
  "start": 10453,
  "end": 101770080,
  "method": {
    "coding": [
      {
        "system": "https://precision.fda.gov/jobs/",
        "code": "ByxYPx809jFVy21KJG74Jg3Y"
      }
    ],
    "text": "Vcfeval + Hap.py Comparison"
  },
  "truthTP": 7749,
  "queryTP": 7984,
  "truthFN": 2554,
  "queryFP": 10670,
  "gtFP": 2186,
  "precision": 0.428005,
  "recall": 0.752111,
  "fScore": 0.545551
}'''

resource = '''
{'variant': [{'end': 8, 'referenceAllele': 'TGGTTTT', 'start': 1, 'observedAllele': 'CCCGTGG'}, {'end': 481, 'referenceAllele': 'GTGCGTC', 'start': 474, 'observedAllele': 'CCGGCTT'}, {'end': 1422, 'referenceAllele': 'TGTCTGGCCC', 'start': 1412, 'observedAllele': 'GTGTGTCCGC'}, {'end': 3357, 'referenceAllele': 'CGCCCTT', 'start': 3350, 'observedAllele': 'TGTTTCC'}, {'end': 5250, 'referenceAllele': 'CC', 'start': 5248, 'observedAllele': 'GT'}], 'referenceSeq': {'windowEnd': 101770080, 'windowStart': 10453, 'referenceSeqId': {'coding': [{'code': 'NC_000001.11', 'system': 'http://www.ncbi.nlm.nih.gov/nuccore'}]}, 'strand': 1}, 'method': 'VCF Comparison', 'standard_sequence': ['NA12878-NISTv2.19', 'NA12878-GIABv3.2']}
'''

def comparision(resource):
    qualitys = []
    for std in resource['standard_sequence']:
        tmp = json.loads(quality)
        tmp['standardSequence']['text'] = std
        tmp['truthTP'] = random.randint(1000,10000)
        tmp['queryTP'] = random.randint(1000,10000)
        tmp['truthFN'] = random.randint(1000,10000)
        tmp['queryFP'] = random.randint(1000,10000)
        tmp['gtFP'] = random.randint(1000,5000)
        tmp['precision'] = random.random()
        tmp['recall'] = random.random()
        tmp['fScore'] = random.random()
        qualitys.append(tmp)
    dic = {}
    dic['quality'] = qualitys
    return json.loads(json.dumps(dic))


