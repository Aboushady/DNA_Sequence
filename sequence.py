class Sequence:
    def __init__(self, seq_string, gene_type):
        # Private fields.
        self._seq_str = seq_string
        self._check_dna_seq = True
        self._type = gene_type

    # Getting the number of bases(characters), in a sequence string.
    def get_dna_bases(self):
        number_of_bases = len(self._seq_str)
        return number_of_bases

    # Checking whether the sequence string is valid,
    # that is if it contains all the valid bases in it ['A', 'T', 'G', 'C'] and 'U' in case it was an RNA sequence.
    def is_valid(self):
        dna_bases = ['a', 't', 'c', 'g']                              # Valid bases.
        if self._type.lower() == 'rna':                               # Checks if the string is RNA seq.
            dna_bases.append('u')                                     # Append 'u' to the valid base.
            dna_bases= [e for e in dna_bases if e not in ['T', 't']]  # Creates a new list without the t' base in it.
        for c in dna_bases:
            if c not in list(self._seq_str.lower()):                  # if one of the bases in the valid list isn't in
                self._check_dna_seq = False                           # the string, return 0.
                return 0

        return 1                                                      # else return 1.

    # Checks the equality of objects.
    def __eq__(self, other):
        if isinstance(other, self.__class__):                               # If the two objects are instances of the
            return self._seq_str.lower() == other.get_seq_str().lower()     # same class. return whether their,
        return False                                                        # seq strings are equal. else return False.

    # Checks for inequality of objects. (same behaviour as the __eq__(self):)
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self._seq_str.lower() != other.get_seq_str().lower()
        return False

    # A get method to access self._seq_str private field, from outside of the class.
    def get_seq_str(self):
        seq_tr_temp = self._seq_str
        return seq_tr_temp

    # Gets the complement of each gene base
    # Return the complement string as the seq string of another object.
    def dna_complement(self):
        # Dictionary of each base(Dict's Key) and it's complement(Dict's value).
        dna_dic = {'A': ['T', 'U'], 'T': 'A', 'C': 'G', 'G': 'C', 'U': 'A', 'u': 'a', 't': 'a', 'a': ['t', 'u'], 'c': 'g', 'g': 'c'}

        # Convert the seq string into a list.
        seq_ls = list(self._seq_str)

        # Looping through seq_ls[] list.
        for i in range(len(seq_ls)):
            # Looping through the Dict.
            for key, value in dna_dic.items():
                if key == seq_ls[i]:                                        # If the Key equals the list's element.
                    if self._type.lower() == 'rna' and key.lower() == 'a':  # Checks for 'a', cause it's the only key,
                        seq_ls[i] = value[1]                                # with a list of two values.
                        break
                    elif key.lower() == 'a':                                # If the string was a DNA string assign the
                        seq_ls[i] = value[0]                                # assign the first value of the list,
                        break                                               # else assign the second value, like the
                    else:                                                   # above if statement.
                        seq_ls[i] = value
                        break
                    continue
        complement_dna_str = ''.join(seq_ls)                                # Convert seq_ls[] list back to a string.
        seq_obj = Sequence(complement_dna_str, self._type)                  # Create a new object with complement_dna_str.
        return seq_obj

    # Checks for the first non-match bases between two seq strings.
    # Takes an object as a parameter.
    # Returns : 1- the non-zero index of the first non-matching indexes.(if there were any).
    #           2- -1 if they were completely matching strings.
    #           3- Raises an exception in case the two strings weren't of the same length.
    def find_non_matching_bases(self, other_obj):
        this_ls, other_ls = list(self._seq_str), list(other_obj.get_seq_str())  # Converting this and the other object's
        if len(this_ls) == len(other_ls):                                       # strings to lists.
            for i in range(len(this_ls)):
                if this_ls[i].lower() != other_ls[i].lower():                   # Checks the equality of each element,
                    return i                                                    # of the two lists, then returns the index.
        else:
            raise Exception('cannot compare sequences of different lengths')    # Raise an exception
        return -1                                                               # other wise returns -1.

    # Compares two objects' seq strings, for swap mutations.
    # Parameters : 1- gene_ls_01 (List of objects).
    #              2- gene_ls_02 (List of objects).
    # Returns : 1- swap_len_ls_temp (List of number swap mutations/gene)
    def compare_dna_seq(self, genes_ls_01, genes_ls_02):
        swap_ls = []
        for i in range(len(genes_ls_01)):
            seq_str_temp = genes_ls_01[i].get_seq_str()                 # gets the seq sting of each object in the list.
            seq_str_temp_1 = genes_ls_02[i].get_seq_str()

            # Creates a new list with indexes for where the swap mutations happened in each gene.
            swap_ls.append([j for j in range(len(seq_str_temp)) if seq_str_temp[j].lower() != seq_str_temp_1[j].lower()])
        swap_len_ls_temp = [len(swap_ls[i]) for i in range(len(swap_ls))]  # Gets the number of swap mutations in each gene.
        return swap_len_ls_temp

    # Split the string at the occurrence of 'AAAAAAAAAATTTTTTTTTT',
    def get_genes_from_seq(self):
        genes_ls = self._seq_str.split('AAAAAAAAAATTTTTTTTTT')
        # returns a list of genes.
        genes_obj_ls_temp = []
        for i in range(len(genes_ls)):
            genes_obj_ls_temp.append(Sequence(genes_ls[i], self._type))  # Creates an object with each gene string in genes_ls[]
        return genes_obj_ls_temp
