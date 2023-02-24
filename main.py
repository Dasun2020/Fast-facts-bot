import discord
from discord.ext import commands
import json
import random
import string
import openai
import os
import keep_alive

my_secret = str(os.environ['openai_key'])
my_secret_dos = str(os.environ['discord'])
openai.api_key = my_secret
model_engine = "text-davinci-003"

keep_alive.keep_alive()

intents = discord.Intents.default()
intents.message_content = True
f = json.load(open("ff_dos.json"))
client = commands.Bot(command_prefix = "f.", intents=intents)

Cats = ["General Scientists", "Units/Dimensions", "Laws/Theories/Theorems/Principles", "Branches of Science", "Other (General)", "Anatomy", "Cells/Genetics", "Biochemistry", "Names", "Taxonomy", "Evolution", "Ecology", "Ecology", "Epidemiology", "Other(Biology)", "Chemistry general", "Elements", "Compounds", "matter", "other(chemistry)", "Earth Science general", "Rocks/minerals/fossils", "Tectonic plates/earth structure", "Landforms/surface structure", "Oceanography", "Space", "Atmosphere", "geologic time", "Maps/Geography", "other(Earthsci)", "General(physics)", "Dynamics/EM", "thermodynamics/waves/particles", "other(physics)", "Atmosphere", "Names", "Names", "Names", "Names", "Names", "Names", "Names", "Names"]

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("I am an alpha"))
    print("Online")

@client.command(aliases=["p"])
async def ping(ctx):
    await ctx.send(f"no {round(client.latency * 1000)}ms")

@client.command(aliases=["f", "facts"])
async def fact(ctx):
    await ctx.send("fetching")
    zeh_cat = random.choice(Cats)
    for i in f:
        if i["Branch name"] == zeh_cat:
            global zeh_catt
            temp = i["Topics"]
            zeh_catt = random.choice(temp)
            break
    global zeh_letter
    zeh_letter = random.choice(Letters)
    await ctx.send(f"Give me a {zeh_catt} starting with the letter {zeh_letter}")

@client.command(aliases=["a"])
async def answer(ctx, *args):
    temp = str(args[0])
    if (temp[0] == zeh_letter or temp[0] == zeh_letter.lower()):
      await ctx.send("Checking")
      print(f"is {temp} an example of {zeh_catt}")
      response = openai.Completion.create(
          model=model_engine,
          #is [example] a [example], if not, what is it?
          prompt="Is " + temp + " a " + zeh_catt + "?", # + ", if not, what is it?",
          max_tokens=1024,
          n=1,
          stop=None,
          temperature=0.5,
      )
      #btw can u like make a copy of this later so i can try different prompts to see if thats better ok (dont remove this, its a reminder)
      result = response.choices[0].text
      user = ctx.message.author
      await ctx.send(result)
    else:
      await ctx.send("That word doesn't start with the correct letter 🫥")

client.run(my_secret_dos)
