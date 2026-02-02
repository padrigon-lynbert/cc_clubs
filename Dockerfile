FROM php:8.2-cli

# Install PDO MySQL
RUN apt-get update && apt-get install -y default-mysql-client \
    && docker-php-ext-install pdo pdo_mysql

WORKDIR /app
COPY . .

EXPOSE 10000
CMD ["php", "-S", "0.0.0.0:10000", "-t", "."]
