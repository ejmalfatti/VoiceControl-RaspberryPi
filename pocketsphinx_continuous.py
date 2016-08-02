#!/usr/bin/python

###################################################################################
# Controla encendido y apagado de un rele por voz
# Autor: Emanuel Malfatti 
# E-mail: ejmalfatti@outlook.com
# GitHub: https://ejmalfatti.github.io
# Licencia: GPLv3
###################################################################################
import os
import subprocess, time

os.system("rm capture.txt")

#os.system("./shut.py &")

#os.system("sudo pocketsphinx_continuous -lm 3906.lm -dict 3906.dic > capture.txt -samprate 16000/8000/48000 &")
os.system("pocketsphinx_continuous -hmm voxforge-es-0.2/model_parameters/voxforge_es_sphinx.cd_ptm_3000/ -lm diccionario/5298.lm -dict diccionario/5298.dic -jsgf diccionario/5298.jsgf > capture.txt -samprate 16000/8000/48000 -inmic yes -adcdev plughw:0,0")
os.system("./read.py &")
