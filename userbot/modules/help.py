# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Modulnya Salah GANTENGGGGG!!**")
            await asyncio.sleep(18)
            await event.delete()
    else:
        await event.edit(f"**╭►▻►▻►▻►▻►▻►◄◅◄◅◄◅◄◅◄◅╮**\
            \n│   Help for [🩸ANCIENT🩸]\
            \n╰►▻►▻►▻►▻►▻►◄◅◄◅◄◅◄◅◄◅╯ \
            \n╭►▻►▻►▻►▻►▻►◄◅◄◅◄◅◄◅◄◅╮\
            \n│   Untuk melihat lengkap Command\
            \n│   Contoh: .help <nama module>\
            \n│   Modules Aktif: {len(modules)}\
           \n╰►▻►▻►▻►▻►▻►◄◅◄◅◄◅◄◅◄◅╯")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t🔅 "
        await event.reply(f"•{string}•"
                          "\n \n Pantek....")
        await event.reply(f"\n**Ketik Contoh** `.help afk` **Untuk Informasi Modulnya**")
        await asyncio.sleep(1000)
        await event.delete()
