# -*- coding: utf-8 -*-
"""
--------------------
comportamiento de properties de status

Tener actualizado el status de un grupo de widgets requeriría llevar un registro
del estado de cada uno de ellos, para determinar el status general se tendría
que consultar el status de cada uno de ellos cuando cualquiera de ellos cambiara.

Es más eficiente consultar el estado de cada uno de los componentes del grupo cada
vez que se requiera conocer el status general, no cada vez que se realize un cambio.

De esta manera se puede saber el status de un grupo de widgets sólo consultando
el status de cada widget del grupo.

A nivel individual, ya que un usuario puede solicitar un proceso sin haber
terminado una captura, el widget deberá mostrar su status actualizado en todo
momento.

--------------------
isModified  .   property

Al inicializar un widget de captura, se alimenta el valor inicial, al ocurrir un
cambio en el contenido del widget, se compara el contenido actual con el valor
inicial y se actualiza la propiedad isModified.

No se ve necesidad al momento de emitir el evento correspondiente 'modified'

--------------------
isValid     .   property

La validez del contenido de un widget de captura estará determinada por una serie
de factores, en este caso properties, predeterminados.

Para mayor flexibilidad se incluye la posibilidad de incluir validación externa en
combinación con la validación interna.

El programador deberá asegurarse que estos factores tengan los valores adecuados.

Al ocurrir un cambio en el contenido del widget, se valida el contenido contra
todos los factores existentes y se actualiza el status de validez.

No se ve necesidad al momento de emitir el evento 'validChanged'

"""
