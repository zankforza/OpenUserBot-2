# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Module that holding database components """

from userbot import DB_URI


# Spotify


async def sfsetartist(artist):
    """ Set Spotify Artist """
    DB_URI.set('sfartist', artist)


async def sfsetsong(song):
    """ Set Spotify Song """
    DB_URI.set('sfsong', song)


async def spotifycheck(spotifychck):
    """ Set Spotify Check (Status) """
    DB_URI.set('spotifycheck', spotifychck)


async def exceptionexist(olexception):
    """ Set if Spotify had exception before """
    DB_URI.set('exceptionexist', olexception)


async def sfgetsong():
    """ Get Spotify Song """
    return DB_URI.get('sfsong').decode("UTF-8")


async def sfgetartist():
    """ Get Spotify Artist """
    return DB_URI.get('sfartist').decode("UTF-8")


async def getexception():
    """ Get if Spotify had exception before """
    exceptcheck = DB_URI.get('exceptionexist')
    if exceptcheck is True:
        return True

    return False


async def getspotifycheck():
    """ Get Spotify Check (Status) """
    spotifychk = DB_URI.get('spotifycheck')
    if spotifychk is True:
        return True

    return False
