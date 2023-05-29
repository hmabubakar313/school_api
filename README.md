# School API

This Django project provides an API for managing school-related data such as students, teachers, courses, and grades. It includes authentication for accessing teacher and course data, while student data is available to anyone. The project also incorporates Swagger documentation for easy API exploration.

## Prerequisites

- Python 3.x installed on your machine
- pip package manager

## Setup

1. Clone the repository:

git clone <https://github.com/hmabubakar313/school_api>


2. Create a virtual environment:

python -m venv myenv


3. Activate the virtual environment:

- For Windows:
  ```
  myenv\Scripts\activate
  ```

- For macOS/Linux:
  ```
  source myenv/bin/activate
  ```

4. Install the required packages:


2. Access the API endpoints:

- Teachers (requires authentication):
  ```
  http://localhost:8000/teachers/
  ```

- Courses (requires authentication):
  ```
  http://localhost:8000/courses/
  ```

- Grades (requires authentication):
  ```
  http://localhost:8000/grades/
  ```

- Students (no authentication required):
  ```
  http://localhost:8000/students/
  ```

3. Explore the API documentation (Swagger):

http://localhost:8000/swagger/


This will provide an interactive documentation of the available API endpoints, request/response examples, and parameter descriptions.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Make sure to create a requirements.txt file in your project root directory and list the required packages along with their versions. For example:

Django==3.2.4
djangorestframework==3.12.4
django-filter==2.4.0
drf-yasg==1.20.0
