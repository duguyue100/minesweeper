# MineSweeper

[![Build Status](https://travis-ci.org/duguyue100/minesweeper.svg?branch=master)](https://travis-ci.org/duguyue100/minesweeper)

A python Minesweeper with interfaces for Reinforcement Learning.

This is a simple game I wrote for learning _Deep Reinforcement Learning_.

## How to Install

In order to install this package, you need to have at least

+   `numpy`
+   `pyqt`

installed. If you don't want to bother with details of packages installation,
you can use [Anaconda](https://anaconda.org/) as your Python distribution.

And then install the package by

```bash
pip install git+git://github.com/duguyue100/minesweeper.git \
-r https://github.com/duguyue100/minesweeper/blob/master/requirements.txt
```

## Objectives

+   A command line mine sweeper game.
+   A GUI interface.
+   Interfaces for receiving move info and send board status.
+   Capability of playing multiple games using different UDP ports.

## Todo List

+   [x] Basic structure setup
+   [x] update rules for `msboard` (click)
+   [x] update rules for `msboard` (flag)
+   [x] update rules for `msboard` (unflag)
+   [x] update rules for `msboard` (question)
+   [x] TCP interface for the game
+   [x] console interface for the game
+   [x] GUI interface for the game
+   [x] Complete reset button and end game condition
+   [ ] Control GUI interface through remote commands (another thread?)

## Screen Shot

![Game Shot](minesweeper/imgs/screen_shot.png)

## Control The Game

TBD

## Contacts

Yuhuang Hu  
Email: duguyue100@gmail.com
