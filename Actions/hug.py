import discord
from discord import app_commands
from discord.ext import commands
import random

class hug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="abraco", description="Dá um abraço em alguém")
    @app_commands.describe(member="Quem vai receber o abraço")
    async def abraco(self, interaction: discord.Interaction, member: discord.Member):
        gifs = [
            "https://media.tenor.com/1Tl0G5cG8sAAAAAC/anime-hug.gif",
            "https://media.tenor.com/9k8zF3J7m6AAAAAC/anime-hug.gif",
            "https://media.tenor.com/8fV6y8h9x4AAAAAC/hug-anime.gif",
        ]
        embed = discord.Embed(
            description=f"{interaction.user.mention} deu um abraço apertado em {member.mention} 🫂",
            color=0xFF69B4
        )
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(hug(client))
