# ResNet- Measuring network resilience  
---------
Overview
---------
Functional failure in essential pathways or proteins leads to the loss of biological function. Network resilience can quantify the interactome’s robustness to such random breakdowns. As described in [(Zitnik et al., 2019)](https://www.pnas.org/doi/10.1073/pnas.1818013116), ResNet computes and plots the graph resilience for any gene/protein or non-biological network, also allowing users to remove nodes of their choice and view the resulting fragmented network. ResNet is written in Python.       

-----------------------
Running ResNet    
-----------------------
Import [ResNet.py](link???) as a module within the Python interpreter of your choice and run the [functions](https://github.com/Unmani199/Network-Resilience/edit/main/README.md#description-of-functions-in-resnet). For convenience, make sure the dependent packages and [ResNet.py](link???) are on the same path. For example, install the dependencies (including ResNet) within the same [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activate-env) when using Conda or in the same folder when using [JupyterLab](https://jupyter.org/install).       

         from ResNet import *

-------------
Dependencies
-------------
Required packages include-    
pandas, os, statistics, numpy, plotly, networkx, random, math, scipy, timeit  
(Code compatible with Python version 3.8.8. Higher or lower Python versions may cause discrepencies)  

-----------------------
Pipeline, I/O Files & Parameters  
-----------------------
Input file = Network file
The networks are considered undirected and binary.

Output files = Statistics files; Interactive Resilience plots

![ResNet workflow with three defining functions](https://github.com/Unmani199/Network-Resilience/blob/main/ResNet_%20workflow_for_GitHub.png)

-------------
Description of Functions in ResNet  (The first 2 should be together)
-------------

### 1. modified_shannon_div  
        input: (network_file= .txt file with input network in with first two columns with node-pairs per connection) ;  
            (op_stat_filename= prefix for the output .txt file);  
            (reps= No. of iterations/ repetitions to perform serial node removal; default=5);  
            (bin= 'yes'/'no', default='yes'; choice of whether to bin the failure rates in 100 values to reduce run-time.  
                If you don't want to bin- The count of failure rates will be equal to total Nodes (N) in the network (for
                e.g. f = [0/N, 1/N, 2/N, .... N/N])  
        output: (Output.txt file with Failure rates coresponding to the Entropy values)  

### 3. plots_stats_for_resilience  
        input: (op_stat_filename= prefix for the output .html plots- SAME as the one in 'modified_shannon_div');  
            (reps= No. of iterations/ repetitions used in 'modified_shannon_div'; default=5);  
        output: (Plot1: Entropy (H) vs failure rates (f) ranging [0,1]);  
            (Plot2: # Components vs F), Both plots saved as .html to current directory  

### 4. remove_ALL_selected_nodes
        input: (network_file= .txt file with input network in with first two columns with node-pairs per connection);
            (removed_nodes_file= List of nodes to be removed in a .txt file, either single or all at once);
            (op_filename= prefix for the output .txt file);  
        output: (.txt file with size and proteins in fragmented network components)   

-------
License
-------
See file 'LICENSE.md' for license. If you found our software useful in your analysis, we ask that you cite us as:

