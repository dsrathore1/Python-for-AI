class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_token=100):
        self.api_key = api_key
        self.model = model
        self.max_token = max_token
        self.base_url = "https://api.openai.com/v1"


dev_config = APIConfig("sk-dev-key", max_token=50)

prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_token=1000)

print(dev_config.api_key)
print(dev_config.max_token)
print(vars(dev_config))
print()
print(prod_config.model)
print(prod_config.max_token)
print(vars(prod_config))
