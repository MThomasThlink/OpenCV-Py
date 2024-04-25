import sys
import msvcrt as m
from Cadastro import cadastro
from VideoCapture import camera_capture

import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements

def usage():
    print('')
    print('openCV-Demo: aplicativo de demonstração do OpenCV no reconhecimento facial.')
    print('Argumentos: ')
    print('   -c <pasta>     # cadastra todas as fotos na pasta indicada.')
    print('   -v <idCam>     # abre a câmera identificada.')


print(f"Script: {sys.argv[0]}. Versão: {'0.0.1'}.")

if len(sys.argv) >= 3:
    if sys.argv[1] == '-c':
        cadastro(sys.argv[2])
    if sys.argv[1] == '-v':
        camera_capture(sys.argv[2])
else:
    usage()
    m.getch()
    exit(0)

