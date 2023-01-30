""""
A-TTG-CTT
ACCTGGC-T
ACTA-GCTA
AGTAGCATT
Yukarıdaki sekansları için
a)	Entropi hesabını yapan (**************)
b)	Sum of Pairs skorunu hesaplayan (İkili sekansların edit uzaklık toplamı.)
c)	Konsensüs sekansı bulan (***************)
bilgisayar programını Python dili ile yazınız."""
import math

seq1 ="A-TTG-CTT"
seq2 ="ACCTGGC-T"
seq3 ="ACTA-GCTA"
seq4 ="AGTAGCATT"

#a)##################################################3
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

#b)#########################################
def editDistance(str1, str2, m, n):
 if m == 0:  # Eğer ilk string boşsa ikinci dizenin tüm karakterlerini birinciye ekleme
  return n
 if n == 0:  # Eğer ikinci string boşsa ilk dizenin tüm karakterlerini ikinciye ekleme
  return m

 # İki dizenin son karakterleri aynıysa,son karakterleri yoksayın ve kalan dizelerin sayısını alma.
 if str1[m - 1] == str2[n - 1]:
  return editDistance(str1, str2, m - 1, n - 1)

 # Son karakterler aynı değilse, ilk dizenin son karakterindeki üç işlemi den
 # yinelemeli olarak minimum maliyeti hesaplama.
 return 1 + min(editDistance(str1, str2, m, n - 1),
                editDistance(str1, str2, m - 1, n),
                editDistance(str1, str2, m - 1, n - 1)
                )


def sumofPairs(seq1, seq2, seq3, seq4):
 len1 = len(seq1)
 len2 = len(seq2)
 len3 = len(seq3)
 len4 = len(seq4)
 x = editDistance(seq1, seq2, len1, len2)
 y = editDistance(seq1, seq3, len1, len3)
 z = editDistance(seq1, seq4, len1, len4)
 k = editDistance(seq2, seq3, len2, len3)
 l = editDistance(seq2, seq4, len2, len4)
 m = editDistance(seq3, seq4, len3, len4)
 return x + y + z + k + l + m


print('İkili sekansların edit uzaklık toplamı:', sumofPairs(seq1, seq2, seq3, seq4))

#c)#################################################


seqList = ['A-TTG-CTT',
           'ACCTGGC-T',
           'ACTA-GCTA',
           'AGTAGCATT']
n = len(seqList[0])
profile = { 'T':[0]*n,'G':[0]*n ,'C':[0]*n,'A':[0]*n,'-':[0]*n }

for seq in seqList:
    for i, char in enumerate(seq):  # nesneleri numaralandırmak için kullanılır
        profile[char][i] += 1
consensus = ""

for i in range(n):
    max_count = 0
    max_nt = ' '
    for nt in "ACGT":   #sekanslarda hangi elemanın max sayıda olduğunu bulma.
        if profile[nt][i] > max_count:
            max_count = profile[nt][i]
            max_nt = nt
    consensus += max_nt
print(consensus)

for key, value in profile.items():  #items tuple çiftlerinin bir listesini görüntüleyen bir görünüm nesnesi döndürür
     print(key,':', " ".join([str(x) for x in value] )) #.join alt dizgilerden bir dizgi oluşturmak için






