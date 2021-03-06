from abc import ABCMeta
from yyagl.gameobject import GameObject
from .logic import TuningLogic
from .gui import TuningGui


class TuningFacade(object):

    def attach_obs(self, meth):
        return self.gui.attach(meth)

    def detach_obs(self, meth):
        return self.gui.detach(meth)

    def load(self, ranking):
        return self.logic.load(ranking)

    def to_dct(self):
        return self.logic.to_dct()

    def show_gui(self):
        return self.gui.show()

    def hide_gui(self):
        return self.gui.hide()

    @property
    def tunings(self):
        return self.logic.tunings


class Tuning(GameObject, TuningFacade):
    __metaclass__ = ABCMeta

    def __init__(self, tuning_props):
        t_p = tuning_props
        init_lst = [
            [('gui', TuningGui, [self, t_p])],
            [('logic', TuningLogic, [self, t_p.cars])]]
        GameObject.__init__(self, init_lst)
