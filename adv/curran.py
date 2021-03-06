from core.advbase import *
from slot.d import *
from slot.a import *


def module():
    return Curran

class Curran(Adv):
    comment = "no fs"

    a1 = ('od',0.15)
    a3 = ('lo',0.6)

    conf = {}
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        """
    conf['slot.a'] = KFM()+FitF()

    def s1_proc(self, e):
        with Modifier("s1killer", "poison_killer", "hit", 0.6):
            self.dmg_make("s1", 14.70)

    def s2_proc(self, e):
        with Modifier("s2killer", "poison_killer", "hit", 1):
            self.dmg_make("s2", 12.54)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)