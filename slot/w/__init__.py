megingjoro_mub = {
        'buff'     : [('self',0.20,-1,'att','buff'), None],
        'sp'       : 3000,
        'startup'  : 0.25,
        'recovery' : 0.90,
    }

megingjoro_0ub = {
        'buff'     : [('self',0.10,-1,'att','buff'), None],
        'sp'       : 3000,
        'startup'  : 0.25,
        'recovery' : 0.90,
    }

qimen_dunjia_mub = {
        'buff'     : [('spd',0.30,-1), ('self',0.40,-1,'defense')],
        'sp'       : 3000,
        'startup'  : 0.25,
        'recovery' : 0.90,
    }

qimen_dunjia_0ub = {
        'buff'     : [('spd',0.20,-1), ('self',0.30,-1,'defense')],
        'sp'       : 3000,
        'startup'  : 0.25,
        'recovery' : 0.90,
    }

agito_buffs = {
    'flame': [
        {
        'buff'     : [('self',0.10,-1,'att','buff'), None],
        'sp'       : 3000,
        'startup'  : 0.25,
        'recovery' : 0.90,
        },
        {
        'buff'     : [('self',0.20,-1,'att','buff'), None],
        'sp'       : 3000,
        'startup'  : 0.25,
        'recovery' : 0.90,
        },
    ],
    'shadow': [
        {
        'buff'     : [('spd',0.20,-1), ('self',0.30,-1,'defense')],
        'sp'       : 3000,
        'startup'  : 0.25,
        'recovery' : 0.90,
        },
        {
        'buff'     : [('spd',0.30,-1), ('self',0.40,-1,'defense')],
        'sp'       : 3000,
        'startup'  : 0.25,
        'recovery' : 0.90,
        },
    ],
}

from slot import *
from slot.w.sword import *
from slot.w.blade import *
from slot.w.axe import *
from slot.w.dagger import *
from slot.w.lance import *
from slot.w.bow import *
from slot.w.wand import *
from slot.w.staff import *