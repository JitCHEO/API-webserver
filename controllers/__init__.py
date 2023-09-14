from controllers.users_controllers import users
from controllers.services_controllers import services
from controllers.parts_controllers import parts
from controllers.locations_controllers import locations
from controllers.jiras_controllers import jiras
from controllers.equipments_controllers import equipments



registered_controllers = (
    users,
    services,
    parts,
    locations,
    jiras,
    equipments,
)
