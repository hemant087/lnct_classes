# import re  

# # Read the large scraped file  
# with open("DSM_website_data.txt", "r", encoding="utf-8") as file:  
#     text = file.read()  

# # Split into sentences  
# sentences = re.split(r'(?<=[.!?]) +', text)  

# # Remove duplicates using a set  
# unique_sentences = list(set(sentences))  

# # Join the cleaned sentences into a single text  
# cleaned_text = " ".join(unique_sentences)  

# # Remove extra white spaces  
# cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  

# # Save the cleaned data  
# with open("cleaned_data.txt", "w", encoding="utf-8") as file:  
#     file.write(cleaned_text)  

# print("Cleaning completed. Check 'cleaned_data.txt'.")  



# ====================================================================================

# Read and clean the file
with open("DSM_website_data.txt", "r", encoding="utf-8") as infile, open("cleaned_data.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        if line.strip():  # Only write non-empty lines
            outfile.write(line)

print("Blank lines removed. Check 'DSMcleaned_data.txt'.")
