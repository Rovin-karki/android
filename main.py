from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import Point3, Vec3
import sys

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the default mouse camera control
        self.disableMouse()

        # Load the environment model
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add a spinning teapot
        self.teapot = self.loader.loadModel("models/teapot")
        self.teapot.reparentTo(self.render)
        self.teapot.setPos(0, 5, 0)
        self.teapot.setScale(1, 1, 1)

        # Set up the camera
        self.camera.setPos(0, -20, 4)
        self.camera.lookAt(Point3(0, 0, 0))

        # Add a task to rotate the teapot
        self.taskMgr.add(self.spinTeapotTask, "SpinTeapotTask")

        # Add keyboard controls
        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.moveTeapot, [-1, 0, 0])
        self.accept("arrow_right", self.moveTeapot, [1, 0, 0])
        self.accept("arrow_up", self.moveTeapot, [0, 1, 0])
        self.accept("arrow_down", self.moveTeapot, [0, -1, 0])

    def spinTeapotTask(self, task):
        """Rotate the teapot each frame."""
        angleDegrees = task.time * 60.0
        self.teapot.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def moveTeapot(self, x, y, z):
        """Move the teapot based on keyboard input."""
        self.teapot.setPos(
            self.teapot.getX() + x,
            self.teapot.getY() + y,
            self.teapot.getZ() + z
        )

# Create and run the game
game = MyGame()
game.run()
