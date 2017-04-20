from models.module import LightModule
from models.segment import Segment
from models.strip import Strip
from sqlalchemy.orm.exc import NoResultFound

from config import Session

session = Session()

name='main module'

try:
    m = session.query(LightModule).filter(LightModule.name==name).one()
    session.delete(m)
except NoResultFound, e:
    pass
m = LightModule(name="main module", hostname="raspberrypi", location="lab")
s1 = Segment(num_pixels=60, module_startpixel=0, forwards=False)
s1.strip_startpixel=0
s2 = Segment(num_pixels=60, module_startpixel=64, forwards=True)
s2.strip_startpixel=60
m.segments = [s1, s2]
print s1.strip
strip = Strip(length=124)
strip.segments = [s1, s2]
session.add(m)
session.commit()
