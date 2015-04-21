# Coding sequence utilities

def test_if_seq_begins_start_codon(sequence):
    if sequence.upper()[0:3] == "ATG":
        return("correctStart")
    else:
        return("wrongStart")
