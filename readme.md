## R1 Identification of the problem you are trying to solve by building this particular app.
#### This particular app will better assist us in keeping track the type of equipments that we have spread out every locations around Australia, parts that will be required for each equipments, services that needed to be done on the equipments whether it be a major services, minor services or breakdowns. Not only that, as the company provides services accross the mines, there are heaps of inductions that need to be keep track on expiration of induction & whether it have been completed. Once all this problems can be solved, it will then be keep track and accessible for different users to go throughs and make changes as required.

## R2 Why is it a problem that needs solving?
#### Due to the expansion in the company with the rapid sales of equipments to the customers, we need to come up with a solution that can be keep track easily by different members of the teams in relates to parts, sites to attend that will have different type of equipments number. By doing so, every team members can do their part in updating the required informations. As different mine site have different process of enrollling employees or contractors before entering the site, it will be easy to keep track of expiration date of each employee that will be attending different mine sites.

## R3 Why have you chosen this database system. What are the drawbacks compared to others?
#### The main reason I chosen PostgreSQL as my database system was mainly because I was taught about it. As a beginner in the programming world, it is easier for me to use what I was taught before venturing into other database system.
 - While PostgreSQL do offer good overall performance, high transactions environments might not be suitable for such database.
 - I have not dive in deep into PostgreSQL but the advanced features & flexibility can result in steeper learning curve for new beginners like myself. It may require more time & effort to be proficient in the database.
 - Even though PostgreSQL might have a robust ecosystem, it might not be as extensive for certain specialized use cases compare to some other database system that will have more extensive ecosystem of third party-tools, libraries as well as plugins.

## R4 Identify and discuss the key functionalities and benefits of an ORM
### Key Functionalities
- Mapping objects to tables
    - ORM tools allow me to map my applications models to related database tables. Each class will corresponds to a table & it's arritributes map to columns.
- Relationship Management
    - ORM allows us to define and manage relationships between objects, whether it be one-to-one, one-to-many, many-to-many relationships.
- Database Queries Abstraction
    - Using ORM, we can perform database operations(SELECT, INSERT, UPDATE & DELETE) using object-oriented code than having to write SQL queries manually.

### Benefits
- Portability
    - Abstracting SQL queires, ORM makes it easier to switch around different database systems without having to re-write significant portions of the code.
- Maintainability
    - ORM tools help us to keep code clean & easily maintain by summarizing database-related logic within objects. By separating this, it makes the code easier to read, understand and to maintain.
- Testing
    - ORM assist us by making it easier to write test unit for database interactions, as we can mock ORM operations for testing purposes.

## R5 Document all endpoints for your API
- Users
    - GET/users : Retrieve list of the users.
    - Get/users/{id} : Retrieve specific user information by user ID.
    - DELETE/users/{id} : Delete a user by user ID.
    - POST/users : Creating a new user. 
    - PUT/users/{id} : Updating an existing user's information.

- Equipments
    - GET/equipments : Retrieve list of all equipments.
    - Get/equipments/{id} : Retrieve a specific equipment by equipment ID.
    - DELETE/equipments/{id} : Delete an equipment by equipment ID. 
    - POST/equipments : Creating a new equipment. 
    - PUT/equipments/{id} : Updating an existing equipment's information.

- Parts
    - GET/parts : Retrieve list of all parts.
    - Get/parts/{id} : Retrieve a specific part by part ID.
    - DELETE/parts/{id} : Delete an part by part ID. 
    - POST/parts : Creating a new part. 
    - PUT/parts/{id} : Updating an existing part's information.

- Locations
    - GET/locationss : Retrieve list of all locationss.
    - Get/locationss/{id} : Retrieve a specific locations by locations ID.
    - DELETE/locationss/{id} : Delete an locations by locations ID. 
    - POST/locationss : Creating a new locations. 
    - PUT/locationss/{id} : Updating an existing locations's information.

- Services
    - GET/services : Retrieve list of all services.
    - Get/services/{id} : Retrieve a specific service by service ID.
    - DELETE/services/{id} : Delete an service by service ID. 
    - POST/services : Creating a new service. 
    - PUT/services/{id} : Updating an existing service's information.

- JIRAs
    - GET/jiras : Retrieve list of all jiras.
    - Get/jiras/{id} : Retrieve a specific jira by jira ID.
    - DELETE/jiras/{id} : Delete an jira by jira ID. 
    - POST/jiras : Creating a new jira. 
    - PUT/jiras/{id} : Updating an existing jira's information.

    

## R6 An ERD for your app
- ![ERD API](../T2A2_API_project/ERD%20.png)

## R7 Detail any third party services that your app will use
- bycrypt
    - Password hashing algorithm to used to securely stored user passwords in the database.
    - Helps to protect user data by ensuring that passwords are not stored in plaintext & are difficult to reverse-engineer.
    - Is used for securely hashing & verifying user passwords during registration & login processes.

- PostgreSQL
    - Open-source relational database management system(RDBMS) that use as the primary database for my application.
    - Provides robust data storage & retrival capabilities.
    - Help me to stores user data & other essential information needed to run the application.
    - Visit [PostgreSQL](https://www.postgresql.org/) for more informations.


- JSON Web Tokens(JWT)
    - Used in my application to handle authentication & authorization processes, allowing users to securely access specific resources & endpoints.
    - To ensure that only authorized user can access certains parts of the application.
    - Visit [JWT](https://jwt.io/introduction/) for more informations.
    
- JWT identity
    - Simplifies user identity management using JWT tokens. Making it easier to integrate JWT-based security into application
    - Used to streamline user identity management, ensuring users are properly authenticated & authorized based on JWT tokens.


## R8 Describe your projects models in terms of the relationships they have with each other
- User model
    - Representing individuals who interact with the system.
    - Relationships:
        - One user can have many equipments to maintain at a single site.
        - One user can be associated with multiple JIRAs.
- Service model
    - Representing services that can be provided or requested.
    - Relationships:
        - Each service will be associated with the equipments which are located at different sites.
- Part model
    - Representing parts of an equipments.
    - Relationships:
        - Each and every part of an equipment will be associated back to the equipment.
- Location model
    - Representing a location or a place.
    - Relationships:
        - Each Location will have multiple equipments.
- JIRA model
    - Representing issues or task that need to be track & follow up.
    - Relationship:
        - Each JIRA will associated with users.
        - Each JIRA will be associated with 1 or more equipments.
- Induction model
    - Representing process of inducting a user to be at a specific location
    - Relationship:
        - Each induction will be associated to each site.
        - Each induction will have the require documents & expiry date of the induction.
- Equipment model
    - Representing physical equipments or assets.
    - Relationships:
        - Each equipment can be associated with different users.
        - Each equipment will also have multiple parts that will need to be replace.


## R9 Discuss the database relations to be implemented in your application
- One-to-Many(1:N) Relationships:
    - Location to Induction
        - A location can have multiple inductions required.
        - 1 location may have several inductions sessions associated.
        - Implementing location_id as Foreign Key in the Inductions model, and referencing the tables.
        - Allows to establish connection between specific induction and the location it is associated.
- Many-to-Many(N:N)
    - User to Equipment
        - Many user can look after multiple equipments  and converserly one equipment may have multiple users associated.
        - This is achieved by having user_id as the ForeignKey in the 'Equipment' model and referencing the tables.
    - User to JIRAs
        - Many user can access to multiple JIRAs.
        - And each JIRA can have multiple users associated with it.
        - This is achieved by having user_id as Foreignkey in the 'JIRA' model and referencing the tables.
        - This enables tracking of which users involved in which JIRAs and vice versa, facilating easier queries & data management.
    - Equipment to Part
        - Many equipment will require many parts.
        - This is achieved by having equipment_id as Foreignkey in the 'Part' model and referencing the tables.
        - Associate each part with a specific piece of equipment, facilitating queries like finding all parts required for a specific equipment.
    - Equipment to Service
        - Many equipment will require different servicing.
        - This is achieved by having equipment_id as Foreignkey in the 'Service' model and referencing the tables.
        - Enable the linkage of each service record to a specific piece of equipment, facilitating queries as in finding the service history for a particular equipment.


## R10 Describe the way tasks are allocated and tracked in your project 
#### Task Allocation
- Identification
    - Identify & define task. Breaking down to-do list into smaller, doable tasks.
- Prioritization
    - Prioritize task based on importance & urgency. Some models, schemas & controllers rely on each other for it to work.
- Deadlines
    - Assign a due date for each task to be completed so that i will not be overwhelmed closer to due date.


#### Task Tracking
- Management Tool
    - i utilize project management tracking tools such as Atlassian to create & manage tasks. 
- Dependencies
    - Keeping track of tasks to ensure that tasks are completed in the right order. 
- Reviewing of Task
    - Review completed task periodically to ensure that it meet the projects standards & requirements.