import gc
from messenger.gui.Scaleform.view.battle.messenger_view import BattleMessengerView
from messenger.gui.Scaleform import FILL_COLORS

def _fakeMSG(name, clan, tank, msg):
    clan_str = "[{}]".format(clan) if clan else ""
    tank_str = " ({})".format(tank) if tank else ""
    
    formatted_msg = "<font color='#80D63A'>{}{}{}: </font><font color='#80D63A'>{}</font>".format(
        name, clan_str, tank_str, msg
    )
    
    for obj in gc.get_objects():
        if isinstance(obj, BattleMessengerView):
            try:
                obj.addMessage(formatted_msg)
                return True
            except Exception as e:
                print "[TRDBG Dev] _fakeMSG error: " + str(e)
    return False
    
_fakeMSG("sherifff", "JUGGR", "", "ya pidor")