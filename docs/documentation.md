### Project and App Setup (Windows)

Source: https://www.django-rest-framework.org/tutorial/quickstart

Installs Django and DRF, creates a Django project, and starts a new app. Ensure you activate the virtual environment first.

```bash
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv .venv
source .venv\Scripts\activate

# Install Django and Django REST framework into the virtual environment
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..
```

--------------------------------

### Project and App Setup (Linux/macOS)

Source: https://www.django-rest-framework.org/tutorial/quickstart

Installs Django and DRF, creates a Django project, and starts a new app. Ensure you activate the virtual environment first.

```bash
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv .venv
source .venv/bin/activate

# Install Django and Django REST framework into the virtual environment
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..
```

--------------------------------

### Setup Virtual Environment and Install Dependencies

Source: https://www.django-rest-framework.org/community/contributing

Set up a virtual environment and install the project dependencies, including development-specific packages, to prepare for running tests.

```bash
python3 -m venv env
source env/bin/activate
pip install -e . --group dev
```

--------------------------------

### Start Django development server

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Command to start Django's built-in development server. Includes validation and server start message.

```bash
python manage.py runserver

Validating models...

0 errors found
Django version 5.0, using settings 'tutorial.settings'
Starting Development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

--------------------------------

### LimitOffsetPagination Request Example

Source: https://www.django-rest-framework.org/api-guide/pagination

Example of a GET request using LimitOffsetPagination with 'limit' and 'offset' query parameters.

```http
GET https://api.example.org/accounts/?limit=100&offset=400
```

--------------------------------

### Install HTTPie

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Command to install HTTPie, a user-friendly command-line HTTP client, using pip.

```bash
pip install httpie
```

--------------------------------

### Example OPTIONS Response

Source: https://www.django-rest-framework.org/api-guide/metadata

This is an example of the JSON response returned by default for an HTTP OPTIONS request, detailing resource information.

```http
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json

{
    "name": "To Do List",
    "description": "List existing 'To Do' items, or create a new item.",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "note": {
                "type": "string",
                "required": false,
                "read_only": false,
                "label": "title",
                "max_length": 100
            }
        }
    }
}
```

--------------------------------

### Example API Request with Accept-Language Header

Source: https://www.django-rest-framework.org/topics/internationalization

Demonstrates an HTTP GET request to an API endpoint, specifying the desired language via the Accept-Language header.

```http
GET /api/users HTTP/1.1
Accept: application/xml
Accept-Language: es-es
Host: example.org
```

--------------------------------

### Example of obtaining authentication token

Source: https://www.django-rest-framework.org/community/release-notes

This example demonstrates how to reimplement the ObtainAuthToken view, which is commonly used for user authentication and token generation.

```python
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user_id': user.pk,
                         'email': user.email})

# Example usage in urls.py:
# from django.urls import path
# from .views import CustomAuthToken
# 
# urlpatterns = [
#     path('auth/token/', CustomAuthToken.as_view(), name='auth_token'),
# ]
```

--------------------------------

### Install Django REST Framework

Source: https://www.django-rest-framework.org/

Install the core package and optional packages like markdown for browsable API support or django-filter for filtering.

```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

--------------------------------

### ListCreateAPIView Example

Source: https://www.django-rest-framework.org/api-guide/generic-views

An example of using ListCreateAPIView to handle both listing and creating user objects, with specific queryset, serializer, and permission configurations.

```APIDOC
## GET /users/

### Description
Retrieves a list of all users.

### Method
GET

### Endpoint
/users/

### Parameters
#### Query Parameters
- **page** (integer) - Optional - The page number for pagination.

### Request Example
```
GET /users/
```

### Response
#### Success Response (200)
- **results** (array) - A list of user objects.
  - **id** (integer) - The user's ID.
  - **username** (string) - The user's username.
  - **email** (string) - The user's email address.

#### Response Example
```json
{
    "results": [
        {
            "id": 1,
            "username": "john_doe",
            "email": "john.doe@example.com"
        }
    ]
}
```

## POST /users/

### Description
Creates a new user.

### Method
POST

### Endpoint
/users/

### Parameters
#### Request Body
- **username** (string) - Required - The username for the new user.
- **email** (string) - Required - The email address for the new user.
- **password** (string) - Required - The password for the new user.

### Request Example
```json
{
    "username": "jane_doe",
    "email": "jane.doe@example.com",
    "password": "securepassword123"
}
```

### Response
#### Success Response (201)
- **id** (integer) - The ID of the newly created user.
- **username** (string) - The username of the new user.
- **email** (string) - The email address of the new user.

#### Response Example
```json
{
    "id": 2,
    "username": "jane_doe",
    "email": "jane.doe@example.com"
}
```
```

--------------------------------

### Basic GET Request with RequestsClient

Source: https://www.django-rest-framework.org/api-guide/testing

Demonstrates a basic GET request using the RequestsClient. Requires fully qualified URLs.

```python
from rest_framework.test import RequestsClient

client = RequestsClient()
response = client.get('http://testserver/users/')
assert response.status_code == 200
```

--------------------------------

### Project Directory Structure

Source: https://www.django-rest-framework.org/tutorial/quickstart

Illustrates the expected file and directory layout after project and app setup.

```bash
$ pwd
<some path>/tutorial
$ find .
.
./tutorial
./tutorial/asgi.py
./tutorial/__init__.py
./tutorial/quickstart
./tutorial/quickstart/migrations
./tutorial/quickstart/migrations/__init__.py
./tutorial/quickstart/models.py
./tutorial/quickstart/__init__.py
./tutorial/quickstart/apps.py
./tutorial/quickstart/admin.py
./tutorial/quickstart/tests.py
./tutorial/quickstart/views.py
./tutorial/settings.py
./tutorial/urls.py
./tutorial/wsgi.py
./env
./env/...
./manage.py
```

--------------------------------

### Obtain Token API Response Example

Source: https://www.django-rest-framework.org/api-guide/authentication

Example JSON response from the `obtain_auth_token` view when valid credentials are provided.

```json
{ 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }
```

--------------------------------

### LimitOffsetPagination Response Example

Source: https://www.django-rest-framework.org/api-guide/pagination

Example of a successful HTTP response when using LimitOffsetPagination.

```json
HTTP 200 OK
{
    "count": 1023,
    "next": "https://api.example.org/accounts/?limit=100&offset=500",
    "previous": "https://api.example.org/accounts/?limit=100&offset=300",
    "results": [
       …
    ]
}
```

--------------------------------

### Custom Mixins Example

Source: https://www.django-rest-framework.org/api-guide/generic-views

Example of creating and using a custom mixin for multiple field lookups.

```APIDOC
## Creating Custom Mixins

### MultipleFieldLookupMixin

#### Description
Apply this mixin to any view or viewset to enable multiple field filtering based on a `lookup_fields` attribute, instead of the default single field filtering.

#### Example Usage
```python
class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field): # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['account', 'username']
```
```

--------------------------------

### Run Development Server

Source: https://www.django-rest-framework.org/tutorial/quickstart

Start the Django development server from the command line.

```bash
python manage.py runserver
```

--------------------------------

### Install Django Filter

Source: https://www.django-rest-framework.org/api-guide/filtering

Install the django-filter library using pip before integrating it with Django REST Framework.

```bash
pip install django-filter
```

--------------------------------

### Install pre-commit Hooks

Source: https://www.django-rest-framework.org/community/contributing

Install the pre-commit tool and set up hooks to automatically check code style conventions before committing. This ensures adherence to PEP 8.

```bash
python -m pip install pre-commit
```

```bash
pre-commit install
```

--------------------------------

### Deploy Documentation with MkDocs

Source: https://www.django-rest-framework.org/community/project-management

Use this command to build and deploy the documentation using MkDocs. Ensure you have MkDocs installed and configured.

```bash
mkdocs gh-deploy
```

--------------------------------

### Build Documentation Locally

Source: https://www.django-rest-framework.org/community/contributing

Install MkDocs and build the project documentation into the `site` directory. This command generates static HTML files for the documentation.

```bash
mkdocs build
```

--------------------------------

### Basic Class-Based View Example

Source: https://www.django-rest-framework.org/api-guide/views

Example of a class-based view using APIView, demonstrating authentication and permission checks for accessing user data.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

--------------------------------

### Example Snippet Creation Response (JSON)

Source: https://www.django-rest-framework.org/tutorial/2-requests-and-responses

This is an example of the JSON response after successfully creating a new snippet via POST request. It returns the created snippet's details.

```json
{
    "id": 3,
    "title": "",
    "code": "print(123)",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}

```

--------------------------------

### Markdown Header Example

Source: https://www.django-rest-framework.org/community/contributing

Example of using the hash style for headers in Markdown documentation. This is the preferred convention for documentation files.

```markdown
# Header Example
```

--------------------------------

### Hostname Versioning Example

Source: https://www.django-rest-framework.org/api-guide/versioning

API version is specified in the hostname. This example shows a request to version 1.0 of the API.

```http
GET /bookings/ HTTP/1.1
Host: v1.example.com
Accept: application/json
```

--------------------------------

### Install JSONP Renderer

Source: https://www.django-rest-framework.org/api-guide/renderers

Install the djangorestframework-jsonp package using pip. This package provides JSONP rendering support.

```bash
$ pip install djangorestframework-jsonp
```

--------------------------------

### Install Package Requirements

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Installs necessary Python packages: Django for web development, Django REST Framework for building APIs, and Pygments for code highlighting.

```bash
pip install django
pip install djangorestframework
pip install pygments
```

--------------------------------

### Install djangorestframework-xml

Source: https://www.django-rest-framework.org/api-guide/parsers

Install the XML package using pip. This package provides XML parsing and rendering support for REST framework.

```bash
$ pip install djangorestframework-xml
```

--------------------------------

### Example ViewSet with Standard Actions

Source: https://www.django-rest-framework.org/api-guide/viewsets

This ViewSet demonstrates the standard actions (list, create, retrieve, update, partial_update, destroy) that routers typically handle. Include `format=None` if using format suffixes.

```python
class UserViewSet(viewsets.ViewSet):
    """
Example empty viewset demonstrating the standard
actions that will be handled by a router class.

If you're using format suffixes, make sure to also include
the `format=None` keyword argument for each action.
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
```

--------------------------------

### Accept Header Versioning Example

Source: https://www.django-rest-framework.org/api-guide/versioning

Client specifies the API version in the 'Accept' header as a media type parameter. This is a recommended approach for versioning.

```http
GET /bookings/ HTTP/1.1
Host: example.com
Accept: application/json; version=1.0
```

--------------------------------

### Serializer Inheritance Example

Source: https://www.django-rest-framework.org/api-guide/serializers

Demonstrates how to create a custom base serializer with a common field and validation, and then inherit from it.

```python
class MyBaseSerializer(Serializer):
    my_field = serializers.CharField()

    def validate_my_field(self, value):
        ...
```

--------------------------------

### Start Django Shell

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Opens the Django shell for interactive use.

```bash
python manage.py shell
```

--------------------------------

### Install drf-excel Package

Source: https://www.django-rest-framework.org/api-guide/renderers

Install the drf-excel package using pip. This package enables rendering endpoints as XLSX spreadsheets.

```bash
$ pip install drf-excel
```

--------------------------------

### PageNumberPagination Request Example

Source: https://www.django-rest-framework.org/api-guide/pagination

Example of a GET request to an API endpoint using `PageNumberPagination`, specifying the desired page number via the `page` query parameter.

```http
GET https://api.example.org/accounts/?page=4
```

--------------------------------

### Example Filtered API Request

Source: https://www.django-rest-framework.org/api-guide/filtering

Demonstrates how to make a request to filter products by category and stock status using the `filterset_fields` configuration.

```http
http://example.com/api/products?category=clothing&in_stock=True
```

--------------------------------

### Install djangorestframework-yaml

Source: https://www.django-rest-framework.org/api-guide/parsers

Install the YAML package using pip. This package provides YAML parsing and rendering support for REST framework.

```bash
$ pip install djangorestframework-yaml
```

--------------------------------

### Install Django OAuth Toolkit

Source: https://www.django-rest-framework.org/api-guide/authentication

Install the Django OAuth Toolkit package using pip. This package provides OAuth 2.0 support for Django.

```bash
pip install django-oauth-toolkit
```

--------------------------------

### Install Schema Generation Dependencies

Source: https://www.django-rest-framework.org/api-guide/schemas

Install pyyaml, uritemplate, and inflection for schema generation. PyYAML is for OpenAPI YAML format, uritemplate for path parameters, and inflection for pluralizing endpoint names.

```bash
pip install pyyaml uritemplate inflection
```

--------------------------------

### Show installed Django REST framework version

Source: https://www.django-rest-framework.org/community/release-notes

Use this command to check the currently installed version of Django REST framework. This is useful after an upgrade or for troubleshooting.

```bash
pip show djangorestframework
```

--------------------------------

### Example Snippet Response (JSON)

Source: https://www.django-rest-framework.org/tutorial/2-requests-and-responses

This is an example of the JSON response when retrieving a list of snippets. It includes details like id, title, code, linenos, language, and style.

```json
[
    {
    "id": 1,
    "title": "",
    "code": "foo = \"bar\"\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
    },
    {
    "id": 2,
    "title": "",
    "code": "print(\"hello, world\")\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
    }
]

```

--------------------------------

### Output of drf_create_token Command

Source: https://www.django-rest-framework.org/api-guide/authentication

Example output from the `drf_create_token` management command, showing the generated token and associated username.

```text
Generated token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b for user user1
```

--------------------------------

### REST Framework Settings Configuration

Source: https://www.django-rest-framework.org/api-guide/settings

Example of how to configure REST framework settings in your Django project's settings.py file.

```APIDOC
## Settings Configuration Example

### Description
This snippet shows how to define the `REST_FRAMEWORK` dictionary in your `settings.py` to customize default renderers and parsers.

### Request Body
```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
```
```

--------------------------------

### Test API: Get list of all snippets

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Uses HTTPie to send a GET request to the API endpoint for listing all snippets. Displays the JSON response.

```bash
http GET http://127.0.0.1:8000/snippets/ --unsorted

HTTP/1.1 200 OK
...
[
    {
        "id": 1,
        "title": "",
        "code": "foo = \"bar\"\n",
        "linenos": false,
        "language": "python",
        "style": "friendly"
    },
    {
        "id": 2,
        "title": "",
        "code": "print(\"hello, world\")\n",
        "linenos": false,
        "language": "python",
        "style": "friendly"
    },
    {
        "id": 3,
        "title": "",
        "code": "print(\"hello, world\")",
        "linenos": false,
        "language": "python",
        "style": "friendly"
    }
]


```

--------------------------------

### Custom Authentication Example

Source: https://www.django-rest-framework.org/api-guide/authentication

Implement custom authentication by subclassing BaseAuthentication and overriding the authenticate method. This example authenticates users based on a username provided in the 'X-USERNAME' header.

```python
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
```

--------------------------------

### Implement Model Create and Update Methods

Source: https://www.django-rest-framework.org/api-guide/serializers

Example of .create() and .update() methods for serializers dealing with Django models, including database saving.

```python
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
```

--------------------------------

### Example Output of Read-only Nested Serializer - JSON

Source: https://www.django-rest-framework.org/topics/writable-nested-serializers

This is an example of the JSON output produced by the read-only nested serializer.

```json
{
    'title': 'Leaving party preparations',
    'items': [
        {'text': 'Compile playlist', 'is_completed': True},
        {'text': 'Send invites', 'is_completed': False},
        {'text': 'Clean house', 'is_completed': False}
    ]
}
```

--------------------------------

### Cache Setup for Throttling

Source: https://www.django-rest-framework.org/api-guide/throttling

Details on configuring Django's cache backend for REST framework's throttle classes and how to use custom cache backends.

```APIDOC
## Setting up the Cache for Throttling

### Overview
REST framework's throttle classes rely on Django's cache backend. Ensure your cache settings are appropriately configured. The default `LocMemCache` is often sufficient for basic setups.

### Custom Cache Backend
To use a cache other than the default, create a custom throttle class and specify the `cache` attribute.

```python
from django.core.cache import caches
from rest_framework.throttling import AnonRateThrottle

class CustomAnonRateThrottle(AnonRateThrottle):
    cache = caches['alternate']
```

Remember to set your custom throttle class in `'DEFAULT_THROTTLE_CLASSES'` in your Django settings or via the `throttle_classes` view attribute.
```

--------------------------------

### Install DRF OAuth Package

Source: https://www.django-rest-framework.org/api-guide/authentication

Install the Django REST framework OAuth package using pip. This package supports both OAuth1 and OAuth2.

```bash
pip install djangorestframework-oauth
```

--------------------------------

### Example Error Response (Method Not Allowed)

Source: https://www.django-rest-framework.org/api-guide/exceptions

Illustrates a typical error response when an unsupported HTTP method is used on a resource.

```http
HTTP/1.1 405 Method Not Allowed
Content-Type: application/json
Content-Length: 42

{"detail": "Method 'DELETE' not allowed."}
```

--------------------------------

### Query Parameter Versioning Example

Source: https://www.django-rest-framework.org/api-guide/versioning

API version is included as a query parameter in the URL. This is a simple and straightforward method for versioning.

```http
GET /something/?version=0.1 HTTP/1.1
Host: example.com
Accept: application/json
```

--------------------------------

### Custom Versioning Scheme Example

Source: https://www.django-rest-framework.org/api-guide/versioning

Implementation of a custom versioning scheme by subclassing `BaseVersioning` and overriding the `determine_version` method to read from a custom header.

```python
from rest_framework import versioning

class XAPIVersionScheme(versioning.BaseVersioning):
    def determine_version(self, request, *args, **kwargs):
        return request.META.get('HTTP_X_API_VERSION', None)
```

--------------------------------

### Configure REST Framework Settings

Source: https://www.django-rest-framework.org/

Define global settings for your REST framework API in the REST_FRAMEWORK dictionary in your settings.py. This example sets default permission classes.

```python
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}
```

--------------------------------

### Token Authentication WWW-Authenticate Header Example

Source: https://www.django-rest-framework.org/api-guide/authentication

When permission is denied for an unauthenticated request using TokenAuthentication, the response includes a WWW-Authenticate header. This example shows the expected format.

```http
WWW-Authenticate: Token
```

--------------------------------

### Basic Authentication WWW-Authenticate Header Example

Source: https://www.django-rest-framework.org/api-guide/authentication

Unauthenticated responses denied permission by BasicAuthentication will include a WWW-Authenticate header. This example shows the typical format for Basic authentication.

```http
WWW-Authenticate: Basic realm="api"
```

--------------------------------

### PageNumberPagination Response Example

Source: https://www.django-rest-framework.org/api-guide/pagination

Example HTTP response for a paginated request using `PageNumberPagination`. Includes total count, links to next and previous pages, and the data for the current page.

```http
HTTP 200 OK
{
    "count": 1023,
    "next": "https://api.example.org/accounts/?page=5",
    "previous": "https://api.example.org/accounts/?page=3",
    "results": [
       …
    ]
}
```

--------------------------------

### Create Django Project and App

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Initializes a new Django project named 'tutorial' and creates a Django app named 'snippets' within it.

```bash
cd ~
django-admin startproject tutorial
cd tutorial
python manage.py startapp snippets
```

--------------------------------

### Example User ViewSet with Custom Action

Source: https://www.django-rest-framework.org/api-guide/routers

A `ReadOnlyModelViewSet` for the `User` model, including a custom action `group_names` that can be routed by a custom router.

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    @action(detail=True)
    def group_names(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        user = self.get_object()
        groups = user.groups.all()
        return Response([group.name for group in groups])
```

--------------------------------

### Basic ModelViewSet Configuration

Source: https://www.django-rest-framework.org/api-guide/viewsets

Configure a ModelViewSet by providing queryset and serializer_class attributes. This is a common setup for basic CRUD operations.

```python
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
```

--------------------------------

### Applying Custom Mixin to a View

Source: https://www.django-rest-framework.org/api-guide/generic-views

Example of applying the `MultipleFieldLookupMixin` to a `RetrieveAPIView` to enable multi-field lookups.

```python
class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['account', 'username']
```

--------------------------------

### Define API Serializer and ViewSet

Source: https://www.django-rest-framework.org/

Create a serializer for your model and a viewset to handle API requests. This example defines a UserSerializer and UserViewSet.

```python
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
```

--------------------------------

### Configure REST framework settings

Source: https://www.django-rest-framework.org/api-guide/settings

Set REST framework configurations in your project's `settings.py` file within the `REST_FRAMEWORK` dictionary. This example configures default JSON renderers and parsers.

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
```

--------------------------------

### Serve Documentation Locally with MkDocs

Source: https://www.django-rest-framework.org/community/project-management

This command serves the documentation locally, allowing you to preview changes before deployment. It's useful for validation.

```bash
mkdocs serve
```

--------------------------------

### Create Schema Endpoint using Metadata API

Source: https://www.django-rest-framework.org/api-guide/metadata

Example of a viewset action to provide a linkable schema endpoint by reusing the metadata API.

```python
@action(methods=['GET'], detail=False)
def api_schema(self, request):
    meta = self.metadata_class()
    data = meta.determine_metadata(request, self)
    return Response(data)
```

--------------------------------

### Create Account Test Case with APITestCase

Source: https://www.django-rest-framework.org/api-guide/testing

An example test case using APITestCase to verify the creation of a new account object via the API.

```python
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myproject.apps.core.models import Account

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'DabApps')
```

--------------------------------

### Create Account Test

Source: https://www.django-rest-framework.org/api-guide/testing

Use APITestCase to test account creation. Ensure the URL is correctly reversed and the initial GET request returns a 200 OK status and the expected data.

```python
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
```

--------------------------------

### Verbose JSON Example

Source: https://www.django-rest-framework.org/api-guide/settings

When COMPACT_JSON is False, JSON responses include spacing after ':' and ','.

```json
{"is_admin": false, "email": "jane@example"}
```

--------------------------------

### URL Path Versioning Example

Source: https://www.django-rest-framework.org/api-guide/versioning

API version is specified as part of the URL path. Ensure your URL conf includes a pattern matching the version as a 'version' keyword argument.

```http
GET /v1/bookings/ HTTP/1.1
Host: example.com
Accept: application/json
```

--------------------------------

### Configure INSTALLED_APPS in settings.py

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Adds the newly created 'snippets' app and the 'rest_framework' app to the project's `INSTALLED_APPS` setting in `tutorial/settings.py`.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets',
]
```

--------------------------------

### Request Snippets List with Accept Header

Source: https://www.django-rest-framework.org/tutorial/2-requests-and-responses

Control the format of the response by using the 'Accept' header in your HTTP requests. This example shows how to request JSON and HTML.

```http
http http://127.0.0.1:8000/snippets/ Accept:application/json  # Request JSON
http http://127.0.0.1:8000/snippets/ Accept:text/html         # Request HTML

```

--------------------------------

### Run Tests Against Multiple Environments with Tox

Source: https://www.django-rest-framework.org/community/contributing

Utilize the tox testing tool to run tests across all supported Python and Django versions. Install tox globally and then run the command.

```bash
tox
```

--------------------------------

### Create Virtual Environment and Activate (Linux/macOS)

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Sets up a new isolated Python environment using venv and activates it. This ensures package configurations are kept separate.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

--------------------------------

### Test API: Get a specific snippet by ID

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Uses HTTPie to send a GET request to the API endpoint for a specific snippet (ID 2). Displays the JSON response for that snippet.

```bash
http GET http://127.0.0.1:8000/snippets/2/ --unsorted

HTTP/1.1 200 OK
...
{
    "id": 2,
    "title": "",
    "code": "print(\"hello, world\")\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}


```

--------------------------------

### Example API Response for Unsupported Media Type

Source: https://www.django-rest-framework.org/topics/internationalization

Illustrates a 406 NOT ACCEPTABLE response from the API when the requested media type is not supported, with a localized error message.

```http
HTTP/1.0 406 NOT ACCEPTABLE

{"detail": "No se ha podido satisfacer la solicitud de cabecera de Accept."}
```

--------------------------------

### Custom Content Negotiation Class

Source: https://www.django-rest-framework.org/api-guide/content-negotiation

Implement a custom content negotiation strategy by subclassing `BaseContentNegotiation`. This example shows a class that ignores client preferences and always selects the first available parser and renderer.

```python
from rest_framework.negotiation import BaseContentNegotiation

class IgnoreClientContentNegotiation(BaseContentNegotiation):
    """
    An example custom content negotiation class which ignores the client request
    when selecting the appropriate parser or renderer.
    """
    def select_parser(self, request, parsers):
        """
        Select the first parser in the `.parser_classes` list.
        """
        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix):
        """
        Select the first renderer in the `.renderer_classes` list.
        """
        return (renderers[0], renderers[0].media_type)
```

--------------------------------

### Example Validation Error Response

Source: https://www.django-rest-framework.org/api-guide/exceptions

Shows how validation errors are returned, including field-specific and non-field errors.

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json
Content-Length: 94

{"amount": ["A valid integer is required."], "description": ["This field may not be blank."]}
```

--------------------------------

### URL Path Versioning URL Configuration

Source: https://www.django-rest-framework.org/api-guide/versioning

Example of a Django URL configuration that captures the version from the URL path using a named regex group.

```python
from django.urls import re_path

urlpatterns = [
    re_path(
        r'^(?P<version>(v1|v2))/bookings/$',
        bookings_list,
        name='bookings-list'
    ),
    re_path(
        r'^(?P<version>(v1|v2))/bookings/(?P<pk>[0-9]+)/$',
        bookings_detail,
        name='bookings-detail'
    )
]
```

--------------------------------

### Build API Documentation with API Star

Source: https://www.django-rest-framework.org/community/3.9-announcement

Generate API documentation from an OpenAPI schema file using the API Star command-line tool. The output is typically an HTML file.

```bash
$ apistar docs --path schema.json --format openapi
✓ Documentation built at "build/index.html".

```

--------------------------------

### Default Permission Classes

Source: https://www.django-rest-framework.org/api-guide/settings

Specifies the default permission classes checked at the start of a view. `AllowAny` is the default, permitting all requests.

```python
[
    'rest_framework.permissions.AllowAny',
]
```

--------------------------------

### Response() Constructor

Source: https://www.django-rest-framework.org/api-guide/responses

Details on how to instantiate the Response class with data, status, headers, and content type.

```APIDOC
## Response() Constructor

### Description
Instantiate a `Response` object with unrendered data. The data should consist of Python primitives. REST framework will handle content negotiation and rendering based on the client's request.

### Signature
`Response(data, status=None, template_name=None, headers=None, content_type=None)`

### Arguments
- **data** (any Python primitive) - The serialized data for the response.
- **status** (int) - A status code for the response. Defaults to 200.
- **template_name** (str) - A template name to use if `HTMLRenderer` is selected.
- **headers** (dict) - A dictionary of HTTP headers to use in the response.
- **content_type** (str) - The content type of the response. Typically set automatically by the renderer.
```

--------------------------------

### Implement a Custom Plaintext Parser

Source: https://www.django-rest-framework.org/api-guide/parsers

Extend BaseParser to create a custom parser for plaintext. This example shows how to read the request stream and return its content as a string.

```python
class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()
```

--------------------------------

### Create and Retrieve a Token Key

Source: https://www.django-rest-framework.org/api-guide/authentication

This Python snippet demonstrates how to create a token for a user using the Token model and print its key. This token is then used for client authentication.

```python
from rest_framework.authtoken.models import Token

token = Token.objects.create(user=...)
print(token.key)
```

--------------------------------

### Serializer Class Management

Source: https://www.django-rest-framework.org/api-guide/generic-views

Customizing the serializer class used by a view, with examples for dynamic serializer selection.

```APIDOC
## `get_serializer_class(self)`

### Description
Returns the class that should be used for the serializer. Defaults to returning the `serializer_class` attribute. May be overridden to provide dynamic behavior, such as using different serializers for read and write operations, or providing different serializers to different types of users.

### Method
`get_serializer_class(self)`

### Example Usage
```python
def get_serializer_class(self):
    if self.request.user.is_staff:
        return FullAccountSerializer
    return BasicAccountSerializer
```
```

--------------------------------

### Set Authentication Classes Per-View (Function-Based View)

Source: https://www.django-rest-framework.org/api-guide/authentication

Apply authentication and permission classes to a function-based view using decorators. This example uses SessionAuthentication and BasicAuthentication, requiring the user to be authenticated.

```python
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)
```

--------------------------------

### HTML Template for List View

Source: https://www.django-rest-framework.org/topics/html-and-forms

An example HTML template that iterates over a list of profiles and displays their names. This template is intended to be used with `TemplateHTMLRenderer`.

```html
<html><body>
<h1>Profiles</h1>
<ul>
    {% for profile in profiles %}
    <li>{{ profile.name }}</li>
    {% endfor %}
</ul>
</body></html>
```

--------------------------------

### Upgrade Django REST framework

Source: https://www.django-rest-framework.org/community/release-notes

Use this command to upgrade to the latest version of Django REST framework. Ensure you have pip installed.

```bash
pip install -U djangorestframework
```

--------------------------------

### Define a Comment Object

Source: https://www.django-rest-framework.org/api-guide/serializers

A simple Python class to represent a comment, used for serialization examples.

```python
from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')
```

--------------------------------

### List and Create API View using Mixins

Source: https://www.django-rest-framework.org/tutorial/3-class-based-views

Compose ListModelMixin and CreateModelMixin with GenericAPIView for listing and creating model instances. Ensure the queryset and serializer_class are defined.

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


class SnippetList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

--------------------------------

### Unicode JSON Example

Source: https://www.django-rest-framework.org/api-guide/settings

When UNICODE_JSON is True, JSON responses allow unicode characters. This is the preferred user-friendly style.

```json
{"unicode black star":"★"}
```

--------------------------------

### Basic get_schema_view() usage

Source: https://www.django-rest-framework.org/api-guide/schemas

Use `get_schema_view` to create a schema view with a title and base URL. This is a common starting point for API schema generation.

```python
schema_view = get_schema_view(
    title='Server Monitoring API',
    url='https://www.example.org/api/'
)
```

--------------------------------

### Create Migrations and Sync Database

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Generates database migrations for the 'snippets' app and applies them to synchronize the database schema with the defined models.

```bash
python manage.py makemigrations snippets
python manage.py migrate snippets
```

--------------------------------

### Simple HTML View with StaticHTMLRenderer

Source: https://www.django-rest-framework.org/api-guide/renderers

An example of a Django REST framework view that uses StaticHTMLRenderer to return a simple, pre-rendered HTML string.

```python
@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def simple_html_view(request):
    data = '<html><body><h1>Hello, world</h1></body></html>'
    return Response(data)
```

--------------------------------

### PageNumberPagination API

Source: https://www.django-rest-framework.org/api-guide/pagination

Details on using the PageNumberPagination style, including request format, response structure, and setup.

```APIDOC
## PageNumberPagination API

### Description
This pagination style uses a page number in the request query parameters to retrieve data.

### Request Example
```
GET https://api.example.org/accounts/?page=4
```

### Response Example (200 OK)
```json
{
    "count": 1023,
    "next": "https://api.example.org/accounts/?page=5",
    "previous": "https://api.example.org/accounts/?page=3",
    "results": [
       ...
    ]
}
```

### Setup
To enable globally:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
```

### Customization
Customize the page query parameter name by overriding `page_query_param`.
```python
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_query_param = 'p' # Clients use ?p=2 instead of ?page=2
```
```

--------------------------------

### Create Virtual Environment and Activate (Windows Bash)

Source: https://www.django-rest-framework.org/tutorial/1-serialization

Sets up a new isolated Python environment using venv and activates it for Windows users using Bash. This ensures package configurations are kept separate.

```bash
python3 -m venv .venv
source .venv\Scripts\activate
```

--------------------------------

### Compact JSON Example

Source: https://www.django-rest-framework.org/api-guide/settings

When COMPACT_JSON is True, JSON responses are minified with no spacing after ':' and ','. This follows Heroku's API design guidelines.

```json
{"is_admin":false,"email":"jane@example"}
```

--------------------------------

### List All Snippets or Create New Snippet (Class-Based View)

Source: https://www.django-rest-framework.org/tutorial/3-class-based-views

Implement a class-based view to handle GET requests for listing all snippets and POST requests for creating a new snippet. Requires Snippet model and SnippetSerializer.

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

--------------------------------

### Create API Root View

Source: https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis

Use a function-based view with `@api_view` to create a single entry point for the API, returning URLs for other endpoints.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse("snippet-list", request=request, format=format),
        }
    )

```

--------------------------------

### Set Default Parsers Globally

Source: https://www.django-rest-framework.org/api-guide/parsers

Configure the default parsers for your entire project using the `DEFAULT_PARSER_CLASSES` setting in `settings.py`. This example restricts requests to only accept JSON content.

```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
```

--------------------------------

### Create superuser command

Source: https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions

Command to create a superuser account for testing and administrative purposes.

```bash
python manage.py createsuperuser
```

--------------------------------

### Custom Schema Subclassing (Leaky Style)

Source: https://www.django-rest-framework.org/api-guide/schemas

An example of subclassing AutoSchema where schema logic might leak into the view via schema_extra_info.

```python
class CustomSchema(AutoSchema):
    """
    AutoSchema subclass using schema_extra_info on the view.
    """

    ...


class CustomView(APIView):
    schema = CustomSchema()
    schema_extra_info = ...  # some extra info
```

--------------------------------

### Read-only Nested Serializer Example - Django

Source: https://www.django-rest-framework.org/topics/writable-nested-serializers

Use this pattern for read-only nested serializers. Ensure related models and serializer classes are defined.

```python
class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['text', 'is_completed']

class ToDoListSerializer(serializers.ModelSerializer):
    items = ToDoItemSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoList
        fields = ['title', 'items']
```

--------------------------------

### Basic Function Based View with @api_view

Source: https://www.django-rest-framework.org/api-guide/views

Demonstrates a simple function-based view using the @api_view decorator to handle GET requests and return a JSON response.

```APIDOC
## GET /

### Description
A simple function-based view that returns a JSON message.

### Method
GET

### Endpoint
/

### Parameters
#### Query Parameters
None

#### Request Body
None

### Request Example
None

### Response
#### Success Response (200)
- **message** (string) - A greeting message.

#### Response Example
```json
{
    "message": "Hello, world!"
}
```
```

--------------------------------

### Expose Obtain Token API Endpoint

Source: https://www.django-rest-framework.org/api-guide/authentication

Integrate the built-in `obtain_auth_token` view into your URL configuration to allow clients to get tokens using username and password.

```python
from rest_framework.authtoken import views
from django.urls import path

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
```

--------------------------------

### Escaped Unicode JSON Example

Source: https://www.django-rest-framework.org/api-guide/settings

When UNICODE_JSON is False, non-ASCII characters are escaped. This conforms to RFC 4627 but is less user-friendly.

```json
{"unicode black star":"\u2605"}
```

--------------------------------

### Set API Description using Docstring

Source: https://www.django-rest-framework.org/topics/documenting-your-api

The description in the browsable API is generated from the docstring of the view or viewset. Markdown syntax can be used if the `Markdown` library is installed.

```python
class AccountListView(views.APIView):
    """
    Returns a list of all **active** accounts in the system.

    For more details on how accounts are activated please [see here][ref].

    [ref]: http://example.com/activating-accounts
    """

```

--------------------------------

### Set Default Renderers Globally

Source: https://www.django-rest-framework.org/api-guide/renderers

Configure the default renderers for your entire API using the REST_FRAMEWORK setting. This example sets JSONRenderer and BrowsableAPIRenderer as the default classes.

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}
```

--------------------------------

### Implement `create` for Writable Nested Representations

Source: https://www.django-rest-framework.org/api-guide/serializers

When supporting writable nested objects, you must implement `create` or `update` methods to handle saving the nested data. This example shows creating a user with a nested profile.

```python
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
```

--------------------------------

### Namespace Versioning URL Configuration

Source: https://www.django-rest-framework.org/api-guide/versioning

Demonstrates URL namespacing for versioning. Different URL prefixes are mapped to different namespaces, allowing views to be accessed via distinct URL patterns.

```python
# bookings/urls.py
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', bookings_list, name='bookings-list'),
    re_path(r'^(?P<pk>[0-9]+)/$', bookings_detail, name='bookings-detail')
]

# urls.py
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^v1/bookings/', include('bookings.urls', namespace='v1')),
    re_path(r'^v2/bookings/', include('bookings.urls', namespace='v2'))
]

--------------------------------

### Usuario API

Source: Local Application API

API endpoints for managing user profiles (Usuario model). Supports listing, creating, retrieving, updating, and deleting user profile records.

```APIDOC
## GET /api/users/

### Description
Retrieves a list of all users.

### Method
GET

### Endpoint
/api/users/

### Parameters
#### Query Parameters
- **page** (integer) - Optional - The page number for pagination.

### Request Example
```
GET /api/users/
```

### Response
#### Success Response (200)
- **count** (integer) - Total number of user profiles.
- **next** (string) - Link to the next page.
- **previous** (string) - Link to the previous page.
- **results** (array) - List of user profile objects.
  - **id** (integer) - The user profile ID.
  - **user** (integer) - Associated Django User ID.
  - **nome** (string) - The user's name.
  - **idade** (integer) - The user's age.
  - **tipo** (string) - The user's type ('admin', 'organizador', 'participante').

#### Response Example
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": 2,
            "nome": "João Silva",
            "idade": 25,
            "tipo": "participante"
        }
    ]
}
```

## POST /api/users/

### Description
Creates a new user profile.

### Method
POST

### Endpoint
/api/users/

### Parameters
#### Request Body
- **user** (integer) - Required - Associated Django User ID.
- **nome** (string) - Required - The user's name.
- **idade** (integer) - Required - The user's age.
- **tipo** (string) - Required - The user's type ('admin', 'organizador', 'participante').

### Request Example
```json
{
    "user": 3,
    "nome": "Maria Souza",
    "idade": 30,
    "tipo": "organizador"
}
```

### Response
#### Success Response (201)
- **id** (integer) - The created user profile ID.
- **user** (integer) - Associated Django User ID.
- **nome** (string) - The user's name.
- **idade** (integer) - The user's age.
- **tipo** (string) - The user's type.

#### Response Example
```json
{
    "id": 2,
    "user": 3,
    "nome": "Maria Souza",
    "idade": 30,
    "tipo": "organizador"
}
```

## GET /api/users/{id}/

### Description
Retrieves a specific user profile by ID.

### Method
GET

### Endpoint
/api/users/{id}/

### Parameters
None

### Request Example
```
GET /api/users/1/
```

### Response
#### Success Response (200)
- **id** (integer) - The user profile ID.
- **user** (integer) - Associated Django User ID.
- **nome** (string) - The user's name.
- **idade** (integer) - The user's age.
- **tipo** (string) - The user's type.

#### Response Example
```json
{
    "id": 1,
    "user": 2,
    "nome": "João Silva",
    "idade": 25,
    "tipo": "participante"
}
```

## PUT /api/users/{id}/

### Description
Updates a specific user profile by ID.

### Method
PUT

### Endpoint
/api/users/{id}/

### Parameters
#### Request Body
- **user** (integer) - Required - Associated Django User ID.
- **nome** (string) - Required - The user's name.
- **idade** (integer) - Required - The user's age.
- **tipo** (string) - Required - The user's type.

### Request Example
```json
{
    "user": 2,
    "nome": "João Silva Alterado",
    "idade": 26,
    "tipo": "participante"
}
```

### Response
#### Success Response (200)
- **id** (integer) - The updated user profile ID.
- **user** (integer) - Associated Django User ID.
- **nome** (string) - The user's name.
- **idade** (integer) - The user's age.
- **tipo** (string) - The user's type.

#### Response Example
```json
{
    "id": 1,
    "user": 2,
    "nome": "João Silva Alterado",
    "idade": 26,
    "tipo": "participante"
}
```

## PATCH /api/users/{id}/

### Description
Partially updates a user profile by ID.

### Method
PATCH

### Endpoint
/api/users/{id}/

### Parameters
#### Request Body
- **nome** (string) - Optional - The user's name.
- **idade** (integer) - Optional - The user's age.
- **tipo** (string) - Optional - The user's type.

### Request Example
```json
{
    "nome": "João S. Alterado"
}
```

### Response
#### Success Response (200)
- **id** (integer) - The updated user profile ID.
- **user** (integer) - Associated Django User ID.
- **nome** (string) - The user's name.
- **idade** (integer) - The user's age.
- **tipo** (string) - The user's type.

#### Response Example
```json
{
    "id": 1,
    "user": 2,
    "nome": "João S. Alterado",
    "idade": 26,
    "tipo": "participante"
}
```

## DELETE /api/users/{id}/

### Description
Deletes a specific user profile by ID.

### Method
DELETE

### Endpoint
/api/users/{id}/

### Parameters
None

### Request Example
```
DELETE /api/users/1/
```

### Response
#### Success Response (204)
No Content
```

--------------------------------

### Evento API

Source: Local Application API

API endpoints for managing events (Evento model). Supports listing, creating, retrieving, updating, and deleting events.

```APIDOC
## GET /api/eventos/

### Description
Retrieves a list of all events.

### Method
GET

### Endpoint
/api/eventos/

### Parameters
#### Query Parameters
- **page** (integer) - Optional - The page number for pagination.

### Request Example
```
GET /api/eventos/
```

### Response
#### Success Response (200)
- **count** (integer) - Total number of events.
- **next** (string) - Link to the next page.
- **previous** (string) - Link to the previous page.
- **results** (array) - List of event objects.
  - **id** (integer) - The event ID.
  - **titulo** (string) - The event title.
  - **descricao** (string) - The event description.
  - **data** (string) - Event date (YYYY-MM-DD).
  - **local** (string) - Event location.
  - **organizador** (integer) - Associated Django User ID of the organizer.
  - **aprovado** (boolean) - Whether the event is approved by an administrator.
  - **publicado** (boolean) - Whether the event is published.

#### Response Example
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "titulo": "Meetup Python",
            "descricao": "Meetup sobre programação em Python",
            "data": "2026-06-15",
            "local": "Sala 1",
            "organizador": 1,
            "aprovado": true,
            "publicado": true
        }
    ]
}
```

## POST /api/eventos/

### Description
Creates a new event.

### Method
POST

### Endpoint
/api/eventos/

### Parameters
#### Request Body
- **titulo** (string) - Required - The event title.
- **descricao** (string) - Required - The event description.
- **data** (string) - Required - Event date (YYYY-MM-DD).
- **local** (string) - Required - Event location.
- **organizador** (integer) - Required - Associated Django User ID of the organizer.
- **aprovado** (boolean) - Optional - Approval status (default: false).
- **publicado** (boolean) - Optional - Publication status (default: false).

### Request Example
```json
{
    "titulo": "Workshop Django",
    "descricao": "Workshop prático de Django",
    "data": "2026-07-20",
    "local": "Auditório Principal",
    "organizador": 1
}
```

### Response
#### Success Response (201)
- **id** (integer) - The created event ID.
- **titulo** (string) - The event title.
- **descricao** (string) - The event description.
- **data** (string) - Event date.
- **local** (string) - Event location.
- **organizador** (integer) - Associated Django User ID of the organizer.
- **aprovado** (boolean) - Approval status.
- **publicado** (boolean) - Publication status.

#### Response Example
```json
{
    "id": 2,
    "titulo": "Workshop Django",
    "descricao": "Workshop prático de Django",
    "data": "2026-07-20",
    "local": "Auditório Principal",
    "organizador": 1,
    "aprovado": false,
    "publicado": false
}
```

## GET /api/eventos/{id}/

### Description
Retrieves a specific event by ID.

### Method
GET

### Endpoint
/api/eventos/{id}/

### Parameters
None

### Request Example
```
GET /api/eventos/1/
```

### Response
#### Success Response (200)
- **id** (integer) - The event ID.
- **titulo** (string) - The event title.
- **descricao** (string) - The event description.
- **data** (string) - Event date.
- **local** (string) - Event location.
- **organizador** (integer) - Associated Django User ID of the organizer.
- **aprovado** (boolean) - Approval status.
- **publicado** (boolean) - Publication status.

#### Response Example
```json
{
    "id": 1,
    "titulo": "Meetup Python",
    "descricao": "Meetup sobre programação em Python",
    "data": "2026-06-15",
    "local": "Sala 1",
    "organizador": 1,
    "aprovado": true,
    "publicado": true
}
```

## PUT /api/eventos/{id}/

### Description
Updates a specific event by ID.

### Method
PUT

### Endpoint
/api/eventos/{id}/

### Parameters
#### Request Body
- **titulo** (string) - Required - The event title.
- **descricao** (string) - Required - The event description.
- **data** (string) - Required - Event date.
- **local** (string) - Required - Event location.
- **organizador** (integer) - Required - Associated Django User ID of the organizer.
- **aprovado** (boolean) - Required - Approval status.
- **publicado** (boolean) - Required - Publication status.

### Request Example
```json
{
    "titulo": "Meetup Python 2026",
    "descricao": "Novo meetup de Python",
    "data": "2026-06-16",
    "local": "Sala 2",
    "organizador": 1,
    "aprovado": true,
    "publicado": true
}
```

### Response
#### Success Response (200)
- **id** (integer) - The event ID.
- **titulo** (string) - The event title.
- **descricao** (string) - The event description.
- **data** (string) - Event date.
- **local** (string) - Event location.
- **organizador** (integer) - Associated Django User ID of the organizer.
- **aprovado** (boolean) - Approval status.
- **publicado** (boolean) - Publication status.

#### Response Example
```json
{
    "id": 1,
    "titulo": "Meetup Python 2026",
    "descricao": "Novo meetup de Python",
    "data": "2026-06-16",
    "local": "Sala 2",
    "organizador": 1,
    "aprovado": true,
    "publicado": true
}
```

## PATCH /api/eventos/{id}/

### Description
Partially updates an event by ID.

### Method
PATCH

### Endpoint
/api/eventos/{id}/

### Parameters
#### Request Body
- **titulo** (string) - Optional - The event title.
- **descricao** (string) - Optional - The event description.
- **data** (string) - Optional - Event date.
- **local** (string) - Optional - Event location.
- **aprovado** (boolean) - Optional - Approval status.
- **publicado** (boolean) - Optional - Publication status.

### Request Example
```json
{
    "local": "Online"
}
```

### Response
#### Success Response (200)
- **id** (integer) - The event ID.
- **titulo** (string) - The event title.
- **descricao** (string) - The event description.
- **data** (string) - Event date.
- **local** (string) - Event location.
- **organizador** (integer) - Associated Django User ID of the organizer.
- **aprovado** (boolean) - Approval status.
- **publicado** (boolean) - Publication status.

#### Response Example
```json
{
    "id": 1,
    "titulo": "Meetup Python 2026",
    "descricao": "Novo meetup de Python",
    "data": "2026-06-16",
    "local": "Online",
    "organizador": 1,
    "aprovado": true,
    "publicado": true
}
```

## DELETE /api/eventos/{id}/

### Description
Deletes a specific event by ID.

### Method
DELETE

### Endpoint
/api/eventos/{id}/

### Parameters
None

### Request Example
```
DELETE /api/eventos/1/
```

### Response
#### Success Response (204)
No Content
```

--------------------------------

### Inscricao API

Source: Local Application API

API endpoints for managing event inscriptions (Inscricao model). Supports listing, creating, retrieving, updating, and deleting inscriptions.

```APIDOC
## GET /api/inscricoes/

### Description
Retrieves a list of all event inscriptions.

### Method
GET

### Endpoint
/api/inscricoes/

### Parameters
#### Query Parameters
- **page** (integer) - Optional - The page number for pagination.

### Request Example
```
GET /api/inscricoes/
```

### Response
#### Success Response (200)
- **count** (integer) - Total number of inscriptions.
- **next** (string) - Link to the next page.
- **previous** (string) - Link to the previous page.
- **results** (array) - List of inscription objects.
  - **id** (integer) - The inscription ID.
  - **evento** (integer) - Associated Event ID.
  - **participante** (integer) - Associated Django User ID of the participant.
  - **status** (string) - Status of the inscription ('pendente', 'confirmado', 'cancelado').

#### Response Example
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "evento": 1,
            "participante": 2,
            "status": "pendente"
        }
    ]
}
```

## POST /api/inscricoes/

### Description
Creates a new event inscription.

### Method
POST

### Endpoint
/api/inscricoes/

### Parameters
#### Request Body
- **evento** (integer) - Required - Associated Event ID.
- **participante** (integer) - Required - Associated Django User ID of the participant.
- **status** (string) - Optional - Inscription status (default: 'pendente').

### Request Example
```json
{
    "evento": 1,
    "participante": 2
}
```

### Response
#### Success Response (201)
- **id** (integer) - The created inscription ID.
- **evento** (integer) - Associated Event ID.
- **participante** (integer) - Associated Django User ID of the participant.
- **status** (string) - Inscription status.

#### Response Example
```json
{
    "id": 2,
    "evento": 1,
    "participante": 2,
    "status": "pendente"
}
```

## GET /api/inscricoes/{id}/

### Description
Retrieves a specific inscription by ID.

### Method
GET

### Endpoint
/api/inscricoes/{id}/

### Parameters
None

### Request Example
```
GET /api/inscricoes/1/
```

### Response
#### Success Response (200)
- **id** (integer) - The inscription ID.
- **evento** (integer) - Associated Event ID.
- **participante** (integer) - Associated Django User ID of the participant.
- **status** (string) - Inscription status.

#### Response Example
```json
{
    "id": 1,
    "evento": 1,
    "participante": 2,
    "status": "pendente"
}
```

## PUT /api/inscricoes/{id}/

### Description
Updates a specific inscription by ID.

### Method
PUT

### Endpoint
/api/inscricoes/{id}/

### Parameters
#### Request Body
- **evento** (integer) - Required - Associated Event ID.
- **participante** (integer) - Required - Associated Django User ID of the participant.
- **status** (string) - Required - Inscription status.

### Request Example
```json
{
    "evento": 1,
    "participante": 2,
    "status": "confirmado"
}
```

### Response
#### Success Response (200)
- **id** (integer) - The inscription ID.
- **evento** (integer) - Associated Event ID.
- **participante** (integer) - Associated Django User ID of the participant.
- **status** (string) - Inscription status.

#### Response Example
```json
{
    "id": 1,
    "evento": 1,
    "participante": 2,
    "status": "confirmado"
}
```

## PATCH /api/inscricoes/{id}/

### Description
Partially updates an inscription by ID.

### Method
PATCH

### Endpoint
/api/inscricoes/{id}/

### Parameters
#### Request Body
- **status** (string) - Optional - Inscription status.

### Request Example
```json
{
    "status": "cancelado"
}
```

### Response
#### Success Response (200)
- **id** (integer) - The inscription ID.
- **evento** (integer) - Associated Event ID.
- **participante** (integer) - Associated Django User ID of the participant.
- **status** (string) - Inscription status.

#### Response Example
```json
{
    "id": 1,
    "evento": 1,
    "participante": 2,
    "status": "cancelado"
}
```

## DELETE /api/inscricoes/{id}/

### Description
Deletes a specific inscription by ID.

### Method
DELETE

### Endpoint
/api/inscricoes/{id}/

### Parameters
None

### Request Example
```
DELETE /api/inscricoes/1/
```

### Response
#### Success Response (204)
No Content
```

--------------------------------

### Presenca API

Source: Local Application API

API endpoints for managing participant presences (Presenca model). Supports listing, creating, retrieving, updating, and deleting presence records.

```APIDOC
## GET /api/presencas/

### Description
Retrieves a list of all presence records.

### Method
GET

### Endpoint
/api/presencas/

### Parameters
#### Query Parameters
- **page** (integer) - Optional - The page number for pagination.

### Request Example
```
GET /api/presencas/
```

### Response
#### Success Response (200)
- **count** (integer) - Total number of presence records.
- **next** (string) - Link to the next page.
- **previous** (string) - Link to the previous page.
- **results** (array) - List of presence objects.
  - **id** (integer) - The presence ID.
  - **inscricao** (integer) - Associated Inscription ID.
  - **presente** (boolean) - Whether the participant is present.

#### Response Example
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "inscricao": 1,
            "presente": false
        }
    ]
}
```

## POST /api/presencas/

### Description
Creates a new presence record.

### Method
POST

### Endpoint
/api/presencas/

### Parameters
#### Request Body
- **inscricao** (integer) - Required - Associated Inscription ID.
- **presente** (boolean) - Optional - Attendance status (default: false).

### Request Example
```json
{
    "inscricao": 1,
    "presente": true
}
```

### Response
#### Success Response (201)
- **id** (integer) - The created presence ID.
- **inscricao** (integer) - Associated Inscription ID.
- **presente** (boolean) - Attendance status.

#### Response Example
```json
{
    "id": 2,
    "inscricao": 1,
    "presente": true
}
```

## GET /api/presencas/{id}/

### Description
Retrieves a specific presence record by ID.

### Method
GET

### Endpoint
/api/presencas/{id}/

### Parameters
None

### Request Example
```
GET /api/presencas/1/
```

### Response
#### Success Response (200)
- **id** (integer) - The presence ID.
- **inscricao** (integer) - Associated Inscription ID.
- **presente** (boolean) - Attendance status.

#### Response Example
```json
{
    "id": 1,
    "inscricao": 1,
    "presente": false
}
```

## PUT /api/presencas/{id}/

### Description
Updates a specific presence record by ID.

### Method
PUT

### Endpoint
/api/presencas/{id}/

### Parameters
#### Request Body
- **inscricao** (integer) - Required - Associated Inscription ID.
- **presente** (boolean) - Required - Attendance status.

### Request Example
```json
{
    "inscricao": 1,
    "presente": true
}
```

### Response
#### Success Response (200)
- **id** (integer) - The presence ID.
- **inscricao** (integer) - Associated Inscription ID.
- **presente** (boolean) - Attendance status.

#### Response Example
```json
{
    "id": 1,
    "inscricao": 1,
    "presente": true
}
```

## PATCH /api/presencas/{id}/

### Description
Partially updates a presence record by ID.

### Method
PATCH

### Endpoint
/api/presencas/{id}/

### Parameters
#### Request Body
- **presente** (boolean) - Optional - Attendance status.

### Request Example
```json
{
    "presente": false
}
```

### Response
#### Success Response (200)
- **id** (integer) - The presence ID.
- **inscricao** (integer) - Associated Inscription ID.
- **presente** (boolean) - Attendance status.

#### Response Example
```json
{
    "id": 1,
    "inscricao": 1,
    "presente": false
}
```

## DELETE /api/presencas/{id}/

### Description
Deletes a specific presence record by ID.

### Method
DELETE

### Endpoint
/api/presencas/{id}/

### Parameters
None

### Request Example
```
DELETE /api/presencas/1/
```

### Response
#### Success Response (204)
No Content
```

--------------------------------

### Relatorio API

Source: Local Application API

API endpoints for managing event reports (Relatorio model). Supports listing, creating, retrieving, updating, and deleting reports.

```APIDOC
## GET /api/relatorios/

### Description
Retrieves a list of all event reports.

### Method
GET

### Endpoint
/api/relatorios/

### Parameters
#### Query Parameters
- **page** (integer) - Optional - The page number for pagination.

### Request Example
```
GET /api/relatorios/
```

### Response
#### Success Response (200)
- **count** (integer) - Total number of reports.
- **next** (string) - Link to the next page.
- **previous** (string) - Link to the previous page.
- **results** (array) - List of report objects.
  - **id** (integer) - The report ID.
  - **evento** (integer) - Associated Event ID.
  - **total_inscritos** (integer) - Total number of inscribed participants.
  - **total_presentes** (integer) - Total number of present participants.
  - **data_geracao** (string) - Generation date/time (ISO 8601 format).

#### Response Example
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "evento": 1,
            "total_inscritos": 25,
            "total_presentes": 20,
            "data_geracao": "2026-06-03T12:00:00Z"
        }
    ]
}
```

## POST /api/relatorios/

### Description
Creates a new event report.

### Method
POST

### Endpoint
/api/relatorios/

### Parameters
#### Request Body
- **evento** (integer) - Required - Associated Event ID.
- **total_inscritos** (integer) - Optional - Total number of inscribed participants (default: 0).
- **total_presentes** (integer) - Optional - Total number of present participants (default: 0).

### Request Example
```json
{
    "evento": 1,
    "total_inscritos": 30,
    "total_presentes": 25
}
```

### Response
#### Success Response (201)
- **id** (integer) - The created report ID.
- **evento** (integer) - Associated Event ID.
- **total_inscritos** (integer) - Total number of inscribed participants.
- **total_presentes** (integer) - Total number of present participants.
- **data_geracao** (string) - Generation date/time.

#### Response Example
```json
{
    "id": 2,
    "evento": 1,
    "total_inscritos": 30,
    "total_presentes": 25,
    "data_geracao": "2026-06-03T12:35:10Z"
}
```

## GET /api/relatorios/{id}/

### Description
Retrieves a specific report by ID.

### Method
GET

### Endpoint
/api/relatorios/{id}/

### Parameters
None

### Request Example
```
GET /api/relatorios/1/
```

### Response
#### Success Response (200)
- **id** (integer) - The report ID.
- **evento** (integer) - Associated Event ID.
- **total_inscritos** (integer) - Total number of inscribed participants.
- **total_presentes** (integer) - Total number of present participants.
- **data_geracao** (string) - Generation date/time.

#### Response Example
```json
{
    "id": 1,
    "evento": 1,
    "total_inscritos": 25,
    "total_presentes": 20,
    "data_geracao": "2026-06-03T12:00:00Z"
}
```

## PUT /api/relatorios/{id}/

### Description
Updates a specific report by ID.

### Method
PUT

### Endpoint
/api/relatorios/{id}/

### Parameters
#### Request Body
- **evento** (integer) - Required - Associated Event ID.
- **total_inscritos** (integer) - Required - Total number of inscribed participants.
- **total_presentes** (integer) - Required - Total number of present participants.

### Request Example
```json
{
    "evento": 1,
    "total_inscritos": 26,
    "total_presentes": 21
}
```

### Response
#### Success Response (200)
- **id** (integer) - The report ID.
- **evento** (integer) - Associated Event ID.
- **total_inscritos** (integer) - Total number of inscribed participants.
- **total_presentes** (integer) - Total number of present participants.
- **data_geracao** (string) - Generation date/time.

#### Response Example
```json
{
    "id": 1,
    "evento": 1,
    "total_inscritos": 26,
    "total_presentes": 21,
    "data_geracao": "2026-06-03T12:00:00Z"
}
```

## PATCH /api/relatorios/{id}/

### Description
Partially updates a report by ID.

### Method
PATCH

### Endpoint
/api/relatorios/{id}/

### Parameters
#### Request Body
- **total_presentes** (integer) - Optional - Total number of present participants.

### Request Example
```json
{
    "total_presentes": 22
}
```

### Response
#### Success Response (200)
- **id** (integer) - The report ID.
- **evento** (integer) - Associated Event ID.
- **total_inscritos** (integer) - Total number of inscribed participants.
- **total_presentes** (integer) - Total number of present participants.
- **data_geracao** (string) - Generation date/time.

#### Response Example
```json
{
    "id": 1,
    "evento": 1,
    "total_inscritos": 26,
    "total_presentes": 22,
    "data_geracao": "2026-06-03T12:00:00Z"
}
```

## DELETE /api/relatorios/{id}/

### Description
Deletes a specific report by ID.

### Method
DELETE

### Endpoint
/api/relatorios/{id}/

### Parameters
None

### Request Example
```
DELETE /api/relatorios/1/
```

### Response
#### Success Response (204)
No Content
```

```