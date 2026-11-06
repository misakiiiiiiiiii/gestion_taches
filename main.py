def main():
    taches = []
    
    while True:
        print("\n=== GESTION DES TACHES ===")
        print("1. Ajouter une tâche")
        print("2. Afficher")
        print("3. Rechercher")
        print("0. Quitter")
        
        choix = input("Votre choix : ").strip()
        
        if choix == "1":
            titre = input("Titre de la tâche : ").strip()
            if titre == "":
                print("Erreur : La saisie ne peut pas être vide.")
            else:
                taches.append(titre)
                print("Tâche ajoutée avec succès.")
                
        elif choix == "2":
            if not taches:
                print("La liste des tâches est vide.")
            else:
                print("\n--- Liste des tâches ---")
                for i, t in enumerate(taches, start=1):
                    print(f"{i}. {t}")
                    
        elif choix == "3":
            if not taches:
                print("La liste est vide, aucune recherche possible.")
            else:
                mot_cle = input("Entrez un mot-clé à rechercher : ").strip().lower()
                resultats = [t for t in taches if mot_cle in t.lower()]
                if resultats:
                    print("\n--- Résultats de la recherche ---")
                    for t in resultats:
                        print(f"- {t}")
                else:
                    print("Aucune tâche trouvée avec ce mot-clé.")
                    
        elif choix == "0":
            print("Fermeture du programme. Au revoir !")
            break
            
        else:
            print("Erreur : Option invalide. Veuillez choisir entre 0, 1, 2 et 3.")

if __name__ == "__main__":
    main()
 