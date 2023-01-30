
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


"""
sekans1 = "A-TTG-CTT"
sekans2 = "ACCTGGC-T"
sekans3 = "ACTA-GCTA"
sekans4 = "AGTAGCATT"


def konsensus(sekans1,sekans2,sekans3,sekans4):
    konsensus=" "
    dic={ }
    for i in range(9):
     liste=[sekans1[i],sekans2[i],sekans3[i],sekans4[i]]
     A=liste.count('A')
     T=liste.count('T')
     G=liste.count('G')
     C=liste.count('C')
     tire=liste.count('-')
     eleman=max(A,T,G,C,tire)
     dic={A:'A',T:'T',C:'C',G:'G',tire:'-'}

     konsensus+=(dic[eleman])
    print(konsensus)
"""