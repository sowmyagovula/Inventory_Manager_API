# Inventory Manager API

## Project Overview
The **Inventory Manager API** is a backend application designed to manage inventory systems efficiently. It provides RESTful endpoints for managing products, categories, stock levels, and more. The project is built with scalability and maintainability in mind, ensuring seamless integration with frontend systems.

---

## Features
- **Product Management**: Add, update, delete, and retrieve product details.
- **Category Management**: Organize products into categories for better management.
- **Stock Tracking**: Monitor stock levels and receive alerts for low inventory.
- **Authentication & Authorization**: Secure API endpoints with user roles and permissions.
- **Audit Logs**: Track changes to inventory for accountability.
- **Search & Filters**: Easily find products using advanced search and filtering options.

---

## Technologies Used
- **Backend Framework**: Node.js with Express.js
- **Database**: MongoDB (NoSQL) or PostgreSQL (SQL) depending on the branch
- **Authentication**: JSON Web Tokens (JWT)
- **Version Control**: Git with multiple branches for feature development
- **Testing**: Jest for unit and integration tests
- **Documentation**: Swagger/OpenAPI for API documentation

---

## Branches Overview
### `main`
- Stable release of the project.
- Contains all tested and production-ready features.

### `dev`
- Active development branch.
- New features and bug fixes are implemented here.

### `feature/authentication`
- Implements user authentication and role-based access control.
- Includes JWT-based token generation and validation.

### `feature/product-management`
- Adds CRUD operations for managing products.
- Includes validation for product data and error handling.

### `feature/category-management`
- Introduces category creation and management.
- Enables linking products to categories.

### `feature/stock-tracking`
- Implements stock level monitoring.
- Includes alerts for low inventory and stock adjustments.

### `feature/audit-logs`
- Tracks changes to inventory and user actions.
- Provides endpoints to retrieve audit logs.

### `feature/search-filters`
- Adds advanced search and filtering capabilities.
- Supports searching by name, category, and stock levels.

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Inventory_Manager_API.git
    cd Inventory_Manager_API
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Set up environment variables:
    Create a `.env` file in the root directory and configure the following:
    ```
    PORT=3000
    DATABASE_URL=<your-database-url>
    JWT_SECRET=<your-secret-key>
    ```

4. Start the server:
    ```bash
    npm start
    ```

---

## API Endpoints
### Authentication
- `POST /api/auth/register`: Register a new user.
- `POST /api/auth/login`: Authenticate a user and return a token.

### Products
- `GET /api/products`: Retrieve all products.
- `POST /api/products`: Add a new product.
- `PUT /api/products/:id`: Update product details.
- `DELETE /api/products/:id`: Delete a product.

### Categories
- `GET /api/categories`: Retrieve all categories.
- `POST /api/categories`: Add a new category.
- `PUT /api/categories/:id`: Update category details.
- `DELETE /api/categories/:id`: Delete a category.

### Stock
- `GET /api/stock`: Retrieve stock levels.
- `PUT /api/stock/:id`: Update stock for a product.

### Audit Logs
- `GET /api/logs`: Retrieve audit logs.

---

## Testing
Run tests using:
```bash
npm test
```

---

## Contributing
1. Fork the repository.
2. Create a new branch for your feature:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes and push to your fork.
4. Open a pull request to the `dev` branch.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For questions or support, please contact:
- **Email**: sowmyagovula@gmail.com
- **GitHub**: [sowmyagovula](https://github.com/sowmyagovula)
