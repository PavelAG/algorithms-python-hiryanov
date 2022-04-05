"""
Draw a flower.
"""

import turtle

# define the cursor shape
turtle.shape('turtle')

petals_number = 6 # number of petals
petals_pair = int(petals_number/2) # calculating the number of pairs
angle = 360/petals_number #identifying angle

for pair in range(petals_pair):
  
    turtle.circle(80) # making 1st petal(circle)
    turtle.circle(-80) # making symmetrical petal(circle)
    turtle.right(angle)

# Prevent window from closing
turtle.mainloop()
