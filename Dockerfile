# Use official PHP CLI image
FROM php:8.2-cli

# Set working directory inside container
WORKDIR /app

# Copy your files into the container
COPY . .

# Expose a port
EXPOSE 10000

# Run PHP built-in server
CMD ["php", "-S", "0.0.0.0:10000", "-t", "a_test_api"]
