from Car import Car
import pandas as pd
from typing import Optional, Tuple

class Parking:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cars = []

    def add_car(self, car: Car) -> None:
        if len(self.cars) < self.capacity:
            self.cars.append(car)
            print(f"La voiture {car.brand} {car.model} avec la plaque {car.plaque} a été ajoutée au parking.")
        else:
            print("Le parking est plein. Impossible d'ajouter une nouvelle voiture.")

    def remove_car_by_index(self, index: int) -> None:
        if 0 <= index < len(self.cars):
            car = self.cars.pop(index)
            print(f"La voiture à l'index {index} avec la plaque {car.plaque} a été supprimée du parking.")
        else:
            print(f"Aucune voiture trouvée à l'index {index}.")
                    
    def get_available_spaces(self) -> int:
        return self.capacity - len(self.cars)

    def get_occupied_spaces(self) -> int:
        return len(self.cars)
    
    def modify_car(self, index: int, new_car: Car) -> None:
        if 0 <= index < len(self.cars):
            self.cars[index] = new_car
            print(f"La voiture à l'index {index} a été modifiée avec succès.")
        else:
            print(f"Aucune voiture trouvée à l'index {index}.")
            
    def get_car_at_index(self, index: int) -> Optional[Car]:
        if 0 <= index < len(self.cars):
            return self.cars[index]
        else:
            return None
    
    def get_car_details(self, index: int) -> None:
        if 0 <= index < len(self.cars):
            car = self.cars[index]
            print(f"Détails de la voiture à l'index {index}:")
            print(f"Plaque: {car.plaque}")
            print(f"Marque: {car.brand}")
            print(f"Modèle: {car.model}")
        else:
            print(f"Aucune voiture trouvée à l'index {index}.")

    def get_all_cars(self) -> list:
        return self.cars
    
    def add_cars_from_excel(self, file_path: str) -> None:
        try:
            df = pd.read_excel(file_path)
            for _, row in df.iterrows():
                brand = row['Brand']
                model = row['Model']
                plaque = row['Plaque']
                car = Car(brand, model, plaque)
                self.add_car(car)
                
            print("Voitures ajoutées avec succès depuis le fichier Excel.")
        except FileNotFoundError:
            print("Le fichier Excel spécifié est introuvable.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'ajout des voitures depuis le fichier Excel: {str(e)}")
            
    def update_car_in_excel(self, index: int, file_path: str) -> None:
        if 0 <= index < len(self.cars):
            try:
                df = pd.read_excel(file_path)
                car = self.cars[index]
                df.loc[index, 'Brand'] = car.brand
                df.loc[index, 'Model'] = car.model
                df.loc[index, 'Plaque'] = car.plaque
                df.to_excel(file_path, index=False)
                print(f"La voiture à l'index {index} a été mise à jour dans le fichier Excel.")
            except FileNotFoundError:
                print("Le fichier Excel spécifié est introuvable.")
            except Exception as e:
                print(f"Une erreur s'est produite lors de la mise à jour de la voiture dans le fichier Excel: {str(e)}")
        else:
            print(f"Aucune voiture trouvée à l'index {index}.")