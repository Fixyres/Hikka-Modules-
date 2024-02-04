from sympy import sympify, Integer
from .. import loader, utils

@loader.tds
class CalculatorModule(loader.Module):
    """Калькулятор просто калькулятор!"""

    strings = {"name": "Calculator"}

    @loader.command("calc", "<expression>", aliases=["calculate"])
    async def calc(self, message):
        """⠀"""
        expression = utils.get_args_raw(message)

        if not expression:
            await utils.answer(message, "⚠️ <b>Ой! Ошыбка!</b>")
            return

        if not all(part.isnumeric() or part.replace(".", "", 1).isnumeric() for part in expression.split()):
            await utils.answer(message, "⚠️ <b>Ой! Ошыбка!</b>")
            return

        try:
            result = sympify(expression)
            result_str = f"{result:.5e}" if isinstance(result, Integer) and abs(result) > 1e6 else str(result)
            await utils.answer(message, f"🧮 <b>{expression} = {result_str}</b>")
        except Exception as e:
            await utils.answer(message, f"⚠️ <b>Ошыбка: {e}</b>")