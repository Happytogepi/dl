#unused now
import slot
from slot.a import *
from slot.d import *
import slot.w
from conf import coability, all_ele_chain

ele_dragon = {
    'flame': Sakuya,
    'water': Siren,
    'wind': Vayu,
    'light': Daikokuten,
    'shadow': Fatalis
}

wp_ct = lambda wp1, wp2, wpc: (wp1, {
        'flame': wpc,
        'water': wpc,
        'light': wpc,
        'all': wp2
    })

wt_prints = {
    'sword': wp_ct(The_Shining_Overlord, Beautiful_Nothingness, Primal_Crisis),
    'blade': wp_ct(Resounding_Rendition, Beautiful_Nothingness, Breakfast_at_Valerios),
    'dagger': (Twinfold_Bonds, {
        'water': The_Prince_of_Dragonyule,
        'shadow': Howling_to_the_Heavens,
        'all': Levins_Champion
    }),
    'axe': wp_ct(Kung_Fu_Masters, Flower_in_the_Fray, Breakfast_at_Valerios),
    'lance': wp_ct(Resounding_Rendition, Beautiful_Nothingness, Breakfast_at_Valerios),
    'wand': (Candy_Couriers, Primal_Crisis),
    'bow': (Forest_Bonds, Dear_Diary),
    'staff': wp_ct(Resounding_Rendition, Beautiful_Nothingness, Breakfast_at_Valerios)
}

ele_punisher = {
    'flame': ('burn', Elegant_Escort),
    'water': ('frostbite', His_Clever_Brother),
    'wind': ('poison', The_Fires_of_Hate),
    'light': ('paralysis', Spirit_of_the_Season),
    'shadow': ('poison', The_Fires_of_Hate)
}

def set(slots, conf):
    ele = slots.c.ele
    wt = slots.c.wt
    # stars = slots.c.stars
    name = slots.c.name

    slots.d = ele_dragon[ele]()
    wp1, wp2 = wt_prints[wt]
    if isinstance(wp2, dict):
        try:
            wp2 = wp2[ele]
        except KeyError:
            wp2 = wp2['all']

    if 'sim_afflict' in conf and conf.sim_afflict.efficiency > 0:
        _, wpa = ele_punisher[ele]
        if 'slots' in conf and 'a' in conf['slots']:
            wp1 = conf['slots.a'].__class__
        wp2 = wpa

    slots.a = wp1()+wp2()

    chain_dict = {**coability['all'], **coability[ele]}
    try:
        chain, _ = chain_dict[name]
        if chain is None or len(chain)<3 or chain[2] != 'hp<40':
            slots.c.coabs[name] = chain_dict[name]
    except:
        try:
            upper_wt = wt[0].upper() + wt[1:].lower()
            slots.c.coabs[upper_wt] = chain_dict[upper_wt]
        except:
            pass

    typeweapon = getattr(slot.w, wt)
    weapon = getattr(typeweapon, ele)

    slots.w = weapon()

    return


