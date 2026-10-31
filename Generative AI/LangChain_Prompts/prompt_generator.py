from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=['paper_input', 'style_input', 'length_input'],
    validate_inputs=True,
    template="Please summarize the research paper titled '{paper_input}' with the followin specifications: \n\n- Explaination Style: {style_input}\n- Explaination Length: {length_input}\n\nPlease provide a clear and concise summary of the paper, highlighting the key concepts, methodologies, and findings. Ensure that the summary is tailored to the specified explaination style and length."
)

template.save('template.json')