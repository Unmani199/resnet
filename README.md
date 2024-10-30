# resnet- Measuring network resilience  
---------
Overview
---------
Functional failure in essential pathways or proteins leads to the loss of biological function. Network resilience can quantify the interactome’s robustness to such random breakdowns. As described in [(Zitnik et al., 2019)](https://www.pnas.org/doi/10.1073/pnas.1818013116), resnet computes and plots the graph resilience for any biological or non-biological network. A network consists of nodes and connections amongst nodes (edges). renset performs a random attack on nodes such as the orange nodes in the schematic, and computes the risen entropy (H) in the network upon its fragmentation, if any. The fraction of nodes removed (failure rate) starting from 0, is increased until the entire netowrk is defragmented. resnet computes this rising entropy (H) in the system, induced by the random attack on nodes, and the network resilience complementary to the entropy (H), stated as 1 - (H), as per [(Zitnik et al., 2019)](https://www.pnas.org/doi/10.1073/pnas.1818013116). resnet also allows users to remove certain nodes of interest to see the effect on the network's resilience.      

<img src="https://github.com/Unmani199/Network-Resilience/blob/main/Figures/IntroNetwork.png"  width=600 />


---------
Input files
---------
1. resnet simply requires one file representing the network. Here, the [example file](https://github.com/Unmani199/Network-Resilience/blob/main/src/tests/network_file.tsv), has two columns that show the pairs of nodes that are connected. For instance, the nodes are gene names and the two columns represent the gene interaction. The gene CX3CR1 is connected to IL1B while, gene TFG is connected to TRIM25, TGFA and so on. Hence, the input file is adviced, but not strictly required, to have the columns nameed as 'node1', 'node2' represent interaction between nodes. The networks are considered undirected and binary. That is, edges do not have direction or flow when connecting nodes, nor are they weighed depending on the strength.   

   
   <img src="https://github.com/Unmani199/Network-Resilience/blob/main/Figures/Input_file.png" width=300 />      


---------
Installing resnet
---------
#### Using the module script   

1. **Get [Conda](https://docs.conda.io/projects/conda/en/latest/index.html#)**    
We recommend getting conda or any other python interpreter of you choice since resnet is written in Python. The [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#) can be helpful for installing the anaconda navigator depending on your device, viz., Windows, MacOS etc.

2. **Launch Jupterlab**  
Once conda is installed successfully, open it and launch jupyterlab or jupyterlab notebook. You may like a [tutorial](https://programminghistorian.org/en/lessons/jupyter-notebooks#using-jupyter-notebooks-for-research) to get started with jupyterlab notebooks.
<img src="https://github.com/Unmani199/Network-Resilience/blob/main/Figures/Anaconda_Navigator.png" width=600 />      

4. **Install dependencies**
   * If you already have conda and _Python_ v3.11 or higher installed, skip the first two steps and install the dependent packages (see [dependencies](https://github.com/Unmani199/resnet/blob/main/README.md#dependencies)) using ``` pip install <package_name> ``` in your terminal/commandline or within your jupyterlab notebook.
   * Import [resnet_module.py](https://github.com/Unmani199/Network-Resilience/blob/main/src/resnet/resnet_module.py) as a python module in your jupyterlab notebook as follows. If not jupterlab, you can do it using your choice of interpreter with the same command ``` from resnet_module import resnet ```. Note that the resnet_module.py file should be in the same directory/path as your input file, as seen in the notebook below. You can now use the resnet functions!   

   <img src="https://github.com/Unmani199/Network-Resilience/blob/main/Figures/Install_Dependencies.png" width=700 />    

#### Using pip   

Alternatively, you can install resnet using pip in your command line (below). You will need to [install pip](https://www.partitionwizard.com/partitionmanager/install-pip.html#) if do not have it already.        

         # Uninstall any previous versions   
         pip uninstall resnet -y    
         
         # Install resnet   
         pip install git+https://github.com/Unmani199/resnet.git    

Post this, you can launch Python either within the same command line shell or through an jupyterlab/notebook using conda as dicussed above. This time, because the module is already installed, you can simply import it using Python as follows. You can now use the functions as described next!  
      

         from resnet import resnet     

---------
Running resnet and Output 
---------
Output consist of stat files and interactive resilience plots depending on the function used from resnet. Since the index of entropy, and hence resilience, are derived from the study of [(Zitnik et al., 2019)](https://www.pnas.org/doi/10.1073/pnas.1818013116), we hihgly recommend a quick read for better understanding of the parameters described below within the functions.


1. **modified_shannon_div**   
   Here, **_op_stat_filename_** is the prefix for your output file. **_reps_** are the number of iterations/ repetitions to perform while the node removal; default is 5. **_binning_** can be'yes'/'no' with default='yes'. It is the choice of whether to bin the failure rates in 100 values to reduce run-time. The failure rate, _f_, ranges from 0 to 1, starting from removing 0 nodes to all _N_ nodes (0/N, 1/N, 2/N, .... N/N). If you don't want to bin (bin="no"), the count of failure rates _(f)_ will be equal to total Nodes (N) in the network, which can significantly increase the computing time.       

         # Input files
         network_file = "Davids network file.tsv"
         op_stat_filename = "Davids output"

         # Run the two functions 
         resnet.modified_shannon_div(network_file, op_stat_filename, reps=50, binning= 100)
         resnet.plots_stats_for_resilience(op_stat_filename, reps=5)

   The output file in this case will be named _'Davids output_Resilience.txt'_ with failure rates coresponding to the Entropy values and other stats similar to below. This will be saved on the path to your current working directory.      
![Output](https://github.com/Unmani199/Network-Resilience/blob/main/Figures/Stat_OutputFile.png)     

3. **plots_stats_for_resilience**   
   As perviously depicted, _plots_stats_for_resilience_ can be run after _modified_shannon_div_ as it will use the output file from _modified_shannon_div_ (_'Davids output_Resilience.txt'_) as input to make plots. Of the two output plots, first will have Entropy (H) plotted against failure rates (f). Second one will represent, on Y-axiz, the chnaging number of fragmented components with failure rate. Both plots will be saved as .html to current directory.

    <img src="https://github.com/Unmani199/Network-Resilience/blob/main/Figures/Plot_OutputFile.png" width=600 />


5. **remove_ALL_selected_nodes**   
   This function allows users to remove the nodes of their interest instead of random attack.
   
            # Input file with the list of nodes to be removed
            removed_nodes_file = "Selected nodes.txt"

            resnet.remove_ALL_selected_nodes(network_file, removed_nodes_file, op_filename)
   
   The output file consists of components formed as a results of the node removal. For instance, from the example gene network, some nodes were removed to form the following components. The largest component, still intact, was of size 1877 nodes. Whereas, the removal resulted in fragmentation of the rest of singular nodes seen in the output file below.
   
   <img src="https://github.com/Unmani199/Network-Resilience/blob/main/Figures/Stat2_OutputFile.png" width=600 />   

-------------
Dependencies
-------------
The following packages are required-    
_pandas, plotly, networkx, scipy_. Other packages (some in-built) include _os, statistics, random, math, timeit_. The code compatible with Python version 3.11. Lower Python versions may cause discrepencies.    

-------
Cite us
-------
If you found our tool useful in your analysis, we ask that you cite us as:  
_(Citation to be displayed soon as our publication is in the reviewing process)_
