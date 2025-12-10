# HEC-NLP 2026

# MATH 60621A : Natural language processing 
(MATH 60621 est introduit plus bas.)

Welcome to the course repository for MATH 60621/60621A of HEC Montréal. You will find course info, assignments and all weekly exercises in this repo. In preparation for the course please follow the instructions below. All coding will be done in Python. 

 ## Course setup and requirements

### STEP 1: Clone or download this repository

You will need to fetch this repository from GitHub (you can use the Terminal (Mac/Linux) or PowerShell (Win) for this). Before running the following command, determine where on your computer you would like to store this course folder.

For the purpose of this guide, we'll assume that coursework will reside under: `/Users/$USER/coursework/MATH-60621A/projects/` on Mac and Linux. You're welcome to use any directory though.

For Mac and linux, open your terminal, for Windows, open `PowerShell` and navigate to the course directory created in Step 1:

```terminal
cd ~
mkdir ./coursework/MATH-60621A/projects/
git clone https://github.com/evaportelance/HEC-NLP.git
```

### STEP 2: Install `uv`
To ensure that your environment is compatible with all assignments and exercises, I recommend installing `uv` as a Python package and project manager.

I recommend using the "Standalone installer" `uv` install instructions unless you already have a preference for another package manager. You can find the `uv` installation instructions for [Mac/Linux](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) and [Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2) on their website.

If you are already familiar with other tools and would like to manage the project differently, that is fine too. Just make sure to install all the required libraries and be cognizant of versioning used by the assignment. These are available in the XXX file of this repository. If you are using `uv` it will automatically create a .venv file with required libraries and python version in your course directory.


### STEP 3: Start Jupyter Lab: 

https://docs.astral.sh/uv/guides/integration/jupyter/
All exercises and asignments will be Jupyter notebooks. Jupyter notebooks allow you to use your browser as your IDE and contain both markdown descriptions as well as runnable code cells. To launch a notebook server
```
cd ~/coursework/MATH-60621A/projects/
uv run --with jupyter jupyter lab
```

By default, jupyter lab will start the server at `http://localhost:8888/lab` and open it in your browser. *Alternatively*, if you are *visual studio code* user, you can use the [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to run notebooks directly in the editor without the above steps and needing to open a browser.

You can now open notebooks for working and create new notebooks.


### You are all set!!

You can deactivate your environment whenever you need to by running

```terminal
deactivate
```

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