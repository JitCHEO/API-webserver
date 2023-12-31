from flask import Blueprint
from datetime import datetime
import time

from main import db, bcrypt
from models import User, Service, Part, Location, Jira, Equipment, Induction

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    # Create db tables based on defined models
    db.create_all()
    print("Tables are created")

@db_commands.cli.command("drop")
def drop_db():
    # Drop(delete) all db tables
    db.drop_all()
    print("Tables are dropped")

@db_commands.cli.command("seed")
def seed_db():
    # create User objects
    user1 = User(
        email = "jit@abraham.com.au",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"), 
        is_admin = True
    )
    user2 = User(
        email = "long@cooper.com.au",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )

    # add all users object to db
    db.session.add_all([
        user1, user2,
    ])
    # commit db for users
    db.session.commit()

    # create equipments
    equipment1 = Equipment(
        equipment_number = "SSR552XT",
        type_equipment = "XT",
        description = "qweq"  
    )

    equipment2 = Equipment(
        equipment_number = "SSR787XT",
        type_equipment = "FX",
        description = "qweqwe"
    )

    # add equipments object to db
    db.session.add_all([
        equipment1, equipment2,
    ])

    # commit db for equipments
    db.session.commit()

        # create Service 
    time_1_day = int(time.time()) + (24 * 60 )
    service1 = Service(
        type_service = "Minor Service", 
        service_date = datetime.fromtimestamp(time_1_day),
        description = "July 3 month MTM",
        state = "QLD",
        equipment_id = equipment2.id
    )

    # time_1_day = int(time.time()) + (24 * 60 )
    service2 = Service(
        type_service = "Major Service", 
        service_date = datetime.fromtimestamp(time_1_day),
        description = "Oct 3 month MTM",
        state = "NSW",
        equipment_id = equipment1.id
    )

    # add services object to db
    db.session.add_all([
        service1, service2,
    ])

    # commit db for services
    db.session.commit()
    

        # create locations
    location1 = Location(
        site = "Capcoal",
        visit_date = datetime.now(),
        site_airport = "Emerald",
        state = "QLD",
        equipment_id = equipment1.id
    )

    location2 = Location(
        site = "Foxleigh",
        visit_date = datetime.now(),
        site_airport = "Emerald",
        state = "QLD",
        equipment_id = equipment1.id
    )

    # add locations object to db
    db.session.add_all([
        location1, location2,
    ])

    # commit db for locations
    db.session.commit()

    # create parts 
    part1 = Part(
        part_name = "Fuel filters",
        purchase_date = datetime.now(),
        description = "Parts that goes to engine side",
        amount_spent = "150",
        equipment_id = equipment1.id
    )

    part2 = Part(
        part_name = "Injectors",
        purchase_date = datetime.now(),
        description = "Parts that goes to engine side",
        amount_spent = "300",
        equipment_id = equipment1.id
    )

    # add parts object to db
    db.session.add_all([
        part1, part2,
    ])

    # commit db for parts
    db.session.commit()


    # create jiras
    jira1 = Jira(
        issue_title = "SSR552XT",
        created_at = datetime.now(),
        service_completion = datetime.now(),
        description = "Completed at laydown area",
        jira_progress = "In Progress",
        equipment_id = equipment1.id,
        user_id = user1.id
    )

    jira2 = Jira(
        issue_title = "SSR787XT",
        created_at = datetime.now(),
        service_completion = datetime.now(),
        description = "Replaced REM",
        jira_progress = "In Progress",
        equipment_id = equipment2.id,
        user_id = user1.id
    )

    # add jiras object to db
    db.session.add_all([
        jira1, jira2,
    ])

    # commit db for jiras
    db.session.commit()

    # create inductions
    induction1 = Induction(
        expiry_date = datetime.now(),
        documents_required = "Drivers license, Medical, DA" ,
        description = "Online induction required, site familiarisation follow after",
        induction_progress = "Not Started",
        location_id = location1.id
    )

    induction2 = Induction(
        expiry_date = datetime.now(),
        documents_required = "Medical" ,
        description = "Site familiarisation required",
        induction_progress = "Completed",
        location_id = location1.id
    )

    # add inductions object to db
    db.session.add_all([
        induction1, induction2,
    ])

    # commit db for inductions
    db.session.commit()
    

    # log if seed is succeeded
    print("Database has been seeded")

