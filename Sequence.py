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
        seq_obj = Sequence(complement_dna_str)
        return seq_obj

    def find_non_matching_bases(self, other_obj):
        this_ls, other_ls = list(self.seq_str), list(other_obj.seq_str)
        if len(this_ls) == len(other_ls):
            for i in range(this_ls):
                if this_ls[i] != other_ls[i]:
                    return i
        else:
            raise Exception('cannot compare sequences of different lengths')
        return -1

    def compare_dna_seq(self, genes_ls_01, genes_ls_02):
        swap_ls = []
        for i in range(len(genes_ls_01)):
            swap_ls.append([j for j in range(len(genes_ls_01[i])) if genes_ls_01[i][j] != genes_ls_02[i][j]])
        swap_ls_len = [len(swap_ls[i]) for i in range(len(swap_ls))]
        return swap_ls_len
