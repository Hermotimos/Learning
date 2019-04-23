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
    Ask user for a DNA sequence, validate it and return number of its occurrences in the sample DNA sequence 'SAMPLE_1'.

    If the searched sequence contains characters not valid as DNA nucleobases, user may decide to modify it by
    removing invalid characters.

    Returns
    -------
    Prints searched sequence (possibly modified), goes to next line, prints number of its occurrences in 'SAMPLE_1'.
    """
    searched_seq = ask_sequence()
    validated_seq = validate_sequence(searched_seq)
    print(validated_seq, '\n', count_sequence_in_sample(validated_seq, SAMPLE_1))


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


def ask_sequence():
    """Return sequence from user's input."""
    return input("Please enter sequence to search for in the DNA sample 'SAMPLE_1'\n")


def validate_sequence(sequence):
    """
    Check if provided sequence is valid DNA sequence. If not offer options for correction.

    Returns
    -------
    str: DNA sequence rid of errors (or not) as per user's choice.
    """
    errors = find_errors(sequence)
    try:
        assert not errors
        return sequence
    except AssertionError:
        answer = input(f"\nThe DNA sequence '{sequence}'' does not belong to the DNA of a terrestrial life form "
                       f"or it contains following errors: \n{get_error_types(errors)}"
                       "\nChoose option:\n"
                       "1 - enter new sequence\n"
                       "2 - continue with current sequence: delete laser misread errors ('n' and 'N')\n"
                       "3 - continue with current sequence: delete all errors excluding lost data ('-')\n"
                       "4 - continue with current sequence: delete all errors\n"
                       "5 - continue with current sequence: no changes\n")
        if answer == "1":
            return ask_sequence()
        elif answer == "2":
            new_seq = from_sequence_delete_errors(sequence, 'n')
            return validate_sequence(new_seq)
        elif answer == "3":
            errors = find_errors(sequence).copy()
            errors.remove("-")
            new_seq = from_sequence_delete_errors(sequence, *errors)
            return validate_sequence(new_seq)
        elif answer == '4':
            errors = find_errors(sequence)
            new_seq = from_sequence_delete_errors(sequence, *errors)
            return validate_sequence(new_seq)
        elif answer == '5':
            return sequence


def find_errors(sequence):
    """
    Return set of letters in seq that aren't valid DNA nucleabases.

    Parameters
    ----------
    seq (str): DNA sequence provided by get_error_types().

    Returns
    -------
    set: All characters in seq recognised as not beeing valid DNA nucleobases.
    """
    return {n for n in set(sequence) if n not in DNA_NUCLEOBASES}


def get_error_types(errs):
    """
    Return info about errors present in sequence 'seq'.

    Parameters
    ----------
    seq (str): DNA sequence provided by validate_sequence().

    Returns
    -------
    str: Information for user about error types found in seq.
    """
    err1, err2, err3 = False, False, False
    for n in errs.copy():             # necessary to avoid: 'RuntimeError: Set changed size during iteration'
        if n == 'n' or n == 'N':
            err1 = True
            errs.remove(n)
        if n == '-':
            err2 = True
            errs.remove(n)
        if n not in ('n', 'N', '-'):
            err3 = True
    return (f"1. [{err1}]: Laser misreads: 'N' or 'n'\n"
            f"2. [{err2}]: Sequence unreadable: '-'\n"
            f"3. [{err3}]: Other errors: {', '.join(e for e in errs)}")


def from_sequence_delete_errors(sequence, *errors):
    """
    Return sequence without given pattern regardless of pattern's upper/lower case.

    For each error in *errors iterated over seq and removes err.

    Parameters
    ----------
    sequence (str): DNA sequence provided by validate_sequence().
    *errors (str or set): Variable length iterable.

    Returns
    -------
    str: Sequence with specified characters removed.
    """
    for err in errors:
        sequence = sequence.replace(err.lower(), "").replace(err.upper(), "")
    return sequence
    # replace() returns copy, hence assignment is needed to return modified sequence


main()
