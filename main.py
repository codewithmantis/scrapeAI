import streamlit as st
from scrape import scrape_website
from transformers import pipeline

st.title("AI WBESS")
url = st.text_input("Enter your website URL")

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

if st.button("Scrape Site"):
    st.write("Scraping Website...")
    result = scrape_website(url)

    # Check if the result is not empty
    if result:
        try:
            # Depending on the length of the content, you might need to truncate it for the model
            if len(result) > 1024:  # max token length for many models
                result = result[:1024]  # Truncate to 1024 characters
                
            # Generate the summary using Hugging Face HuggingFace
            summary_result = summarizer(result, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
        except Exception as e:
            summary_result = f"Error in summarizing the text: {str(e)}"
      
        # Display the results
        st.subheader("Full Scraped Text:")
        st.markdown(f"<p>{result}</p>", unsafe_allow_html=True)

        st.subheader("Summary:")
        st.markdown(f"<p>{summary_result}</p>", unsafe_allow_html=True)
    else:
        st.write("No content retrieved from the website.")
