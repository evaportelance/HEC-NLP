# HEC-NLP

Welcome to the course repo for MATH 60621A of HEC Montréal. You will find assignments and all weekly exercises in this repo. In preparation for the course please follow the instructions below. All coding will be done in Python. 

## Course setup and requirements

### STEP 1: Clone or download this repo

### STEP 2: Install Anaconda
To ensure that your environment is compatible with all assignments and exercises, I recommend installing Anaconda as a virtual env and package manager. You can find the installation instructions for [MAC OS](https://docs.anaconda.com/anaconda/install/mac-os/), [WINDOWS](https://docs.anaconda.com/anaconda/install/windows/), and [LINUX](https://docs.anaconda.com/anaconda/install/linux/) on their website.

### STEP 3: Create a new virtual environment for this course
Once anaconda is installed we'll create a new environment that we will use for the rest of the course. For Macs or linux, open your Terminal, for Windows, open PowerShell. Type in the following commands:
```
conda create -n nlp_py39 python=3.9 anaconda
```

### STEP 4: Install package requirements 
Once your environment is created, you'll need to activate it by running:
```
conda activate nlp_py39
```
Now you'll need to install pytorch in this new environment. We'll assume that you need CPU binaries, if you have access to a GPU by all means [install gpu binaries instead](https://pytorch.org/get-started/locally/). Otherwise, for Macs, run the following:
```
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```
For Windows or Linux, run this line instead:
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

Once pytorch is installed you can install all the other required packages. To do this navigate to your cloned course repository on the Terminal or PowerShell. Then run:
```
pip install -r requirements.txt
```

### STEP 5: Start Jupyter notebook
All exercises and asignments will be Jupyter notebooks. Jupyter notebooks allow you to use your browser as your IDE and contain both markdown descriptions as well as runnable code cells. To launch a notebook server
```jupyter notebook```

You can optionally specify a port to use with the specification `--port 2222`. 

This should launch a browser that takes you to a view of the directory you're in. You can then open notebooks for working and create new notebooks.


### You are all set!!

You can deactivate your environment whenever you need to by running
```
conda deactivate
```


## Suggested readings 

Dan Jurafsky and James H. Martin. (2024). *Speech and Language Processing* (3rd Edition draft). URL:  https://web.stanford.edu/~jurafsky/slp3/
 
## Acknowledgement

 Some of the files in this repo were heavily inspired or taken from [Chris Potts's Stanford NLU course repo](https://github.com/cgpotts/cs224u/tree/main), a course I took as a graduate student myself and thoroughly enjoyed!
