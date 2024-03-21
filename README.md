# AirBnB Clone - The Console

## Description

This project is a command-line interface (CLI) for managing objects in an AirBnB clone application. It allows users to create, retrieve, update, and delete various objects such as users, listings, and bookings.

## Command Interpreter

The command interpreter is a Python-based CLI tool. To start it, follow the instructions below:

### How to Start

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the command `python console.py` to start the command interpreter.

### How to Use

Once the command interpreter is running, you can use various commands to interact with objects. Here are some examples:

- `create User` : Create a new user.
- `show User 123` : Show details of the user with ID 123.
- `update User 123 name "John Doe"` : Update the name of the user with ID 123 to "John Doe".
- `destroy User 123` : Delete the user with ID 123.

For a full list of commands and options, refer to the documentation or use the `help` command within the interpreter.

## Examples

Here are some examples of how to use the command interpreter:

```bash
$ python console.py
(hbnb) create User
User created with ID 1
(hbnb) show User 1
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
}
(hbnb) update User 1 name "Jane Doe"
User updated successfully
(hbnb) destroy User 1
User deleted successfully

