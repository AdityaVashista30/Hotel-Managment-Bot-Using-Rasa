# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime


class ActionGiveCleanTime(Action):

    def name(self) -> Text:
        return "action_schedule_cleaning"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        after = tracker.get_slot("hours")
        t=datetime.now()
        newH=t.hour + after
        if newH>24:
            newH= newH%24
            s="Sure, I have scheduled a cleaning for "+str(newH)+":"+str(t.minute)+" am today."
        if newH>12:
            newH= newH%12
            s="Sure, I have scheduled a cleaning for "+str(newH)+":"+str(t.minute)+" pm today."
        else:
            s="Sure, I have scheduled a cleaning for "+str(newH)+":"+str(t.minute)+" am today."
        dispatcher.utter_message(text=s)

        return []
