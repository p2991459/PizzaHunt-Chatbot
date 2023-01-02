# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet



class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_tell_name"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        print(name)
        dispatcher.utter_message(text="Hey, {}. ! Welcome to PizzHunt. In today's menu, we have Funghi,"
                " Hawaii, Margherita, Pepperoni, Vegetarian,"
         "all available in sizes Small, Medium or Large . What would you like to have?".format(name))

        return []


class PizzaOrderForm(FormValidationAction):

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "pizza_order_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["pizza_type", "pizza_amount", "pizza_size"]
    # async def run(
    #         self,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any],
    # ) -> List[Dict[Text, Any]]:
    #     pizza_type = tracker.get_slot("pizza_type")
    #     pizza_amount = tracker.get_slot("pizza_amount")
    #     pizza_size = tracker.get_slot("pizza_size")
    #     if pizza_type is None:
    #         dispatcher.utter_message(text="What type of pizza do you want?")
    #         print("pizza type none tha")
    #     elif pizza_amount is None:
    #         dispatcher.utter_message(text="How many pizzas do you want?")
    #         print("pizza amount none tha")
    #     elif pizza_size is None:
    #         dispatcher.utter_message(text="What size of pizza do you want?")
    #         print("pizza size none tha")
    #
    #     return []

class FormSubmit(Action):
    def name(self) -> Text:
        return "action_form_submit"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        pizza_type = tracker.get_slot("pizza_type")
        pizza_amount = (tracker.get_slot("pizza_amount"))
        pizza_size = tracker.get_slot("pizza_size")
        print("user want {} size of pizza is {} and quantities of pizza are {}".format(pizza_type,pizza_size,pizza_amount))
        dispatcher.utter_message(text="Okay Great. Your order is {} {} {} pizzas. Can you confirm please".format(pizza_amount,pizza_size,pizza_type))

        return []

# class total_order(Action):
#     def name(self) -> Text:
#         return "action_total_order"
#
#     async def run(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         pizza_type = tracker.get_slot("pizza_type")
#         pizza_amount = tracker.get_slot("pizza_amount")
#         pizza_size = tracker.get_slot("pizza_size")
#         total_order = [str(pizza_amount + " "+pizza_type + " is of "+pizza_size )]
#
#         print(total_order)
#         dispatcher.utter_message(text="Here is your total order, {} . what is your name and phone number?".format(total_order))
#
#         return []

class providing_order_number(Action):
    def name(self) -> Text:
        return "action_order_number"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        global order_number
        import random
        order_number = random.randint(383847, 485878)
        print(order_number)
        pizza_type = tracker.get_slot("pizza_type")
        if pizza_type == None:
            dispatcher.utter_message(text="Your delivery address is saved! thank you for reaching us.")

        else:
            dispatcher.utter_message(
                text="Here is your order number {}. Your order will be sent at your doorstep in 15minutes. "
                     "Thanks for the opportunity to serve you.".format(
                    order_number))

        return []


class ResetSlot(Action):
    def name(self) -> Text:
        return "action_reset_form_slot"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        pizza_type = tracker.get_slot("pizza_type")
        pizza_amount = tracker.get_slot("pizza_amount")
        pizza_size = tracker.get_slot("pizza_size")
        print(" slot reseting done")

        return [SlotSet("pizza_type", None), SlotSet("pizza_amount", None), SlotSet("pizza_size", None)]


class ActionCheckUserLog_in(Action):
    def name(self) -> Text:
        return "action_user_logged"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        print(name)
        if name == None:
            dispatcher.utter_message(text="Hii! What is your name?")
        else:
            dispatcher.utter_message(text="Hey, {} ! Welcome back to PizzHunt."
                            " In today's menu, we have Funghi, Hawaii, Margherita, Pepperoni, Vegetarian,"
                    "all available in sizes Small, Medium or Large . What would you like to have?".format(name))

        return []


class ActionYesResponse(Action):
    def name(self) -> Text:
        return "action_res_order_confirm_if_yes"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        pizza_type = tracker.get_slot("pizza_type")
        pizza_amount = tracker.get_slot("pizza_amount")
        pizza_size = tracker.get_slot("pizza_size")
        if pizza_type == None:
            dispatcher.utter_message(text="Sorry, I didn’t understand that. Can you please retype it?")
        else:
            dispatcher.utter_message(text="Great. Anything else?")

        return []


class ActionResponseNo(Action):
    def name(self) -> Text:
        return "action_user_said_no"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        pizza_type = tracker.get_slot("pizza_type")
        pizza_amount = tracker.get_slot("pizza_amount")
        pizza_size = tracker.get_slot("pizza_size")
        total_order = [str(str(pizza_amount) + " " + pizza_size+ " size " + pizza_type + " Pizza")]

        print(total_order)
        if pizza_type == None:
            dispatcher.utter_message(text="Sorry, I didn’t understand that. Can you please retype it?")
        else:
            dispatcher.utter_message(text="Here is your total order, {} . "
                                          "what is your name and phone number?".format(total_order))


        return []


class ActionOrder_Cancellation(Action):
    def name(self) -> Text:
        return "action_res_order_cancel"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        global order_number
        cancel_number = tracker.get_slot("cancel_number")
        print("cancel order number is {} and order number is {} ".format(cancel_number,order_number))

        if int(order_number) == int(cancel_number):
            dispatcher.utter_message(text="Your order has been cancelled successfully!!if any amount deducted it will be refund within 10 minutes.")
        else:
            dispatcher.utter_message(text="Cancellation failed.You have entered incorrect "
                                          "or depricated order number. Please try again")
        return []