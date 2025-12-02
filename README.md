# HEC-NLP 2026

# MATH 60621A : Natural language processing 
(MATH 60621 est introduit plus bas.)

Welcome to the course repo for MATH 60621/60621A of HEC Montréal. You will find course info, assignments and all weekly exercises in this repo. In preparation for the course please follow the instructions below. All coding will be done in Python. 

 ## Course setup and requirements
 
 Coming soon.

<!-- ### STEP 1: Clone or download this repo

### STEP 2: Install Anaconda
To ensure that your environment is compatible with all assignments and exercises, I recommend installing Anaconda as a virtual env and package manager. You can find the installation instructions for [MAC OS](https://docs.anaconda.com/anaconda/install/mac-os/), [WINDOWS](https://docs.anaconda.com/anaconda/install/windows/), and [LINUX](https://docs.anaconda.com/anaconda/install/linux/) on their website.

If you are already familiar with python libraries and virtual environments and would like to manage them differently that is fine too, just make sure to install all the required libraries and be cognizant of versioning.

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
Now you'll need to install pytorch in this new environment. We'll assume that you need CPU binaries:

```
conda install conda-forge::pytorch-cpu
```

If you have access to a GPU you can run this line instead:
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
-->

## Suggested readings 

Dan Jurafsky and James H. Martin. (2025). *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models, 3rd edition*. Online manuscript released August 24, 2025. URL: https://web.stanford.edu/~jurafsky/slp3/

For chapter week by week breakdown see syllabus or [readings schedule](./Readings/Lectures/readings.md).


*****************************************************************

# MATH 60621 Traitement automatique du language naturel

Bienvenue dans le repo du cours MATH 60621/60621A de HEC Montréal. Vous trouverez dans ce repo des informations sur le cours, les diapos, les devoirs et tous les exercices hebdomadaires. Pour vous préparer au cours, veuillez suivre les instructions ci-dessous. Tout le codage sera effectué en Python. 

## Configuration de l'environnement virtuel du cours

À venir bientôt.

<!-- ### ÉTAPE 1 : Clonez ou téléchargez ce repo

### ÉTAPE 2 : Installez Anaconda

Afin de vous assurer que votre environnement est compatible avec tous les devoirs et exercices, je vous recommande d'installer Anaconda comme gestionnaire d'environnement virtuel et de libraries. Vous trouverez les instructions d'installation pour [MAC OS](https://docs.anaconda.com/anaconda/install/mac-os/), [WINDOWS](https://docs.anaconda.com/anaconda/install/windows/) et [LINUX](https://docs.anaconda.com/anaconda/install/linux/) sur leur site web. Si vous connaissez déjà les libraries Python et les environnements virtuels et que vous souhaitez les gérer différemment, cela est également possible. Veillez simplement à installer toutes les libraries requises et tenir compte des versions.

### ÉTAPE 3 : Créer un nouvel environnement virtuel pour ce cours

Une fois Anaconda installé, nous allons créer un nouvel environnement que nous utiliserons pour le reste du cours. Pour Mac ou Linux, ouvrez votre terminal, pour Windows, ouvrez PowerShell. Tapez les commandes suivantes :

```
conda create -n nlp_py39 python=3.9 anaconda
```

### ÉTAPE 4 : Installez les libraries requises 

Une fois votre environnement créé, vous devrez l'activer en exécutant :
```
conda activate nlp_py39
```
Vous devez maintenant installer pytorch dans ce nouvel environnement. Nous assumons que vous avez besoin des binaires CPU. Si vous avez accès à un GPU, [installez plutôt les binaires GPU](https://pytorch.org/get-started/locally/). Sinon, pour les Mac, exécutez la commande suivante :
```
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```
Pour Windows ou Linux, exécutez plutôt cette ligne :
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

Une fois pytorch installé, vous pouvez installer tous les autres librairies requises. Pour ce faire, accédez à votre repo cloné du cours dans le Terminal ou PowerShell. Exécutez ensuite :

```
pip install -r requirements.txt
```

### ÉTAPE 5 : Démarrer le notebook Jupyter

Tous les exercices et devoirs seront des notebooks Jupyter. Les notebooks Jupyter vous permettent d'utiliser votre navigateur comme IDE et contiennent à la fois des descriptions markdown et des cellules de code exécutables. Pour lancer un serveur notebook, tapez :

```jupyter notebook```

Vous pouvez éventuellement spécifier un port à utiliser avec la spécification `--port 2222`. Cela devrait lancer un navigateur qui vous amènera à une page du repo dans lequel vous vous trouvez. Vous pouvez ensuite ouvrir des notebooks pour travailler et créer de nouveaux notebooks.

### Vous êtes prêt ! 

Vous pouvez désactiver votre environnement à tout moment en exécutant
```
conda deactivate
```
-->
## Lectures suggérées 

Dan Jurafsky and James H. Martin. (2025). *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models, 3rd edition*. Online manuscript released August 24, 2025. URL: https://web.stanford.edu/~jurafsky/slp3/

Pour les chapitres à lire chaque semaine voyez le plan de cous ou [le plan des lectures.](./Readings/Lectures/readings.md).



## Acknowledgement

The exercise files for week 1 is heavily inspired from [Chris Potts's Stanford NLU course repo](https://github.com/cgpotts/cs224u/tree/main) and many of the course slides are based on Dan Jurafsky's.
