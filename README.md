# Job Recommendation Backend Service

## Overview
The Job Recommendation Backend Service is a RESTful API designed to suggest relevant job postings to users based on their profiles and preferences by using Django and PostgreSQL. This service is a part of an AI-powered talent acquisition platform that matches user profiles with job postings based on skills, experience, and preferences.

## Features
- Accepts user profile data via a RESTful API.
- Recommends job postings based on a custom recommendation logic.
- Supports a variety of job posting attributes including title, company, location, required skills, experience level, and job type.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [License](#license)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Pgangothri/peoplebox.git
2. Navigate to the project directory
   ```bash
   cd your_project
3. Install the required dependencies
   ```bash
   pip install -r requirements.txt
## Usage
To run the application, use the following command:
- Update the database credentials in the settings.py file to connect to your PostgreSQL database
1. We have to make the migrations
   ```bash
   python manage.py makemigrations
2. Apply Migrations to the database
   ```bash
   python manage.py migrate
3. Run the Application
   ```bash
   python manage.py runserver
## API Documentation

### Base URL
All endpoints are prefixed with the base URL:  
`http://127.0.0.1:8000/`

### Endpoints

1. **POST /api/register**
   - **Description**: This endpoint registers a new user.
   - **Request**:
     - **Content-Type**: `application/json`
     - **Request Body**: JSON object containing user registration data.

2. **POST /api/token**
   - **Description**: This endpoint generates an access token for the user.
   - **Request**:
     - **Content-Type**: `application/json`
     - **Request Body**: JSON object containing user credentials.

3. **POST /api/token/refresh**
   - **Description**: This endpoint refreshes the access token.
   - **Request**:
     - **Content-Type**: `application/json`
     - **Request Body**: JSON object containing the refresh token.

4. **POST /api/populate**
   - **Description**: This endpoint populates the database with mock job postings.
   - **Request**:
     - **Content-Type**: `application/json`
     - **Request Body**: JSON object containing mock job data.

5. **POST /api/recommend**
   - **Description**: This endpoint accepts user profile data and returns recommended job postings.
   - **Request**:
     - **Content-Type**: `application/json`
     - **Request Body**: JSON object containing user profile data.
     ```json
     {
       "name": "John Doe",
       "skills": ["JavaScript", "Node.js", "React"],
       "experience_level": "Intermediate",
       "preferences": {
         "desired_roles": ["Software Engineer", "Full Stack Developer"],
         "locations": ["San Francisco", "Remote"],
         "job_type": "Full-Time"
       }
     }
     ```

### Testing the API
The entire API has been tested using Postman. You can find the API documentation and details here:  
[Postman Documentation](https://documenter.getpostman.com/view/27536473/2sAXxMgtUo)
### License
This project is licensed under the MIT License. See the LICENSE file for more details.
## Notes
- Ensure that the Postman documentation link is functional and directs users to the right resource.
- Keep the API documentation updated as your endpoints evolve or new features are added.
- If you have specific details about the request body and responses for each endpoint, you may want to expand on those sections under API Documentation.
- Feel free to modify any part of this to better fit your project needs! Let me know if there’s anything else you need help with!



   
