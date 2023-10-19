import streamlit as st
from difflib import SequenceMatcher
import difflib

def similarity_score(text1, text2):
    # Calculate the similarity score using SequenceMatcher
    return SequenceMatcher(None, text1, text2).ratio()

def visualize_differences(text1, text2):
    differ = difflib.Differ()
    diff = list(differ.compare(text1.splitlines(), text2.splitlines()))

    return '\n'.join(diff)

def main():
    st.title("Plagiarism Checker")

    uploaded_file_1 = st.file_uploader("Upload the first document (TXT, DOC, PDF)", type=["txt", "doc", "pdf","docx"])
    uploaded_file_2 = st.file_uploader("Upload the second document (TXT, DOC, PDF)", type=["txt", "doc", "pdf","docx"])

    if uploaded_file_1 is not None and uploaded_file_2 is not None:
        # Read the contents of both uploaded documents
        file_contents_1 = uploaded_file_1.read()
        file_contents_2 = uploaded_file_2.read()

        st.subheader("Comparison Results")

        st.write("Document 1:")
        st.code(file_contents_1)

        st.write("Document 2:")
        st.code(file_contents_2)

        similarity = similarity_score(file_contents_1, file_contents_2)
        st.write(f"Similarity Score: {similarity:.2%}")

        st.subheader("Visualize Differences")
        differences = visualize_differences(file_contents_1, file_contents_2)
        st.text(differences)

if __name__ == "__main__":
    main()
