from transformers import pipeline


class TextSummarizationPipeline:
    def __init__(self, model_name="dhivyeshrk/bart-large-cnn-samsum"):
        self.pipe = pipeline("text2text-generation", model=model_name)

    def generate_summary(self, input_text):
        words = input_text.split(" ")
        if len(words) > 500:
            input_text = " ".join(words[:500])
        return self.pipe(input_text)


# Example Usage
if __name__ == "__main__":
    text_generator = TextSummarizationPipeline()
    input_text = "Arena BioWorks is promising big paydays to nearly 100 researchers from Harvard, M.I.T. and other prestigious institutions. Arena BioWorks is promising big paydays to nearly 100 researchers from Harvard, M.I.T. and other prestigious institutions. In an unmarked laboratory stationed between the campuses of Harvard and the Massachusetts Institute of Technology, a splinter group of scientists is hunting for the next billion-dollar drug."

    output_summary = text_generator.generate_summary(input_text)
    print(output_summary)
