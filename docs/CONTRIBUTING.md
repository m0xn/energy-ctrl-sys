# Contribuir en el proyecto

## Creando un fork del repositorio

Para contribuir con el proyecto, primero debes hacer un `fork` del mismo (https://docs.github.com/en/get-started/quickstart/fork-a-repo).

Para ello, la forma más accesible y fácil para hacerlo es desde la propia web de GitHub en la página del repositorio.

1. Debes dirigirte al botón `fork` de la esquina superior derecha en la página del repositorio.

![](/docs/images/contributing/forking_ghw_1.png)

2. Posteriormente se te redireccionará a la página correspondiente para realizar un `fork` del repositorio (*similar a la página de crear un nuevo repositorio*).

![](/docs/images/contributing/forking_ghw_2.png)

3. Finalmente, sólo tendrás que pulsar al botón: **Crear fork**. 
*La casilla que está marcada en esta página dependerá de si quieres acceder a otras ramas de desarrollo del proyecto sobre otras versiones o si quieres editar a partir de la versión estable*

Este comando creará por defecto un `fork` en tu cuente de GitHub. Además, añadirá al repositorio actual una nueva URL remota para publicar los cambios que realices localmente en tu `fork` (por defecto se crea un nuevo `remote` para el repositorio original llamado `upstream` y el `remote` `origin` es reemplazado por la URL de tu repositorio).

Si quieres profundizar más en las opciones (`flags`) que puededs utilizar para modificar alguinos parámetros del comando, puedes visitar el siguiente enlace -> https://cli.github.com/manual/gh_repo_fork.


## Aportando cambios al proyecto

Además de poder hacer cambios en tu propio `fork` del repositorio, también puedes proponer la implementación de cambios en el repositorio original a través de ***pull requests*** o `pr` (https://docs.github.com/en/pull-requests).
Para hacerlo desde la página web debes seguir los siguientes pasos.

1. Modifica el archivo en el cual quieras añadir los cambios.

2. Una vez hayas realizado las modificaciones, crea un `commit` para añadirlo a tu repositorio. Esto lo puedes hacer dándole al botón verde de *Commit changes*.

![](/docs/images/contributing/pr_ghw_1.png)

3. Al pulsar el botón encontrarás el siguiente panel

![](/docs/images/contributing/pr_ghw_2.png)

En este panel, tendrás que introducir un título relacionado con los cambios relacionados que hayas realizado.
Trata de ser preciso añadiendo una descripción si es necesario. 
También, es recomendable que crees una nueva rama o `branch` dentro de tu repositorio *forkeado* que incluya los cambios efectuados. Esto puedes hacerlo marcando la casilla señalada.

4. Una vez rellenes la información y pulses el botón de proponer cambios (*Propose changes*), se creará un nuevo comit con los cambios que hayas realizados.
Para finalizar, puedes crear una nueva pull request pulsando el botón verde *Create pull request*.

![](/docs/images/contributing/pr_ghw_3.png)

La pull request será revisada para ser implementada dentro del proyecto en otra rama.
¡Have fun making changes :)
