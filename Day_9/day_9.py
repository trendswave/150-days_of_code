# Prompt user to input number of blocks
block = int(input("Enter the numnber of blocks"))
# initialize block height to zero
height = 0
# initialise block layer to 1
layer_block = 1
# while block is greater or equal to layer_blocks
while block >= layer_block:
 height += 1
blocks -= layer_blocks
layer_blocks += 1
print("The height of the pyramid is:", height)
