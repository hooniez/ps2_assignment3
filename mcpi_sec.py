from mcpi.minecraft import Minecraft

# Assignment 1 main file
# Feel free to modify, and/or to add other modules/classes in this or other files

mc = Minecraft.create()
mc.postToChat("Hello world")
mc.setBlock(10,10,10,2)