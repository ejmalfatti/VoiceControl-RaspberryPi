#Control por voz con una Raspberry Pi3


Me compré una **Raspberry Pi 3** y para darle solo un uso tipo sysadmin, había algo más que podría hacer, tantos proyectos realizados con una simple Raspberry Pi y que mis conocimientos no llegan a cubrir todo eso.

Pero decidí hacer una prueba y compré un relé octroacoplado y comencé a jugar con eso. Hasta que surgío, a raíz de algunos videos que vi en Internet, la idea de controlar el encendido por voz de una luz o cualquier otra "cosa" conectada al relé.

Para ello, lo mejor que ví es utilizar **CMU Sphinix** para la decodificación de la voz, es decir, interpretar lo que capta el microfóno y decodificarlo a texto, ***speech to text***. 

El leguaje de programación que más conozco es **Python** por ende la programación está hecha en ese idioma.

Utilicé también los modelos acústicos en español del proyecto **VoxForge**. Los diccionarios los armé yo, siguiendo la guia de la comunidad en inglés y algunos diccionarios en español, pude armar los míos.

La idea es que **CMU Sphinix** esté escuchando continuamente y que, mediante Python, al detectar las palabras "mágicas" ejecute ciertas acciones.

He visto otros proyectos un poco complicado en su programación, este es más sencillo creo yo, y se acerca más a lo que necesitaba.