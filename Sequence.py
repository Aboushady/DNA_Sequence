class Sequence:
    def __init__(self, seq_string):
        self.seq_str = seq_string
        self.check_dna_seq = True

    def get_dna_bases(self):
        number_of_bases = len(self.seq_str)
        return number_of_bases

    def is_dna(self):
        dna_bases = ['A', 'T', 'C', 'G']
        for c in dna_bases:
            if c not in self.seq_str:
                self.check_dna_seq = False
                return 0

        return 1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.seq_str == other.seq_str
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.seq_str != other.seq_str
        return False

    def dna_complement(self):
        dna_dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        seq_ls = list(self.seq_str)
        for key, value in dna_dic.items():
            for i in range(len(seq_ls)):
                if key == seq_ls[i]:
                    seq_ls[i] = value
        complement_dna_str = str(seq_ls)
        seq_obj = Sequence()
        seq_obj.seq_str = complement_dna_str
        return seq_obj