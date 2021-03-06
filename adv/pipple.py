import adv.adv_test
from core.advbase import *
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Pipple

pipple_conf = {
    'x1.dmg': 2.21,
    'x2.dmg': 1.19*2,
    'x3.dmg': 0.80*3,
    'x4.dmg': 1.65*2,
    'x5.dmg': 0.80*4+1.32,
}

class Pipple(Adv):
    a3 = ('epassive_att_crit', 7)
    conf = pipple_conf.copy()
    conf['slot.a'] = Primal_Crisis()+Brothers_in_Arms()
    conf['slot.d'] = Dragonyule_Jeanne()
    conf['acl'] = """
        `s1
        `s2, x=5
    """
    coab = ['Blade', 'Xander', 'Axe2']
    def prerun(self):
        self.stance = 0

    def s1_proc(self, e):
        Teambuff('s1', 0.25, 15, 'defense').on()
        if self.stance == 0:
            self.stance = 1
        elif self.stance == 1:
            self.stance = 2
        elif self.stance == 2:
            self.energy.add(1)
            self.stance = 0

    def s2_proc(self, e):
        self.energy.add(2, team=True)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


