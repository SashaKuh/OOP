class ListDataProvider:
    def get_data(self):
        return ["one", "two", "three"]


class StringDataClient:
    def display_data(self, data):
        print(f"Data: {data}")


class ListToStringAdapter:
    def __init__(self, list_provider):
        self.list_provider = list_provider

    def get_data_as_string(self):
        return ", ".join(self.list_provider.get_data())


list_provider_obj = ListDataProvider()
adapter = ListToStringAdapter(list_provider_obj)
client = StringDataClient()

client.display_data(adapter.get_data_as_string())
