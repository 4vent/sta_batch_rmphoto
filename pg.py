import photos
import ui
from objc_util import ObjCInstance

assets = photos.get_assets()
for a in assets:
    filename = str(ObjCInstance(a).filename())
    if filename.startswith('IMG_3543'):
        print('asset founded!')
        img = a.get_ui_image()
        v = ui.ImageView(image=img)
        v.present()
        print('done.')
