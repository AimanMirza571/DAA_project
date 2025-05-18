import streamlit as st
import time
import pandas as pd

def build_bad_char_table(pattern):
    """Build the bad character table for Boyer-Moore algorithm."""
    pattern = pattern.lower()
    table = {}
    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        table[pattern[i]] = pattern_length - 1 - i
    return table

def boyer_moore_search(text, pattern):
    """Implement Boyer-Moore string matching algorithm."""
    text = text.lower()
    pattern = pattern.lower()
    matches = []
    pattern_length = len(pattern)
    text_length = len(text)
    
    if pattern_length == 0 or text_length == 0:
        return matches

    # Build bad character table
    bad_char = build_bad_char_table(pattern)
    
    shift = 0
    while shift <= text_length - pattern_length:
        mismatch = False
        for i in range(pattern_length - 1, -1, -1):
            if pattern[i] != text[shift + i]:
                mismatch = True
                break
        
        if not mismatch:
            matches.append(shift)
            shift += 1
        else:
            char = text[shift + pattern_length - 1]
            shift += bad_char.get(char, pattern_length)
            
    return matches

def rabin_karp_search(text, pattern):
    """Implement Rabin-Karp string matching algorithm."""
    text = text.lower()
    pattern = pattern.lower()
    matches = []
    
    if not pattern or not text:
        return matches
    
    # Prime number for hash calculation
    prime = 101
    # Number of characters in the input alphabet
    d = 256
    
    pattern_length = len(pattern)
    text_length = len(text)
    
    if pattern_length > text_length:
        return matches
    
    # Calculate hash value for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = pow(d, pattern_length - 1) % prime
    
    for i in range(pattern_length):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime
    
    # Slide the pattern over text one by one
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            if text[i:i + pattern_length].lower() == pattern:
                matches.append(i)
        
        if i < text_length - pattern_length:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % prime
            if text_hash < 0:
                text_hash += prime
    
    return matches

def highlight_matches(text, pattern, matches):
    """Highlight matches in the text using HTML bold tags."""
    if not matches:
        return text
    
    result = []
    last_pos = 0
    pattern_length = len(pattern)
    
    for pos in matches:
        result.append(text[last_pos:pos])
        result.append(f"**{text[pos:pos + pattern_length]}**")
        last_pos = pos + pattern_length
    
    result.append(text[last_pos:])
    return ''.join(result)

def main():
    st.title("String Matching Algorithm Comparison")
    st.write("Compare Boyer-Moore and Rabin-Karp algorithms for pattern matching")
    
    # Input text area for the main text
    text = st.text_area("Enter the text to search in:", height=200)
    
    # Input for the pattern to search
    pattern = st.text_input("Enter the pattern to search for:")
    
    # Input for replacement text
    replacement = st.text_input("Enter replacement text (optional):")
    
    if st.button("Search and Compare"):
        if not text or not pattern:
            st.error("Please enter both text and pattern.")
            return
        
        # Boyer-Moore search
        start_time = time.time()
        bm_matches = boyer_moore_search(text, pattern)
        bm_time = time.time() - start_time
        
        # Rabin-Karp search
        start_time = time.time()
        rk_matches = rabin_karp_search(text, pattern)
        rk_time = time.time() - start_time
        
        # Display results
        st.subheader("Results")
        
        # Create comparison table
        comparison_data = {
            'Algorithm': ['Boyer-Moore', 'Rabin-Karp'],
            'Execution Time (seconds)': [bm_time, rk_time],
            'Matches Found': [len(bm_matches), len(rk_matches)]
        }
        df = pd.DataFrame(comparison_data)
        st.table(df)
        
        # Determine which algorithm was more efficient
        if bm_time < rk_time:
            st.success("Boyer-Moore algorithm was more efficient in this case!")
        elif rk_time < bm_time:
            st.success("Rabin-Karp algorithm was more efficient in this case!")
        else:
            st.info("Both algorithms performed similarly.")
        
        # Display matches
        if len(bm_matches) > 0:
            st.subheader("Matches Found")
            highlighted_text = highlight_matches(text, pattern, bm_matches)
            st.markdown(highlighted_text)
            
            # Replace functionality
            if replacement and st.button("Replace Matches"):
                new_text = text
                offset = 0
                for pos in bm_matches:
                    adjusted_pos = pos + offset
                    new_text = new_text[:adjusted_pos] + replacement + new_text[adjusted_pos + len(pattern):]
                    offset += len(replacement) - len(pattern)
                st.subheader("Text after replacement")
                st.write(new_text)
        else:
            st.warning("No matches found!")

if __name__ == "__main__":
    main() 