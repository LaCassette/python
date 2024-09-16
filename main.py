def solve_linear_combination(a, b, c):
    """
    Résout une combinaison linéaire de la forme a*x + b*y = c
    et retourne les valeurs de x et y telles que x + y = 1.
    
    Paramètres :
    a (float) : première constante
    b (float) : deuxième constante
    c (float) : valeur cible

    Retourne :
    tuple : valeurs de x et y
    """
    # Calcul des coefficients x et y
    y = (c - a) / (b - a)
    x = 1 - y
    return x, y

def main():
    """
    Fonction principale pour saisir les valeurs,
    résoudre le système et afficher les résultats.
    """
    try:
        # Saisie des valeurs par l'utilisateur
        a = float(input("Valeur de a : "))
        b = float(input("Valeur de b : "))
        c = float(input("Valeur de c : "))

        # Résolution du système
        x, y = solve_linear_combination(a, b, c)

        # Affichage des résultats
        print(f"\nRésultat : {a:.1f} * {x:.2f} + {b:.1f} * {y:.2f} = {c:.1f}")
        print(f"Vérification : {x:.2f} + {y:.2f} = 1")

    except ValueError:
        print("Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    main()

