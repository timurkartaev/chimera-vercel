from connectors.scripts.coherence_checker.comparer import FieldComparer
from connectors.views import get_customer_token

if __name__ == "__main__":
    # print(get_customer_token(""))
    FieldComparer.run()
