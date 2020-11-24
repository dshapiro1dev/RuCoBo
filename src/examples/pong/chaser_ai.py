def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    """Return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball

    Keyword arguments:
    paddle_frect -- a rectangle representing the coordinates of the paddle
                    paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                    corner of the rectangle
                    paddle_frect.size[0], paddle_frect.size[1] are the
                    dimensionsof the paddle along the x and y axis,
                    respectively
   other_paddle_frect --
                    a rectangle representing the opponent paddle. It is
                    formattedin the same way as paddle_frect

   ball_frect --    a rectangle representing the ball. It is formatted in the
                    same way as paddle_frect
   table_size --    table_size[0], table_size[1] are the dimensions of the table,
                    along the x and the y axis respectively

   The coordinates look as follows:

            0             x
            |------------->
            |
            |
            |
        y   v
    """

    if paddle_frect.pos[1] + paddle_frect.size[1] / 2 < ball_frect.pos[1] + ball_frect.size[1] / 2:
        return "down"
    else:
        return "up"