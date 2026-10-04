import discord
from discord import app_commands
from discord.ext import commands
import random

class shoot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="tiro", description="Atira em alguém")
    @app_commands.describe(member="Quem vai levar o tiro")
    async def tiro(self, interaction: discord.Interaction, member: discord.Member):
        gifs = [
            "https://media.tenor.com/3x5c7v9b2nAAAAAC/anime-shoot.gif",
            "https://media.tenor.com/6y8u0i2o4pAAAAAC/gun-anime.gif",
            "https://media.tenor.com/9a1s3d5f7gAAAAAC/anime-gun.gif",
        ]
        embed = discord.Embed(
            description=f"{interaction.user.mention} atirou em {member.mention} 🔫",
            color=0x8B0000
        )
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(shoot(client))
