DNA_NUCLEOBASES = {"A", "C", "G", "T", "a", "c", "g", "t"}

dna_sample1 = "ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAGGGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCC" \
      "AGAGGCGGGGGGGCAGCCGGGTGGGGCAGCGGGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGGNNNAGGGT" \
      "AGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCCCCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCg" \
      "agacAGGTGATCTGTTGACCTGAAACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCTCCACGTGTGTGTACAG" \
      "CCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGAGGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGAT" \
      "GACGGCATNNGCGATGGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACGGCGCTCATGTCACtcaccgtcagc" \
      "ggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTCGCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAG" \
      "CCTGCGCCAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTGGGGCGTGAGCAGGGGGGTTGGACAtttAGTCT" \
      "CCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCACAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNCG" \
      "CATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCCTGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACG" \
      "TACATCCCCTGTTCcggCCAACACACAGACATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACAGGCAACACA" \
      "CACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCCCTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGT" \
      "GGAGCACCAGGCACGGAGCTGGTTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNNTGTCAGTGCCGCCGTGT" \
      "GGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAGACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGC" \
      "ACAGAGGAGAGAGGCCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGACGGTGAAGTAGCTTCG-GGCGTTGG" \
      "GTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACGGTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCN" \
      "CCAGCC"


def delete_n(seq=""):
    """
    Deletes "N" and "n" from sequence as "N" stands for misread that has been corrected:
    Laser goes back to the misread nucleobase so there's no gap in data
    :param seq: any DNA sequence
    :return: seq without "N" and "n"
    """
    return seq.replace("N", "").replace("n", "")
print("Test delete_n:", delete_n(dna_sample1))


def isdna(seq):
    """
    Checks whether given sequence is combined of possible DNA nucleobases
    :param seq: any dna sequence
    :return: True | False
    """
    assert isinstance(seq, str), "Please enter data in str format!"
    return set(seq).issubset(DNA_NUCLEOBASES)
# print("Test is_dna_seq:", isdna("atgc"))
# print("Test is_dna_seq:", isdna("h"))
# print("Test is_dna_seq:", isdna(2))


def find_errs(seq=""):
    """
    Finds signs in sequence that aren't valid DNA nucleabases
    :param seq: Any DNA sequence
    :return: Set of signs
    """
    return {n for n in set(seq) if n not in DNA_NUCLEOBASES}


def find_errtypes(seq=""):
    """
    :param seq: Any DNA sequence
    :return: Info about types of errors found in entry sequence
    """
    err1, err2, err3 = False, False, False
    for n in find_errs(seq):
        if n == 'n' or n == 'N':
            err1 = True
        if n == '-':
            err2 = True
        if n not in ('n', 'N', '-'):
            err3 = True
    return ("Determined following errors in DNA sequence:\n"
            "1. {}: Laser misreads: 'N' or 'n'\n"
            "2. {}: Sequence unreadable: '-'\n"
            "3. {}: Other errors"
            .format(err1, err2, err3))
# print("Test find_errtypes:", find_errtypes('AAAAGGGTTTnnnAAAGGTTTTnNnN'))


def seq_cnt_case_insensitive(dna_seq="", searched_seq=""):
    """
    Counts DNA sequence or single nucleobase occurrences in a given DNA sequence
    :param dna_seq: DNA sequence
    :param searched_seq: searched nucleobae (A or C or G or T) or DNA sequence
    :return: count of nucleobases/DNA sequences regardless of nucleobase letter's case
    """
    if isdna(searched_seq):
        dna_seq = dna_seq.upper()
        searched_seq = searched_seq.upper()
        return dna_seq.count(searched_seq)
    else:
        return("Given DNA sequence does not belong to the DNA of a terrestrial lifeform "
               "or it contains following errors: \n{}".format(find_errtypes(dna_seq)))


print("GAGA", seq_cnt_case_insensitive(dna_sample1, "GAGA"))
print("CTGAA", seq_cnt_case_insensitive(dna_sample1, "CTGAA"))
print("c", seq_cnt_case_insensitive(dna_sample1, "c"))
print()
print("JJJJXXX", seq_cnt_case_insensitive(dna_sample1, "JJJJXXX"))
