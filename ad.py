@bot.command()
async def ad(ctx):
    if ctx.author.id==476012428170362880:
        pass
    else:   
        embed = d.Embed(title="sina-chatに広告を載せる", description="サービス規約", color=0xe31e3c)
        embed.add_field(name="利用規約(1) - モラルについて", value="モラルを守りましょう。広告の内容はほかのサーバーにも送信されます。見た人が不愉快になる内容は宣伝しないようにしましょう。")
        embed.add_field(name="利用規約(2) - 責任問題について", value="広告の追加はTakuTukirouに一切の責任はありません。")
        embed.add_field(name="利用規約(3) - BANについて", value="もし思椎奈ちゃん側からクレームが入り次第問題の広告を掲載した人物の使用を禁止します。")
        embed.add_field(name="そのほか", value="TakuPointを使用します。")
        await ctx.send(embed=embed)
        sleep(15)
        with open("GAMEPOINT.json", 'r') as fr:
            Taku = json.load(fr)
            if Taku.get(str(ctx.author.id)) == None:
                await ctx.send("あなたのTakuPointを確認できませんでした。")
                return
            await ctx.send("広告の内容を120秒以内に入力してください。")
            def msgchk(m):
                return m.author==ctx.author and m.channel.id==ctx.channel.id
            naiyou=await bot.wait_for("message",check=msgchk,timeout=120)
            if naiyou==None:
                await ctx.send("メッセージが送信されませんでした...広告の追加をやめるよ。")
            else:
                await ctx.send("広告のプレビュー")
                embed = d.Embed(title="--広告--", description="{}".format(naiyou.content),color=randint(0, 0xffffff))
                await ctx.send(embed=embed)
                msg3=await ctx.send("追加していい場合リアクションをクリックしてください。\nもし広告を編集・取り消しをする場合60秒待って下さい。")
                await msg3.add_reaction('☑')
                def adtuikasaisyuu(r):
                    return str(r.emoji)=="☑" and r.message_id==msg3.id and r.user_id==ctx.author.id
                try:
                    rea=await bot.wait_for('raw_reaction_add', check=adtuikasaisyuu,timeout=60)
                except a.TimeoutError:
                    await ctx.send("タイムアウト...\nもう一度最初からやり直してください。")
                await ctx.send("追加に成功しました。")
                with open("ad.json", 'r',encoding="utf-8") as fr:
                    ad=json.load(fr)
                    ad[str(ctx.author.name)]={}
                    ad[str(ctx.author.name)]["ad"]=str(naiyou.content)
                    ad[str(ctx.author.name)]["author"]=str(ctx.author.name)
                    ad[str(ctx.author.name)]["count"]=5
                    with open("ad.json", 'w',encoding="utf-8") as fr:
                        json.dump(ad,fr)
from random import choice
async def adtuuti():
    await bot.wait_until_ready()
    while True:
        with open("ad.json", 'r', encoding="utf-8") as fr:
            ad1 = json.load(fr)
            print(ad1)
            ad2=list(ad1.values())
            saisyuu=random.choice(list(ad1.values()))
            print(saisyuu)
            count=saisyuu['count']
            if count==0:
                return
            else:
                saisyuu['count']=saisyuu['count'] - 1
                embed = d.Embed(title="--広告--", description="{}".format(saisyuu['ad']),color=randint(0, 0xffffff))
                embed.set_footer(text=saisyuu['author']+"さんの広告")
                channel = bot.get_channel(551740753324539906)
                await channel.send(embed=embed)
        with open("ad.json", 'w',encoding="utf-8") as fs:
            json.dump(saisyuu,fs)
            await asyncio.sleep(3)
bot.loop.create_task(adtuuti())
