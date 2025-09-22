# Calcul d'entropie et sélection de l'attribut

## Données par tranche d'âge
- Jeune — 4 / 14  
    - 4/4 n'ont pas de dyspnée, 0/4 en ont  
    - Entropie n°1.1 (base 2) : `- log2(4/4) * 4/4 - log2(0/4) * 0/4`

- Adulte — 4 / 14  
    - 2/4 n'ont pas de dyspnée, 2/4 en ont  
    - Entropie n°1.2 : `- log2(2/4) * 2/4 - log2(2/4) * 2/4`

- Âgé — 6 / 14  
    - 3/6 n'ont pas de dyspnée, 3/6 en ont  
    - Entropie n°1.3 : `- log2(3/6) * 3/6 - log2(3/6) * 3/6`

## Autres variables (à compléter de la même manière)
- Fumeur — ...
    - Entropie n°2.1 : ...
- Non fumeur — ...
    - Entropie n°2.2 : ...
- Pareil pour : Asthmatique, Poids

## Résultats (exemple chiffré)
- Age : 0.104 (valeurs d'exemple)
- Fumeur : 0.594
- Asthmatique : 0.226
- Poids : 0.100

## Conclusion
La variable "Fumeur" a l'entropie la plus élevée (0.594) — c'est donc celle sur laquelle effectuer le premier découpage dans l'arbre de décision.
