class Sequence:
    def __init__(self, seq_string, type):
        self._seq_str = seq_string
        self._check_dna_seq = True
        self._type = type

    def get_dna_bases(self):
        number_of_bases = len(self._seq_str)
        return number_of_bases

    def is_valid(self):
        dna_bases = ['a', 't', 'c', 'g']
        if self._type.lower() == 'rna':
            dna_bases.append('u')
            dna_bases= [e for e in dna_bases if e not in ['T', 't']]
        for c in dna_bases:
            if c not in list(self._seq_str.lower()):
                self._check_dna_seq = False
                return 0

        return 1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._seq_str.lower() == other.get_seq_str().lower()
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self._seq_str.lower() != other.get_seq_str().lower()
        return False

    def get_seq_str(self):
        seq_tr_temp = self._seq_str
        return seq_tr_temp

    def dna_complement(self):
        dna_dic = {'A': ['T', 'U'], 'T': 'A', 'C': 'G', 'G': 'C', 'U': 'A', 'u': 'a', 't': 'a', 'a': ['t', 'u'], 'c': 'g', 'g': 'c'}
        seq_ls = list(self._seq_str)
        for i in range(len(seq_ls)):
            for key, value in dna_dic.items():
                if key == seq_ls[i]:
                    if self._type.lower() == 'rna' and key.lower() == 'a':
                        seq_ls[i] = value[1]
                        break
                    elif key.lower() == 'a':
                        seq_ls[i] = value[0]
                        break
                    else:
                        seq_ls[i] = value
                        break
                    continue
        complement_dna_str = ''.join(seq_ls)
        seq_obj = Sequence(complement_dna_str, self._type)
        return seq_obj

    def find_non_matching_bases(self, other_obj):
        this_ls, other_ls = list(self._seq_str), list(other_obj.get_seq_str())
        if len(this_ls) == len(other_ls):
            for i in range(len(this_ls)):
                if this_ls[i].lower() != other_ls[i].lower():
                    return i
        else:
            raise Exception('cannot compare sequences of different lengths')
        return -1

    def compare_dna_seq(self, genes_ls_01, genes_ls_02):
        swap_ls = []
        for i in range(len(genes_ls_01)):
            seq_str_temp = genes_ls_01[i].get_seq_str()
            seq_str_temp_1 = genes_ls_02[i].get_seq_str()
            swap_ls.append([j for j in range(len(seq_str_temp)) if seq_str_temp[j].lower() != seq_str_temp_1[j].lower()])
        swap_len_ls_temp = [len(swap_ls[i]) for i in range(len(swap_ls))]
        return swap_len_ls_temp
