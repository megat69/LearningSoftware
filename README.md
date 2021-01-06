# LearningSoftware
A console software that allows you to create your own irregular verbs lists to learn, and gives you 8 ways to learn them !

## Documentation
### French
#### Lancement
Le lancement du fichier se fait **OU** en lançant le fichier Python si vous avez Python installé **OU** en exécutant le fichier `exe` si vous n'avez pas Python.

#### Paramètres
Les paramètres se trouvent dans le fichier `startup.json`.

**filename** correspond au fichier de verbes que vous voulez charger. Il peut être de n'importe extension, tant qu'il s'agit de texte brut.

**colors_enabled** vaut `true` si les couleurs sont activées. Si vous obtenez des caractères bizarres sur les lignes de la console, c'est qu'elles ne marchent pas avec votre système, il faut donc les désactiver en remplaçant `true` par `false`.

**multi_answers_require_all** détermine si, dans le cas de réponses multiples, vous aurez juste si vous rentez UNE des réponses possibles (`false`) ou si vous devez rentrer TOUTES les réponses possibles pour avoir juste (`true`).

#### Choisir vos verbes
Pour choisir vos verbes, procédez comme suit :
- Créez un fichier de n'importe quelle extension *(préféré : `txt`)*, tant qu'il s'agit de texte brut.
- Ouvrez-le.
- La première ligne déterminera le nom des temps pour chaque colonne de la manière suivante :
  - `infinitif, présent, parfait, traduction`
  - L'ordi comprendra -> Colonne 1 : Infinitif, Colonne 2 : Présent, Colonne 3 : Parfait, Colonne 4 : Traduction
- Les lignes suivantes seront les verbes, et leurs différents temps selon la colonne
  - En reprenant l'exemple du dessus :
  - `fallen, fällt, ist gefallen, tomber`
- Les réponses multiples sont séparées par des points-virgules (`;`)
  - Exemple, selon le format défini au-dessus :
  - `lassen, lässt, hat gelassen, laisser; faire`
  - *Laisser* et *faire* sont deux choix possibles pour la traduction de ce verbe.
- N'oubliez pas de régler le paramètre `filename` de `startup.json` au nom de ce fichier
  - Exemple : `VerbesAllemand.txt`

### English
#### Running
The file laucnh is done by **OR** running the Python file if you have Python installed and if you have chosen the Python version **OR** by running the `exe` file if you installed the `exe` version *(Python is not required for this one)*.

#### Settings
The settings can be found in the file `startup.json`.

**filename** corresponds to the name of the verbs file you want to load. This file can be of any extension, as long as it is plain text.

**colors_enabled** is set to `true` if the colors are enabled. If you see some weird characters on the console lines, it is simply that colors do not work on your system. You just need to disable them by replacing `true` with `false`.

**multi_answers_require_all** determines if, in the case of multi-answers, you will be counted correct if you enter ONE of the possible answers (`false`) or if you need to enter EVERY possible answer to be counted as correct (`true`).

#### Choosing your verbs
To choose your verbs, do as follow :
- Create a file of any extension *(recommended : `txt`)*, as long as it is plain text.
- Open it.
- The first line will determine the name of the times for each column in the following way :
  - `infinitive, present, perfect, translation`
  - The computer will understand -> Column 1 : Infinitive, Column 2 : Present, Column 3 : Perfect, Column 4 : Translation
- The following lines will be the verbs, and their different times depending on the column.
  - By using the example above :
  - `fallen, fällt, ist gefallen, fall`
- Multi-answers are separated by semi-colon (`;`)
  - Example, with the defined format above :
  - `lassen, lässt, hat gelassen, leave; do`
  - *leave* and *do* are two possible choices for this verb's translation.
- Don't forget to modify the setting `filename` in `startup.json` with the name of this file.
  - Example : `GermanVerbs.txt`

## Changelog
#### 1.4
First official release
