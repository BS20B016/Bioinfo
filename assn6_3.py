from Bio.SubsMat import MatrixInfo
import math as m
M = MatrixInfo.blosum62


seq = [
    '-SLSDKDKAAVRALWSKIGKSADAIGNDALSRMIVVYPQTKTYFSHWPDVTPGSPHIKAHGKKVMGGIALAVSKIDDLKTGLMELSEQHAYKLRVDPANFKILNHCILVVISTMFPKEFTPEAHVSLDKFLSGVALALAERYR',
    'MVLSANDKSNVKSIFSKISSHAEEYGAETLERMFTTYPQTKTYFPHF-DLHHGSAQVKAHGKKVAAALIEAANHIDDIAGALSKLSDLHAEKLRVDPVNFKLLGQCFMVVVAIHHPSALTPEIHASLDKFLCAVGNVLTSKYR',
    '-VLSPADKTNIKSTWDKIGGHAGDYGGEALDRTFQSFPTTKTYFPHF-DLSPGSAQVKAHGKKVADALTTAVAHLDDLPGALSALSDLHAYKLRVDPVNFKLLSHCLLVTLACHHPTEFTPAVHASLDKFFAAVSTVLTSKYR',
    'MVLSADDKTNIKNCWGKIGGHGGEYGEEALQRMFAAFPTTKTYFSHI-DVSPGSAQVKAHGKKVADALAKAADHVEDLPGALSTLSDLHAHKLRVDPVNFKFLSHCLLVTLACHHPGDFTPAMHASLDKFLASVSTVLTSKYR',
    '-VLSAADKANVKAAWGKVGGQAGAHGAEALERMFLGFPTTKTYFPHF-NLSHGSDQVKAHGQKVADALTKAVGHLDDLPGALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHHPDDFNPSVHASLDKFLANVSTVLTSKYR',
    'MVLSGEDKSNIKAAWGKIGGHGAEYGAEALERMFASFPTTKTYFPHF-DVSHGSAQVKGHGKKVADALASAAGHLDDLPGALSALSDLHAHKLRVDPVNFKLLSHCLLVTLASHHPADFTPAVHASLDKFLASVSTVLTSKYR',
    'MVLSAADKTNVKAAWSKVGGHAGEYGAEALERMFLGFPTTKTYFPHF-DLSHGSAQVKAHGKKVGDALTLAVGHLDDLPGALSNLSDLHAHKLRVDPVNFKLLSHCLLSTLAVHLPNDFTPAVHASLDKFLSSVSTVLTSKYR',
    'MVLSAADKTNVKAAWSKVGGNAGEFGAEALERMFLGFPTTKTYFPHF-DLSHGSAQVKAHGKKVGDALTLAVGHLDDLPGALSNLSDLHAHKLRVDPVNFKLLSHCLLSTLAVHLPNDFTPAVHASLDKFLSTVSTVLTSKYR',
    'MVLSAADKGNVKAAWGKVGGHAAEYGAEALERMFLSFPTTKTYFPHF-DLSHGSAQVKGHGAKVAAALTKAVEHLDDLPGALSELSDLHAHKLRVDPVNFKLLSHSLLVTLASHLPSDFTPAVHASLDKFLANVSTVLTSKYR',
    'MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHF-DLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR',
    'MVLSPADKTNVKTAWGKVGAHAGDYGAEALERMFLSFPTTKTYFPHF-DLSHGSAQVKDHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR'
]


entropy_scores = []

variance_scores = []

sum_scores = []

i = 0

frequencies = {}

for sq in seq:
    for res in sq:
        if res not in frequencies:
            frequencies[res] = 1
        else:
            frequencies[res] += 1

gaps = 0
gaps = frequencies['-']

total = len(seq)*len(seq[0]) - gaps

while i < len(seq[0]):
    j = 0

    dist_res = {}

    while j < len(seq):
        if seq[j][i] not in dist_res:
            dist_res[seq[j][i]] = 1
        else:
            dist_res[seq[j][i]] += 1
        j += 1

    score_entropy = 0.0

    if len(dist_res.keys()) > 1:
        for key in dist_res:
            if key != '-':
                Gaps = 0
                if '-' in dist_res:
                    Gaps = dist_res['-']
        score_entropy += (float(dist_res[key])/float(len(seq) - Gaps)) * \
            (m.log(
                float((dist_res[key]))/float(len(seq) - Gaps)))

    score_variance = 0.0

    for key in frequencies:
        if key != '-':
            fai = 0
            fa = float(frequencies[key])/float(total)
            Gaps = 0
            if '-' in dist_res:
                Gaps = dist_res['-']
            if key in dist_res:
                fai = float(
                    dist_res[key])/float(len(seq) - Gaps)
            score_variance += (fai - fa)**2

    score_sum = 0.0

    _sums = []

    for key1 in dist_res:
        for key2 in dist_res:
            if key1 != '-' and key2 != '-':
                Gaps = 0
                if '-' in dist_res:
                    Gaps = dist_res['-']
                fai = float(dist_res[key1])/float(len(seq) - Gaps)
                fbi = float(dist_res[key2])/float(len(seq) - Gaps)
                s = 0
                if (key1, key2) in M:
                    s = float(fai*fbi*M[(key1, key2)])
                else:
                    s = float(fai*fbi*M[(key2, key1)])
                if s not in _sums:
                    _sums.append(s)
                    score_sum += s**2

    entropy_scores.append(score_entropy)
    variance_scores.append(m.sqrt(score_variance))
    sum_scores.append(m.sqrt(score_sum))

    i += 1


print("Conservation score from MSA using unweighted frequency and entropy method")
print(entropy_scores)

print("Conservation score from MSA using unweighted frequency and varaince method")
print(variance_scores)

print("Conservation score from MSA using unweighted frequency and sum of pairs method")
print(sum_scores)
