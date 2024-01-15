import os
import replicate
import envs


class ReplicateAPI:
    """
    High Level and Scalable API for accessing any model hostel on Replicate AI.
    """
    def __init__(self, model_name, api_token=envs.REPLICATE_API):
        os.environ['REPLICATE_API_TOKEN'] = api_token
        self.model_name = model_name
        self.input_params = {
            "top_p": 0.95,  # Probability threshold for generating the output.
            "prompt": "",  # input prompt
            "max_new_tokens": 3,  # Max. number of output tokens being generated.
            "temperature": 0.2,  # Keep temperature low to avoid creativity (and hallucination)
            "frequency_penalty": 1,  # Avoidance of repetition
            "prompt_template":  # Prompt template
                '''
                <s>[INST] {prompt}
                ```ANSWER STRICTLY IN ONE WORD.  
                \nWhich of the following classes does the above statement fall into : 
                1. Technology\n 2. Sports\n 3. Science\n 4. Health\n
                [/INST] 
                '''
        }

    def run_model(self, prompt) -> list:
        self.input_params['prompt'] = prompt
        out = replicate.run(self.model_name, self.input_params)
        return out


if __name__ == '__main__':
    api = ReplicateAPI(model_name='mistralai/mixtral-8x7b-instruct-v0.1')
    output = api.run_model("NASA Rocket Launch")
    print(output)
