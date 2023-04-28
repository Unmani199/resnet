# Network-Resilience
The 2 functions measure and plot resilience of the given network using a modified Shannon diversity index that as demonstrated in [(Zitnik et al., 2019)](https://github.com/Unmani199/Network-Resilience/files/11356259/Evolution_of_PPIN_across_tree_of_life.pdf)
. Required packages include-  
(pandas, networkx, random, plotly, math, scipy, os, statistics, ????? )   
Compatible with Python version 3.8.8 and above  

# Functions in ResNet

## 1. tsv_to_edgeliist  
        input: (ip_file= .txt .csv .sv file as input with 2 tab-seperated columns 'Node1', 'Node2')  
        output: (edgelist= or the list of node pairs forming the network)  

## 2. modified_shannon_div  
        input: (edgelist= list of node pairs forming the network generated from the function 'tsv_to_edgeliist');  
            (op_filename= prefix for the output .txt file);  
            (reps= No. of iterations/ repetitions to perform serial node removal; default=5);  
            (bin= 'yes'/'no', default='yes'; choice of whether to bin the failure rates in 100 values to reduce run-time.  
                If you don't want to bin- The count of failure rates will be equal to total Nodes (N) in the network (for
                e.g. f = [0/N, 1/N, 2/N, .... N/N])  
        output: (Output.txt file with Failure rates coresponding to the Entropy values)  

## 3. plots_stats_for_resilience  
        input: (f_to_Hmsh= Dictionary from 'modified_shannon_div');  
            (op_filename= prefix for the output .html plots);  
            (reps= No. of iterations/ repetitions used in 'modified_shannon_div'; default=5);  
        output: (Plot1: Entropy (H) vs failure rates (f) ranging [0,1]);  
            (Plot2: # Components vs F), Both plots saved as .html to current directory  

## 4. remove_ALL_selected_nodes
        input: (edgelist= or the list of node pairs forming the network);
            (removed_nodes_file= List of nodes to be removed in a .txt file, either single or all at once);
            (op_filename= prefix for the output .txt file);  
        output: (.txt file with size and proteins in fragmented network components)
