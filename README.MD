# ProfilePro

ProfilePro is a dynamic CV and portfolio website built with Django. It allows users to input their personal information, education, work experiences etc. through an admin panel. The site also includes features like sending emails via the contact page, downloadable CVs in Turkish and English, and links to social medias, GitHub repositories etc.

## Features

- Dynamic data input through the admin panel
- Email functionality via the contact page
- Downloadable CVs in Turkish and English
- Display of education and experience details
- Docker and Gunicorn integration
- Static files collection with `collectstatic`
- SQLite database

## Technologies Used

- Django
- Docker
- Gunicorn
- SQLite
- HTML/CSS/JS
- Python

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mertcolakoglu/profile-pro.git
    cd profilepro
    ```

2. Create a `docker.env` file based on `docker.env.txt` and fill in the necessary parameters.

3. Build and start the Docker containers:
    ```sh
    docker-compose up --build -d
    ```

4. Collect static files:
    ```sh
    docker-compose exec app python manage.py collectstatic --noinput
    ```

5. Access the application at `http://localhost:8000`.

### Usage

1. To input your personal information, education, work experiences, etc... access the Django admin panel at `http://localhost:8000/admin`.
   
2. To send an email through the contact page, navigate to `http://localhost:8000/contact`.

3. Downloadable CVs are available on the CV page in both Turkish and English.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [MIT](https://choosealicense.com/licenses/mit/) file for details.

## Contact

For questions or inquiries, please contact me at [xmert45@gmail.com].
