# HEC-NLP 2026

# MATH 60621A : Natural language processing 
(MATH 60621 est introduit plus bas.)

Welcome to the course repository for MATH 60621/60621A of HEC Montréal. You will find course info, slides and all weekly exercises in this repo. In preparation for the course please follow the instructions below. All coding will be done in Python. 

 ## Course setup and requirements

### STEP 1: Clone or download this repository

You will need to fetch this repository from GitHub. Before running the following command, determine where on your computer you would like to store this course folder.

For the purpose of this guide, we'll assume that coursework will reside under: `/Users/$USER/coursework/MATH-60621A/projects/` on Mac and Linux. You're welcome to use any directory though.

For Mac and linux, open your terminal, for Windows, open `PowerShell` and navigate to the chosen course directory and clone this repo:

```terminal
cd ~
mkdir ./coursework/MATH-60621A/projects/
git clone https://github.com/evaportelance/HEC-NLP.git
```

### STEP 2: Install `uv`
To ensure that your environment is compatible with all assignments and exercises, I recommend installing `uv` as a Python package and project manager.

I recommend using the "Standalone installer" `uv` install instructions unless you already have a preference for another package manager. You can find the `uv` installation instructions for [Mac/Linux](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) and [Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2) on their website.

If you are already familiar with other tools and would like to manage the project differently, that is fine too. Just make sure to install all the required libraries and be cognizant of versioning used. These are available in the `pyproject.toml` file of this repository. If you are using `uv` it will automatically create a .venv file with required libraries and python version in your course directory.


### STEP 3: Start Jupyter Lab: 

https://docs.astral.sh/uv/guides/integration/jupyter/
All exercises and asignments will be Jupyter notebooks. Jupyter notebooks allow you to use your browser as your IDE and contain both markdown descriptions as well as runnable code cells. To launch a notebook server go to the course directory and start up jupyterlab:
```
cd ~/coursework/MATH-60621A/projects/
uv run --with jupyter jupyter lab
```

By default, jupyter lab will start the server at `http://localhost:8888/lab` and open it in your browser. *Alternatively*, if you are *visual studio code* user, you can use the [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to run notebooks directly in the editor without the above steps and needing to open a browser.

You can now open notebooks for working and create new notebooks.


### You are all set!!


## Suggested readings 

Dan Jurafsky and James H. Martin. (2025). *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models, 3rd edition*. Online manuscript released August 24, 2025. URL: https://web.stanford.edu/~jurafsky/slp3/

For chapter week by week breakdown see syllabus or [readings schedule](./Readings/Lectures/readings.md).



*****************************************************************

# MATH 60621 Traitement automatique du language naturel

Bienvenue dans le repo du cours MATH 60621/60621A de HEC Montréal. Vous trouverez dans ce repo des informations sur le cours, les diapos, et tous les exercices hebdomadaires. Pour vous préparer au cours, veuillez suivre les instructions ci-dessous. Tout le codage sera effectué en Python. 

## Configuration de l'environnement virtuel du cours

### ÉTAPE 1 : Clonez ou téléchargez ce repo

Vous devrez récupérer ce repo depuis GitHub. Avant d'exécuter la commande suivante, déterminez où vous souhaitez sauvegarder ce dossier de cours sur votre ordinateur.

Dans le cadre de ce guide, nous supposerons que les travaux de cours seront gardés sous : `/Users/$USER/coursework/MATH-60621A/projects/` sur Mac et Linux. Vous pouvez toutefois utiliser n'importe quel dossier.

Pour Mac et Linux, ouvrez votre Terminal, pour Windows, ouvrez `PowerShell` et accédez au dossier du cours choisi puis clonez le repo:

```terminal
cd ~
mkdir ./coursework/MATH-60621A/projects/
git clone https://github.com/evaportelance/HEC-NLP.git
```

### ÉTAPE 2 : Installer `uv`
Pour vous assurer que votre environnement est compatible avec tous les devoirs et exercices, je vous recommande d'installer `uv` en tant que gestionnaire de paquets et de projets Python.

Je vous recommande d'utiliser les instructions d'installation « Standalone installer » `uv`, sauf si vous avez déjà une préférence pour un autre gestionnaire de paquets. Vous trouverez les instructions d'installation de `uv` pour [Mac/Linux](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) et [Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2) sur leur site web.

Si vous connaissez déjà d'autres outils et souhaitez gérer le projet différemment, cela est également possible. Veillez simplement à installer toutes les bibliothèques requises et respecter les versions utilisées. Celles-ci sont disponibles dans le fichier `pyproject.toml` de ce repo. Si vous utilisez `uv`, un fichier .venv contenant les librairies requises et la version Python sera automatiquement créé dans le répertoire de votre cours.

### ÉTAPE 3 : Démarrer Jupyter Lab : 

https://docs.astral.sh/uv/guides/integration/jupyter/
Tous les exercices et devoirs seront des notebooks Jupyter. Les notebooks Jupyter vous permettent d'utiliser votre navigateur comme IDE et contiennent à la fois des descriptions markdown et des cellules de code exécutables. Pour lancer un serveur de notebooks, navigez au dossier du cours puis lancez jupyterlab:
```
cd ~/coursework/MATH-60621A/projects/
uv run --with jupyter jupyter lab
```

Par défaut, jupyter lab démarrera le serveur à l'adresse `http://localhost:8888/lab` et l'ouvrira dans votre navigateur. *Sinon*, si vous utilisez *Visual Studio Code*, vous pouvez utiliser l'extension Jupyter (https://code.visualstudio.com/docs/datascience/jupyter-notebooks) pour exécuter les notebooks directement dans l'éditeur sans avoir à suivre les étapes ci-dessus ni à ouvrir un navigateur.

Vous pouvez désormais ouvrir des notebooks pour travailler et en créer de nouveaux.


## Lectures suggérées 

Dan Jurafsky and James H. Martin. (2025). *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models, 3rd edition*. Online manuscript released August 24, 2025. URL: https://web.stanford.edu/~jurafsky/slp3/

Pour les chapitres à lire chaque semaine voyez le plan de cous ou [le plan des lectures.](./Readings/Lectures/readings.md).



## Acknowledgement

The exercise files for week 1 is heavily inspired from [Chris Potts's Stanford NLU course repo](https://github.com/cgpotts/cs224u/tree/main) and many of the course slides are based on Dan Jurafsky's.