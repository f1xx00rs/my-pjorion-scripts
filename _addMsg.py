import gc
from messenger.gui.Scaleform.view.battle.messenger_view import BattleMessengerView
from messenger.gui.Scaleform import FILL_COLORS

def _addMsg(text_message):
    for obj in gc.get_objects():
        if isinstance(obj, BattleMessengerView):
            try:
                obj.addMessage(text_message, fillColor=FILL_COLORS.BLACK)
                return True
            except Exception as e:
                print "[TRDBG] _addMsg error: " + str(e)
    return False

_addMsg("\xD0\xB3\xD0\xBB\xD0\xB8\xD0\xBD\xD0\xBE\xD0\xB7\xD0\xB5\xD0\xBA\x20\xD0\xBF\xD0\xBE\xD0\xB4\xD1\x81\xD0\xB0\xD0\xB4\xD0\xBA\xD0\xBE")