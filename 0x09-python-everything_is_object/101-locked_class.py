#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from dynamiclly creating new instance attrubutes, 
    except if the new intance attributes is called 'first_name'.

    """

     __slots__ = ["first_name"]
