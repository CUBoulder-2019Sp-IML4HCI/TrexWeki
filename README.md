# TrexWeki 🦖

![Alt text](https://github.com/CUBoulder-2019Sp-IML4HCI/TrexWeki/blob/master/results/trex_auto.gif)


This project concentrates on using wekinator utilizing `Python-OSC` to develop a game engine that works on a few supervised examples. [Wekinator](http://www.wekinator.org/) is a free, open-source project created by [Rebecca Fiebrink](https://www.doc.gold.ac.uk/~mas01rf/homepage/) a machine learning engine for interactive system that utilizes ports as communication channel.

This is undertaken as a part of course assignment for CSCI 5880 under the guidance of [Ben Shapiro](https://www.colorado.edu/atlas/ben-shapiro)

 [video](https://www.youtube.com/watch?v=J0dqglfylI4&feature=youtu.be)

## Getting Started

To utilize this repository, clone the repository in your machine. Also make sure you have the following prerequirements settled.
deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [wekinator](http://www.wekinator.org/downloads/): Follow the instructions on the wekinator site to get started with wekinator. 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See 

* [python](https://www.python.org/download/releases/2.7/): This project uses python for creating OSCClients and OSCServers

* python-requirements

    * [OSC](http://www.wekinator.org/examples/#Python) : although this project uses OSC prescribed by wekinator, you are free to use any OSC library that seems fit.
    * [gym](https://gym.openai.com/) : basic platform for open ai projects
    * [chrome_dino](https://pypi.org/project/gym-chrome-dino/) : chrome trex open ai gym
    * [pynput](https://pypi.org/project/pynput/) : handling keyboard inputs
    * [sklearn](https://scikit-learn.org/stable/) : extracting features
    * Selenium driver for chrome browser : Varies based on OS. Copy chrome driver and paste it in the root directory of the project named `chromedriver`


### Installing

Installing the requirements :


```
pip install -r requirements.txt
```

Copy chrome driver and paste it in the root directory of the project named `chromedriver`.

### How to run already existing model
* Open wekinator and open an existing project. Select `data/bestmodel/MyTrex2.wekproj` from the data directory of the project.
* In your terminal, with root directory of the project `python dino_gym.py`.
* In another terminal, with root directory of the project `python output_keyboard_event.py`.
* In wekinator, click on run. 
* Get ☕️ and see the dino play for you.

### How to train your model
* Open wekinator and open an existing project. Select `data/bestmodel/MyTrex2.wekproj` from the data directory of the project.
* In your terminal, with root directory of the project `python dino_gym.py`.
* In wekinator, click on `Start Recording`
* Collect around 500 $\pm$ 50  recording samples.
* Train on a classifier of your liking. SVM and knn seems to work better than other classifiers.
* Click on `Train`

## Architecture

![Alt text](https://github.com/CUBoulder-2019Sp-IML4HCI/TrexWeki/blob/master/results/flow.png)

## Built With

* [chrome_dino](https://pypi.org/project/gym-chrome-dino/) 
* [wekinator](http://www.wekinator.org/downloads/)



## License

Feel free to build on this, but beware if you are copying this for your academic assignments. It is always better to learn from assignments than to burn! 🔥

## Acknowledgments

* Chrome_dino Developer
* Prof. Ben Shapiro 


