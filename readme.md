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
- 

## R7 Detail any third party services that your app will use
- Authentication Service
    - My app will require user authentication, i might need need to use a third-party authentication servuce such as AuthO for user management & authentication.
- Hosting Databases
    - Using Amazon Relational Database Service(RDS) or Google Cloud SQL to manage app's databases
- File Storage
    - Amazon S3, Google Cloud Storage or Dropbox are the third-party file storage services that i can utilize.
- Notification services
    - Firebase Cloud Messaging(FCM) to sent push notifications for upcoming-services.

## R8 Describe your projects models in terms of the relationships they have with each other
- User model
    - Representing individuals who interact with the system.
    - Relationships:
        - One user can have many equipments to maintain at a single site.
        - One user can be associated with multiple JIRAs.
- Service model
    - 
- Part model
    - Representing parts of an equipments.
    - Relationships:
        - Each and every part of an equipment will be associated back to the equipment.
- Location model
    - Representing a location or a place.
    - Relationships:
        - 
- JIRA model
    - 
- Induction model
    - 
- Equipment model
    - Representing physical equipments or assets.
    - Relationships:
        - Each equipment can be associated with different users.
        - Each equipment will also have multiple parts that will need to be replace.


## R9 Discuss the database relations to be implemented in your application
- 

## R10 Describe the way tasks are allocated and tracked in your project 
- 