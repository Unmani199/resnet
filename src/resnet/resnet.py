# Install dependencies 
import pandas as pd
import time, os
from statistics import *
from math import *
import numpy as np
import plotly
import plotly.express as px
import networkx as nx
import random as rn
from scipy.integrate import simpson
from timeit import default_timer as timer
import plotly.graph_objects as go
import plotly.io as pio

# class resnet:
#     def __init__(self):
#             pass
    
def modified_shannon_div(network_file, op_stat_filename, reps=50, binning= 100):
    """
    Input params: 
        edgelist: List of node pairs (each pair in a tuple) forming the network
        reps: No. of iterations/ repetitions to perform serial node removal; default=50
        binning : ([integer value]/'no', default=100) whether to bin the failure rates in (100) values to reduce run-time
                  If you don't want to bin- #failure rates will be #Nodes in the network (for e.g. f = [0/N, 1/N, 2/N, .... N/N] )
    Output Params: 
        Output file : Stats file
    """
    start = timer()
    
    ### Network file to edge-list [(node1, node2), (node2, node3), ... (nodeN, NodeN-1)]
    
    # Set working dir to the network file's location
    os.chdir(os.path.dirname(os.path.abspath(network_file)))
    
    # Read & display ip_file using pandas
    df = pd.read_csv(ip_file, sep='s+', na_filter= False, engine='python')
    # print('Your input file with edge pairs:\n', df)
    
    # Pandas dataframe --> edgelist [ (node1, node2), (node1, node3), ... ]
    edgelist = list()
    for idx, row in df.iterrows():
        edgelist.append((row[0].split('\t')[0].strip().upper(), row[0].split('\t')[1].strip().upper()))
    
    
    ### Calculate modified Shannon diversity (Entropy) for the increasing failure rates (f)
    
    f_to_Hmsh = {}
    isolated_comps = {}
    # Form the input network from edge-pair list
    G = nx.from_edgelist(edgelist); N = len(list(G.nodes())); N1=N; E1 = len(list(G.edges()))
    print('Total nodes: ', N)
    
    # Check for binning
    if binning == 'no' or binning == 'No' or binning == 'NO':
        binning = N 
    
    
    # Compute the entropy for each failure rate, f 
    for f in np.linspace(0, N, num = int(binning), dtype = int):
        # Status update
        print('Computing network entropy (H) for Failure rate: ', f/N, '\t#Nodes removed', f)
        Hmsh=[];  mean_no_comps_list=[]

        for r in range(0, reps):
            # Status update
            print('iteration= ', r+1)

            G = nx.from_edgelist(edgelist)
            rand_nodes_removal = rn.sample(list(nx.nodes(G)), k=f)
            G.remove_edges_from(list(G.edges(rand_nodes_removal)))

            comps = list(nx.connected_components(G))
            C = [len(comps[x]) for x in range(0, len(comps))]; C.sort(reverse=True)

            # Get modified entropy H for this iteration, r    
            Hmsh.append(abs(sum([c*log(c/N)/N for c in C]))/log(N))       # Sum of entropies (H) of all fragments or components added in list
            mean_no_comps_list.append(len(C))                             # Component size added to the list, which is len(C)

        f_to_Hmsh.update({f/N:[mean(Hmsh), stdev(Hmsh), mean(mean_no_comps_list), stdev(mean_no_comps_list)]})   
    end = timer()
    time = (end-start)/60
    print('Time Elapased (mins): ', time)
    
    
    # X, Y axes values for calculating AUC-Area Under Curve
    failure_rates = list(f_to_Hmsh.keys())                                # X values
    H_msh = [x[0] for x in f_to_Hmsh.values()]                            # Y values for plot1 (mean Hmsh (Modified Shannon diversity) for each set of Reps)
    
    # Measure AUC using 2 methods - composite trapezoidal rule & composite Simpson's rule
    area_trz = np.trapz(x = failure_rates, y = H_msh)                     # Got same area for np.trapz(H_msh, dx = mean(np.diff(failure_rates)))  
    area_smp = simpson(H_msh, dx = mean(np.diff(failure_rates)))
    

    # Add Resilience values from Dictionary to DataFrame
    df = pd.DataFrame.from_dict(f_to_Hmsh, orient='index',  columns=['Mean Entropy per failure rate', 'Std Dev of Entropy per failure rate', 'Mean Number of Isolated components per failure rate', 'Std Dev of Isolated components per failure rate']).rename_axis('Failure Rate').reset_index()
    
    
    ### Save stats to .txt file
    # Header
    txt = open("_".join([op_stat_filename, 'Resilience_stats.txt']), "w")
    txt.write(" ".join(["AUC (Area Under Curve) by Trapz method =", str(area_trz), "Resilience (1-AUC) =", str(1-area_trz)])); txt.write('\n')
    txt.write(" ".join(["AUC (Area Under Curve) by Simpson method =", str(area_smp), "Resilience (1-AUC) =", str(1-area_smp)])); txt.write('\n')
    txt.write(''.join(['Time elapsed (mins): ', str(time)])); txt.write('\n')
    txt.write(' '.join(['No of nodes/edges in the network: ', str(N1), str(E1)])); txt.write('\n')
    txt.write(" ".join(["Number of Iterations/ Repetitions:", str(reps)])); txt.write('\n\n')
    
    # Columns
    txt.write('\t'.join([str(x) for x in df.columns])); txt.write('\n')
    for idx, row in df.iterrows():
        txt.write('\t'.join([str(x) for x in row])); txt.write('\n')
    txt.close()

    

def plots_stats_for_resilience(op_stat_filename, reps=5):
    """
    Input params: 
        Dictionary from modified_shannon_div
        reps: No. of iterations/ repetitions performed for serial node removal; default=5
        op_stat_filename : Ouput file name to saved 
    Output params:
        Plot1: Entropy (H) vs failure rates f ranging [0,1] (Exported to curr_dir)
        Plot2: # Components vs F
    """
    # Import the stats .txt file from previous function
    dict_file = pd.read_csv("_".join([op_stat_filename, 'Resilience_stats.txt']), sep = '\t', skiprows = 5)
    

    # Plot & Save -- Entropy (H) vs F
    fig = go.Figure()
    fig.add_traces(go.Scatter(x=dict_file['Failure Rate'], y=dict_file['Mean Entropy per failure rate'], mode='lines',fill="tozeroy"))    #  name = k,
    fig.update_layout(
        title={'text': " ".join(["Mean Entropy (H) for", str(reps), "iterations"]),  'y':0.9, 'x':0.45, 'xanchor': 'center', 'yanchor': 'top'},
            xaxis_title="Failure rate [0,1]",
            yaxis_title="Entropy (H) [0,1]",
            font=dict(family="Century Gothic, monospace, bold", size=12, color="White"),
            width=1400, height=800,
            template='plotly_dark'  
    )
    pio.write_html(fig, "_".join([op_stat_filename, 'Resilience.html']))

    
    # Plot & Save -- # Components vs F
    fig = go.Figure()
    fig.add_traces(go.Scatter(x=dict_file['Failure Rate'], y=dict_file['Mean Number of Isolated components per failure rate'], mode='lines', fill="tozeroy"))   # name = k,
    fig.update_layout(
        title={'text': " ".join(["Mean # Components for", str(reps), "iterations"]),  'y':0.9, 'x':0.45, 'xanchor': 'center', 'yanchor': 'top'},
            xaxis_title="Failure rate [0,1]",
            yaxis_title="No. of fragmenting components",
            font=dict(family="Century Gothic, monospace, bold", size=12, color="White"),
            width=1400, height=800,
            template='plotly_dark'  
    )
    pio.write_html(fig, "_".join([op_stat_filename, 'Isolated_Components.html']))

    
    
def remove_ALL_selected_nodes(network_file, removed_nodes_file, op_filename):
    
    start = timer()
    
    # Set working dir to the input file's location
    os.chdir(os.path.dirname(os.path.abspath(network_file)))
    
    # Network file to edgelist
    edgelist = []
    with open(network_file, 'r') as n:
        n.readline()         # Read the column name
        edgelist = [(line.split('\t')[0].strip().upper(), (line.split('\t')[1].strip().upper()) ) for line in n]
        
    # Get the list of nodes to be removed from .txt file
    df = pd.read_csv(removed_nodes_file, sep='\t', na_filter= False, engine='python')
    removed_nodes_list = []
    with open(removed_nodes_file, 'r') as fil:
        removed_nodes_list = [line.strip().upper() for line in fil]
    
    # Establish & display the nodes-edges of the input network
    G = nx.from_edgelist(edgelist); N = len(list(G.nodes()));
    print('Total nodes/ edges in the network: ', N, len(list(G.edges())))
    
    # Remove the nodes& edges from user ALL at once 
    G.remove_edges_from(list(G.edges(removed_nodes_list)))
    comps = list(nx.connected_components(G))
    C = [len(comps[x]) for x in range(0, len(comps))]; C.sort(reverse=True)

    
    print('Fragments (arranged by size) after removing ALL given nodes at once: ', C, len(list(G.nodes())), len(list(G.edges())))
    
    txt = open(op_filename, 'w')
    txt.write('\t\t'.join(['Count of fragments', 'Size of the fragment', 'Proteins in this fragment\n']))
    c = 0
    for i in range(0, len(comps)):
        # Exclude the removed nodes from the list of 'fragmented components'
        if len([x for x in list(comps[i])] ) == 1 and [x for x in list(comps[i])][0] in removed_nodes_list:
            continue
        else:
            c+=1
            txt.write(''.join([str(c) ,'\t\t', str(len(comps[i])),   '\t\t',  '\t'.join([x for x in list(comps[i])]) ]))
            txt.write('\n')
    
    end = timer()
    time = (end-start)/60

    
    
