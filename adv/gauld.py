from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Gauld

class Gauld(Adv):
    a1 = ('a', 0.10, 'hp70')
    a3 = ('k_frostbite', 0.20)
    conf = {}
    conf['slot.a'] = Primal_Crisis()+His_Clever_Brother()
    conf['slot.d'] = Siren()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s2, s=1
        `s3, x=5 or fsc
        `fs, x=5
    """
    coab = ['Dagger', 'Xander', 'Summer_Estelle']
    conf['afflict_res.frostbite'] = 0

    def prerun(self):
        self.s1p = 0
        self.s1_frostbite = [(120,0.37),(160,0.74),(160,0.74)]

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.20, ['frostbite']):
            self.dmg_make('s1', 2.11)
            self.hits += 1
            self.afflics.frostbite('s1',*self.s1_frostbite[self.s1p])
            self.dmg_make('s1', 2.11)
            self.hits += 1
        if self.s1p == 2:
            Selfbuff('s1',0.15,10).on()
        self.s1p = (self.s1p + 1) % 3

    def s2_proc(self, e):
        Selfbuff('s2',0.25,5).on()
        self.s1.charge(self.s1.sp)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
