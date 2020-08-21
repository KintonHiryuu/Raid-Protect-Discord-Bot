import discord
import asyncio
import json

from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions

# ------------------------ COGS ------------------------ #  

class SettingsCog(commands.Cog, name="settings command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'settings')
    async def settings (self, ctx):

        with open("configuration.json", "r") as config:
            data = json.load(config) 
            captcha = data["captcha"] 
            captchaChannel = data["captchaChannel"]  
            logChannel = data["logChannel"]
            temporaryRole = data["temporaryRole"]
            roleGivenAfterCaptcha = data["roleGivenAfterCaptcha"]
            minAccountAge = data["minAccountDate"]

            minAccountAge = int(minAccountAge/3600)

            if roleGivenAfterCaptcha != False:
                roleGivenAfterCaptcha = f"<@&{roleGivenAfterCaptcha}>"
            
        embed = discord.Embed(title=f"**SERVER SETTINGS**", description=f"[**GitHub**](https://github.com/Darkempire78/Raid-Protect-Discord-Bot)", color=0xdeaa0c)
        embed.add_field(name= f"**CAPTCHA PROTECTION** - ``({self.bot.command_prefix}setup <on/off>)``", value= f"Captcha enabled : {captcha}\nCaptcha channel : <#{captchaChannel}>\nBot logs : <#{logChannel}>\nTemporary role : <@&{temporaryRole}>", inline=False)
        embed.add_field(name= f"**ROLE GIVEN AFTER CAPTCHA** - ``({self.bot.command_prefix}giveroleaftercaptcha <role ID/off>)``", value= f"Role given after captcha : {roleGivenAfterCaptcha}", inline=False)
        embed.add_field(name= f"**MINIMUM ACCOUNT AGE** - ``({self.bot.command_prefix}minaccountage <number (hours)>)``", value= f"Minimum account age : {minAccountAge} hours", inline=False)
        embed.set_footer(text="Bot Created by Darkempire#8245")
        return await ctx.channel.send(embed=embed)


# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(SettingsCog(bot))