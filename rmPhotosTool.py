import photos
from objc_util import ObjCInstance
import dialogs

albums = photos.get_albums()
albumNames = [a.title for a in albums]

select = dialogs.list_dialog(items=albumNames)
index = albumNames.index(select)
album = albums[index]

okfileNames = []
with open('OKfiles.txt', 'r')as f:
    okfileNames = f.read().splitlines()

assets = album.assets
delAssets = []
for asset in assets:
    if str(ObjCInstance(asset).filename()) in okfileNames:
        delAssets.append(asset) 
        
photos.batch_delete(delAssets)
