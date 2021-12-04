import openai


class AI:

    def __init__(
            self,
            organization, api_key,
            prompt, temperature, max_tokens, presence_penalty, frequency_penalty,
            blacklisted_words):

        openai.organization = organization
        openai.api_key = api_key

        self.prompt = prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.presence_penalty = presence_penalty
        self.frequency_penalty = frequency_penalty
        self.blacklisted_words = blacklisted_words


    def generate_advice(self):
        response = openai.Completion.create(
            engine="davinci",
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stop="\n",
            presence_penalty=self.presence_penalty,
            frequency_penalty=self.frequency_penalty
        )
        advice = response.get("choices")[0].get("text")
        for blacklistedWord in self.blacklisted_words:
            if blacklistedWord in advice.lower():
                return self.generate_advice()
        return advice
