"""
    This simple program was written for learning and exercise purposes.
    Searches for nucleobases' sequence occurences in a DNA sample (constant SAMPLE_1). Returns number of occurrences.
    If invalid sequence is searched, informs user about errors and offers options of cleansing the sequence.


    Features involved:
        - flow control: for loop, if else
        - exception handling, assertion
        - comprehensions
        - multiple assignment
        - arguments packing/unpacking
        - docstrings

    Sources:
        https://www.flynerd.pl/2018/01/python-metody-typu-string.html
"""


DNA_NUCLEOBASES = {"A", "C", "G", "T", "a", "c", "g", "t"}
SAMPLE_1 = "ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAGGGTGGGGGTCCCGGGTACTGGTAGGGGTAGCTGC" \
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
      "GGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGTGNAGACnACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGC" \
      "ACAGAGGAGAGAGGCCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGACGGTGAAGTAGCTTCG-GGCGTTGG" \
      "GTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACGGTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCN" \
      "CCAGCC"


def main():
    """
    Ask user for DNA sequence, return number of its occurrences in the sample DNA sequence 'SAMPLE_1'.

    If the searched sequence contains characters not valid as DNA nucleobases, user may decide to modify it by
    removing invalid characters.

    Returns
    -------
    Prints searched sequence (possibly modified), goes to next line, prints number of its occurrences in 'SAMPLE_1'.
    """
    searched_seq = ask_valid_sequence()
    print(searched_seq, '\n', count_sequence_in_sample(searched_seq, SAMPLE_1))


def count_sequence_in_sample(sequence, sample):
    """
    Return count of given DNA sequence/nucleobase occurrences in sample DNA sequence ignoring case.

    Parameters
    ----------
    sequence (str): Arbitrarily long sequence.
    sample (str): Arbitrarily long sequence.

    Returns
    -------
    int: Count of occurrences of sequence in sample.
    """
    sequence, sample = sequence.upper(), sample.upper()
    return sample.count(sequence)


def ask_valid_sequence():
    """
    Ask user for a DNA sequence, check if provided sequence is valid DNA sequence. If not offer options for correction.

    Returns
    -------
    str: DNA sequence rid of errors as per user's choice.
    """
    sequence = input("Please enter sequence to search for in the DNA sample 'SAMPLE_1'\n")
    try:
        assert isdna(sequence)
        return sequence
    except AssertionError:
        answer = input("Given DNA sequence does not belong to the DNA of a terrestrial lifeform "
                       f"or it contains following errors: \n{get_error_types(sequence)}"
                       "\nChoose option:\n"
                       "1 - enter new sequence\n"
                       "2 - continue with current sequence: delete laser misread errors ('n' and 'N')\n"
                       "3 - continue with current sequence: delete all errors excluding lost data ('-')\n"
                       "4 - continue with current sequence: delete all errors\n")
        if answer == "1":
            return ask_valid_sequence()
        elif answer == "2":
            return from_sequence_delete_errors(sequence, 'n')
        elif answer == "3":
            errors = find_errors(sequence).copy()
            errors.remove("-")
            return from_sequence_delete_errors(sequence, *errors)
        elif answer == '4':
            errors = find_errors(sequence)
            print(from_sequence_delete_errors(sequence, *errors))
            return from_sequence_delete_errors(sequence, *errors)


def isdna(seq):
    """
    Verify if sequence is combined of possible DNA nucleobases. Return bool.

    Parameters
    ----------
    seq (str): DNA sequence acquired from user in ask_valid_sequence().

    Returns
    -------
    bool: True when seq is subset of DNA_NUCLEOBASES (i.e. seq is composed of letters for valid DNA nucleobases).
          False otherwise.
    """
    assert isinstance(seq, str), "Please enter data in str format!"
    return set(seq).issubset(DNA_NUCLEOBASES)


def get_error_types(seq):
    """
    Return info about errors present in sequence 'seq'.

    Parameters
    ----------
    seq (str): DNA sequence provided by ask_valid_sequence().

    Returns
    -------
    str: Information for user about error types found in seq.
    """
    err1, err2, err3 = False, False, False
    errors_set = find_errors(seq)
    for n in errors_set.copy():             # necessary to avoid: 'RuntimeError: Set changed size during iteration'
        if n == 'n' or n == 'N':
            err1 = True
            errors_set.remove(n)
        if n == '-':
            err2 = True
            errors_set.remove(n)
        if n not in ('n', 'N', '-'):
            err3 = True
    return (f"1. [{err1}]: Laser misreads: 'N' or 'n'\n"
            f"2. [{err2}]: Sequence unreadable: '-'\n"
            f"3. [{err3}]: Other errors: {', '.join(e for e in errors_set)}")


def find_errors(seq):
    """
    Return set of letters in seq that aren't valid DNA nucleabases.

    Parameters
    ----------
    seq (str): DNA sequence provided by get_error_types().

    Returns
    -------
    set: All characters in seq recognised as not beeing valid DNA nucleobases.
    """
    return {n for n in set(seq) if n not in DNA_NUCLEOBASES}


def from_sequence_delete_errors(sequence, *errors):
    """
    Return sequence without given pattern regardless of pattern's upper/lower case.

    For each error in *errors iterated over seq and removes err.

    Parameters
    ----------
    sequence (str): DNA sequence provided by ask_valid_sequence().
    *errors: variable length iterable

    Returns
    -------
    str: Sequence with specified characters removed.
    """
    for err in errors:
        sequence = sequence.replace(err.lower(), "").replace(err.upper(), "")   # assignment! (replace() returns copy)
    return sequence


main()
