import adv.adv_test
import adv.ezelith
from core.advbase import Debuff

def module():
    return Ezelith

class Ezelith(adv.ezelith.Ezelith):

    def dmg_proc(self, name, amount):
        if name[0] == 'x' and self.s2_buff.get():
            Debuff('s2_ab', 0.05, 5, self.s2_chance()).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

