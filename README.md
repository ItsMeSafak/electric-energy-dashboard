# Electric energy dashboard
Hello there! Welcome to the dashboard made by team 1!

*We not yet live!*

---
## Setup and installations
First of all, lets clone the repo. You can do this by opening your command prompt (terminal) and executing the following command:
```sh
git clone https://github.com/ItsMeSafak/electric-energy-dashboard
```
This creates a copy of the project on you local machine! There may occur an error saying that 'git is unrecognized'. This means that you should install git first. 
- *Installing git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git*

Open a terminal and execute the following command:
```sh 
pip install -r requirements.txt
```
It may be saying things like 'Requirements already satisfied', but thats a good thing. Once you can enter another command in the terminal, that means the installation of the packages is complete. Also in case you add new packages, add them to the requirements.txt file and rerun the same script.

---
## Executing the code
To run the streamlit application locally, simply execute the following command:
```sh
streamlit run main.py
```
After compiling the code, it should tell you that you can view the app in your browser at the URL *http://localhost:8501* or something like that. If not, there may have gone something wrong with the installation of packages. Perhaps rerun the command above.

---
## Commit changes
Committing changes can be a bit of a pain in the a**. But to ease it out, I made a [commit](commit.sh) script that does all the work for you. Before we get into let, let's discuss the theory. 

While working on a project, we would like to seperate the development and main or master versions of the project. In this project, there are 2 branches: development and master. All our progress should be pushed on the development branch and all that is finished and done should be pushed on the master branch. The development branch is exactly the same as master, but a bit more messy.

**IMPORTANT!** When working on the project, please stay in the **development** branch. You can do this by simply executing the following command:
```sh
git checkout development
```

Now you are allowed to break everything (but don't). Now in order to push your changes live, we need to open up the terminal again (left-below **Terminal** tab) and this time press the **down arrow** and select command prompt. Now you can execute the following command:
```sh
commit.sh [your message]
```
Note that the [your message] part should be in quotes, so you get something like 
```sh
commit.sh "this is my message"
```

In case an error pops up, please contact me or check out the following link (if you dare):
- https://www.jetbrains.com/help/pycharm/resolving-conflicts.html#distributed-version-control-systems
- https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
 
 ---
 ## API/dataset usage

 ---
 ## Handy links
- [Streamlit cheat sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)
- [How to actually use git properly](https://www.freecodecamp.org/news/how-to-use-git-efficiently-54320a236369/)
- [Streamlit dashboard example(s)](https://streamlit.io/gallery)


*Now you are ready to go! Happy coding :smile:!*
