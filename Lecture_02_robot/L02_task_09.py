#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    """
    Task 09: Go to the wall on the right. The distance to the wall is
    not known. Paint over the cells if there is no wall is above.
    """

    # Moves right while there is no wall on the right.
    while not wall_is_on_the_right():

        # Fill the cell if there is no wall above.
        if not wall_is_above():
            fill_cell()

        move_right()

    # Fills the last cell if there is no wall above.
    if not wall_is_above():
        fill_cell()

if __name__ == '__main__':
    run_tasks()