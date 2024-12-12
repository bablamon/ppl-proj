from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

data = {
    "Nigdi": {
        "Akurdi": {"Walking": (2, 25), "Driving": (2, 5), "Cycling": (2, 10), "Bus": (2, 7)},
        "Ravet": {"Walking": (5, 60), "Driving": (5, 15), "Cycling": (5, 25), "Bus": (5, 20)},
        "Wakad": {"Walking": (10, 120), "Driving": (10, 25), "Cycling": (10, 50), "Bus": (10, 30)},
        "Chinchwad": {"Walking": (3, 35), "Driving": (3, 7), "Cycling": (3, 15), "Bus": (3, 10)},
        "Pimpri": {"Walking": (6, 75), "Driving": (6, 15), "Cycling": (6, 35), "Bus": (6, 20)},
    },
    "Akurdi": {
        "Nigdi": {"Walking": (2, 25), "Driving": (2, 5), "Cycling": (2, 10), "Bus": (2, 7)},
        "Ravet": {"Walking": (3, 40), "Driving": (3, 10), "Cycling": (3, 15), "Bus": (3, 12)},
        "Wakad": {"Walking": (8, 100), "Driving": (8, 20), "Cycling": (8, 40), "Bus": (8, 25)},
        "Chinchwad": {"Walking": (1, 15), "Driving": (1, 3), "Cycling": (1, 5), "Bus": (1, 5)},
        "Pimpri": {"Walking": (5, 60), "Driving": (5, 12), "Cycling": (5, 25), "Bus": (5, 15)},
    },
    "Ravet": {
        "Nigdi": {"Walking": (5, 60), "Driving": (5, 15), "Cycling": (5, 25), "Bus": (5, 20)},
        "Akurdi": {"Walking": (3, 40), "Driving": (3, 10), "Cycling": (3, 15), "Bus": (3, 12)},
        "Wakad": {"Walking": (6, 75), "Driving": (6, 12), "Cycling": (6, 20), "Bus": (6, 15)},
        "Chinchwad": {"Walking": (4, 50), "Driving": (4, 8), "Cycling": (4, 15), "Bus": (4, 10)},
        "Pimpri": {"Walking": (8, 100), "Driving": (8, 20), "Cycling": (8, 35), "Bus": (8, 25)},
    },
    "Wakad": {
        "Nigdi": {"Walking": (10, 120), "Driving": (10, 25), "Cycling": (10, 50), "Bus": (10, 30)},
        "Akurdi": {"Walking": (8, 100), "Driving": (8, 20), "Cycling": (8, 40), "Bus": (8, 25)},
        "Ravet": {"Walking": (6, 75), "Driving": (6, 12), "Cycling": (6, 20), "Bus": (6, 15)},
        "Chinchwad": {"Walking": (5, 60), "Driving": (5, 10), "Cycling": (5, 20), "Bus": (5, 12)},
        "Pimpri": {"Walking": (4, 50), "Driving": (4, 8), "Cycling": (4, 15), "Bus": (4, 10)},
    },
    "Chinchwad": {
        "Nigdi": {"Walking": (3, 35), "Driving": (3, 7), "Cycling": (3, 15), "Bus": (3, 10)},
        "Akurdi": {"Walking": (1, 15), "Driving": (1, 3), "Cycling": (1, 5), "Bus": (1, 5)},
        "Ravet": {"Walking": (4, 50), "Driving": (4, 8), "Cycling": (4, 15), "Bus": (4, 10)},
        "Wakad": {"Walking": (5, 60), "Driving": (5, 10), "Cycling": (5, 20), "Bus": (5, 12)},
        "Pimpri": {"Walking": (2, 25), "Driving": (2, 5), "Cycling": (2, 10), "Bus": (2, 7)},
    },
    "Pimpri": {
        "Nigdi": {"Walking": (6, 75), "Driving": (6, 15), "Cycling": (6, 35), "Bus": (6, 20)},
        "Akurdi": {"Walking": (5, 60), "Driving": (5, 12), "Cycling": (5, 25), "Bus": (5, 15)},
        "Ravet": {"Walking": (8, 100), "Driving": (8, 20), "Cycling": (8, 35), "Bus": (8, 25)},
        "Wakad": {"Walking": (4, 50), "Driving": (4, 8), "Cycling": (4, 15), "Bus": (4, 10)},
        "Chinchwad": {"Walking": (2, 25), "Driving": (2, 5), "Cycling": (2, 10), "Bus": (2, 7)},
    },
}

class PCMCNavigation(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

    
        self.title_label = Label(text="PCMC Navigation", font_size=24, bold=True, size_hint=(1, 0.2))
        self.add_widget(self.title_label)

        
        self.step1_label = Label(text="Where are you currently?", font_size=18, size_hint=(1, 0.1))
        self.add_widget(self.step1_label)

        self.current_location_spinner = Spinner(
            text="Select Location",
            values=["Nigdi", "Akurdi", "Ravet", "Wakad", "Chinchwad", "Pimpri"],
            size_hint=(1, 0.2),
        )
        self.add_widget(self.current_location_spinner)

        
        self.proceed_button = Button(
            text="Proceed",
            size_hint=(1, 0.2),
            on_press=self.proceed_to_step2
        )
        self.add_widget(self.proceed_button)

    def proceed_to_step2(self, instance):
        current_location = self.current_location_spinner.text
        if current_location == "Select Location":
            return  

        self.clear_widgets()
        self.add_widget(Label(text="Where do you want to travel?", font_size=18, size_hint=(1, 0.1)))

        self.destination_spinner = Spinner(
            text="Select Destination",
            values=["Nigdi", "Akurdi", "Ravet", "Wakad", "Chinchwad", "Pimpri"],
            size_hint=(1, 0.2),
        )
        self.add_widget(self.destination_spinner)

        self.add_widget(Label(text="How do you want to travel?", font_size=18, size_hint=(1, 0.1)))

        self.transport_spinner = Spinner(
            text="Select Mode of Transport",
            values=["Walking", "Driving", "Cycling", "Bus"],
            size_hint=(1, 0.2),
        )
        self.add_widget(self.transport_spinner)

        self.add_widget(Button(
            text="Show Time and Distance",
            size_hint=(1, 0.2),
            on_press=self.show_route
        ))

    def show_route(self, instance):
        current_location = self.current_location_spinner.text
        destination = self.destination_spinner.text
        transport_mode = self.transport_spinner.text

        if (
            current_location == "Select Location"
            or destination == "Select Destination"
            or transport_mode == "Select Mode of Transport"
        ):
            self.display_error("Please select valid options.")
            return

        if current_location == destination:
            self.display_error("You are already at the selected destination!")
            return

        route_info = data.get(current_location, {}).get(destination, {})
        if transport_mode in route_info:
            distance, time = route_info[transport_mode]
            self.display_route(current_location, destination, transport_mode, distance, time)
        else:
            self.display_error("No route information available for this selection.")

    def display_route(self, start, end, mode, distance, time):
        self.clear_widgets()
        self.add_widget(Label(
            text=f"Route from {start} to {end} via {mode}:",
            font_size=18,
            size_hint=(1, 0.2),
        ))
        self.add_widget(Label(
            text=f"Distance: {distance} km\nEstimated Time: {time} minutes",
            font_size=16,
            size_hint=(1, 0.4),
        ))
        self.add_widget(Button(
            text="Back to Start",
            size_hint=(1, 0.2),
            on_press=lambda x: self.__init__()
        ))

    def display_error(self, message):
        self.clear_widgets()
        self.add_widget(Label(text=message, font_size=18, size_hint=(1, 0.2)))
        self.add_widget(Button(text="Back", size_hint=(1, 0.2), on_press=lambda x: self.__init__()))


class PCMCNavigationApp(App):
    def build(self):
        return PCMCNavigation()


if __name__ == "__main__":
    PCMCNavigationApp().run()
