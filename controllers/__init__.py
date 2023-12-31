from controllers.users_controllers import users
from controllers.services_controllers import services
from controllers.parts_controllers import parts
from controllers.locations_controllers import locations
from controllers.jiras_controllers import jiras
from controllers.equipments_controllers import equipments
from controllers.inductions_controllers import inductions
from controllers.auth_controllers import auths



registered_controllers = (
    users,
    services,
    parts,
    locations,
    jiras,
    equipments,
    inductions,
    auths,
)
