from discord.ext import commands
import requests
import html
import random

client = commands.Bot(command_prefix='.')

@client.command()
async def upscale(ctx, url):
    try:
        r = requests.post("https://api.deepai.org/api/waifu2x", data={'image': str(url)}, headers={'api-key': '51eeb896-1c4a-4da7-a594-f0688f9c97ae'})
        await ctx.send(r.json()['output_url'])
    except:
        await ctx.send("please input a valid image url")
        
@client.command()
async def anime(ctx):
    """sends random anime image to channel after command .anime is typed in
        the site used is safebooru.org which is SFW 
    """
    
    num_id = random.randrange(1000000,3900000) #random genrator for uniqe image id
    link_gen = ("https://safebooru.org/index.php?page=post&s=view&id=" + str(num_id))
    
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    img_link = requests.get(link_gen, headers=header)
    site_html = img_link.text
    site_html = html.escape(site_html).split(";") #html parsar for direct image link 
    
    for link in site_html: #searching the html for direct link
        if ("//images/") in link:
            link_gen = (link[0:-5]) 
            break
        
    await ctx.channel.send(link_gen)

# TODO put in key here
client.run()