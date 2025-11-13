# Exercice 1 : Dyspnée

## Énoncé
Sur la base des données présentées dans le tableau, construire un arbre de décision permettant de savoir dans quel ordre effectuer les tests. Les quatre premières variables sont les variables d'entrée (X), la cinquième est la variable cible (Y).

## Données

| Age    | Fumeur | Asthmatique | Poids     | Dyspnée |
|--------|--------|-------------|-----------|---------|
| Jeune  | Oui    | Non         | Normal    | Non     |
| Jeune  | Oui    | Oui         | Maigre    | Non     |
| Adulte | Non    | Non         | Corpulent | Non     |
| Âgé    | Oui    | Non         | Maigre    | Non     |
| Âgé    | Non    | Non         | Normal    | Non     |
| Adulte | Oui    | Oui         | Corpulent | Oui     |
| Jeune  | Non    | Non         | Normal    | Non     |
| Adulte | Oui    | Non         | Normal    | Oui     |
| Adulte | Non    | Oui         | Maigre    | Non     |
| Âgé    | Oui    | Non         | Corpulent | Oui     |
| Âgé    | Oui    | Oui         | Normal    | Oui     |
| Âgé    | Oui    | Non         | Corpulent | Oui     |
| Âgé    | Non    | Oui         | Normal    | Non     |
| Jeune  | Non    | Non         | Normal    | Non     |

**Total : 14 exemples**
- **Dyspnée = Oui : 5**
- **Dyspnée = Non : 9**

---

## 1. Calculer l'entropie de la variable cible (Dyspnée)

L'entropie mesure l'impureté de la variable cible.

**Formule :**
$$H(Y) = -\sum_{i} p_i \log_2(p_i)$$

Avec :
- $p(\text{Oui}) = \frac{5}{14}$
- $p(\text{Non}) = \frac{9}{14}$

$$H(\text{Dyspnée}) = -\frac{5}{14}\log_2\left(\frac{5}{14}\right) - \frac{9}{14}\log_2\left(\frac{9}{14}\right)$$

$$H(\text{Dyspnée}) = -\frac{5}{14} \times (-1.485) - \frac{9}{14} \times (-0.637)$$

$$H(\text{Dyspnée}) = 0.530 + 0.410 = \boxed{0.940 \text{ bits}}$$

---

## 2. Calculer l'entropie des 4 variables X et déduire celle à choisir en premier

Pour chaque variable, on calcule le **gain d'information** :
$$\text{Gain}(Y, X) = H(Y) - H(Y|X)$$

où $H(Y|X)$ est l'entropie conditionnelle :
$$H(Y|X) = \sum_{v \in \text{valeurs}(X)} \frac{|X=v|}{|D|} \times H(Y|X=v)$$

### 2.1. Variable **Age**

| Age    | Total | Oui | Non | Entropie |
|--------|-------|-----|-----|----------|
| Jeune  | 4     | 0   | 4   | 0        |
| Adulte | 4     | 2   | 2   | 1.000    |
| Âgé    | 6     | 3   | 3   | 1.000    |

$$H(\text{Dyspnée}|\text{Age}) = \frac{4}{14}(0) + \frac{4}{14}(1.000) + \frac{6}{14}(1.000)$$
$$= 0 + 0.286 + 0.429 = 0.715$$

$$\text{Gain}(\text{Age}) = 0.940 - 0.715 = \boxed{0.225}$$

### 2.2. Variable **Fumeur**

| Fumeur | Total | Oui | Non | Entropie |
|--------|-------|-----|-----|----------|
| Oui    | 8     | 5   | 3   | 0.954    |
| Non    | 6     | 0   | 6   | 0        |

$$H(\text{Dyspnée}|\text{Fumeur}) = \frac{8}{14}(0.954) + \frac{6}{14}(0)$$
$$= 0.545 + 0 = 0.545$$

$$\text{Gain}(\text{Fumeur}) = 0.940 - 0.545 = \boxed{0.395}$$

### 2.3. Variable **Asthmatique**

| Asthmatique | Total | Oui | Non | Entropie |
|-------------|-------|-----|-----|----------|
| Oui         | 4     | 2   | 2   | 1.000    |
| Non         | 10    | 3   | 7   | 0.881    |

$$H(\text{Dyspnée}|\text{Asthmatique}) = \frac{4}{14}(1.000) + \frac{10}{14}(0.881)$$
$$= 0.286 + 0.629 = 0.915$$

$$\text{Gain}(\text{Asthmatique}) = 0.940 - 0.915 = \boxed{0.025}$$

### 2.4. Variable **Poids**

| Poids     | Total | Oui | Non | Entropie |
|-----------|-------|-----|-----|----------|
| Normal    | 6     | 2   | 4   | 0.918    |
| Maigre    | 3     | 0   | 3   | 0        |
| Corpulent | 5     | 3   | 2   | 0.971    |

$$H(\text{Dyspnée}|\text{Poids}) = \frac{6}{14}(0.918) + \frac{3}{14}(0) + \frac{5}{14}(0.971)$$
$$= 0.393 + 0 + 0.347 = 0.740$$

$$\text{Gain}(\text{Poids}) = 0.940 - 0.740 = \boxed{0.200}$$

### Récapitulatif des gains d'information :

| Variable    | Gain d'information |
|-------------|--------------------|
| Fumeur      | **0.395**          |
| Age         | 0.225              |
| Poids       | 0.200              |
| Asthmatique | 0.025              |

**→ La variable à choisir en premier est : Fumeur** (gain maximal)

---

## 3. Effectuer la même démarche sur les différentes branches non terminales

### Branche : **Fumeur = Non**
6 exemples, tous avec Dyspnée = Non → **Nœud terminal : Non**

### Branche : **Fumeur = Oui**
8 exemples : 5 Oui, 3 Non

$$H(\text{Dyspnée}|\text{Fumeur=Oui}) = 0.954$$

On calcule le gain pour les variables restantes :

#### 3.1. Variable **Age** (Fumeur = Oui)

| Age    | Total | Oui | Non | Entropie |
|--------|-------|-----|-----|----------|
| Jeune  | 2     | 0   | 2   | 0        |
| Adulte | 2     | 2   | 0   | 0        |
| Âgé    | 4     | 3   | 1   | 0.811    |

$$H(\text{Dyspnée}|\text{Age, Fumeur=Oui}) = \frac{2}{8}(0) + \frac{2}{8}(0) + \frac{4}{8}(0.811) = 0.406$$

$$\text{Gain}(\text{Age}) = 0.954 - 0.406 = \boxed{0.548}$$

#### 3.2. Variable **Asthmatique** (Fumeur = Oui)

| Asthmatique | Total | Oui | Non | Entropie |
|-------------|-------|-----|-----|----------|
| Oui         | 3     | 2   | 1   | 0.918    |
| Non         | 5     | 3   | 2   | 0.971    |

$$H(\text{Dyspnée}|\text{Asthmatique, Fumeur=Oui}) = \frac{3}{8}(0.918) + \frac{5}{8}(0.971) = 0.951$$

$$\text{Gain}(\text{Asthmatique}) = 0.954 - 0.951 = \boxed{0.003}$$

#### 3.3. Variable **Poids** (Fumeur = Oui)

| Poids     | Total | Oui | Non | Entropie |
|-----------|-------|-----|-----|----------|
| Normal    | 2     | 2   | 0   | 0        |
| Maigre    | 2     | 0   | 2   | 0        |
| Corpulent | 4     | 3   | 1   | 0.811    |

$$H(\text{Dyspnée}|\text{Poids, Fumeur=Oui}) = \frac{2}{8}(0) + \frac{2}{8}(0) + \frac{4}{8}(0.811) = 0.406$$

$$\text{Gain}(\text{Poids}) = 0.954 - 0.406 = \boxed{0.548}$$

**→ Les variables Age et Poids ont le même gain (0.548). On choisit : Age**

#### Sous-branches de Age (quand Fumeur = Oui) :

- **Age = Jeune** : 2 exemples, tous Non → **Nœud terminal : Non**
- **Age = Adulte** : 2 exemples, tous Oui → **Nœud terminal : Oui**
- **Age = Âgé** : 4 exemples (3 Oui, 1 Non) → Continuer la division

#### Pour Age = Âgé et Fumeur = Oui (4 exemples : 3 Oui, 1 Non)

Variables restantes : Asthmatique, Poids

**Asthmatique :**
- Oui : 2 exemples (1 Oui, 1 Non) → Entropie = 1.000
- Non : 2 exemples (2 Oui, 0 Non) → Entropie = 0

$$H(\text{Dyspnée}|\text{Asthmatique}) = \frac{2}{4}(1.000) + \frac{2}{4}(0) = 0.500$$
$$\text{Gain}(\text{Asthmatique}) = 0.811 - 0.500 = 0.311$$

**Poids :**
- Normal : 1 exemple (Oui) → Entropie = 0
- Corpulent : 3 exemples (2 Oui, 1 Non) → Entropie = 0.918

$$H(\text{Dyspnée}|\text{Poids}) = \frac{1}{4}(0) + \frac{3}{4}(0.918) = 0.689$$
$$\text{Gain}(\text{Poids}) = 0.811 - 0.689 = 0.122$$

**→ On choisit Asthmatique (gain = 0.311)**

- **Asthmatique = Oui** : continuer (1 Oui, 1 Non) → besoin de Poids
  - Poids = Normal : 1 exemple (Oui) → **Oui**
  - Poids = Corpulent : 1 exemple (Non) → **Non**
- **Asthmatique = Non** : 2 exemples, tous Oui → **Nœud terminal : Oui**

---

## 4. Arbre de décision obtenu

```
                        Fumeur ?
                       /        \
                    Oui          Non
                    /              \
                 Age ?            [Non]
               /   |   \
           Jeune Adulte Âgé
            /      |      \
         [Non]   [Oui]   Asthmatique ?
                         /            \
                       Oui            Non
                       /                \
                   Poids ?             [Oui]
                   /     \
               Normal  Corpulent
                /          \
             [Oui]        [Non]
```

### Règles de décision :

1. **Si Fumeur = Non** → **Dyspnée = Non**
2. **Si Fumeur = Oui et Age = Jeune** → **Dyspnée = Non**
3. **Si Fumeur = Oui et Age = Adulte** → **Dyspnée = Oui**
4. **Si Fumeur = Oui et Age = Âgé et Asthmatique = Non** → **Dyspnée = Oui**
5. **Si Fumeur = Oui et Age = Âgé et Asthmatique = Oui et Poids = Normal** → **Dyspnée = Oui**
6. **Si Fumeur = Oui et Age = Âgé et Asthmatique = Oui et Poids = Corpulent** → **Dyspnée = Non**

---

## Conclusion

L'arbre de décision permet de classifier la dyspnée en fonction des 4 variables d'entrée. L'ordre des tests à effectuer est :
1. **Fumeur** (meilleur gain d'information)
2. **Age** (pour la branche Fumeur = Oui)
3. **Asthmatique** (pour la branche Age = Âgé)
4. **Poids** (pour affiner certains cas)
