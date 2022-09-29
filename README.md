# RetiSpec-Assignment

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Ashimasadana/RetiSpec-Assignment.git
$ cd RetiSpec-Assignment
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd RetiSpec
```

Update db connection configuration under Databases in settings.py inside RetiSpec folder.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

In order to test the test the Restful services, the urls are listed separately for patient and acquisition at main page.

### Patients

1. Creating a new patient.
http://127.0.0.1:8000/patient/CreatePatient/

2. Get a patient by ID (write id in place of <id>)
http://127.0.0.1:8000/patient/GetPatientByID/<id>

3. Get patients by first + last name.
http://127.0.0.1:8000/patient/GetPatientByName/?FirstName=PatientFirstName&LastName=PatientLastName

4. Delete a patient. (pass id to be deleted)
http://127.0.0.1:8000/patient/DeletePatient/<id>


### Acquisitions

1. Add a new acquisition for a patient.
http://127.0.0.1:8000/acquisition/AddAcquisition/

2. List all patient acquisitions (by patient id)
http://127.0.0.1:8000/acquisition/ListAcquistionsOfPatient/<id>

3. Delete an acquisition (by acquisition id)
http://127.0.0.1:8000/acquisition/DeleteAcquisition/<id>

4. Download an image (by acquisition id).
http://127.0.0.1:8000/acquisition/DownloadAcquistionImage/<id>
