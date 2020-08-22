# thunder_file_utils
# @lessw2020

import json
from pathlib import Path, PurePath

def coco_compressor(fn_in, fn_out=None, prefix='compact_'):
    '''opens coco format json file, compresses and re-indexes category_ids to start at 0, 
    related image_ids and cat_id annotations to new mapping, 
    saves to fn_out'''

    # change str to Path if needed
    if isinstance(fn_in,str):
        fn_in = Path(fn_in)

    with open(fn_in) as f:
        j = json.load(f)

    remap_catid = {}
    remap_imageid = {}

    for i, item in enumerate(j['categories']):
        # save old_id to new mapping
        remap_catid[item['id']] = i
        # write new id
        item['id'] = i

    for i, item in enumerate(j['images']):
        remap_imageid[item['id']] = i
        item['id'] = i

    for i, item in enumerate(j['annotations']):
        item['image_id'] = remap_imageid[item['image_id']]
        item['category_id'] = remap_catid[item['category_id']]
        item['id'] = i
    
    if not fn_out:
        fn_out = prefix+fn_in.name
    
    print(f"Saving {fn_in} to {fn_out}")

    with open(fn_out, 'w') as f:
        json.dump(j, f)


def show_catids(fn):
    '''display the category_ids for a given json file
        compute the proper num_classes for detr.
    '''
    max_catid=0
    
    if not isinstance(fn,PurePath):
        fn = Path(fn)
    
    with open(fn) as f:
        j = json.load(f)
        
    for i, item in enumerate(j['categories']):
        print(item)
        if item['id']>max_catid:
            max_catid = item['id']
    
    total_catids = i+1  # i is zero based
    num_classes = total_catids if total_catids > max_catid else max_catid
    
    print(f"\ntotal categories = {total_catids}.  Use {num_classes} for detr 'num_classes'")

    