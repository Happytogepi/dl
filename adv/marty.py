from core.advbase import *
from slot.a import *
from slot.d import *
def module():
    return Marty

class Marty(Adv):
    a1 = ('sp',0.05)
    conf = {}
    conf['slot.d'] = Dreadking_Rathalos()
    conf['slots.a'] = Resounding_Rendition()+The_Lurker_in_the_Woods()
    conf['acl'] = """
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `fs, x=2
        """


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)