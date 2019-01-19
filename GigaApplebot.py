@bot.command(pass_context=True)
async def Gigatrade(msg,point=None):
    REGEX = r"([a-z,A-Z])"
    URL_PATTERN = re.compile(REGEX)
    match_obj = URL_PATTERN.search(point)
    print(point)
    if point==None:
        await bot.say("不備があります。`tb:Gigatrade [変換するポイント数]`")
    else:
        if match_obj:
            await bot.say("数字以外の言葉が入っているので実行できませんでした。")
        if int(point)<0:
            await bot.say("数字以外の言葉が入っているので実行できませんでした。")
        else:
            embed = discord.Embed(title="GAMEポイントをGigaApplebot硬貨に変換する", description="", color=0x006699)
            embed.add_field(name="変換するポイント数", value=point+"ポイント")
            embed.add_field(name="変換先", value="GigaApplebot通貨")
            embed.add_field(name="注意", value="あなたのGAMEポイントを"+point+"変換します。")
            embed.add_field(name="状況", value="送信していい場合は⭕を送信を中止する場合は❌を押してください。")
            msg3 = await bot.say(embed=embed)
            await bot.add_reaction(msg3, '⭕')
            await bot.add_reaction(msg3, '❌')
            rea = await bot.wait_for_reaction(['⭕','❌'],user=msg.message.author, message=msg3)
            if str(rea.reaction.emoji) == "⭕":
                with open("GAMEPOINT.json", 'r') as fr:
                    level = json.load(fr)
                    if level.get(str(msg.message.author.id)) == None:
                        await bot.say("あなたのGAMEポイントを確認できませんでした。")
                    else:
                        gamepoint = level[str(msg.message.author.id)]['point']
                        sendpoint=level[str(msg.message.author.id)]['point'] = level[str(msg.message.author.id)]['point'] - int(point)
                        with open("GAMEPOINT.json", 'w') as fs:
                            json.dump(level,fs)
                            with open("取引.log", 'a') as log:
                                naiyou=("\n名前:{0}\nID:{1}\nもともとのポイント数:{2}\n変換後:{3}\n変換先GigaApplebot".format(msg.message.author,msg.message.author.id,gamepoint,sendpoint))
                                print(naiyou, file=log)
                            embed = discord.Embed(title=msg.message.author.id, description=point)
                            channel = bot.get_channel('ID')
                            await bot.send_message(channel, embed=embed)
                            embed = discord.Embed(title="GAMEポイントを変換する|変換完了", description="",color=0x00cc66)               
                            embed.add_field(name="状況", value="GAMEポイントを"+point+"変換しました。")
                            embed.add_field(name="変換先", value="GigaApplebot通貨")
                            await bot.edit_message(msg3,embed=embed)
                            msg3 = await bot.say("ポイント確認中です。お待ちください。")
                            await bot.send_typing(msg.message.channel)
                            sleep(2)
                            await bot.delete_message(msg3)
                            embed = discord.Embed(title="GAMEポイント変動について", description="{0}→{1}に変動しました。".format(gamepoint,sendpoint), color=0xa1d8e2)
                            await bot.say(embed=embed)
            else:
                await bot.say("変換しません。")
