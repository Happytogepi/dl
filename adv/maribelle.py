from core.advbase import *
from slot.d import *

def module():
    return Maribelle

class Maribelle(Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('prep','100%')
    conf = {}
    conf['slot.d'] = AC011_Garland()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s1
        `s2, seq=5 and cancel
        `s3
        """
    coab = ['Blade','Akasha','Lin_You']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)