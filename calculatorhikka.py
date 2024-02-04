from sympy import sympify, Rational
from .. import loader, utils
import time

@loader.tds
class CalculatorModule(loader.Module):
    """Калькулятор просто калькулятор!"""

    strings = {"name": "Calculator"}

    def __init__(self):
        self.round_down = False
        self.use_e = False

    @loader.unrestricted
    @loader.command("rounddown")
    async def zi(self, message):
        """Включить/выключить закругление до меньшего числа."""
        self.round_down = not self.round_down
        await self.update_mode_message(message)

    @loader.unrestricted
    @loader.command("mode")
    async def mode(self, message):
        """Переключить режим ответа между обычными числами и e."""
        self.use_e = not self.use_e
        await self.update_mode_message(message)

    async def update_mode_message(self, message):
        """Обновить сообщение о текущем режиме."""
        mode_text = "🔢 Обычные числа" if not self.use_e else "Числа в формате 🅴"
        round_text = "🔄 Включено" if self.round_down else "🔄 Выключено"
        reply_msg = await utils.answer(message, f"{mode_text} | {round_text} закругление до меньшего числа.")
        time.sleep(5)
        await reply_msg.delete()

    def remove_decimal(self, number_str):
        """Удалить десятичную часть числа вплоть до 'e'."""
        if '.' in number_str and 'e' in number_str:
            integer_part, remainder = number_str.split('.')
            return f"{integer_part}e{remainder.split('e')[1]}"
        return number_str

    def format_result(self, result):
        """Форматировать результат в соответствии с настройками."""
        if isinstance(result, Rational):
            if self.round_down:
                result_str = self.remove_decimal(f"{int(result.evalf()):e}") if self.use_e else f"{int(result.evalf())}"
            else:
                result_str = f"{result.evalf():e}" if self.use_e else f"{result.evalf()}"
        else:
            if self.round_down:
                result_str = self.remove_decimal(f"{int(result):e}") if self.use_e else f"{int(result)}"
            else:
                result_str = self.remove_decimal(f"{result:e}") if self.use_e else f"{result}"
        return result_str

    @loader.command("calc", "<expression>", aliases=["calculate"])
    async def calc(self, message):
        """Вычислить математическое выражение."""
        expression = utils.get_args_raw(message)

        try:
            result = sympify(expression)
            result_str = self.format_result(result)
            await utils.answer(message, f"🧮 <b>{expression} = {result_str}</b>")
        except Exception as e:
            error_message = await utils.answer(message, f"⚠️ <b>Ой! Ошибка!</b>")
            time.sleep(5)
            await error_message.delete()
