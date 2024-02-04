from sympy import sympify, Rational
from .. import loader, utils
import time

@loader.tds
class CalculatorModule(loader.Module):
    """Калькулятор просто калькулятор!"""

    strings = {"name": "Calculator"}

    def __init__(self):
        self.round_down = False

    @loader.unrestricted
    @loader.command("rounddown")
    async def zi(self, message):
        """Включить/выключить закругление до меньшего числа."""
        self.round_down = not self.round_down
        await utils.answer(message, f"{'🔄 Включено' if self.round_down else '🔄 Выключено'} округление до меньшего числа.")

    @loader.command("calc", "<expression>", aliases=["calculate"])
    async def calc(self, message):
        """Вычислить математическое выражение."""
        expression = utils.get_args_raw(message)

        try:
            result = sympify(expression)
            if isinstance(result, Rational):
                if self.round_down:
                    result_str = f"{int(result.evalf())}"
                else:
                    result_str = f"{result.evalf()}"
            else:
                if self.round_down:
                    result_str = f"{int(result)}"
                else:
                    result_str = f"{result}"
            await utils.answer(message, f"🧮 <b>{expression} = {result_str}</b>")
        except Exception as e:
            error_message = await utils.answer(message, f"⚠️ <b>Ой! Ошибка!</b>")
            time.sleep(5)
            await error_message.delete()
