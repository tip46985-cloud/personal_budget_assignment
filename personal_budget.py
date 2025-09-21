# Personal Budget Management System
# Demonstrates encapsulation using private attributes, getters, and setters

class BudgetCategory:
    def __init__(self, name, allocated_budget):
        # Private attributes
        self.__category_name = name
        if allocated_budget < 0:
            raise ValueError("Allocated budget must be positive")
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, new_name):
        if not new_name:
            print("Category name cannot be empty.")
            return
        self.__category_name = new_name
        print(f"Category name updated to: {self.__category_name}")

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget
    def set_allocated_budget(self, new_budget):
        if new_budget < 0:
            print("Allocated budget must be positive.")
            return
        # Adjust remaining budget relative to previous allocation
        difference = new_budget - self.__allocated_budget
        self.__allocated_budget = new_budget
        self.__remaining_budget += difference
        print(f"Allocated budget updated to: ${self.__allocated_budget}")

    # Method to add an expense
    def add_expense(self, amount):
        if amount <= 0:
            print("Expense amount must be positive.")
            return
        if amount > self.__remaining_budget:
            print(f"Cannot add expense of ${amount}. Only ${self.__remaining_budget} remaining.")
            return
        self.__remaining_budget -= amount
        print(f"Expense of ${amount} added. Remaining budget: ${self.__remaining_budget}")

    # Method to display category summary
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")
        print("-" * 30)


# ----------------------------
# Demonstration of functionality
# ----------------------------

# Create budget categories
food_category = BudgetCategory("Food", 500)
entertainment_category = BudgetCategory("Entertainment", 300)

# Display initial summaries
food_category.display_category_summary()
entertainment_category.display_category_summary()

# Add expenses
food_category.add_expense(150)
entertainment_category.add_expense(50)

# Update category details
food_category.set_category_name("Groceries")
entertainment_category.set_allocated_budget(400)

# Display updated summaries
food_category.display_category_summary()
entertainment_category.display_category_summary()

