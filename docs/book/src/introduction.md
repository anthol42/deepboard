# Introduction

Has it ever happened to you when you run experiments, change some things, run it again, then, few hours or days later, 
you have worst performances than before, but you don't remember what you changed? Your search for hours before finding 
it, or even worse, never find it again?

This is why I created **Deepboard**, a modern experiment tracking tool to help you organise your 
deep learning / machine learning research. We currently find ourselves overwhelmed by a lot of experiment tracking 
tools such as Weights & Biases, ClearML, MLFlow, Tensorboard, *etc.*, so why a new one? I believe these tools can be 
split into two main categories: full ML lifecycle management and lightweight experiment tracking. Popular proprietary 
tools such as Weights & Biases and ClearML and the open source MLFlow are designed to manage the full ML lifecycle. On 
the other side, tensorboard is a lightweight experiment tracking tool as it focuses on logging and visualizing 
experiment results, and comparing them. Tensorboard have been introduced quite some time ago, and while it is still a 
great tool, I believe it lacks some useful features. Deepboard aims to replace tensorboard as a lightweight experiment
tracking tool, while providing a modern and user-friendly interface, and some useful features missing in the classic 
Tensorboard. 

With deepboard, all your logs are stored locally in a single database file, similar to tensorboard that stores the logs 
in binary files. This mean you do not have to be connected to internet, or send your data to a cloud service, 
everything is local. Deepboard uses a sqlite3 database, which makes its format transparent easy to work with. In 
addition, it comes with a public api to read the logs programmatically, which is not the case with tensorboard. It also 
comes with a beautiful and modern web interface to visualize and compare your experiments.

However, where deepboard really separates itself from others is with its unique designed philosophy around 
reproducibility. Deepboard is designed not only to track and visualize your experiments, but also to allow you to reproduce 
the results of any previously run experiment.
