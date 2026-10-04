import discord
from discord import app_commands
from discord.ext import commands

class slap(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="slap", description="Dá um tapa em alguém")
    @app_commands.describe(member="Quem vai levar o tapa")
    async def slap(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(
            f"{interaction.user.mention} deu um tapa em {member.mention} ☠️"
        )

async def setup(client):
    await client.add_cog(slap(client))
