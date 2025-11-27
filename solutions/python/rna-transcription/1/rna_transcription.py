def convert(nucleotide):
    convertion = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
        'A' : 'U'
    }
    return convertion[nucleotide]
    
def to_rna(dna_strand):
    rna_strand = []
    for item in dna_strand:
        rna_strand.append(convert(item))

    return ''.join(rna_strand)