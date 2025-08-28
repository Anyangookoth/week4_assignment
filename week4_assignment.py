# FILE HANDLING SECTION

# Step 1: Try to read from 'input.txt' and modify its content
try:
    # Open the input file in read mode
    with open("input.txt", "r") as infile:
        original_content = infile.read()
        print("✅ Original content from 'input.txt':")
        print(original_content)

    # Step 2: Modify the content (convert to uppercase)
    modified_content = original_content.upper()

    # Step 3: Write the modified content to 'output.txt'
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)
        print("\n✅ Modified content written to 'output.txt'")

except FileNotFoundError:
    print("❌ Error: 'input.txt' not found. Please make sure the file exists.")
except Exception as error:
    print(f"❌ Unexpected error while handling files: {error}")

# 🧪 ERROR HANDLING SECTION

# Step 4: Ask the user for a filename and try to read it
print("\n📂 Let's test error handling with a custom filename.")
filename = input("🔍 Enter the name of the file you want to read: ")

try:
    with open(filename, "r") as user_file:
        user_content = user_file.read()
        print("\n📄 File content:")
        print(user_content)

except FileNotFoundError:
    print("❌ Error: That file doesn't exist. Double-check the name and try again.")
except Exception as error:
    print(f"❌ Something went wrong: {error}")
finally:
    print("✅ File operation completed.")