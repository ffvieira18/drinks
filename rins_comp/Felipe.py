import sys
import os
import subprocess
sys.path.append('./rins_comp')
from Aminoacid import *
from Functions import *



def script(directory): 
    param = []
    cabno = '_nodes.txt'
    cabed = '_edges.txt'
    chain_dict_nodes = []
    chain_dict_edges = []

    for file in os.listdir(directory + '/nodes/'):
        name = file.split('_')[0]
        if name not in param:
            param.append(name)

    os.makedirs(directory + "Result/")
    path_res = directory + "Result/"

    for i in param:
        if os.path.exists(directory+ "/nodes/" + i + cabno):
            if os.path.exists(directory + "/edges/" + i + cabed):
                chain_dict_nodes.append(dict_construct(array_construct(directory+ "/nodes/" + i + cabno, path_res + i + '.txt')))
                chain_dict_edges.append(dict_construct(array_construct(directory + "/edges/" + i + cabed, path_res + i + '.txt')))
            else:
                print('File ' + i + cabed + ' (Not Found!)')
        else:
            print('File ' + i + cabno + ' (Not Found!)')

    #os.makedirs(directory + "Result/")
    #path_res = directory + "Result/"

    tam = len(chain_dict_nodes)
    for i in range(1, tam):
        compare_nodes(chain_dict_nodes[0], chain_dict_nodes[i], 0, path_res + 'dif_nodes_' + param[0] + '_' + param[i] + '.txt')
        compare_nodes(chain_dict_nodes[i], chain_dict_nodes[0], 0, path_res + 'dif_nodes_' + param[i] + '_' + param[0] + '.txt')

        compare_atrib(chain_dict_nodes[0], chain_dict_nodes[i], 'degree', path_res + 'dif_degree_' + param[0] + '_' + param[i] + '.txt')

        compare_edges(chain_dict_edges[0], chain_dict_edges[i], 0, path_res + 'dif_edges_' + param[0] + '_' + param[i] + '.txt')
        compare_edges(chain_dict_edges[i], chain_dict_edges[0], 0, path_res + 'dif_edges_' + param[i] + '_' + param[0] + '.txt')

    #subprocess.call ("Rscript --vanilla ./code.R", shell=True)
    for i in param:
        print(i)
    param.clear()
    
if (__name__ == "__main__"):
    #print(sys.argv[1])
    script(sys.argv[1])