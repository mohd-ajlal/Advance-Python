import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to the temporary file
tempFile.write(b"Save this special number for me: 5678309")

# Move pointer to beginning
tempFile.seek(0)

# Read data
print(tempFile.read())

# Close file
tempFile.close()