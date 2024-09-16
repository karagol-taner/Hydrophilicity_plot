# hydrophilicity_plot

This Python tool allows users to generate hydrophilicity (Kyte-Doolittle) plots from single/multiple protein sequences provided in FASTA format. It checks for necessary dependencies like biopython and matplotlib and prompts users to install them if needed. The tool processes amino acid sequences, calculates hydropathy scores using a sliding window, and visualizes the results in a simple plot. It supports both manual sequence input and file-based sequence input, making it a versatile utility for protein sequence analysis.

### Installation

- Option 1 (RECOMMENDED, for all platforms): You can install the package via pip (if you have Python 3.x on your system), and use the command hydrophilicity_plot directly:
```
pip install hydrophilicity_plot  
```
```
hydrophilicity_plot
```


- Option 2 (for all platforms): You can run the script directly from Google Colab.

### Requirements
If you want to run the script natively on your local computer (Option 1), ensure you have Python 3.x installed on your system. 

If Biopython and matplotlib is not already installed, the script will prompt you to install it automatically. 
If the script fails to automatically install Biopython and matplotlib, you can install it manually using the following steps:

- Open a terminal or command prompt after installing Python.
- Run the following command to install Biopython and matplotlib using pip:
  
   ```
   pip install biopython
   pip install matplotlib
   ```


### Questions
If you have any questions or encounter issues, don't hesitate to reach out.

### License
This project is licensed under the  GPL-3.0 License - see the LICENSE file for details.
