# Exercice 1
## Données du problème

Vous avez un réseau bayésien pour surveiller les incendies et cambriolages avec :
- **I** (Incendie), **C** (Cambriolage), **V** (Vidéo), **Ca** (Capteur)
- **D** (Défaut), **A** (Alerte), **S** (Sirène)

Les probabilités données sont :
- P(C) = 0.01
- P(I) = 0.02
- P(D) = 0.04

## Questions à résoudre

### 1. Donner la forme du réseau

Le réseau bayésien a cette structure :
- **C** et **I** sont indépendants (pas de lien entre eux)
- **V** dépend de **C** et **I**
- **Ca** dépend de **C** et **I**
- **A** dépend de **V** et **Ca**
- **S** dépend de **A** et **D**

```
    C       I       D
    |\_____/|       |
    |   |   |       |
    V   |   Ca      |
     \  |  /        |
       A -----------+
       |
       S
```

### 2. Quelle est la probabilité élémentaire P(A, S, V, Ca, I, D, C̄) ?

La probabilité jointe se décompose selon la structure du réseau :

**P(A, S, V, Ca, I, D, C̄)** = P(C̄) × P(I) × P(D) × P(V | C̄, I) × P(Ca | C̄, I) × P(A | V, Ca) × P(S | A, D)

En utilisant les tables :
- P(C̄) = 1 - 0.01 = 0.99
- P(I) = 0.02
- P(D) = 0.04
- P(V | C̄, I) = 0.75 (table V)
- P(Ca | C̄, I) = 0.95 (table Ca)
- P(A | V, Ca) = 0.8 (table A)
- P(S | A, D) = 0.98 (table S)

**Résultat** : 0.99 × 0.02 × 0.04 × 0.75 × 0.95 × 0.8 × 0.98 ≈ 0.00044

### 3. Quelle est la probabilité conditionnelle P(A, S | V, Ca, I, D̄, C̄) ?

Par définition de la probabilité conditionnelle et en utilisant l'indépendance conditionnelle :

**P(A, S | V, Ca, I, D̄, C̄)** = P(A | V, Ca) × P(S | A, D̄)

En utilisant les tables :
- P(A | V, Ca) = 0.8
- P(S | A, D̄) = 0.3 (table S, ligne V, D̄)

**Résultat** : 0.8 × 0.3 = 0.24

**Note importante** : I et C̄ n'influencent pas directement A et S une fois que V et Ca sont connus (séparation d-separation dans le réseau bayésien).

# Exercice 2