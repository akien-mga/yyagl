from yyagl.gameobject import GameObjectMdt
from .gfx import TrackGfx
from .phys import TrackPhys
from .gui.gui import TrackGui
from .event import TrackEvent
import yaml


class Track(GameObjectMdt):

    def __init__(self, path, cb, split_world, submodels):
        eng.log_mgr.log('init track')
        self.path = path
        init_lst = [
            [('phys', TrackPhys, [self]),
             ('gfx', TrackGfx, [self, split_world, submodels],
              lambda: self.gfx.attach(self.on_loading)),
             ('gui', TrackGui, [self, path[6:]])],
            [('event', TrackEvent, [self])]]
        GameObjectMdt.__init__(self, init_lst, cb)
        with open('assets/models/%s/track.yml' % path) as track_file:
            track_conf = yaml.load(track_file)
            self.camera_vector = track_conf['camera_vector']
            self.shadow_source = track_conf['shadow_source']
            self.laps = track_conf['laps']

    def on_loading(self, txt):
        self.notify('on_loading', txt)
