#!/usr/bin/env python3
#coding:utf-8

import discord, datetime, time
from discord.ext import commands
from src.api_response import *


help_commands = """`*help` - returns help commands""" 
# iter_number = iter(["1.",
#                     "2.",
#                     "3.",
#                     "4.",
#                     "5.:",
#                     "6.",
#                     "7.",
#                     "8.",
#                     "9.",
#                     "10.",
#                     "11."])

class Trader(commands.Cog):
    """Trader commands"""
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0x87DABC

    @commands.command(pass_context=True)
    async def wtb(self, ctx, *args):
        try:
            embed = discord.Embed(title='`💰`Items on sale`💰` (Online in game - Sort by prices)',
                        colour=self.colour,
                        timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            args_endpoint = '_'.join(args).lower()
            api_orders = WfmApi("items", args_endpoint, "orders")
            api_icons = WfmApi("items", args_endpoint)
            item_data = sort_orders(run(api_orders.data()), "wtb")
            item_thumb = run(api_icons.icon_endpoint())
            capitalize_args = [x.capitalize() for x in args]
            formatted_args = ' '.join(capitalize_args)
            for i, d in enumerate(item_data["data"], start = 1):
                pl = int(d["platinum"])
                embed.add_field(name="`{0}.` **{1}** *Online in game* "\
                "+**{2}**`🙂` **{3}** platinum "\
                "{4} pieces".format(i,d["name"],d["rep"], pl, d["quantity"]),
                value="||`/w {0} Hi! I want to buy: {1} "\
                "for {2} platinum. (warframe.market - Warframe Trader bot)`||"\
                .format(d["name"],formatted_args, pl))
            embed.set_thumbnail(url=item_thumb)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | using api.warframe.market",
                            icon_url=ctx.guild.me.avatar_url)
        except StatusError as e:
            embed = discord.Embed(title='`❌`Error`❌`',
                                    colour=self.colour,
                                    timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                                    description=f"{type(e).__name__} : ERROR {e} (You might have spelled a wrong item name or the API is down)`🤔`")
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | using api.warframe.market",
                                icon_url=ctx.guild.me.avatar_url)
        except  
        finally:
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def wts(self, ctx, *args):
        embed = discord.Embed(title='**Supported Commands**',
                            colour=self.colour)
        embed.add_field(name="Commands",value=help_commands)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.author.send(embed=embed)

def setup(bot):
    bot.add_cog(Trader(bot))
    print("Added Trader")