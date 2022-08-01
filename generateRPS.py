from datetime import datetime
import shutil
import os
from xmls import setxml

class linerotine():
    def insertdata(self, req):
        self.req=req
        try:
            shutil.rmtree('lotes')
        except:
            pass
        try:
            shutil.rmtree('compactados')
        except:
            pass
        try:
            os.mkdir('lotes')
        except:
            pass
        try:
            os.mkdir('compactados')
        except:
            pass
        second = datetime.today().strftime('%Y%m%d%H%M%S')
        try:
            os.mkdir('lotes'+'//'+second)
        except:
            pass
        baseboard = setxml.baseboard()
        open(f'lotes/{second}/a1.xml', 'w').write(baseboard)
        print(baseboard)
        file = 'compactados/'+second
        shutil.make_archive(file, 'zip', './','lotes/'+second+'/')
        return (file+'.zip',201)