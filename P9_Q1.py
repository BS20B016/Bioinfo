def Q1(Seq1, Seq2):
      AminoAcid_Seq1 = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0,'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}
      AminoAcid_Seq2 = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0,'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}
      Hamming_Dis_AB, Euclidean_Dis_AB = 0, 0
      d1 = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L','M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
      for i in Seq1:
            AminoAcid_Seq1[i] += 100 / len(Seq1)
      for j in Seq2:
            AminoAcid_Seq2[j] += 100 / len(Seq2)
      for k in range(20):
            d = AminoAcid_Seq1[d1[k]] - AminoAcid_Seq2[d1[k]]
            Hamming_Dis_AB += abs(d) 
            Euclidean_Dis_AB += d ** 2
            Euclidean_Dis_AB = Euclidean_Dis_AB ** 0.5
      return Hamming_Dis_AB, Euclidean_Dis_AB
if __name__ == '_main_':
    Seq1 ='AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA'
    Seq2 ='AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI'
    Seq3 ='MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA'
    Hamming_Dis_12, Euclidean_Dis_12 = Q1(Seq1, Seq2)
    Hamming_Dis_23, Euclidean_Dis_23 = Q1(Seq2, Seq3)
    Hamming_Dis_31, Euclidean_Dis_31 = Q1(Seq3, Seq1)
    st = '{:<25} {:<25} {:<25}'
    print(st.format('Pair', 'Hamming Distance', 'Euclidian Distance'))
    print(st.format('Seq 1 and Seq 2', Hamming_Dis_12, Euclidean_Dis_12))
    print(st.format('Seq 2 and Seq 3', Hamming_Dis_23, Euclidean_Dis_23))
    print(st.format('Seq 3 and Seq 1', Hamming_Dis_31, Euclidean_Dis_31))