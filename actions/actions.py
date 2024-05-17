from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
import rasa_sdk.executor
import random

from rasa_sdk.events import SlotSet


class ActionVerifierDisponibilite(Action):

    def name(self) -> Text:
        return "action_verifier_disponibilite"

    def run(self, dispatcher: rasa_sdk.CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Supposons que la disponibilité est toujours vérifiée et est positive.
        dispatcher.utter_message(text="Vérification de la disponibilité en cours...")
        return []


class ActionGenererNumeroReservation(Action):

    def name(self) -> Text:
        return "action_generer_numero_reservation"

    def run(self, dispatcher: rasa_sdk.CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        numero_reservation = str(random.randint(1000, 9999))
        return [SlotSet("numero_reservation", numero_reservation)]


class ActionAnnulerReservation(Action):

    def name(self) -> Text:
        return "action_annuler_reservation"

    def run(self, dispatcher: rasa_sdk.CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Votre réservation a été annulée avec succès.")
        return []


class ActionObtenirInformationReservation(Action):

    def name(self) -> Text:
        return "action_obtenir_information_reservation"

    def run(self, dispatcher: rasa_sdk.CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date_reservation = tracker.get_slot("date_reservation")
        nombre_personnes = tracker.get_slot("nombre_personnes")
        nom_reservation = tracker.get_slot("nom_reservation")
        nom_restaurant = tracker.get_slot("nom_restaurant")
        message = f"Voici les informations sur votre réservation : Date : {date_reservation}, Nombre de personnes : {nombre_personnes}, Nom de réservation : {nom_reservation}, Restaurant : {nom_restaurant}."
        dispatcher.utter_message(text=message)
        return []
