from sequence import Sequence
import matplotlib.pyplot as plt

def main():
    file_name = 'genome_01.dat'
    file_name_1 = 'genome_02.dat'

    seq_type = input('Please write \'DNA\' if the sequence is a DNA sequence\n'
                     'and \'RNA\' if the it\'s an RNA sequence')

    #Object created from sequence string in genome_02.dat file.
    genome_02_obj = read_genome(file_name_1, seq_type)

    #Two objects  created from sequence string in genome_01.dat file, equals each other but not the same object.
    genome_01_obj = read_genome(file_name, seq_type)
    genome_01_obj_1 = read_genome(file_name, seq_type)

    #Applying all the testing required.
    test_functionality(genome_01_obj, genome_01_obj_1, seq_type)



    genes_obj_ls_01 = get_genes_from_seq(genome_01_obj.get_seq_str(), seq_type)
    genes_obj_ls_02 = get_genes_from_seq(genome_02_obj.get_seq_str(), seq_type)

    swap_len_ls = genome_02_obj.compare_dna_seq(genes_obj_ls_01, genes_obj_ls_02)

    print('This is the first Gene : ' + genes_obj_ls_01[0].get_seq_str())
    genes_len_ls = plot_gene_lengths(genes_obj_ls_01)

    plot_swap_mutations(genes_len_ls, swap_len_ls)


def read_genome(file_name, seq_type_temp):
    f = open(file_name, 'r')
    count = 0
    seq_str_temp = ''
    for line in f:
        if count == 0:
            count += 1
            continue
        else:
            seq_str_temp = line
    f.close()
    seq_obj_temp = Sequence(seq_str_temp, seq_type_temp)
    print('The total number of bases is:' + str(len(seq_str_temp)))
    return seq_obj_temp


def get_genes_from_seq(seq_str, seq_type_temp):
    genes_ls = seq_str.split('AAAAAAAAAATTTTTTTTTT')
    genes_obj_ls_temp = []
    for i in range(len(genes_ls)):
        genes_obj_ls_temp.append(Sequence(genes_ls[i], seq_type_temp))
    return genes_obj_ls_temp


def plot_gene_lengths(genes_obj_ls_temp):
    genes_len_ls_temp = []
    for i in genes_obj_ls_temp:
        genes_len_ls_temp.append(len(i.get_seq_str()))
    fig = plt.figure()
    plt.title('Genes Histogram')
    plt.xlabel('Genes Lengths')
    plt.ylabel('Genes Density')
    plt.hist(genes_len_ls_temp, bins=30, normed=True, alpha=0.5,
             histtype='stepfilled', color='steelblue',
             edgecolor='none');

    plt.show()
    fig.savefig('genes_hist.png')
    return genes_len_ls_temp


def plot_swap_mutations(genes_len_ls_temp, swap_len_ls_temp):
    plt.title('Number of swap mutations/gene against gene length')
    plt.xlabel('Genes Lengths')
    plt.ylabel('Number of swap mutations')
    plt.plot(genes_len_ls_temp,swap_len_ls_temp,'.', color='black')

    plt.show()


def test_functionality(seq_obj_01_temp, seq_obj_02_temp, seq_type_temp):
    #Test task #3, is_valid(self).
    if seq_type_temp.lower() == 'dna' :
        assert seq_obj_01_temp.is_valid()



    #Test task#4, __eq__(self, other).
    assert (seq_obj_01_temp == seq_obj_02_temp)                 #Equal objects but not the same.

    #Test task #5, dna_complement(self).
    test_obj = Sequence('ACGTTCGATCG', 'DNA')                    #Creating an object
    test_complement_obj = test_obj.dna_complement()              #Getting the complement of sequence string of test_obj object.
    assert (test_complement_obj.get_seq_str() == 'TGCAAGCTAGC')  #Comparing the two sequences strings.

    #Test task#6, find_non_matching_bases(self, other_obj):
    non_match = test_obj.find_non_matching_bases(test_complement_obj)        #Each object has the complement string of the other,
    assert (non_match == 0)                                                  # should return the first non-zero index.

    #Test task#11,  __eq__(self, other).
    test_lower_case_obj = Sequence(seq_obj_01_temp.get_seq_str().lower(), seq_type_temp)    #test_lower_case_obj. has the same sequence string
                                                                             # as seq_obj_01, but in lower case.

    assert(seq_obj_01_temp == test_lower_case_obj)                           #Testing the equality with different cases.

    #Test task#13,  __eq__(self, other), and dna_complement(self),
    #when the user specify that the sequence is RNA.
    rna_seq_str = seq_obj_01_temp.get_seq_str().replace('T', 'U')
    rna_obj = Sequence(rna_seq_str, seq_type_temp)
    if seq_type_temp.lower() == 'rna':
        assert rna_obj.is_valid()

    test_obj = Sequence('ACGUUCGAUCG', 'rna')        # Creating an object
    test_complement_obj = test_obj.dna_complement()  # Getting the complement of sequence string of test_obj object.
    assert (test_complement_obj.get_seq_str() == 'UGCAAGCUAGC')


if __name__=='__main__':
    main()
