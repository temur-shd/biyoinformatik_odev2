# Entropi bulma
import math
seq1 = "A-TTG-CTT"
seq2 = "ACCTGGC-T"
seq3 = "ACTA-GCTA"
seq4 = "AGTAGCATT"

def entropiHesabı(seq1, seq2, seq3, seq4):
 listx = ['A', 'T', 'G', 'C', '-']  # sekansta bulunan elemanları listye atma

 for i in range(9):
  list = [seq1[i], seq2[i], seq3[i], seq4[i]]
  entropi = 0
  list1 = [list.count('A'), list.count('T'), list.count('G'), list.count('C'), list.count('-')]
  for k in list1:
   p = k / len(list)
   if p != 0.0:
    entropi += (p * math.log10(p))
  if entropi != 0:
   print(i + 1, " sütunun entropisi {:.5f}".format(-entropi))
  else:
   print(i + 1, " sütunun entropisi", entropi)

entropiHesabı(seq1, seq2, seq3, seq4)

"""


def entropiHesapla(sekans1,sekans2,sekans3,sekans4):
 list = ['A', 'T', 'G', 'C', '-']


 for i in range(9):
  list=[sekans1[i],sekans2[i],sekans3[i],sekans4[i]]
  entropi = 0
  list1 = [list.count('A'),list.count('T'),list.count('G'),list.count('C'), list.count('-')]
  for k in list1:
      p=k/len(list)
      if p!=0.0:
       entropi+=(p*math.log10(p))
  if entropi!=0:
   print(i+1," sütunu için entropi {:.2f}".format(-entropi))
  else:
   print(i+1," sütunu için entropi",entropi)
         
 entropiHesapla(sekans1,sekans2,sekans3,sekans4)
 """
