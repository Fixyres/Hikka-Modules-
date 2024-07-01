from .. import loader
import asyncio

@loader.tds
class GramAutoBonusMod(loader.Module):
    strings = {"name": "GramAutoBonus"}
    task = None

    async def client_ready(self, client, db):
        self.client = client

    async def send_bonus_message(self):
        while True:            
            await self.client.send_message("@valyutaTG_bot", "🎁 Бонусы")
            await self.client.send_message("@valyutaTG_bot", "🎁 Бонуси")
            await asyncio.sleep(24 * 60 * 60)

    @loader.sudo
    async def gabcmd(self, message):
        '''- Включить авто собирание бонуса ✅'''
        if self.task is not None and not self.task.done():
            await message.edit("Авто собирание бонуса включено! ✅")
            return
        self.task = asyncio.create_task(self.send_bonus_message())
        await message.edit("Авто собирание бонуса включено! ✅")

    @loader.sudo
    async def gabscmd(self, message):
        '''- Выключить авто собирание бонуса ⛔'''
        if self.task is not None:
            self.task.cancel()
            self.task = None
            await message.edit("Авто собирание бонуса остановлено! ⛔")
        else:
            await message.edit("Авто собирание бонуса остановлено! ⛔")