def eat_ghost(power_pellet_active, touching_ghost):
    return True if (power_pellet_active + touching_ghost) > 1 else False


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    return True if not power_pellet_active and touching_ghost else False


# print(eat_ghost(True, False))
# print(lose(False, True))
print(127.5%20)
