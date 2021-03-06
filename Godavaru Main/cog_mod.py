import os
from discord.ext import commands
import datetime, re
import json
import discord
import asyncio
import random
import time
import platform
import datetime
import inspect

class Mod():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kick(self, ctx):
        if ctx.message.server.me.server_permissions.kick_members == True:
            if ctx.message.author.server_permissions.kick_members == True:
                if len(ctx.message.mentions) == 0:
                    await self.bot.say(":x: Tell me who to kick.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            msg = ctx.message.content
                            args = msg.split(' ')
                            if args[1] != ctx.message.mentions[0]:
                                await self.bot.say(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
                            else:
                                reason = msg.replace(args[0]+" "+args[1]+" ", "")
                                await self.bot.kick(ctx.message.mentions[0])
                                await self.bot.say(":white_check_mark: Kicked **"+str(ctx.message.mentions[0])+"** with reason:"+str(reason))
                            try:
                                if args[2] != "":
                                    await self.bot.kick(ctx.message.mentions[0])
                                    await self.bot.say(":white_check_mark: Kicked **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            except IndexError:
                                await self.bot.say(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
                        except IndexError:
                            await self.bot.say(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
                        except Exception as e:
                            await self.bot.say(":x: I can't kick someone equal to or higher than me.")
                    else:
                        await self.bot.say(":x: You can't kick someone equal to or higher than yourself.")
            else:
                await self.bot.say(":x: You cannot kick members.")
        else:
            await self.bot.say(":x: I cannot kick members.")

    @commands.command(pass_context=True)
    async def ban(self, ctx):
        if ctx.message.server.me.server_permissions.ban_members == True:
            if ctx.message.author.server_permissions.ban_members == True:
                if len(ctx.message.mentions) == 0:
                    await self.bot.say(":x: Tell me who to ban.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            args = ctx.message.content
                            args = args.replace(self.bot.command_prefix[0]+"ban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[0]+"ban <@!"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[1]+"ban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[1]+"ban <@!"+ctx.message.mentions[0].id+">", "")
                            if args == "":
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
                                await self.bot.say(":white_check_mark: Banned **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            else:
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
                                await self.bot.say(":white_check_mark: Banned **"+str(ctx.message.mentions[0])+"** with reason:"+str(args))
                        except Exception as e:
                            await self.bot.say(":x: I can't ban someone equal to or higher than me.")
                    else:
                        await self.bot.say(":x: You can't ban someone equal to or higher than yourself.")
            else:
                await self.bot.say(":x: You cannot ban members.")
        else:
            await self.bot.say(":x: I cannot ban members.")

    @commands.command(pass_context=True)
    async def softban(self, ctx):
        if ctx.message.server.me.server_permissions.ban_members == True:
            if ctx.message.author.server_permissions.ban_members == True:
                if len(ctx.message.mentions) == 0:
                    await self.bot.say(":x: Tell me who to softban.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            args = ctx.message.content
                            args = args.replace(self.bot.command_prefix[0]+"softban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[0]+"softban <@!"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[1]+"softban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[1]+"softban <@!"+ctx.message.mentions[0].id+">", "")
                            if args == "":
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
                                await self.bot.unban(ctx.message.server, ctx.message.mentions[0])
                                await self.bot.say(":white_check_mark: Softbanned **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            else:
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
                                await self.bot.unban(ctx.message.server, ctx.message.mentions[0])
                                await self.bot.say(":white_check_mark: Softbanned **"+str(ctx.message.mentions[0])+"** with reason:"+str(args))
                        except Exception as e:
                            await self.bot.say(":x: I can't softban someone equal to or higher than me.")
                    else:
                        await self.bot.say(":x: You can't softban someone equal to or higher than yourself.")
            else:
                await self.bot.say(":x: You cannot ban members.")
        else:
            await self.bot.say(":x: I cannot ban members.")

    @commands.command(pass_context=True, aliases=["purge", "clean"])
    async def prune(self, ctx):
        args = ctx.message.content
        args = args.split(' ')
        if ctx.message.server.me.server_permissions.manage_messages == True:
            if ctx.message.author.server_permissions.manage_messages == True:
                try:
                    if args[1] != "":
                        try:
                            mgs = [] 
                            number = int(str(args[1]))
                            async for x in self.bot.logs_from(ctx.message.channel, limit=number):
                                mgs.append(x)
                            await self.bot.delete_messages(mgs)
                            prunemsg = await self.bot.say(":white_check_mark: Deleted **{}** messages!".format(number))
                            await asyncio.sleep(5)
                            await self.bot.delete_message(prunemsg)
                        except ValueError:
                            await self.bot.say(":x: That's not a valid number.")
                except IndexError:
                    await self.bot.say(":x: Specify messages to prune.")
            else:
                await self.bot.say(":x: You cannot manage messages.")
        else:
            await self.bot.say(":x: I cannot manage messages.")

    @commands.command(pass_context=True)
    async def hackban(self, ctx):
        if ctx.message.server.me.server_permissions.ban_members == True:
            if ctx.message.author.server_permissions.ban_members == True:
                umsg = ctx.message.content
                args = umsg.split(' ')
                try:
                    uid = int(args[1])
                    try:
                        member = await self.bot.get_user_info(uid)
                    except discord.NotFound:
                        await self.bot.say("That user doesn't exist.")
                    else:
                        reason = umsg.replace(self.bot.command_prefix[0]+"hackban "+args[1], "")
                        reason = umsg.replace(self.bot.command_prefix[1]+"hackban "+args[1], "")
                        if reason == "":
                            await self.bot.http.ban(uid, ctx.message.server.id, delete_message_days=1)
                            await self.bot.say(":white_check_mark: hackbanned "+str(member)+" with reason: Not defined.")
                        else:
                            await self.bot.http.ban(uid, ctx.message.server.id, delete_message_days=1)
                            await self.bot.say(":white_check_mark: hackbanned {0.name}#{0.discriminator} with reason: {1}".format(member, reason[1:]))
                except ValueError:
                    await self.bot.say("That is not an ID.")
                except IndexError:
                    await self.bot.say("Usage: `{}hackban <user id> [reason]`".format(self.bot.command_prefix))
            else:
                await self.bot.say("You can't ban users.")
        else:
            await self.bot.say("I can't ban users.")

    @commands.command(pass_context=True)
    async def unban(self, ctx):
        if ctx.message.server.me.server_permissions.ban_members == True:
            if ctx.message.author.server_permissions.ban_members == True:
                try:
                    umsg = ctx.message.content
                    args = umsg.split(' ')
                    uid = int(args[1])
                    try:
                        member = await self.bot.get_user_info(uid)
                    except discord.NotFound:
                        await self.bot.say("I didn't find that user.")
                    else:
                        await self.bot.unban(ctx.message.server, member)
                        await self.bot.say(":white_check_mark: unbanned "+str(member))
                except ValueError:
                    await self.bot.say("That is not an ID.")
                except IndexError:
                    await self.bot.say("Usage: `{}unban <user id>`".format(self.bot.command_prefix))
            else:
                await self.bot.say("You can't manage bans.")
        else:
            await self.bot.say("I can't manage bans.")
        
def setup(bot):
    bot.add_cog(Mod(bot))
