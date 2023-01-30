#Sum of Pairs skorunu hesaplayan (İkili seqların edit uzaklık toplamı.)
seq1 ="A-TTG-CTT"
seq2="ACCTGGC-T"
seq3="ACTA-GCTA"
seq4="AGTAGCATT"

def editDistance(str1, str2, m, n):
    if m == 0:       # Eğer ilk string boşsa ikinci dizenin tüm karakterlerini birinciye ekleme
        return n
    if n == 0:  #Eğer ikinci string boşsa ilk dizenin tüm karakterlerini ikinciye ekleme
        return m

    #İki dizenin son karakterleri aynıysa,son karakterleri yoksayın ve kalan dizelerin sayısını alma.
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

    # Son karakterler aynı değilse, ilk dizenin son karakterindeki üç işleminden
    # yinelemeli olarak minimum maliyeti hesaplama.
    return 1 + min(editDistance(str1, str2, m, n - 1),
                   editDistance(str1, str2, m - 1, n),
                   editDistance(str1, str2, m - 1, n - 1)
                   )

def sumOfPairs(seq1,seq2,seq3,seq4):
    len1 = len(seq1)
    len2 = len(seq2)
    len3 = len(seq3)
    len4 = len(seq4)
    x=editDistance(seq1,seq2,len1,len2)
    y=editDistance(seq1, seq3, len1, len3)
    z=editDistance(seq1, seq4, len1, len4)
    k=editDistance(seq2, seq3, len2, len3)
    l=editDistance(seq2, seq4, len2, len4)
    m=editDistance(seq3, seq4, len3, len4)
    return x+y+z+k+l+m

print('İkili sekansların edit uzaklık toplamı:',sumOfPairs(seq1,seq2,seq3,seq4))
