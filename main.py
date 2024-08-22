
from Parking import Parking
from Car import Car  # Import the Car class
from typing import Optional

# Instantiate the Parking class
parking = Parking(capacity=20)  # Replace '20' with the desired capacity value

file_path = 'CarFile.xlsx'

# Votre code ici
def main():
    # Créer une instance de la classe Parking
    #parking = Parking.Parking(capacity=20)  # Replace '10' with the desired capacity value
    parking.add_cars_from_excel(file_path)  # Add cars from the Excel file

    # Utiliser les fonctionnalités du parking
    # Exemple: Ajouter une voiture
    
    car = Car(brand="Toyota", model="Corolla", plaque="ABC123")  # Create a Car object with appropriate attributes
    parking.add_car(car)

    # Exemple: Vérifier si une place est occupée
    place_occupee = parking.get_available_spaces()

    # Exemple: Afficher toutes les voitures dans le parking
    voitures = parking.get_all_cars()
    for voiture in voitures:
        print(f"Marque: {voiture.brand}, Modèle: {voiture.model}, Plaque: {voiture.plaque}")


        # Menu de choix
        while True:
            print("Menu:")
            print("1. Ajouter une voiture")
            print("2. Afficher toutes les voitures")
            print("3. Vérifier si une place est occupée")
            print("4. Supprimer une voiture")
            print("5. Modifier une voiture")
            print("6. Afficher détails une voiture")
            print("7. Quitter")

            choice = input("Choisissez une option (1-5): ")

            if choice == "1":
                # Ajouter une voiture
                brand = input("Marque de la voiture: ")
                model = input("Modèle de la voiture: ")
                plaque = input("Plaque d'immatriculation de la voiture: ")
                car = Car(brand=brand, model=model, plaque=plaque)
                parking.add_car(car)
                parking.update_car_in_excel(index=len(parking.get_all_cars())-1, file_path=file_path)
                print("Voiture ajoutée avec succès!")

            elif choice == "2":
                # Afficher toutes les voitures
                voitures = parking.get_all_cars()
                for index, voiture in enumerate(voitures):
                    print(f"Place {index+1}: Marque: {voiture.brand}, Modèle: {voiture.model}, Plaque: {voiture.plaque}")


            elif choice == "3":
                # Vérifier si une place est occupée
                place_occupee = parking.get_available_spaces()
                if place_occupee:
                    print("Il y a des places occupées.")
                else:
                    print("Toutes les places sont disponibles.")

            elif choice == "4":
                # Supprimer une voiture
                index = int(input("Index de l'emplacement de la voiture à supprimer: "))
                if index >= 1 and index <= parking.capacity:
                    voiture = parking.get_car_at_index(index-1)
                    if voiture:
                        parking.remove_car_by_index(index-1)
                        parking.remove_car_from_excel(index-1, file_path)
                        print("Voiture supprimée avec succès!")
                    else:
                        print("Aucune voiture à cet emplacement.")
                else:
                    print("Index invalide. Veuillez choisir un index valide.")

            elif choice == "5":
                # Modifier les données d'une voiture
                index = int(input("Index de l'emplacement de la voiture à modifier: "))
                if index >= 1 and index <= parking.capacity:
                    voiture = parking.get_car_at_index(index-1)
                    if voiture:
                        brand = input("Nouvelle marque de la voiture: ")
                        model = input("Nouveau modèle de la voiture: ")
                        plaque = input("Nouvelle plaque d'immatriculation de la voiture: ")
                        voiture.brand = brand
                        voiture.model = model
                        voiture.plaque = plaque
                        parking.update_car_in_excel(index-1, file_path)
                        print("Voiture modifiée avec succès!")
                    else:
                        print("Aucune voiture à cet emplacement.")
                else:
                    print("Index invalide. Veuillez choisir un index valide.")
                    
                    
            elif choice == "6":
                # Afficher les détails d'une voiture en donnant l'index
                index = int(input("Index de l'emplacement de la voiture: "))
                if index >= 1 and index <= parking.capacity:
                    voiture = parking.get_car_at_index(index-1)
                    if voiture:
                        print(f"Marque: {voiture.brand}, Modèle: {voiture.model}, Plaque: {voiture.plaque}")
                    else:
                        print("Aucune voiture à cet emplacement.")
                else:
                    print("Index invalide. Veuillez choisir un index valide.")

            elif choice == "7":
                # Quitter le programme
                break

            else:
                print("Option invalide. Veuillez choisir une option valide.")

# Appeler la fonction principale
if __name__ == "__main__":
    main()