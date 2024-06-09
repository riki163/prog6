import requests
import pprint
import matplotlib.pyplot as plt

class CurrencyTracker:
    def __init__(self):
        self.TrackedCurrencies = []
        self.LastUpdateTime = None

    def __repr__(self):
        return f'CurrencyTracker(tracked_currencies={self.TrackedCurrencies}, last_update_time={self.LastUpdateTime})'

    def GetCurrencies(self):
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        result = response.json()
        return result

    def GetCurrencyValue(self, currency_code):
        currencies_data = self.GetCurrencies()
        return currencies_data['Valute'][currency_code]['Value']

    def AddTrackedCurrency(self, currency_code):
        if currency_code not in self.TrackedCurrencies:
            self.TrackedCurrencies.append(currency_code)
            print(f'{currency_code} добавлен в отслеживаемые валюты.')

    def GetTrackedCurrencies(self):
        return self.TrackedCurrencies

    def SetTrackedCurrencies(self, currencies):
        for currency in currencies:
            self.TrackedCurrencies.append(currency)
        return self.TrackedCurrencies

    def VisualizeCurrencies(self):
        currencies_data = self.GetCurrencies()
        TrackedCurrenciesData = {currency: currencies_data['Valute'][currency]['Value'] for currency in self.TrackedCurrencies}

        plt.figure(figsize=(10, 6))
        bars = plt.bar(TrackedCurrenciesData.keys(), TrackedCurrenciesData.values(), width=0.5, color='r', alpha=0.5)
        plt.title('График')
        plt.xlabel('Код валюты')
        plt.ylabel('Курс валюты')
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, max(TrackedCurrenciesData.values()) + 10)
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{round(yval, 2)} ₽', ha='center', va='bottom', weight='bold')
        plt.tight_layout()
        plt.savefig('images/currencies.jpg')
        plt.show()

if __name__ == "__main__":
    tracker = CurrencyTracker()
    AllCurrencies = tracker.GetCurrencies()
    pprint.pprint(AllCurrencies)

    tracker.SetTrackedCurrencies(['USD', 'TRY'])
    print(f'Отслеживаемые валюты - {tracker.GetTrackedCurrencies()}')
    currency_code = input('Введите код валюты: ')
    value = tracker.GetCurrencyValue(currency_code.upper())
    print(f'{currency_code} - это {value:.2f} рублей')

    currency_tracked = input('Введите валюту: ')
    tracker.AddTrackedCurrency(currency_tracked.upper())
    print(f'Отслеживаемые валюты - {tracker.GetTrackedCurrencies()}')

    tracker.SetTrackedCurrencies(['GEL', 'MDL'])
    tracker.VisualizeCurrencies()
