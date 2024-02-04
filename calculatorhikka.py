from sympy import sympify, Rational
from .. import loader, utils
import time

@loader.tds
class CalculatorModule(loader.Module):
    """Калькулятор просто калькулятор!"""

    strings = {"name": "Calculator"}

    @loader.command("calc", "<expression>", aliases=["calculate"])
    async def calc(self, message):
        """⠀"""
        expression = utils.get_args_raw(message)

        try:
            result = sympify(expression)
            result_str = f"{result.evalf():.5e}" if abs(result.evalf()) > 1e6 else str(result.evalf())
            await utils.answer(message, f"🧮 <b>{expression} = {result_str}</b>")
        except Exception as e:
            error_message = await utils.answer(message, f"⚠️ <b>Ой! Ошибка!</b>")
            time.sleep(5)
            await error_message.delete()