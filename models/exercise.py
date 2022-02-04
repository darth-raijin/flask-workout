class Exercise:

    def _init_(self, name: str, category: str = "", sets: list = []):
        self.__name = name
        self.__sets = sets
        self.__category = category
        self.__total_weight = 0
        self.__distance = 0
        self.__time = "hh:mm:ss"
        return

    def calculate_weight(self):
        """Calculates total weight moved during exercise
        """
        for item in self.__sets:
            # Iterates through a list with dictionaries
            
            repetitions = item.get("repetitions")
            weight = item.get("weight")

            self.__total_weight += weight * repetitions
    
    def get_sets(self):
        return self.__sets
    
    def set_sets(self, sets: list):
        self.__sets = sets
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name: str):
        self.__name = name

    def get_total_weight(self):
        return self.__total_weight
    
    def get_category(self):
        return self.__category

    def set_category(self, category: str):
        """Setting category and changing exercise type
            By changing category, 
            category-specific attributes will be set to default.
        Args:
            category (str): Either "Strength" or "Cardio". 
        """
        if category == "Strength":
            self.__category = "Strength"
            self.__distance = None
            self.__time = None

        if category == "Cardio":
            self.__category = "Cardio"
            self.__sets = []
            self.__total_weight = 0
    
    def get_distance(self):
        return self.__distance

    def set_distance(self, distance: float):
        self.__distance = distance

    def get_time(self):
        return self.__time
    
    def set_time(self, time: str):
        self.__time = time
