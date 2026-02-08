class TicketClassifier:
    def classify(self, description):
      
        desc = description.lower()

        if "network" in desc or "internet" in desc or "wifi" in desc:
            return "NETWORK"
        elif "sap" in desc or "abap" in desc:
            return "SAP"
        elif "salary" in desc or "payroll" in desc:
            return "HR"
        elif "server" in desc or "database" in desc:
            return "IT"
        else:
            return "GENERAL"
        
        