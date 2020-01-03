# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Module that holding database components """

from userbot import DONGO, REDIS


# Spotify


async def sfsetartist(artist):
    """ Set Spotify Artist """
    REDIS.set('sfartist', artist)


async def sfsetsong(song):
    """ Set Spotify Song """
    REDIS.set('sfsong', song)


async def spotifycheck(spotifychck):
    """ Set Spotify Check (Status) """
    REDIS.set('spotifycheck', spotifychck)


async def exceptionexist(olexception):
    """ Set if Spotify had exception before """
    REDIS.set('exceptionexist', olexception)


async def sfgetsong():
    """ Get Spotify Song """
    return REDIS.get('sfsong').decode("UTF-8")


async def sfgetartist():
    """ Get Spotify Artist """
    return REDIS.get('sfartist').decode("UTF-8")


async def getexception():
    """ Get if Spotify had exception before """
    exceptcheck = REDIS.get('exceptionexist')
    if exceptcheck is True:
        return True

    return False


async def getspotifycheck():
    """ Get Spotify Check (Status) """
    spotifychk = REDIS.get('spotifycheck')
    if spotifychk is True:
        return True

    return False
