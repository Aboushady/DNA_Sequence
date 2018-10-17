from Sequence import Sequence
import matplotlib.pyplot as plt

def main():
    file_name = 'genome_01.dat'
    file_name_1 = 'genome_02.dat'

    seq_obj_02 = read_genome(file_name_1)
    seq_obj_01 = read_genome(file_name)

    genes_obj_ls_01 = get_genes_from_seq(seq_obj_01.seq_str)
    genes_obj_ls_02 = get_genes_from_seq(seq_obj_02.seq_str)

    seq_obj_02.compare_dna_seq(genes_obj_ls_01, genes_obj_ls_02)

    print('This is the first Gene : ' + genes_obj_ls_01[0].seq_str)
    plot_gene_lengths(genes_obj_ls_01)

def read_genome(file_name):
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
    seq_obj_temp = Sequence(seq_str_temp)
    return seq_obj_temp


def get_genes_from_seq(seq_str):
    genes_ls = seq_str.split('AAAAAAAAAATTTTTTTTTT')
    genes_obj_ls_temp = []
    for i in range(len(genes_ls)):
        genes_obj_ls_temp.append(Sequence(genes_ls[i]))
    return genes_obj_ls_temp

def plot_gene_lengths(genes_obj_ls_temp):
    genes_len_ls = []
    for i in genes_obj_ls_temp:
        genes_len_ls.append(len(i.seq_str))
    fig = plt.figure()
    plt.title('Genes Histogram')
    plt.xlabel('Genes Lengths')
    plt.ylabel('Genes Density')
    plt.hist(genes_len_ls, bins=30, normed=True, alpha=0.5,
             histtype='stepfilled', color='steelblue',
             edgecolor='none');

    plt.show()
    fig.savefig('genes_hist.png')

if __name__=='__main__':
    main()
