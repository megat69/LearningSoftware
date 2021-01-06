# LearningSoftware
A console software that allows you to create your own irregular verbs lists to learn, and gives you 8 ways to learn them !

## Documentation
### Fr
#### Lancement
Le lancement du fichier se fait **OU** en lançant le fichier Python si vous avez Python installé **OU** en exécutant le fichier `exe` si vous n'avez pas Python.

#### Paramètres
Les paramètres se trouvent dans le fichier `startup.json`.

**filename** correspond au fichier de verbes que vous voulez charger. Il peut être de n'importe extension, tant qu'il s'agit de texte brut.

**colors_enabled** vaut `true` si les couleurs sont activées. Si vous obtenez des caractères bizarres sur les lignes de la console, c'est qu'elles ne marchent pas avec votre système, il faut donc les désactiver.

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

## Changelog
#### 1.4
First official release
