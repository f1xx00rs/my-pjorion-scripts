from helpers import dependency
from skeletons.gui.shared import IItemsCache

def dump_sorted_cache():
    items_cache = dependency.instance(IItemsCache)

    all_vehs = items_cache.items.getVehicles()
    
    data_list = []

    for intCD, v in all_vehs.items():
        data_list.append({
            'nation': v.nationName.upper(),
            'intCD': intCD,
            'type': v.type,
            'name': v.userName.encode('utf-8'),
            'level': v.level
        })

    data_list.sort(key=lambda x: (x['nation'], x['level'], x['name']))

    out = []
    for d in data_list:
        line = "[%s] [%s] %s [%s] [%s]" % (
            d['intCD'],
            d['type'],
            d['name'],
            d['nation'],
            d['level']
        )
        out.append(line)

    with open('tanks.txt', 'wb') as f:
        f.write('\n'.join(out))

    print "Dumped!"

dump_sorted_cache()