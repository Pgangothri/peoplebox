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
- In settings.py file change database credintials related to postgreSQL database
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

#### 1. **POST api/register**
#### 2. **POST api/token**
#### 2. **POST api/token/refresh**
#### 2. **POST api/populate**
#### 2. **POST api/recommend**
This endpoint accepts user profile data and returns recommended job postings.

- **Request**
  - **Content-Type**: `application/json`
  - **Request Body**: JSON object containing user Registration.
  
- The entire API tested by using postman and published over it
- Check out: https://documenter.getpostman.com/view/27536473/2sAXxMgtUo

   
