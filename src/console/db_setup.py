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
m = LightModule(name="first pi lit", hostname="raspberrypi", location="lab")
s1 = Segment(num_pixels=60, module_startpixel=0, forwards=False)
s1.strip_startpixel=0
s2 = Segment(num_pixels=60, module_startpixel=64, forwards=True)
s2.strip_startpixel=60
m.segments = [s1, s2]
strip = Strip(length=124, name='main1')
strip.segments = [s1, s2]
session.add(m)

m = LightModule(name="second pi lit", hostname="secondpilit", location="lab")
s1 = Segment(num_pixels=64, module_startpixel=0, forwards=False)
s1.strip_startpixel=0
s2 = Segment(num_pixels=64, module_startpixel=64, forwards=True)
s2.strip_startpixel=64
m.segments = [s1, s2]
strip = Strip(length=128, name='main2')
strip.segments = [s1, s2]
session.add(m)
session.commit()
