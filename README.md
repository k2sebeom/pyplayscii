<p align="center">
  <img src="https://github.com/k2sebeom/pyplayscii/blob/master/src/img/PlayScii.png" width=700 height=200>
</p>

------

[![PyPI version](https://badge.fury.io/py/pyplayscii.svg)](https://badge.fury.io/py/pyplayscii)
[![image](https://img.shields.io/pypi/pyversions/pyplayscii.svg)](https://pypi.python.org/pypi/pyplayscii)
![Build Status](https://github.com/k2sebeom/pyplayscii/workflows/Build%20Status/badge.svg?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/k2sebeom/pyplayscii/blob/master/LICENSE)

## Description
PyPlayScii is a Python package that enables an simple object oriented implementation of ascii art games. By asigning the shapes of the game objects by texts seprated by newline characters and determining what to do every frame, you can quickly implement an ascii art game which can be run directly on terminal window. The following shows an example of an ascii art game implemented by PyPlayScii.

Click the image to watch Galaga made with PyPlayscii!!

<p align=center>
  <a href="https://www.youtube.com/watch?v=H7KVIrGrmZE">
    <img alt="Youtube Video of Playscii Game" src="https://img.youtube.com/vi/H7KVIrGrmZE/0.jpg"></a>
</p>

## Installation

    $ pip install pyplayscii --user

## Features

| System | Linux | macOS | Windows |
| :---: | :---: | :---: | :---: |
| Status | [![Unit Test (Ubuntu)](https://github.com/k2sebeom/pyplayscii/workflows/Unit%20Test%20(Ubuntu)/badge.svg?branch=master)](https://github.com/k2sebeom/pyplayscii/actions?query=workflow%3A%22Unit+Test+%28Ubuntu%29%22) | [![Unit Test (macOS)](https://github.com/k2sebeom/pyplayscii/workflows/Unit%20Test%20(macOS)/badge.svg?branch=master)](https://github.com/k2sebeom/pyplayscii/actions?query=workflow%3A%22Unit+Test+%28macOS%29%22) | [![Unit Test (Windows)](https://github.com/k2sebeom/pyplayscii/workflows/Unit%20Test%20(Windows)/badge.svg?branch=master)](https://github.com/k2sebeom/pyplayscii/actions?query=workflow%3A%22Unit+Test+%28Windows%29%22) |

* Easy implementation of ascii style games on terminal screen
* Supports Windows 10, Ubuntu, and macOs => Tested on github action
* Support python 3.6, 3.6, 3.8 => Tested on github action

## Quickstart

Let's make a very simple example of a bouncing ball!! A full source code for the following tutorial can be found <a href="examples/bounce.py">here.</a>

#### Step 1. Importing the package
Once you download the pyplayscii package, you can access the module by the following codes.

```python
from playscii import GameObject, GameManager
from playscii.input import Input
```

GameObject and GamaManager are the most important classes of the pyplayscii package. GameManager will be the backbone of the game engine, and the GameObject will be the members of your game.

#### Step 2. Making a GameObject
The GameManager is the stage, and the GameObjects will be your actors!! Make a game object so that those objects can be used in the GameManager. You can use the plain form of GameObject, but you can also define your own one. In this example, we will make an object named a Ball. One of the most important methods of the GameObject is "update" method. This method will be called every frame when your gamemanager is running.

First, let's define how the ball looks like. All you need to do is make a string, separated by newline characters.

```python
BALL = "    **\n" \
       "   ****\n" \
       "    **"
```
See? It does look like a ball! In the game, your object look exactly like this.

Each gameobject has its position with respect to the lower right corner of the screen. We will update the position of the ball at each frame.

```python
class Ball(GameObject): # Ball inherits the GameObject class
    def __init__(self): # Constructor of your object
        super().__init__(pos=(40, 10), render=BALL)
        self.vel = (10, 10)

    def update(self): # This method is called every frame. self.delta_time is the time it took between the frames.
        self.x += self.vel[0] * self.delta_time # Update the position
        self.y += self.vel[1] * self.delta_time # Update the posiiton
 ```
 
 #### Step 3. Make a GameManager
 Now, we are building a stage for your objects. You should always make a new GameManager by inheriting an abstract class, GameManager.
 Two methods that you must implement in GameManager are "setup()" and "update()." First, setup method is called at the very beginning of the game, right after the game starts. You will want to set the initial properties for your gameobjects, or register gameobjects to your manager by add_object() method. Update method is just the same as that of GameObject; it is called at each frame.
 
 ```python
 class BounceManager(GameManager): # Inherits GameManager
    def __init__(self): # Constructor: If you want to keep track of the object, construct them here!
        super().__init__((80, 20)) # (80, 20) is the size of your game screen.
        self.ball = Ball() # Create a Ball object
        self.set_title("Press q to quit") # set_title changes the title which will appear at the top of your game.

    def setup(self): # This is called right before the first update call.
        self.add_object(self.ball) # Register the object to your manager. If the object is not registered, they will not appear on the screen.

    def update(self): # This is called every frame.
        if self.ball.x < 0 or self.ball.x > 74: # If the ball hits the wall,
            self.ball.vel = (-self.ball.vel[0], self.ball.vel[1]) # Reflect the velocity
        if self.ball.y < 2 or self.ball.y > 20: # Same logic for the floor and the ceiling.
            self.ball.vel = (self.ball.vel[0], -self.ball.vel[1]) # Reflect the velocity

        if Input.get_key_down('q'): # if 'q' key is pressed,
            self.quit() # quit the game.
```

#### Step 4. Play the Game!
You have your gameobject, and well defined gamemanager. Now you have everything you need to play the game. 
To start the game, just call "start" method of your gamemanger. Make sure your terminal screen is big enough for your game.

```python
if __name__ == "__main__":
    manager = BounceManager()
    manager.start()
```

