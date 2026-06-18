from gui.shared.gui_items.badge import Badge

_old_init = Badge.__init__

def _new_init(self, data, proxy=None):
    _old_init(self, data, proxy)
    self.isAchieved = True

Badge.__init__ = _new_init