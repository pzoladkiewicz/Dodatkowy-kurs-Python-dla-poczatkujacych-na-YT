from Chef import Chef

class ChineseChef(Chef):                                    # inherits all from Chef
    
        
    def make_special_dish(self):                            # override make_special_dish
        print("This chef makes a orange chicken")

    def make_fried_rice(self):
        print("This chef makes fried rice")
