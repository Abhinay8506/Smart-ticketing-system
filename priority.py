class PriorityEngine:
    def assign_priority(self, category):
    
        if category in ["NETWORK", "SAP", "IT"]:
            return 1      # HIGH
        elif category == "HR":
            return 2      # MEDIUM
        else:
            return 3      # LOW