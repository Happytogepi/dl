import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Waike


class Waike(Adv):
    a1 = ('edge_bog', 40, 'hp100')

    conf = {}
    conf['slot.a'] = Mega_Friends()+Primal_Crisis()
    conf['slot.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    coab = ['Blade', 'Xander', 'Thaniel']
    conf['afflict_res.bog'] = 100

    def s2_proc(self, e):
        self.afflics.bog.on('s2', 80)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

