from distutils.core import setup
import py2exe

# setup(windows=['ViOpenCV-Demo.py'], options={"py2exe": {"includes": ["sip"]}})
setup(console=['OpenCV-Demo.py'])
